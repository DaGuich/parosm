from parosm.types.osmtype import OSMBaseType


class Way(OSMBaseType):
    def __init__(self, identifier, nodes=None, **kwargs):
        super().__init__(identifier, **kwargs)
        self._nodes = list() if nodes is None else nodes

    def add_node(self, identifier):
        self._nodes.append(identifier)

    @property
    def nodes(self):
        for node in self._nodes:
            yield node

    def __str__(self):
        attr_str = list()
        attr_str.append('(id={})'.format(self._id))
        attr_str.append('(nodes={})'.format(len(self._nodes)))
        if len(self._tags) > 0:
            attr_str.append('(tags={})'.format(self._tags))
        attr_str = ', '.join(attr_str)
        return 'Way<{}>;'.format(attr_str)
