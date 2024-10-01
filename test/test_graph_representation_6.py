import subprocess
import re
import pytest

@pytest.fixture
def binary_graph():
    from student_code import BinaryGraph
    return BinaryGraph()

def test_add_node_right(binary_graph):
    binary_graph.add_node_right("RightChild", 2)
    assert binary_graph.get_node_value("RightChild") == 2
    assert binary_graph.get_node_right("Root") == "RightChild"
    