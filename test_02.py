# NOTE: A function like this shouldn't even be necessary seeing that the types are
# all over the place from int to list[int] and so on. Stricter types avoids this
# situation entirely. Pydantic can't even check this. >_<

def nested_sum(l):
    total = 0  # don't use `sum` as a variable name
    for val in l:
        if isinstance(val, list):  # checks if `val` is a list
            total += nested_sum(val)
        else:
            total += val
    return total


def main() -> None:
    print(nested_sum([1, [2, [3, [4]], 5]]))  # 15


if __name__ == '__main__':
    main()
