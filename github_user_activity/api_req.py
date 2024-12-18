import requests

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("HTTP request successful")
        elif response.status_code == 404:
            print("User not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect. {e}")

    return []