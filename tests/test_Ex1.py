import pytest

from src.Ex1 import Friends

friends = Friends({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})

@pytest.mark.parametrize(
    'connection, is_new_connection',
    [
        ({"a", "f"}, True),
        ({"a", "b"}, False)
    ]
)
def test_add(connection, is_new_connection):
    # Arrange & Act
    is_new_conn = friends.add(connection=connection)

    # Assert
    assert is_new_conn == is_new_connection

@pytest.mark.parametrize(
    'connection, is_existing_connection',
    [
        ({"a", "f"}, False),
        ({"a", "b"}, False)
    ]
)
def test_remove(connection, is_existing_connection):
    # Arrange & Act
    is_new_conn = friends.add(connection=connection)

    # Assert
    assert is_new_conn == is_existing_connection