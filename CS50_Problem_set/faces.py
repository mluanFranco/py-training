def convert(emoticon):
    emoticon =  emoticon.replace(":)", "🙂")
    emoticon =  emoticon.replace(":(", "🙁")
    return emoticon


def main():
    message = input("")
    emoji = convert(message)
    print(emoji)

main()
