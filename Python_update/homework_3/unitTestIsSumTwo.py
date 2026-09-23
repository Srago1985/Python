from isSumTwo import isSumTwo
def test_isSumTwo():
    tests = [
        ([1, 2, 3, 4], 5, True),
        ([1, 2, 3, 4], 8, False),
        ([1, 2, 3, 4], 7, True),
        ([1, 2, 3, 4], 1, False),
        ([], 0, False),
    ]

    for numbers, target, expected in tests:
        result = isSumTwo(numbers, target)
        print(f"isSumTwo({numbers}, {target}) = {result}")
        assert result == expected

if __name__ == "__main__":
    test_isSumTwo()