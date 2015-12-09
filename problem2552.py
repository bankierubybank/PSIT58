#import problem year 2552
import csv
file=open('pol_stat2552-Table-1.csv')
data=csv.reader(file)
table=[row for row in data]
province, problem_1 = [], []
for i in table[1:78]:
    province.append(i[0])
    problem_1.append(i[1])
