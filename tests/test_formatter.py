import unittest
from github_user_activity.formatter import format_activity

class TestFormatter(unittest.TestCase):
    def test_format_push_event(self):
        events = [{
            "type": "PushEvent",
            "repo": {"name": "user/repo1"},
            "payload": {
                "commits": [{"sha": "12345abcde"}]
            }
        }]
        result = format_activity(events)
        self.assertEqual(result, " - Pushed 1 commit(s) to user/repo1")

    def test_format_pull_event(self):
        events = [{
            "type": "PullRequestEvent",
            "repo": {"name": "user/repo2"},
            "payload": {
                "action": "opened"
            }
        }]
        result = format_activity(events)
        self.assertEqual(result, " - Opened a pull request inuser/repo2")
if __name__ == "__main__":
    unittest.main()