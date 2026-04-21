"""
Task: Write a Python function to find the length of the longest increasing sub-sequence in a list of numbers.
Sample input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 6
"""

def longest_subsequence(numbers):
    count = 1
    max = 0
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]
        max = a if a > b else b

    return count


nums = list(map(int, input("Enter numbers: ").split()))
res = longest_subsequence(nums)
print(res)
