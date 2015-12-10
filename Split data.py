#Split data each year to list of each problem.
import csv
table = []
file=open('pol_stat2551.csv')
data_51=csv.reader(file)
table.append([row for row in data_51])
file=open('pol_stat2552.csv')
data_52=csv.reader(file)
table.append([row for row in data_52])
file=open('pol_stat2553.csv')
data_53=csv.reader(file)
table.append([row for row in data_53])
file=open('pol_stat2554.csv')
data_54=csv.reader(file)
table.append([row for row in data_54])
file=open('pol_stat2555.csv')
data_55=csv.reader(file)
table.append([row for row in data_55])
file=open('pol_stat2556.csv')
data_56=csv.reader(file)
table.append([row for row in data_56])
file=open('pol_stat2557.csv')
data_57=csv.reader(file)
table.append([row for row in data_57])
province = []
problem_1 = [[], [], [], [], [], [], []]
problem_2 = [[], [], [], [], [], [], []]
problem_3 = [[], [], [], [], [], [], []]
problem_4 = [[], [], [], [], [], [], []]
problem_5 = [[], [], [], [], [], [], []]
problem_6 = [[], [], [], [], [], [], []]
problem_7 = [[], [], [], [], [], [], []]
problem_8 = [[], [], [], [], [], [], []]

for i in range(9): #i is number of problem.
    for j in range(7): # j is year.
        for k in range(1, 78): # k is province.
            if i == 0 and j == 0:
                province.append(table[j][k][i])
            if i == 1:
                problem_1[j].append(int(table[j][k][i]))
            if i == 2:
                problem_2[j].append(int(table[j][k][i]))
            if i == 3:
                problem_3[j].append(int(table[j][k][i]))
            if i == 4:
                problem_4[j].append(int(table[j][k][i]))
            if i == 5:
                problem_5[j].append(int(table[j][k][i]))
            if i == 6:
                problem_6[j].append(int(table[j][k][i]))
            if i == 7:
                problem_7[j].append(int(table[j][k][i]))
            if i == 8:
                problem_8[j].append(int(table[j][k][i]))
