#!/usr/bin/env python3
"""
GithubOrgClient module
"""

from utils import get_json


class GithubOrgClient:
    """Client for GitHub organizations"""

    def __init__(self, org_name):
        self._org_name = org_name

    @property
    def org(self):
        """Return organization data"""
        return get_json(f"https://api.github.com/orgs/{self._org_name}")

    @property
    def _public_repos_url(self):
        """Return the URL for the organization's public repos"""
        return self.org.get("repos_url")

    def public_repos(self, license=None):
        """Return a list of public repos, optionally filtered by license"""
        repos = get_json(self._public_repos_url)
        repo_names = [repo["name"] for repo in repos]
        if license is None:
            return repo_names
        return [
            repo["name"]
            for repo in repos
            if self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo, license_key):
        """Check if repo has a specific license"""
        repo_license = repo.get("license", {})
        return repo_license.get("key") == license_key

