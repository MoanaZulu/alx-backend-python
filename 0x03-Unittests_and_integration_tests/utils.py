#!/usr/bin/env python3
"""
Utility functions for unit testing.
"""

import requests


def access_nested_map(nested_map, path):
    """Access a nested map with a given path."""
    current = nested_map
    for key in path:
        if not isinstance(current, dict) or key not in current:
            raise KeyError(key)
        current = current[key]
    return current


def get_json(url):
    """Get JSON from a URL."""
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

