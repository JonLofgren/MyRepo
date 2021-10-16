classes = []


class MakeClass:
    def __init__(self):
        self.class_name = input("What is the name of the class that you are adding?\n")
        self.student = []
        self.grades = []
        self.average = 0
        while True:
            add_choice = input("Want to add a student and his or her grade? Y|n\n").lower()
            if add_choice == "y" or add_choice == "":
                self.student.append(input("What is the student's name?\n"))
                while True:
                    grade = input(f"What is {self.student[-1]}'s grade (A, B, C, D, or F)?\n").upper()
                    if grade not in list("ABCDF"):
                        print("Please input a valid choice!")
                        continue
                    else:
                        self.grades.append(grade)
                        if grade == "A":
                            self.average += 4
                        elif grade == "B":
                            self.average += 3
                        elif grade == "C":
                            self.average += 2
                        elif grade == "D":
                            self.average += 1
                        elif grade == "F":
                            self.average += 0
                        break
            elif add_choice == "n":
                if len(self.student) > 0:
                    self.average /= len(self.student)
                break
            else:
                print("Please input a valid choice!")


def print_lists():
    if len(classes) == 0:
        print("There are no classes entered!")
    else:
        while True:
            print("Please choose a class:")
            for i in range(len(classes)):
                print(f"{i}) {classes[i].class_name}")
            try:
                class_choice = int(input())
                if class_choice not in range(len(classes)):
                    print("Please input a valid choice!")
                    continue
                else:
                    for index in range(len(classes[class_choice].student)):
                        print(f"{classes[class_choice].student[index]} got a grade of"
                              f" {classes[class_choice].grades[index]}")
                    print(f"The class {classes[class_choice].class_name}"
                          f" has an average GPA of {round(classes[class_choice].average, 1)}\n")
                    break
            except ValueError:
                print("Please input a valid choice!\n")


def main():
    while True:
        choice = input("Add a class - a\nList grades - b\nExit (does not save data) - c\n").lower()
        if choice == "a":
            classes.append(MakeClass())
        elif choice == "b":
            print_lists()
        elif choice == "c":
            break
        else:
            print("Invalid input!\n")


if __name__ == "__main__":
    main()
else:
    exit()
