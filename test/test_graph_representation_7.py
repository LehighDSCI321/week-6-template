import subprocess
import re
import pytest

@pytest.fixture
def binary_graph():
    from student_code import BinaryGraph
    return BinaryGraph()

def test_add_node_left_to_non_root(binary_graph):
    binary_graph.add_node_left("LeftChild", 1)
    binary_graph.add_node_left("LeftGrandChild", 3, "LeftChild")
    assert binary_graph.get_node_value("LeftGrandChild") == 3
    assert binary_graph.get_node_left("LeftChild") == "LeftGrandChild"
    