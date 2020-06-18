'''
Input: a List of integers
Returns: a List of integers
'''


# def moving_zeroes(arr): #o(n)
#     for zero in arr:
#         if zero == 0:
#             arr.remove(zero)#o(n)
#             arr.append(zero)
#     return arr

def moving_zeroes(arr):
    # arr[left]pointer at the beggining
    # arr[right]pointer at the end
    left = 0
    right = (len(arr) - 1)
    # loop until arr[left] and arr[right] pointers meet
    while arr[right] < arr[left]:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            left += 1
            right -= 1
    return arr
# swap situatuion:

# arr[left] sees zero and arr[right] sees non-zero

# swap the items

# increment arr[left]

# decrement the arr[right]

# non-swap situation

# if lefrt sees non zero

# increment arr[left]

# if arr[right] sees zero

# decrement arr[right]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
