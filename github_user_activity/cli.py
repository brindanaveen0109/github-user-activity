import sys
from github_user_activity.api_req import fetch_github_activity
from github_user_activity.formatter import format_activity
def main():
    if len(sys.argv) != 2:
        print("Usage: python -m github_user_activity <username>")
        return

    username = sys.argv[1]
    print(f"Fetching recent activity for GitHub user: {username}...\n")
    events = fetch_github_activity(username)
    print(format_activity(events))

if __name__ == "__main__":
    main()