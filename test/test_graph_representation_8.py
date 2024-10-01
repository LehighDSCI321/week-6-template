import subprocess
import re
import pytest

@pytest.fixture
def binary_graph():
    from student_code import BinaryGraph
    return BinaryGraph()

def test_add_node_right_to_non_root(binary_graph):
    binary_graph.add_node_right("RightChild", 2)
    binary_graph.add_node_right("RightGrandChild", 4, "RightChild")
    assert binary_graph.get_node_value("RightGrandChild") == 4
    assert binary_graph.get_node_right("RightChild") == "RightGrandChild"
    