import requests
import sys

class GitHubActivityFetcher:
    def __init__(self, username):
        self.username = username
        self.url = f"https://api.github.com/users/{self.username}/events"

    def fetch_activity(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print("HTTP request successful")
                return response.json()
            elif response.status_code == 404:
                print("User not found")
                sys.exit(0)
        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to connect. {e}")
            sys.exit(1)
        return []
