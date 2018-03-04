class OSMBaseType:
    def __init__(self,
                 identifier,
                 user=None,
                 uid=None,
                 timestamp=None,
                 visible=None,
                 version=0,
                 changeset=0,
                 tags=None, **kwargs):
        self._id = identifier
        self._user = "" if user is None else user
        self._uid = 0 if uid is None else uid
        self._timestamp = "" if timestamp is None else timestamp
        self._visible = "false" if visible is None else visible
        self._version = 0 if version is None else version
        self._changeset = 0 if changeset is None else changeset
        self._tags = dict() if tags is None else tags

    def add_tag(self, key, value):
        self._tags[key] = value

    def __get_tags(self):
        for key, value in self._tags:
            yield key, value

    tags = property(__get_tags)


class OSM:
    def __init__(self, version):
        self._version = version
        self._bounds = {
            'minlat': None,
            'minlon': None,
            'maxlat': None,
            'maxlon': None
        }

    def set_bounds(self,
                   minlat=None,
                   minlon=None,
                   maxlat=None,
                   maxlon=None):
        self._bounds['minlat'] = minlat
        self._bounds['minlon'] = minlon
        self._bounds['maxlat'] = maxlat
        self._bounds['maxlon'] = maxlon

    def __str__(self):
        attr_str = list()
        attr_str.append('(version={})'.format(self._version))
        for key, value in self._bounds.items():
            attr_str.append('({}={})'.format(key, value))
        attr_str = ', '.join(attr_str)

        return 'OSM<{}>'.format(attr_str)
