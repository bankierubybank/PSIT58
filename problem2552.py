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
#plot graph for all problem of year 2552
import matplotlib.pyplot as ptl
x = [province]
y1 = [problem_1]
y2 = [problem_2]
y3 = [problem_3]
y4 = [problem_4]
y5 = [problem_5]
y6 = [problem_6]
y7 = [problem_7]
y8 = [problem_8]
p1=plt.plot(x,y1,'ro-')
p2=plt.plot(x,y2,'go-')
p3=plt.plot(x,y3,'bo-')
p4=plt.plot(x,y4,'yo-')
p5=plt.plot(x,y5,'r*-')
p6=plt.plot(x,y6,'g*-')
p7=plt.plot(x,y7,'b*-')
p8=plt.plot(x,y8,'y*-')
plt.legend((p1[0],p2[0],p3[0],p4[0],p5[0],p6[0],p7[0],p8[0]),('problem 1','problem 2','problem 3','problem 4','problem 5','problem 6','problem 7','problem 8'))
plt.title("Problem of year 2552")
plt.xlabel("Province")
plt.ylabel("number of problem")
plt.show()
