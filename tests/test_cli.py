import unittest
import sys
from github_user_activity.cli import main


class TestCLI(unittest.TestCase):

    def test_main_with_no_arguments(self):
        """Test CLI without any arguments."""
        sys.argv = ["github_activity.py"]  # No username provided
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 2)  # Exits with code 2 if incorrect arguments are provided

if __name__ == "__main__":
    unittest.main()
