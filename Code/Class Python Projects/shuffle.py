from random import shuffle as shuf
import os

os.system("cls" if os.name == "nt" else "clear")

my_list = ["Apple", "Banana", "Cherry", "Date", "Fig", "Gundam"]
print(my_list)
shuf(my_list)
print(my_list)
