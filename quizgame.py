questions = (("how many planets known in the solar system"),
             ("how many continents on earth"),
             ("how many bones in the human body"),
             ("whats 5 * 5 "))
options = (("A.8","B.23","C.9"),
           ("A.7","B.6","C.5"),
           ("A.206","B.207","C.208"),
           ("A.25","B.30","C.20"))
answers = (("A"),
           ("A"),
           ("A"),
           ("A"))
guessess = []
question_num = 0
score = 0

for question in questions:
    print("-------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter your guess: ").upper()
    guessess.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} was the correct answer")
    question_num += 1

print("-------------")
print("-------------")
print("-------------")
print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

score = int(score/len(answers)) * 100

import os
os.system("pause")


