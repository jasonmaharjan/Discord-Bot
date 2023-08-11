def handle_responses(message) -> str:
    message = message.lower()

    # ! is for commands, ? for help
    if message[0] == "!" or message[0] == "?":

        if message == "?help":
            return "Help will only be given to those who need it."

        else:
            return "Command is incorrect"
