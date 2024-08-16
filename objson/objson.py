class OBJson:
    def __init__(self, data: dict):
        self._data = data

    def __getattr__(self, attr):
        if attr == "_data":
            return getattr(self, attr)

        try:
            result = self._data[attr]
        except KeyError:
            return self._data.__getattribute__(attr)

        if isinstance(result, dict):
            return objson(result)
        else:
            return result

    def __setattr__(self, attr, value):
        if attr == "_data":
            super().__setattr__(attr, value)
        else:
            self._data[attr] = value

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __contains__(self, item):
        try:
            getattr(self, item)
            return True
        except (KeyError, AttributeError):
            return False

    def __delitem__(self, key):
        del self._data[key]

    def __delattr__(self, key):
        del self[key]


def objson(dict: dict) -> OBJson:
    return OBJson(dict)
