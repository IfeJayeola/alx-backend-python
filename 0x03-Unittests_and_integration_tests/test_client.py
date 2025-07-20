#!/usr/bin/env python3
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch
from client import GithubOrgClient
from fixtures import fixtures


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

    def test_public_repos_url(self):
        """Test the _public_repos_url property."""
        with patch("client.GithubOrgClient.org") as mock_get:
            mock_get.return_value = {
                "repos_url": "https://api.github.com/orgs/gle/repos"}
            client = GithubOrgClient('org_name')
            res = client.org()
            assert res['repos_url'] == "https://api.github.com/orgs/gle/repos"

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """Test the public_repos method."""
        mock_get.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}}
        ]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as pub_get:
            pub_get.return_value = "https://api.github.com/orgs/org/repos"
            git_client = GithubOrgClient('org')
            mock_result = git_client.public_repos()
            mock_get.assert_called_once_with(
                "https://api.github.com/orgs/org/repos")
            self.assertEqual(mock_result, ["repo1", "repo2", "repo3"])
            self.assertEqual(mock_get.call_count, 1)

        @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)])
        def test_has_license(self, repo, license_key, expected):
            """Test the has_license method."""
            assert GithubOrgClient.has_license(repo, license_key) == expected


class TestIntegrationGithubOrgClient(unittest.TestCase):
    @parameterized_class([{
        "org_payload": "fixures.org_payload",
        "repos_payload": "fixtures.repos_payload",
        "expected_repos": "fixtures.expected_repos",
        "apache2_repos": "fixtures.apache2_repos",

    }])
    @classmethod
    def setUp(cls):
        """Set up the test class with mock data."""
        cls.patcher = patch('utils.requests.get')
        cls.mock_get = cls.patcher.start()
        cls.mock_get.return_value.json = fixtures.TEST_PAYLOAD

        def side_effect(url):
            """Mock the requests.get method."""
            if url == "https://api.github.com/orgs/google":
                cls.mock_get.json.return_value = cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                cls.mock_get.json.return_value = cls.repos_payload
            else:
                raise ValueError("Unexpected URL")
            return cls.mock_get
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDown(cls):
        """Stop the patcher after tests."""
        cls.patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method with integration data."""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self, license="apache-2.0"):
        """Test the public_repos method with a specific license."""
        client = GithubOrgClient("google")
        repos = client.public_repos(license=license)
        self.assertEqual(repos, self.apache2_repos)

