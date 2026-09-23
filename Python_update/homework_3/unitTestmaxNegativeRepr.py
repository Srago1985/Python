import maxNegativeRepr

def test_maxNegativeRepr():
    tests = [
        ([100, 1, 1, 4, 100, -1, -4], 4),
        ([1, 2, 3, 4], -1),
        ([1, 2, 3, 4, -2], 2),
        ([], -1),
    ]

    for numbers, expected in tests:
        result = maxNegativeRepr.maxNegativeRepr(numbers)
        print(f"maxNegativeRepr({numbers}) = {result}")
        assert result == expected

if __name__ == "__main__":
    test_maxNegativeRepr()