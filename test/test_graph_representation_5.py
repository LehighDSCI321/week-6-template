import subprocess
import re
import pytest

@pytest.fixture
def binary_graph():
    from student_code import BinaryGraph
    return BinaryGraph()

def test_add_node_left(binary_graph):
    binary_graph.add_node_left("LeftChild", 1)
    assert binary_graph.get_node_value("LeftChild") == 1
    assert binary_graph.get_node_left("Root") == "LeftChild"
    