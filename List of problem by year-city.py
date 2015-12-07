"""Print list of problem by year/city"""
import csv
import matplotlib.pyplot as plt
import numpy as np

def sum_of_problem_year(year):
    """Return sum of problem by year"""
    temp = 0
    selected_data = 'pol_stat' + str(year) + '.csv'
    with open(selected_data) as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
            for i in range(1, len(row)):
                temp += int(row[i])
    print('END OF YEAR', str(year), 'SUM OF PROBLEM =', str(temp))
    return temp

def list_of_problem_city(city):
    """Return list of problem by city"""
    years = list(range(2551, 2555))
    temp = []
    sum_of_problem = 0
    for year in years:
        selected_data = 'pol_stat' + str(year) + '.csv'
        with open(selected_data) as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                if row[0] == city:
                    data_per_year = []
                    for i in row:
                        if i.isalpha():
                            data_per_year.append(i)
                        else:
                            data_per_year.append(int(i))
        temp.append(data_per_year)
    for i in range(len(temp)):
        sum_of_problem += sum(temp[i][1:])
    return temp

def problem_per_year_to_problem_type():
    """Convert problem per year(input from list_of_problem_city)
    into problem type"""
    year = 4
    problem = []
    for i in range(year):
        temp = list_of_problem_city('Bangkok')[i][1:]
        problem.append(temp)
    problem = np.array(problem)
    array = problem.reshape(year,10)
    array = array.transpose()
    return array
    
def plot_problem_by_city():
    """Plot problem by city"""
    years = [2551,2552,2553,2554]
    array = problem_per_year_to_problem_type()
    plt.title("Plot problem by city")
    p1 = plt.plot(years,array[0], ':bp')
    p2 = plt.plot(years,array[1], ':r*')
    p3 = plt.plot(years,array[2], ':gp')
    p4 = plt.plot(years,array[3], ':kD')
    plt.legend((p1[0],p2[0],p3[0],p4[0]),('Problem1','Problem2','Problem3','Problem4'))
    plt.xlabel("Year")
    plt.ylabel("Y")
    plt.show()
plot_problem_by_city()
