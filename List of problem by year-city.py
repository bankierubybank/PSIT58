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
    temp = [city,0,0,0,0]
    for year in years:
        selected_data = 'test_pol_stat' + str(year) + '.csv'
        with open(selected_data) as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                if row[0] == city:
                    for i in range(1, len(row)):
                        temp[i] += int(row[i])
    sum_of_problem = sum(temp[1:])
    print(temp, '=', sum_of_problem)
