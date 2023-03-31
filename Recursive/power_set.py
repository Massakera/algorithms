def power_set(input_set):
    if not input_set:
        return [[]]

    first_element = input_set[0]
    rest_set = input_set[1:]

    power_set_without_first = power_set(rest_set)

    power_set_with_first = [subset + [first_element] for subset in power_set_without_first]

    return power_set_without_first + power_set_with_first

