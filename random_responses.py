from random import choice


def get_random_response() -> str:
    random_list: list[str] = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet.",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else.",
        "Can you please clarify what you mean?",
        "I'm not sure I understand, could you explain it differently?",
        "Let's try that again in different words.",
        "I'm having trouble understanding, can you ask in another way?",
        "Oops! That doesn't make sense to me. Try again?",
        "I'm sorry, but I'm not sure what you mean.",
        "Could you provide more details?",
        "I'm not quite following, can you rephrase?",
        "I didn't get that. Could you try saying it differently?",
        "That seems unclear to me. Can you elaborate?"
    ]

    return choice(random_list)


if __name__ == '__main__':
    for i in range(5):
        print(get_random_response())
