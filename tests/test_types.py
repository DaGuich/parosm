import unittest
from parosm.types import *


class TestNode(unittest.TestCase):
    def test_identifier(self):
        n = Node(5, 0, 0)
        self.assertEqual(5, n.id)

        n = Node(10, 0, 0)
        self.assertEqual(10, n.id)
