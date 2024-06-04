import csv
from time import sleep

dict = input("Which dictionary would you want to go over? (csv document):")
first, last = input("Please enter the first number and the last number of the dictionary(split by space):").split()
first, last = int(first), int(last)
data = []

with open("D:\\Projects\\SpellWords_py\\dictionary\\U1-30.csv", "r", encoding="utf-8-sig") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

right_words_num = 0
false_words = []
for i in range(first-1, last):
    print("\033[H\033[J")
    print("==" + data[i][1] + "==")
    word = input()
    if word == data[i][0]:
        print("true")
        right_words_num += 1
    else:
        print("true: \033[1;31m[37{}\033[0m".format(data[i][0]))
        false_words.append(data[i][0])
    sleep(0.5)

print("\033[H\033[J")
print("=== Right:{}/{} ===".format(right_words_num, last-first+1))
print("False Words: ", false_words)