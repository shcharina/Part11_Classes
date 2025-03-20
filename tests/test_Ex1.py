import pytest

from src.Ex1 import Friends

@pytest.mark.parametrize(
    'connection, is_new_connection',
    [
        ({"a", "f"}, True),
        ({"a", "b"}, False)
    ]
)
def test_add(connection, is_new_connection):
    friends = Friends({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
    # Arrange & Act
    is_new_conn = friends.add(connection=connection)

    # Assert
    assert is_new_conn == is_new_connection

@pytest.mark.parametrize(
    'connection, is_existing_connection',
    [
        ({"a", "f"}, True),
        ({"a", "b"}, True),
        ({"a", "z"}, False)
    ]
)
def test_remove(connection, is_existing_connection):
    friends = Friends({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}, {"a", "f"})

    # Arrange & Act
    is_existing_conn = friends.remove(connection=connection)

    # Assert
    assert is_existing_conn == is_existing_connection

@pytest.mark.parametrize(
    'connections, expected_names_of_their_friends',
    [
        (({"a", "b"}, {"b", "c"}, {"c", "d"}), {"a", "b", "c", "d"}),
        (({"a", "b"}, {"b", "c"}), {"a", "b", "c"})
    ]
)
def test_names(connections, expected_names_of_their_friends):
    friends = Friends(*connections)
    # Arrange & Act
    names_of_their_friends = friends.names()

    # Assert
    assert names_of_their_friends == expected_names_of_their_friends

@pytest.mark.parametrize(
    'name, their_expected_friends',
    [
        ("a", {"b", "c"}),
        ("d", set())
    ]
)
def test_connected(name, their_expected_friends):
    friends = Friends({"a", "b"}, {"b", "c"}, {"c", "a"})
    # Arrange & Act
    their_friends = friends.connected(name)

    # Assert
    assert their_friends == their_expected_friends