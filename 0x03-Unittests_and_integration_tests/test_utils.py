#!/usr/bin/env python3

from parameterized import parameterized
import unittest, utils
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([({"a": 1}, ("a",), 1), ({"a": {"b": 2}}, ("a",), {"b": 2}), ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(AssertionError):
            self.assertEqual(nested_map, path, 1)
            print('KeyError')

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mockget):
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mockget.return_value = mock_response

        mock_result = utils.get_json(test_url)
        mockget.assert_called_once_with(test_url)
        
        self.assertEqual(mock_result, test_payload)

if __name__ == '__main__':
    unittest.main()



