import pytest

from page_ordering import (
    get_sum_middle_pages_of_correctly_ordered_updates,
    get_correctly_ordered_updates,
    get_dict_ordering_rules,
    filter_correct_updates,
)


def test_get_sum_middle_pages_of_correctly_ordered_updates_input_is_str():
    with pytest.raises(TypeError):
        get_sum_middle_pages_of_correctly_ordered_updates(45)


def test_get_correctly_ordered_updates_input_ordering_rules_is_str():
    with pytest.raises(TypeError):
        get_correctly_ordered_updates(None, "aaa")


def test_get_correctly_ordered_updates_input_updates_is_str():
    with pytest.raises(TypeError):
        get_correctly_ordered_updates("zersq", 12)


def test_filter_correct_updates_input_updates_is_str():
    with pytest.raises(TypeError):
        filter_correct_updates(1.2, "dszqf")


def test_filter_correct_updates_input_dict_ordering_rules_is_dict():
    with pytest.raises(TypeError):
        filter_correct_updates("1.2", "dszqf")


def test_filter_correct_updates_empty_inputs_return_empty_tuple():
    assert filter_correct_updates("", {}) == ()


def test_filter_correct_updates_wrong_update_return_empty_tuple():
    assert filter_correct_updates("11,10", {10: (11,)}) == ()


def test_filter_correct_updates_correct_update_returned_in_tuple():
    assert filter_correct_updates("10,11", {10: (11,)}) == ((10, 11),)


def test_filter_1_correct_update_1_wrong_update_return_1_correct_update():
    updates = """22,33
44,55"""

    assert filter_correct_updates(updates, {33: (22,), 44: (55,)}) == ((44, 55),)


def test_filter_2_correct_updates_return_2_correct_updates():
    updates = """22,33
44,55"""

    assert filter_correct_updates(updates, {22: (33,), 44: (55,)}) == ((22, 33), (44, 55))


def test_filter_1_update_without_matching_rule_return_1_correct_update():
    updates = """22,33"""

    assert filter_correct_updates(updates, {44: (55,)}) == ((22, 33),)


def test_get_dict_ordering_rules_input_ordering_rules_is_str():
    with pytest.raises(TypeError):
        get_dict_ordering_rules(None)


def test_get_dict_ordering_rules_of_empty_rules_return_empty_dict():
    assert get_dict_ordering_rules("\t") == {}


def test_get_dict_ordering_rules_of_1_incorrect_rule_return_value_error():
    with pytest.raises(ValueError):
        get_dict_ordering_rules("47/53")


def test_get_dict_ordering_rules_of_1_correct_rule_return_correct_dict():
    assert get_dict_ordering_rules("47|53") == {47: (53,)}


def test_get_dict_ordering_rules_of_2_correct_rules_different_first_number_return_correct_dict():
    rules = """47|53
97|13"""

    assert get_dict_ordering_rules(rules) == {47: (53,), 97: (13,)}


def test_get_dict_ordering_rules_of_2_correct_rules_same_first_number_return_correct_dict():
    rules = """47|53
47|56"""

    assert get_dict_ordering_rules(rules) == {47: (53, 56)}


def test_use_case_dict_rules_is_correct():
    rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

    assert get_dict_ordering_rules(rules) == {
        29: (13,),
        47: (53, 13, 61, 29),
        53: (29, 13),
        61: (13, 53, 29),
        75: (29, 53, 47, 61, 13),
        97: (13, 61, 47, 29, 53, 75),
    }


def test_use_case():
    rules_and_updates = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    sum_correct_updates_middle_pages = get_sum_middle_pages_of_correctly_ordered_updates(rules_and_updates)
    assert sum_correct_updates_middle_pages == 143


if __name__ == "__main__":
    pytest.main([__file__])
