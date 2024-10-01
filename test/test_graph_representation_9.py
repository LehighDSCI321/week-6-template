import subprocess
import re
import pytest

@pytest.fixture
def binary_graph():
    from student_code import BinaryGraph
    return BinaryGraph()

def test_get_node_left_non_existent(binary_graph):
    with pytest.raises(KeyError):
        binary_graph.get_node_left("NonExistentNode")

    