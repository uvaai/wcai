import math

def is_smaller(a, b):
    return a < b # 12 < 4 => False

def is_bigger(a, b):
    return a > b

def get_temp_and_date(dates, temps, comparison_function):
    '''
    Boilerplate function that will find a single temperature and corresponding
    date depending on a passed comparison_function.
    '''
    some_temp = temps[0]

    for i in range(len(temps)):
        temp = temps[i]

        if comparison_function(temp, some_temp):
            some_temp = temp
            some_date = dates[i]

    return some_date, some_temp

def get_lowest_temp(dates, temps):
    '''
    This function will calculate the lowest temperature and return both the
    date on which this occured and the temperature itself.
    '''
    return get_temp_and_date(dates, temps, is_smaller)

def get_highest_temp(dates, temps):
    '''
    This function will calculate the highest temperature and return both the
    date on which this occured and the temperature itself.
    '''
    return get_temp_and_date(dates, temps, is_bigger)

if __name__ == "__main__":
    dates = ['19450601', '19450602', '19450603', '19450604', '19450605', '19450606']
    temps = [24.0, 25.1, 24.9, 28.3, 27.3, 25.1, 23.2]

    print(get_lowest_temp(dates, temps))
    print(get_highest_temp(dates, temps))
