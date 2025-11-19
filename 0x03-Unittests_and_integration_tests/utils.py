#!/usr/bin/env python3
"""
Utility functions for unit testing.
"""

def access_nested_map(nested_map, path):
    """Access a nested map with a given path."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """Get JSON from a URL."""
    import requests
    response = requests.get(url)
    return response.json()


def memoize(fn):
    """Decorator to memoize a function."""
    attr_name = "_{}".format(fn.__name__)

    @property
    def memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return memoized
