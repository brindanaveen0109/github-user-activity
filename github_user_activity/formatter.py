class ActivityFormatter:
    def format_activity(self, events):
        if not events:
            return "No recent activity found or failed to fetch the activity"

        output = []
        for event in events[:5]:
            event_type = event["type"]
            repo_name = event["repo"]["name"]
            action = ""

            if event_type == "PushEvent":
                commits = len(event['payload']['commits'])
                action = f"Pushed {commits} commit(s) to "
            elif event_type == "PullRequestEvent":
                action = f"{event['payload']['action'].capitalize()} a pull request in"
            else:
                action = f"Performed {event_type} on"

            output.append(f" - {action}{repo_name}")
        return "\n".join(output)
