def test_find_and_apply_mul_is_correct():
    reports = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    total = find_and_apply_mul(reports)

    assert total == 161
