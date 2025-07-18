#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""
    @parameterized.expand([
        ("google", {"url": "https://api.github.com/orgs/google",
                    "repos_url": "https://api.github.com/orgs/google/repos"},),
        ("abc", {"url": "https://api.github.com/orgs/abc",
                 "repos_url": "https://api.github.com/orgs/abc/repos"},)])
    @patch("client.get_json")
    def test_org(self, test_org, test_object, mockget):
        """Test the org method of GithubOrgClient."""
        mockget.return_value = test_object
        org_client = GithubOrgClient(test_org)
        mock_result = org_client.org

        mockget.assert_called_once_with(
            f"https://api.github.com/orgs/{test_org}",
        )
        mockget.assert_called_once()
        self.assertEqual(mock_result, test_object)
