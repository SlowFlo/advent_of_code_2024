import pytest

from finding_mul import find_and_apply_mul, find_mul


def test_find_mul_input_corrupted_memory_is_str():
    with pytest.raises(TypeError):
        find_mul(45)


def test_find_mul_empty_str_return_empty_tuple():
    assert find_mul("") == ()


def test_find_mul_random_str_return_empty_tuple():
    assert find_mul("??ASDZAFAZ464daa2") == ()


def test_find_mul_almost_mul_instruction_str_return_empty_tuple():
    assert find_mul("mul(4*") == ()
    assert find_mul("mul(6,9!") == ()
    assert find_mul("?(12,34)") == ()
    assert find_mul("mul ( 2 , 4 )") == ()


def test_find_multiple_almost_mul_instruction_str_return_empty_tuple():
    assert find_mul("%&mul[3,7]!@^do_not_mul(5,5+mul(32,64]then(") == ()


def test_mul_instruction_0_0_return_tuple_of_0_0():
    assert find_mul("mul(0,0)") == ((0, 0),)


def test_mul_instruction_1_5_return_tuple_of_1_5():
    assert find_mul("mul(1,5)") == ((1, 5),)


def test_mul_instruction_75_8_return_tuple_of_75_8():
    assert find_mul("mul(75,8)") == ((75, 8),)


def test_mul_instruction_1_833_return_tuple_of_1_833():
    assert find_mul("mul(1,833)") == ((1, 833),)


def test_find_and_apply_mul_input_corrupted_memory_is_str():
    with pytest.raises(TypeError):
        find_and_apply_mul(None)


def test_find_and_apply_mul_is_correct():
    corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    total = find_and_apply_mul(corrupted_memory)

    assert total == 161


if __name__ == "__main__":
    pytest.main([__file__])
