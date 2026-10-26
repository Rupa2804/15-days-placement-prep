def first_non_repeating(str):
    freq = {}

    for char in str:
        if char == " ":
            continue

        freq[char]=freq.get(char,0)+1


    for char in str:
        if char !=" " and freq[char] == 1:
            return char

    return None

str = input("Enter a string: ")
first_non_repeating = first_non_repeating(str)
print("first_non_repeating: ", first_non_repeating)
