import pytest

from finding_mul import find_and_apply_mul


def test_find_and_apply_mul_corrupted_memory_is_str():
    with pytest.raises(TypeError):
        find_and_apply_mul(None)


def test_find_and_apply_mul_is_correct():
    corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    total = find_and_apply_mul(corrupted_memory)

    assert total == 161


if __name__ == "__main__":
    pytest.main([__file__])
