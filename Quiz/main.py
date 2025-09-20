# Quiz Application: Python Test MCQs

import json     #importing json cuz of quiz.json file have questions

#main quiz function

def main_quiz():
    print("Welcome To Python MCQs Test \n")
    init_score = 0      #initialize Score as 0

    #Loading Questions from file

    with open ("quiz.json", "r") as file:
        quiz = json.load(file)

    #looping through each questions
    for q in quiz:
        print(q["question"])
        for options in q ["options"]:
            print(options)
            
        user_answer = input("Select an Option: A/B/C/D: ").upper()

        if user_answer == q["answer"]:
            print("CORRECT!\n")
            init_score += 1
        else:
            print(f"INCORRECT! The correct answer is {q['answer']}\n")

    #Calculating Final Results
    print(f"Your Final Score is {init_score}/{len(quiz)}")
    percent = (init_score / len(quiz) * 100)
    print(f"That’s {percent:.2f}% correct!\n")

main_quiz()
