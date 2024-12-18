import argparse
from github_user_activity.api_req import fetch_github_activity
from github_user_activity.formatter import format_activity
def main():
    parser = argparse.ArgumentParser(
        description="This script fetches and displays recent activity for a GitHub user. \n"
                    "It shows events such as commits, issues, pull requests, and more from their GitHub account. \n"
                    "To execute the script, follow the command : python github_user_activity.cli <username>"
    )    
    parser.add_argument('username', type=str, help ="Github username to fetch activity for. For example: brindanaveen0109" )
    args = parser.parse_args()

    print(f"Fetching recent activity for GitHub user: {args.username}...\n")
    events = fetch_github_activity(args.username)
    print(format_activity(events))
    
if __name__ == "__main__":
    main()