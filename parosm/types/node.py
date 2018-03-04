from parosm.types.osmtype import OSMBaseType


class Node(OSMBaseType):
    def __init__(self, identifier, lat, lon, **kwargs):
        super().__init__(identifier=identifier, **kwargs)
        self._lat = lat
        self._lon = lon

    def __str__(self):
        attr_str = list()
        attr_str.append('(id={})'.format(self._id))
        attr_str.append('(lat={})'.format(self._lat))
        attr_str.append('(lon={})'.format(self._lon))
        if len(self._tags) > 0:
            attr_str.append('(tags={})'.format(self._tags))
        attr_str = ', '.join(attr_str)
        return 'Node<{}>;'.format(attr_str)
