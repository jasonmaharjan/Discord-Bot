import vocab


def handle_responses(message) -> str:
    message = message.lower()

    # ! is for commands, ? for help
    if message[0] == "!" or message[0] == "?":

        if message == "?help":
            return "Help will only be given to those who need it."

        elif message == "!joke":
            return "You"

        elif message == "!word" or message == "!w":
            return vocab.get_word()

        elif message.split(" ")[0] == "!meaning" or message.split(" ")[0] == "!m":
            return vocab.get_meaning(message.split(" ")[1])

        elif message == "!sleep":
            return "https://tenor.com/view/sleep-time-gif-25989026"

        else:
            return "Command is incorrect"
