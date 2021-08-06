class Question:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer



question_prompt =[
    "\nWhat color are apples?\n (a)Red/Green\n (b) Purple \n (c) Orange\n\n",
    "\nWhat color are Bananas\n (a)Teal\n(b) Magenta\n (c) Yellow\n\n"

]

questions = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"b")

]

def run_test(questions):
    score=0
    for question in questions:
        answer = input(question_prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions))+ " correct")

run_test(questions)