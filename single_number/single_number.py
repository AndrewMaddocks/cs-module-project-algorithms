'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# ```
# Sample input: [2, 2, 1]
# Expected output: 1
# ```
# I need to loop through arr
# inner loop
# base case when we are left with one element
# recursive function

# remove numbers that are doubled if current and match are equal
# base case
# if len(arr) == 1
#     return arr[0]


# def single_number(nums):

#     for num in nums:
#         current = 0
#         match = 1
#         if len(nums) == 1:
#             return nums[0]

#         elif nums[current] != nums[match]:
#             match += 1

#         else:
#             nums.pop(match)
#             nums.pop(current)
#             return single_number(nums)
#     return nums[0]

#     # remove els
#     # single_number(arr)

def single_number(nums):
    counts = {}

    for num in nums:
        if num in counts:
            del counts[num]
        else:
            counts[num] = 1
    return counts[counts.keys()[0]]
    for k, v in counts.items():  # O(1)
        if v == 1:
            return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
