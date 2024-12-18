import argparse
from github_user_activity.api_req import GitHubActivityFetcher
from github_user_activity.formatter import ActivityFormatter

class GitHubUserActivityCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="This script fetches and displays recent activity for a GitHub user. \n"
                        "It shows events such as commits, issues, pull requests, and more from their GitHub account. \n"
                        "To execute the script, follow the command : python github_user_activity.cli <username>"
        )
        self.parser.add_argument('username', type=str, help="GitHub username to fetch activity for. For example: brindanaveen0109")

    def run(self):
        args = self.parser.parse_args()
        username = args.username

        # Create instances of the fetcher and formatter
        fetcher = GitHubActivityFetcher(username)
        formatter = ActivityFormatter()

        # Fetch and format activity
        events = fetcher.fetch_activity()
        formatted_activity = formatter.format_activity(events)

        print(formatted_activity)


if __name__ == "__main__":
    cli = GitHubUserActivityCLI()
    cli.run()
