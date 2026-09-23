def maxNegativeRepr(lst):
    positive_numbers = [
        num for num in lst
        if num > 0 and -num in lst
    ]

    return max(positive_numbers, default=-1)