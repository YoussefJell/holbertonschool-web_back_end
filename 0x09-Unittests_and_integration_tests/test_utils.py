#!/usr/bin/env python3
""" Parameterize a unit test, Mock HTTP calls, Parameterize and patch """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ test class """
    """ param """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """ test func """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    """  param """
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test func """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ test class """
    """ param """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test func """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ test class """

    def test_memoize(self):
        """ test func """
        class TestClass:
            """ test class """

            def a_method(self):
                """ test func  """
                return 42

            @memoize
            def a_property(self):
                """ propertie """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            testClass = TestClass()
            testClass.a_property
            testClass.a_property
            mockMethod.assert_called_once
