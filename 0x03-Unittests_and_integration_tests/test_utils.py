#!/usr/bin/env python3
"""
Unit tests for utils.py
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('requests.get') as mock_get:  # <-- FIXED
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)



class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator"""

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            obj = TestClass()
            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map_0(self):
        """Test that access_nested_map returns correct values for given inputs."""
        # your test code here


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map function."""

    def test_access_nested_map_0(self):
        """Test that access_nested_map returns correct values for given inputs."""
        # test code...



with patch.object(
    TestClass, "a_method", return_value=42
) as mock_method:






class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""

    def test_access_nested_map_0(self):
        """Test that access_nested_map returns correct values for given inputs."""
        # test code...



import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos method."""

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get and configure side_effect."""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url.endswith("/orgs/google"):
                return MockResponse(cls.org_payload)
            if url.endswith("/orgs/google/repos"):
                return MockResponse(cls.repos_payload)
            return MockResponse(None)

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher for requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns expected repos."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)


class MockResponse:
    """Helper mock response object with .json() method."""

    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload
