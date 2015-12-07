"""Print list of problem by year/city"""
def list_of_problem_year(year):
    """print list of problem by year"""
    import csv
    temp = 0
    selected_data = 'test_pol_stat' + str(year) + '.csv'
    with open(selected_data) as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
            for i in range(1, len(row)):
                temp += int(row[i])
    print('END OF YEAR', str(year), 'SUM OF PROBLEM =', str(temp))

def list_of_problem_city(city):
    """print list of problem by city"""
    import csv
    years = list(range(2551, 2555))
    temp = []
    sum_of_problem = 0
    for year in years:
        selected_data = 'test_pol_stat' + str(year) + '.csv'
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

def test_plot():
    """Test matplotlib"""
    import matplotlib.pyplot as plt
    import numpy as np
    x = [2551,2552,2553,2554]
    y = []
    for i in range(4):
        temp = list_of_problem_city('Bangkok')[i][1:]
        y.append(temp)
        print(temp)
    y = np.array(y)
    z = y.reshape(4,4)
    z = z.transpose()
    plt.title("Test matplotlib with data from list_of_problem_city")
    p0 = plt.plot(x,z[0], ':bp')
    p1 = plt.plot(x,z[1], ':r*')
    p2 = plt.plot(x,z[2], ':gp')
    p3 = plt.plot(x,z[3], ':kD')
    plt.legend((p0[0],p1[0],p2[0],p3[0]),('Problem1','Problem2','Problem3','Problem4'))
    plt.xlabel("Year")
    plt.ylabel("Y")
    plt.show()
test_plot()
