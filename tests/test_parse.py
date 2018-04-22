from os import path
import unittest

from parosm.parse import PBFParser, XMLParser, MultiParser
from parosm.types import *


class TestParser(unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        test_dir = path.abspath(path.dirname(__file__))
        self._xml_file = path.join(test_dir, 'test_map.osm')
        self._pbf_file = path.join(test_dir, 'test_map.osm.pbf')

    def setUp(self):
        self._node_counter = 0
        self._way_counter = 0
        self._rel_counter = 0

    def tearDown(self):
        del self._node_counter
        del self._way_counter
        del self._rel_counter

    def parser_callback(self, obj):
        if isinstance(obj, Node):
            self._node_counter += 1
        elif isinstance(obj, Way):
            self._way_counter += 1
        elif isinstance(obj, Relation):
            self._rel_counter += 1

    def test_xml(self):
        parser = XMLParser(self._xml_file, callback=self.parser_callback)
        parser.parse()

        self.assertEqual(3173, self._node_counter)
        self.assertEqual(628, self._way_counter)
        self.assertEqual(39, self._rel_counter)

    def test_pbf(self):
        parser = PBFParser(self._pbf_file, callback=self.parser_callback)
        parser.parse()

        self.assertEqual(3173, self._node_counter)
        self.assertEqual(628, self._way_counter)
        self.assertEqual(39, self._rel_counter)

    def test_multi_xml(self):
        parser = MultiParser(self._xml_file, callback=self.parser_callback)
        parser.parse()

        self.assertEqual(3173, self._node_counter)
        self.assertEqual(628, self._way_counter)
        self.assertEqual(39, self._rel_counter)

    def test_multi_pbf(self):
        parser = MultiParser(self._pbf_file, callback=self.parser_callback)
        parser.parse()

        self.assertEqual(3173, self._node_counter)
        self.assertEqual(628, self._way_counter)
        self.assertEqual(39, self._rel_counter)

