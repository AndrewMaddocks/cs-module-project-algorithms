'''
Input: an integer
Returns: an integer
'''


# def eating_cookies(n):
#     print(n)
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4

#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


def eating_cookies(n, cache=None):
    print(n)
    # check for negative values
    if n < 0:
        return 0
        # base case
    if n == 0:
        return 1
    # check if cache exists
    # check if n is in cache
        # return cache[n]
    if cache is None:
        cache = {}
    # if cache is none ( no cache yet)
        # create the cache
    if n in cache:
        return cache[n]

    cache[n] = eating_cookies(
        n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
