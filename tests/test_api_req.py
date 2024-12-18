import unittest
from github_user_activity.api_req import fetch_github_activity

class TestAPI(unittest.TestCase):
    def test_fetch_valid_user(self):
        events = fetch_github_activity("brindanaveen0109")
        self.assertIsInstance(events, list)

    