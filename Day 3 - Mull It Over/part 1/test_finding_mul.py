import pytest

from finding_mul import find_and_apply_mul, find_all_mul


def test_find_mul_input_corrupted_memory_is_str():
    with pytest.raises(TypeError):
        find_all_mul(45)


def test_find_mul_empty_str_return_empty_tuple():
    assert find_all_mul("") == ()


def test_find_mul_random_str_return_empty_tuple():
    assert find_all_mul("??ASDZAFAZ464daa2") == ()


def test_find_mul_almost_mul_instruction_str_return_empty_tuple():
    assert find_all_mul("mul(4*") == ()
    assert find_all_mul("mul(6,9!") == ()
    assert find_all_mul("?(12,34)") == ()
    assert find_all_mul("mul ( 2 , 4 )") == ()


def test_find_multiple_almost_mul_instruction_str_return_empty_tuple():
    assert find_all_mul("%&mul[3,7]!@^do_not_mul(5,5+mul(32,64]then(") == ()


def test_mul_instruction_0_0_return_tuple_of_0_0():
    assert find_all_mul("mul(0,0)") == ((0, 0),)


def test_mul_instruction_1_5_return_tuple_of_1_5():
    assert find_all_mul("mul(1,5)") == ((1, 5),)


def test_mul_instruction_75_8_return_tuple_of_75_8():
    assert find_all_mul("mul(75,8)") == ((75, 8),)


def test_mul_instruction_1_833_return_tuple_of_1_833():
    assert find_all_mul("mul(1,833)") == ((1, 833),)


def test_mul_with_number_more_than_3_digits_return_empty_tuple():
    assert find_all_mul("mul(86,2003)") == ()


def test_mul_with_minus_char_return_empty_tuple():
    assert find_all_mul("mul(-7,3)") == ()


def test_mul_with_special_char_return_empty_tuple():
    assert find_all_mul("mul(7!3,3)") == ()


def test_mul_with_a_missing_number_return_empty_tuple():
    assert find_all_mul("mul(43,)") == ()


def test_mul_with_leading_comma_return_empty_tuple():
    assert find_all_mul("mul(,45)") == ()


def test_mul_with_comma_and_no_arguments_return_empty_tuple():
    assert find_all_mul("mul(,)") == ()


def test_mul_with_space_after_comma_return_empty_tuple():
    assert find_all_mul("mul(12, )") == ()


def test_mul_with_spaces_return_empty_tuple():
    assert find_all_mul("mul( 12 , 333 )") == ()


def test_multiple_mul_operations_return_multiple_tuples():
    assert find_all_mul("mul(43,4)mul(564,0)") == ((43, 4), (564, 0))


def test_multiple_mul_operations_with_partial_operation_between_return_multiple_tuples():
    assert find_all_mul("mul(1,222)afazey12mul(AZZmul(3,8)") == ((1, 222), (3, 8))


def test_find_and_apply_mul_input_corrupted_memory_is_str():
    with pytest.raises(TypeError):
        find_and_apply_mul(None)


def test_find_and_apply_mul_is_correct():
    corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    total = find_and_apply_mul(corrupted_memory)

    assert total == 161


if __name__ == "__main__":
    pytest.main([__file__])
