# coding=utf8
# Fit 4


def abs_sort(numbers_array: tuple) -> list:
    # Programmier - Aufgabe 4
    # Input: tuple
    # Bedingungen: sortiere tuple nach absoluten Werten (aufsteigend)
    # Output: Liste

    return sorted(numbers_array, key=abs)


if __name__ == '__main__':
    print('Example:')
    print(list(abs_sort((-20, -5, 10, 15))))


    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)


    assert check_it(abs_sort((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(abs_sort((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive Zahlen"
    assert check_it(abs_sort((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative Zahlen"
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
