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
    years = list(range(2551, 2553))
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
        print('Year', str(2551 + i), '=', temp[i])
    print('Sum of Problem in ' + str(len(years)), 'Years =', sum_of_problem)
list_of_problem_city('Bangkok')
