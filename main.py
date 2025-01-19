import csv
from time import sleep

dict = input("Which dictionary would you want to go over? (csv document):")
first, last = input("Please enter the first number and the last number of the dictionary(split by space):").split()
first, last = int(first), int(last)
data = []

with open(".\\dictionary\\" + dict + ".csv", "r", encoding="utf-8-sig") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

right_words_num = 0
false_words = []
for i in range(first-1, last):
    print("\033[H\033[J")
    print("== {} ==".format(data[i][1]))
    word = input()
    if word == data[i][0]:
        print("-- True --")
        right_words_num += 1
    else:
        print("-- false {} --".format(data[i][0]))
        print("true: \033[31{}\033[0m".format(data[i][0]))
        false_words.append(data[i])
    input()
    # sleep(0.1)

print("\033[H\033[J")
print("=== True:{}/{} ===".format(right_words_num, last-first+1))
print("False Words: ", false_words)