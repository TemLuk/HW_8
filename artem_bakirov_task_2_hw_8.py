def finding_max_tw(one, two):
    max_of_two = max(one, two)
    return max_of_two


def finding_max_three(one, two, three):
    middle_result = finding_max_tw(one, two)
    return finding_max_tw(middle_result, three)


print(finding_max_three(20, -3, 0))