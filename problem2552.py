#split problem of year 2552 on list.
import csv
file=open('pol_stat2552-Table-1.csv')
data=csv.reader(file)
table=[row for row in data]
province, problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8 = [x for x in range(1,78)], [], [], [], [], [], [], [], []
for i in table[1:78]:
    problem_1.append(i[1])
    problem_2.append(i[2])
    problem_3.append(i[3])
    problem_4.append(i[4])
    problem_5.append(i[5])
    problem_6.append(i[6])
    problem_7.append(i[7])
    problem_8.append(i[8])
#plot graph for problem 1 of year 2552
import matplotlib.pyplot as ptl
x=[province]
y=[problem_1]
ptl.plot(x,y,':go')
ptl.xlabel("province")
ptl.ylabel("Problem 1")
ptl.show()
