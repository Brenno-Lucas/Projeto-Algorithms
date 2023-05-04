def order(list, start, end):
    if start < end:
        item = partition(list, start, end)
        order(list, start, item - 1)
        order(list, item + 1, end)


def partition(list, start, end):
    item = list[end]
    limite = start - 1
    for index in range(start, end):
        if list[index] <= item:
            limite = limite + 1
            list[index], list[limite] = list[limite], list[index]

    list[limite + 1], list[end] = list[end], list[limite + 1]
    return limite + 1


def is_anagram(first_string, second_string):
    first = list(first_string.lower())
    second = list(second_string.lower())
    order(first, 0, len(first) - 1)
    order(second, 0, len(second) - 1)
    return (
        "".join(first),
        "".join(second),
        first == second and (first_string != "" or second_string != ""),
    )
