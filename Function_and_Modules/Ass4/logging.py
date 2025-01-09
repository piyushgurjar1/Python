def log(username,activity):
    with open("activity_log.txt", "a") as file:
        file.write(f"{username}: {activity}\n")