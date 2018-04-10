import unittest
from parosm.types import *


class TestNode(unittest.TestCase):
    def test_identifier(self):
        n = Node(5, 0, 0)
        self.assertEqual(5, n.id)

        n = Node(10, 0, 0)
        self.assertEqual(10, n.id)

    def test_lat(self):
        n = Node(0, 1.0, 0)
        self.assertAlmostEqual(1.0, n.lat)
        n.lat = 2.0
        self.assertAlmostEqual(2.0, n.lat)
        with self.assertRaises(TypeError):
            n.lat = 'a'
            n = Node(0, 'a', 0)
            self.assertEqual(n.lat, 'a')

    def test_lon(self):
        n = Node(0, 0, 1.0)
        self.assertAlmostEqual(1.0, n.lon)
        n.lon = 2.0
        self.assertAlmostEqual(2.0, n.lon)
        with self.assertRaises(TypeError):
            n.lon = 'a'
            n = Node(0, 0, 'a')
            self.assertEqual(n.lon, 'a')

    def test_coords(self):
        n = Node(0, 1.0, 1.5)
        self.assertAlmostEqual(1.0, n.lat)
        self.assertAlmostEqual(1.5, n.lon)
        n.lat = 2.0
        n.lon = 2.5
        self.assertAlmostEqual(2.0, n.lat)
        self.assertAlmostEqual(2.5, n.lon)
        n.coords = 3.0, 3.5
        self.assertAlmostEqual(3.0, n.lat)
        self.assertAlmostEqual(3.5, n.lon)
        with self.assertRaises(TypeError):
            n.coords = 'a', 0.0

        with self.assertRaises(TypeError):
            n.coords = 'b', 0.0

    def test_2str(self):
        n = Node(0, 1.0, 1.0)
        self.assertEqual(str(n), 'Node<(id=0), (lat=1.0, lon=1.0)>;')
