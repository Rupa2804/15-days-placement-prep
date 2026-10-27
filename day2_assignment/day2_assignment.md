Name: Rupa kasarla
Date: 27/10/2026

Day-2

1. CODING PROBLEM

APPROACH:
To remove duplicates while preserving the order we need to use 2 data structure. (1) set to avoid duplicates and (2) list to preserve the insertion order of the data. we need to create a empty list as results to store the data while preserving the order and a set to keep track of duplicates. for eacg item in the list we check if its present in the set if its not present then we add it to both the list and the set. after completion a one traversal we get the list of non duplicates while preserving the order

CODE:
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
print("After removing duplicates list is: ",result)


TEST CASES:
test case 1:
Enter items in the list seprated by space: tea coffee coffee tea milk
After removing duplicates list is:  ['tea', 'coffee', 'milk']

test case 2:
Enter items in the list seprated by space: 4 2 5 3 1
After removing duplicates list is:  ['4', '2', '5', '3', '1']

test case 3:
Enter items in the list seprated by space: 2 1 3 2 1 1 3
After removing duplicates list is:  ['2', '1', '3']

test case 4:
Enter items in the list seprated by space: 23 45 12 11 34 45 12 76 23 45 56 98
After removing duplicates list is:  ['23', '45', '12', '11', '34', '76', '56', '98']

test case 5:
Enter items in the list seprated by space: 
After removing duplicates list is:  []

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)

2.CODING PROBLEM:

APPROACH:
To find the maximum sum of any contiguous window first we must validate the size of the window k and make sure its not less than or equal to zero and not greater than the size of the list. then we start by adding elements from index 0 as oer the size of the window and store it then we move the window one position towards right from left and we subtract the outgoing value and add incoming value to the existing sum and compare it with the previous highest sum. similarly we do it till we get the maximum sum.


CODE:
def maximum_sum(numbers, k):
    if k <= 0 or k > len(numbers):
        return None

    window_sum = sum(numbers[:k])
    best = window_sum

    for right in range(k,len(numbers)):
        window_sum = window_sum - numbers[right-k] + numbers[right]
        best = max(best,window_sum)

    return best



numbers = list(map(int, input("Enter the numbers(seprated by space): ").split()))
size = int(input("Enter the size of the window: "))
maximum_sum = maximum_sum(numbers,size)
print("Maximum sum is: ", maximum_sum)


TEST CASES:
test case 1:
Enter the numbers(seprated by space): 1 2 3 4 3 2 1
Enter the size of the window: 2
Maximum sum is:  7

test case 2:
Enter the numbers(seprated by space): 1 2 3 2
Enter the size of the window: 4
Maximum sum is:  8

test case 3:
Enter the numbers(seprated by space): 1 2 3 2 1 2
Enter the size of the window: 0
Maximum sum is:  None

test case 4:
Enter the numbers(seprated by space): 1 2 3 2
Enter the size of the window: 1
Maximum sum is:  3

test case 5:
Enter the numbers(seprated by space): 2 -4 3 5  
Enter the size of the window: 3
Maximum sum is:  4

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)


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

REFLECTION

1. What I learned

Today, I practised Python data structures, duplicate removal, list sorting, dictionary frequency counting, input validation, and the sliding-window technique. I also learned how to take lists as user input and how to use sets for efficient membership checks.