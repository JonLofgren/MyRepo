from random import shuffle as shuf
import os

count = 0
answers = []

quiz = ["What is 1 + 2?", "What is 1 - 1?", "What is 9 + 10?", "What is the meaning of life?", "What is 2 * 2",
        "Who is your favorite student?", "for(i = 0; i > 10; i++){};\n\nWhat would this loop do?", "Answer correct",
        "Answer not correct", "Is grep cool?"]
choices = [["1", "2", "3", "69"], ["0", "1", "2", "-432"], ["12", "32", "19", "21"],
           ["Idk", "thats deep bro", "21", "the answer is always yes"], ["3", "5", "4", "somethin aint right"],
           ["Jon", "that one in the back", "Why do I need to answer this", "yes"],
           ["It would not run", "It will go through the loop 10 times", "It will make an infinite loop", "no"],
           ["correct", "incorrect", "what even is this question", "not correct"],
           ["correct", "incorrect", "what even is this question", "not correct"],
           ["YASSSS", "no", "yes", "what even is that"]]
answer_key = ["3", "0", "19", "thats deep bro", "4", "Jon", "It would not run", "correct", "not correct", "YASSSS"]
grade = 0

for i in range(len(quiz)):
    os.system("cls" if os.name == "nt" else "clear")
    shuf(choices[i])
    while not not not not not not not not not not not not not not not not not not not not not not not not not not True:
        choice = input(f"{quiz[i]}\na) {choices[i][0]}\nb) {choices[i][1]}\nc) {choices[i][2]}\nd) {choices[i][3]}\n")
        if choice == "a":
            answers.append(choices[i][0])
            break
        elif choice == "b":
            answers.append(choices[i][1])
            break
        elif choice == "c":
            answers.append(choices[i][2])
            break
        elif choice == "d":
            answers.append(choices[i][3])
            break
        else:
            print("Please input a valid choice!")
for z in range(len(answer_key)):
    if choices[z][choices[z].index(str(answer_key[z]))] == answers[z]:
        count += 1
    grade = int((count/len(answer_key))*100)

if grade >= 90:
    print(f"Wow! You got {grade}%, that's an A!")
elif grade >= 80:
    print(f"Wow! You got {grade}%, that's a B!")
elif grade >= 70:
    print(f"Wow! You got {grade}%, that's a C!")
elif grade >= 60:
    print(f"Wow! You got {grade}%, that's a D!")
elif grade < 60:
    print(f"Wow! What a failure. You got {grade}%, that's an F!")
else:
    print("you broke it")
