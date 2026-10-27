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
