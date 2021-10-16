import os

quiz = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class MakeQuiz:
    def __init__(self):
        self.quiz_name = input("What do you want to call this quiz?\n")
        self.questions = []
        self.answers = []
        self.possible_answers = [[]]
        while True:
            choice = input("Add a question? Y|n\n").lower()
            if choice == "y" or choice == "":
                self.questions.append(input("What would you like the question to be?\n"))
                self.possible_answers.append([])
                for i in list("abcd"):
                    self.possible_answers[len(self.questions) - 1].append(f"{i} - " + input(f"What is option {i}?\n"))
                while True:
                    choice_for_correct = input("What is the correct answer (a, b, c, or d)?\n")
                    if choice_for_correct in list("abcd"):
                        self.answers.append(choice_for_correct)
                        break
                    else:
                        print("Please input a valid choice!\n")
            elif choice == "n":
                break
            else:
                print("Please input a valid choice!\n")


def main():
    while True:
        choice1 = input("Would you like to make a quiz? Y|n\n").lower()
        if choice1 == "y" or choice1 == "":
            quiz.append(MakeQuiz())
        elif choice1 == "n":
            if len(quiz) == 0:
                print("There are not quizzes to be taken!")
                break
            elif len(quiz) > 0:
                choice2 = input("Would you like to take a quiz? Y|n\n").lower()
                if choice2 == "y" or choice2 == "":
                    while True:
                        try:
                            print("Which quiz would you like to take?")
                            for i in range(len(quiz)):
                                print(f"{i} - {quiz[i].quiz_name}")
                            quiz_choice = int(input())
                            if quiz_choice not in range(len(quiz)):
                                print("Please input a valid choice!")
                                continue
                            answers_to_questions = []
                            for i in range(len(quiz)):
                                if quiz_choice == i:
                                    for num in range(len(quiz[quiz_choice].questions)):
                                        while True:
                                            print(f"Question {num + 1}\n{quiz[quiz_choice].questions[num]}")
                                            for index in range(4):
                                                print(f"{quiz[quiz_choice].possible_answers[num][index]}")
                                            answer = input()
                                            if answer == "a":
                                                answers_to_questions.append("a")
                                                break
                                            elif answer == "b":
                                                answers_to_questions.append("b")
                                                break
                                            elif answer == "c":
                                                answers_to_questions.append("c")
                                                break
                                            elif answer == "d":
                                                answers_to_questions.append("d")
                                                break
                                            else:
                                                print("Please input a valid choice!")
                                    count = 0
                                    print(answers_to_questions)
                                    print(quiz[quiz_choice].answers)
                                    for grade in range(len(answers_to_questions)):
                                        if answers_to_questions[grade] == quiz[quiz_choice].answers[grade]:
                                            count += 1
                                    average = round((count/len(answers_to_questions)) * 100, 2)
                                    print(f"You got grade of {average}%!")
                            break
                        except ValueError:
                            print("Please input a valid choice!")
                elif choice2 == "n":
                    print("aight, imma head out")
                    break
                else:
                    print("Please input a valid choice!")
        else:
            print("Please input a valid choice!\n")


if __name__ == "__main__":
    main()
else:
    quit()
