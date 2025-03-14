def log_action(action):
    with open("activity.log", "a") as file:
        file.write(action + "\n")
