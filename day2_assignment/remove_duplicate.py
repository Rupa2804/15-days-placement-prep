def remove_duplicates(items):
    seen = set()
    result = []


    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result


items = list(input("Enter items in the list seprated by space: ").split())
result = remove_duplicates(items)
if result is []:
    print("List cannot be empty")
print("After removing duplicates list is: ",result)