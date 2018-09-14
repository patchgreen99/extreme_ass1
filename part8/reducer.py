#!/usr/bin/python


import sys

sum_total = 0
count_total = 0
winning_total = 0
winning_student = ""
prev_student = ""
student = ""
ignore = ""

for line in sys.stdin:  # For ever line in the input from stdin
    line = line.strip()  # Remove trailing characters
    try:
        studentid, ignore, student = line.split(".")

        if count_total > 3 and prev_student:
            temp = float(sum_total) / float(count_total)
            if temp > winning_total:
                winning_student = prev_student
                winning_total = temp

        sum_total = 0
        count_total = 0

    except:
        studentid, ignore, exam, grade = line.split(".")

        sum_total += int(grade)
        count_total += 1

    prev_student = student



if count_total > 3 and ignore == "1" and float(sum_total)/float(count_total) > winning_total:
    print("{}".format(prev_student))
else:
    print("{}".format(winning_student))





