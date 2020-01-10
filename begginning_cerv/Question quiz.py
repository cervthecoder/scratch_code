from Question import questionclass
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    questionclass(question_prompts[0], "a"),
    questionclass(question_prompts[1], "c"),
    questionclass(question_prompts[2], "b"),


]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)


file = open(username, "r+")
    password = getpass.getpass("Enter your password: ")
    pass_hashed = hashlib.md5(str.encode(password)).hexdigest()
    read_password = file.readline()
