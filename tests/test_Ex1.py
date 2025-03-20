import pytest

from src.Ex1 import Friends
@pytest.mark.parametrize(
    'friends_',
    [
        ({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
    ]
)
def test_add_connection(area_from, area_to, expected_title):
    # Arrange & Act
    title = get_area_filter_title(area_from=area_from, area_to=area_to)

    # Assert
    assert title == expected_title