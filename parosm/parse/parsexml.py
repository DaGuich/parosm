import os.path
from queue import Queue
import xml.sax
from xml.sax.handler import ContentHandler

from parosm.types import OSM, Node, Way, Relation


class Element:
    def __init__(self, tag, attrib=None):
        self.tag = tag
        self.attrib = dict() if attrib is None else attrib


class OSMContentHandler(ContentHandler):
    def __init__(self):
        super().__init__()
        self._event_queue = Queue()

    def read_events(self):
        while not self._event_queue.empty():
            yield self._event_queue.get()

    def startElement(self, name, attrs):
        attrib = {key: attrs.get(key) for key in attrs.getNames()}
        self._event_queue.put(('start', Element(name, attrib)))

    def endElement(self, name):
        self._event_queue.put(('end', Element(name)))


class XMLParser:
    def __init__(self, file, callback=None):
        self.__file = file
        self.__callback = self.__default_callback \
                if callback is None else callback
        self.__parser = xml.sax.make_parser()
        self.__handler = OSMContentHandler()

        self.__parser.setContentHandler(self.__handler)

        self.__in_node = False
        self.__in_way = False
        self.__in_relation = False
        self.__in_osm = False
        self.__last_event = None

        self.__osm_object = None
        self.__current_object = None

        if not os.path.isfile(file):
            raise Exception('is not a file')

    @staticmethod
    def __default_callback(element):
        print(str(element))

    def parse(self):
        with open(self.__file, 'r') as f:
            for ln, line in enumerate(f):
                try:
                    self.__parse_internal(line)
                except AttributeError as e:
                    print(ln)
                    raise e

    def __parse_internal(self, line):
        self.__parser.feed(line)
        for event, element in self.__handler.read_events():
            if element.tag == 'osm' and event == 'start':
                self.__in_osm = True
                self.__osm_object = OSM(element.attrib['version'])
            elif element.tag == 'osm' and event == 'end':
                self.__in_osm = False
                self.__callback(self.__osm_object)
            elif element.tag == 'tag' and event == 'start':
                key = element.attrib['k']
                value = element.attrib['v']
                self.__current_object.add_tag(key, value)
            elif element.tag == 'bounds' and event == 'start':
                self.__osm_object.set_bounds(**element.attrib)
            elif element.tag == 'bounds' and event == 'end':
                pass
            elif element.tag == 'node' and event == 'start':
                attrs = element.attrib
                self.__current_object = Node(identifier=attrs['id'], **attrs)
                self.__in_node = True
            elif element.tag == 'node' and event == 'end':
                self.__callback(self.__current_object)
                self.__in_node = False
                self.__current_object = None
            elif element.tag == 'way' and event == 'start':
                attrs = element.attrib
                self.__current_object = Way(identifier=attrs['id'], **attrs)
                self.__in_way = True
            elif element.tag == 'way' and event == 'end':
                self.__callback(self.__current_object)
                self.__in_way = False
                self.__current_object = None
            elif element.tag == 'nd' and event == 'start' and self.__in_way:
                self.__current_object.add_node(element.attrib['ref'])
            elif element.tag == 'relation' and event == 'start':
                attrs = element.attrib
                self.__current_object = Relation(identifier=attrs['id'], **attrs)
                self.__in_relation = True
            elif element.tag == 'relation' and event == 'end':
                self.__callback(self.__current_object)
                self.__in_relation = False
                self.__current_object = None
            elif element.tag == 'member' and event == 'start' and self.__in_relation:
                attrs = element.attrib
                self.__current_object.add_member(attrs['ref'],
                                                 attrs['type'],
                                                 attrs['role'])
            elif element.tag == 'member' and event == 'end':
                pass

