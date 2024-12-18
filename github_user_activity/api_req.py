import requests
import sys

def fetch_github_activity(username): 
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url)
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
