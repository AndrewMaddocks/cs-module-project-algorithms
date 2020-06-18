'''
Input: a List of integers
Returns: a List of integers
'''
# import numpy


def product_of_all_other_numbers(arr):
 # need a pointer
 # selecting a range, [:pointer] left hand side
 # selecting a range [pointer:]right hand side
 # we have to multiply LHS and RHS separetley and then together and store that new value in the pointer index
 # must return new array
    # pointer = 0
    # new_arr = []
    # for el in arr:

    #     # for el in range(len(arr) - 1):
    #     left = arr[:pointer]
    #     right = arr[pointer + 1:]

    #     if left != []:
    #         l_product = 1
    #         for l in left:
    #             return product_of_all_other_numbers(l_product * l)
    #     if right != []:
    #         r_product = 1

    #         for r in right:
    #             return product_of_all_other_numbers(r_product * r)

    #     new_arr[pointer] = l_product * r_product
    #     if pointer <= (len(arr) - 1):
    #         pointer += 1
    # return new_arr
    final_index = []
    for index, i in enumerate(arr):
        new_list = arr[:index] + arr[index + 1:]
        result = 1
        for x in new_list:
            result = result * x
        final_index.append(result)
    return final_index


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
