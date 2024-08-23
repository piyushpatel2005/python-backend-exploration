def test_add_two():
    x = 1
    y = 2
    assert x + y == 3


def test_dict_contains():
    data = {"id": 1, "name": "John Doe"}
    assert "id" in data
    assert "name" in data
    expected = {"id": 1}
    assert expected.items() <= data.items()
