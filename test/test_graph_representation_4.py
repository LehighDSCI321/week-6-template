import subprocess
import re
import pytest

@pytest.fixture
def binary_graph():
    from student_code import BinaryGraph
    return BinaryGraph()

def test_initial_root_node(binary_graph):
    assert binary_graph.get_node_value("Root") == 0
