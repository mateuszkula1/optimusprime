import csv

DATE=0
TIME=1
SYMBOL=2
AMOUNT=3
PRICE=4
SIDE=5

textfile = open("exec_02.09.txt")
lines = textfile.readlines()
reversed_content = []

if ("\n" not in lines[-1]):
    lines[-1] = lines[-1] + "\n"

for line in reversed(lines):
    reversed_content.append(line)

csv_sorted_string = ''.join(reversed_content)

reader = csv.reader(csv_sorted_string.splitlines())
for row in reader:
    print(row)