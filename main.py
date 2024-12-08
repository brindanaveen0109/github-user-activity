import sys
import requests

def fetch_github_activity(username): 
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("htpp request successful")
            return response.json()
        elif response.status_code == 404:
            print("User not found")
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect. {e}")
    return []

def display_activity(events):
    if not events:
        print("No recent activity found or failed to fetch activity.")
        return
    for event in events[:5]:
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        action = ""

        if event_type == "PushEvent":
            commits = len(event["payload"]["commits"])
            action = f"Pushed {commits} commit(s) to"
        elif event_type == "PullRequestEvent":
            action = f"{event['payload']['action'].capitalize()} a pull request in"
        else:
            action = f"Performed {event_type} on"

        print(f"- {action} {repo_name}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        return

    username = sys.argv[1]
    print(f"Fetching recent activity for GitHub user: {username}...\n") 
    events = fetch_github_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()
