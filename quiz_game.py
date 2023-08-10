def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses  += check_answer(questions.get(key),guess)

        question_num += 1

    display_score(correct_guesses,guesses)
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT...!")
        return 1
    else:
        print("WRONG...!")
        return 0


def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = (correct_guesses/len(questions))*100
    print("Your score is : "+str(score)+"%")



def play_again():

    respone = input("Do you want to play again? (yes/no): ")
    respone = respone.upper()

    if respone == "YES":
        return True
    else:
        return False



questions = {
    "what is the capital of India? ": "A",
    "what is the highest score of Rohit_sharma?": "B",
    "How many double century's Rohit_sharma had?": "C",
    "How many bones are there in human body?": "D"
}
options = [["A. New Delhi", "B. Hyderabad", "C. Chennai", "D. Mumbai"],
           ["A. 204", "B. 264", "C. 246", "D. 216"],
           ["A. 5", "B. 4", "C. 3", "D. 2"],
           ["A. 210", "B. 190", "C. 209", "D. 206"]]

new_game()

while play_again():
    new_game()

print("Byeee..!...Exist")

