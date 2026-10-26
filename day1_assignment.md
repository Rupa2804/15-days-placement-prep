Name: Rupa kasarla
Date: 26/10/2026

Day-1

1. CODING PROBLEM

APPROACH:
create a empty dictionary to store character frequency. count the frequency of each character and ignore white spaces. store the frequency of each character in a dictionary. Now traverse again through the string and return the first character whose frequency is 1. if none found return None.

code:
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
print(first_non_repeating)

TEST CASES:
test case 1:
Enter a string: sunshine
first_non_repeating:  u

test case 2:
Enter a string: aabcbddab
first_non_repeating:  c

test case 3:
Enter a string: hello
first_non_repeating:  h

test case 4:
Enter a string: aabbcddcde
first_non_repeating:  e

test case 5:
Enter a string: rupa
first_non_repeating:  a


2. CONCEPT QUESTION:

List[ ]: A list is an ordered, mutable collection which allows duplicate values. elements are accessed by index
ex: [1,2,3,2]

Tuple( ): A tuple is a ordered, immutable collection which allows duplicate values. Once the tuple is created we cannot change it directly.
ex: (1,2,3,2)

Set{ }: Set is collection which does not allow duplicate values and has no guaranteed positional order.Set is mutable. its used for membership testing and for set operations. Empty set = set()
ex: {1,2}

Dictionary{key : value}: Dictionary stores the data as key-value pairs. It is an ordered, mutable collection. Keys must be unique. accessed using key.
ex:{"id" : 1, "name" : "rupa"}

scenario 1: Storing Unique Student IDs
A set is a best option to store the student ids because it does not allow duplicate values

scenario 2: Storing Student Profile Fields
A Dictionary is best sutiable choice as maps the keys with the values such as "name: : "name of the student" , "age" " "age os the student" , etc.


3.DEBUGGING CHALLENGE:

original code:
students = ["Anil", "Kiran", "Ravi"]

for student in students:
    if student == "Kiran":
        print("Kiran found")
    else:
        print("Kiran not found")


->here, kiran not found is print for each iteration as it is inside the for loop right after if condition

debugged code:
students = ["Anil", "Kiran", "Ravi"]

for student in students:
    if student == "Kiran":
        print("Kiran found")
        break
else:
    print("Kiran not found")

-> here the else block gets executed after completion of the for loop so if the tagert is not present then this else block gets executed. is the target is found this block gets skipped.


4.REFLECTION:

What I Learned
I learned how to use dictionaries to count character frequencies, the differences between Python data structures, and how to fix errors in loops using break and else.





