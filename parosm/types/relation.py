from parosm.types.osmtype import OSMBaseType


class Relation(OSMBaseType):
    def __init__(self, identifier, members=None, **kwargs):
        super().__init__(identifier, **kwargs)
        self._members = dict() if members is None else members

    def add_member(self, identifier, mtype, role):
        self._members[identifier] = (mtype, role)

    def __get_members(self):
        for identifier, (mtype, role) in self._members.items():
            yield (identifier, mtype, role)

    def __str__(self):
        attr_str = list()
        attr_str.append('(id={})'.format(self._id))
        attr_str.append('(members={})'.format(len(self._members)))
        if len(self._tags) > 0:
            attr_str.append('(tags={})'.format(self._tags))
        attr_str = ', '.join(attr_str)
        return 'Relation<{}>;'.format(attr_str)

    members = property(__get_members)
