#!/usr/bin/env python3

"""test_utils.py
This module contains unit tests for the utils module.
It tests the access_nested_map, get_json, and memoize functions.
"""
from utils import memoize

from parameterized import parameterized
import unittest
import utils
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function."""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test the access_nested_map function."""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test the access_nested_map function raises KeyError."""
        with self.assertRaises(AssertionError):
            self.assertEqual(nested_map, path, 1)
            print('KeyError')


class TestGetJson(unittest.TestCase):
    """Test the get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mockget):
        """Test the get_json function."""
        mockget.return_value.json.return_value = test_payload


        mock_result = utils.get_json(test_url)
        mockget.assert_called_once_with(test_url)

        self.assertEqual(mock_result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test the memoize decorator functionality."""
    def test_memoize(self):
        """Test that the memoize decorator caches the result of a method."""
        class TestClass:
            """ This class is used to test the memoize decorator. """
            def a_method(self):
                """A method that returns a value and should be called once."""
                return 42

            @memoize
            def a_property(self):
                """A property that uses the memoize decorator."""
                return self.a_method()
        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()
            self.assertEqual(mock_method.call_count, 1)


if __name__ == '__main__':
    unittest.main()
