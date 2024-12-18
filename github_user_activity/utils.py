def validate_username(username):
    if not username or not username.isalnum():
        raise ValueError("Invalid GitHub username.")
