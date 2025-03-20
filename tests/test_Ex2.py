import pytest

from src.Ex2 import Student, Group, Deanery

deanery = Deanery()
map(lambda group: deanery.add_group(group), ["442-1", "441-1"])

@pytest.mark.parametrize(
    '',
    [

    ]
)
def test_add(connection, is_new_connection):
    pass
    # friends = Friends({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
    # # Arrange & Act
    # is_new_conn = friends.add(connection=connection)
    #
    # # Assert
    # assert is_new_conn == is_new_connection
