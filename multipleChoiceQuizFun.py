from Question import Question

question_promopts = [
    "What colour are apples? \n(a) Red/Green \n (b) Purple \n (c) Orange \n\n",
    "What colour are bananas? \n(a) Black \n (b) Yellow \n (c) Magenta \n\n",
    "What colour are strawberries? \n(a) Red \n (b) Purple \n (c) Orange \n\n",
]

questions = [
    Question(question_promopts[0], "a"),
    Question(question_promopts[1], "b"),
    Question(question_promopts[2], "a"),
]

def run_test(questions):
    score = 0;
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)