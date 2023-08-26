def my_function(x: int) -> int:
    return x*2


def test_my_functions_returns_double_the_input():
    actural_result = my_function(x=5)

    assert actural_result == 10