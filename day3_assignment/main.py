from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from pydantic import BaseModel, ConfigDict, Field, field_validator

app = FastAPI(title="ITEMS")

class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Item cannot be empty")
        return value


class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float

items: dict[int, dict] = {}
next_id = 1

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id : int):
    item = items.get(item_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    return item

@app.get("/items", response_model=list[ItemResponse])
def list_items(limit: int = Query(default=10, ge=1, le=100)):
    return list(items.values())[:limit]

@app.post(
    "/items",
    response_model=ItemResponse,
    status_code=201
    )
def create_item(item: ItemCreate):
    global next_id

    new_item = {
        "id": next_id,
        "name": item.name,
        "price": item.price,
    }

    items[next_id] = new_item
    next_id += 1

    return new_item

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_TYPES = {"text/plain", "application/pdf"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Only PDF and plain text files are accepted"
        )

    content = await file.read(MAX_FILE_SIZE + 1)

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File exceeds the 5 MB limit"
        )

    
    if file.content_type == "application/pdf":
        if not content.startswith(b"%PDF-"):
            raise HTTPException(
                status_code=400,
                detail="Invalid PDF file"
            )

    
    safe_filename = f"{uuid4().hex}"
    suffix = ".pdf" if file.content_type == "application/pdf" else ".txt"
    destination = UPLOAD_DIR / f"{safe_filename}{suffix}"

    try:
        destination.write_bytes(content)
    finally:
        await file.close()

    return {
        "message": "File uploaded successfully",
        "filename": destination.name,
        "size_bytes": len(content)
    }



