#import problem year 2552
import csv
file=open('pol_stat2552-Table-1.csv')
data=csv.reader(file)
table=[row for row in data]
province, problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8 = [], [], [], [], [], [], [], [], []
for i in table[1:78]:
    province.append(i[0])
    problem_1.append(i[1])
    problem_2.append(i[2])
    problem_3.append(i[3])
    problem_4.append(i[4])
    problem_5.append(i[5])
    problem_6.append(i[6])
    problem_7.append(i[7])
    problem_8.append(i[8])
