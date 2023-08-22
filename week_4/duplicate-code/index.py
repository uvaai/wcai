def fake_index(list_, element):
    """
    This function shows how index works internally. It loops over all elements
    in the list and returns the index of the first occurance of the element
    that was searched.
    """
    for i in range(len(list_)):
        elem = list_[i]
        if elem == element:
            return i

def find_last_summerday(dates, temps):
    '''
    This function finds the last summerday in a list of temperatures containing
    exactly one heatwave. A summerday is a day where the temperature is at least
    25 degrees.

    Returns the date of the last summerday.
    '''
    summerday_threshold = 25

    # Wrong result because of use of .index()...
    # for temp in temp:
    #     if temp >= summerday_threshold:
    #         last_temp = temp
    #     else:
    #         return dates[temps.index(last_temp)]

    # Correct use of looping over indices
    for i in range(len(temps)):
        temp = temps[i]
        if temp >= summerday_threshold:
            last_date = dates[i]
        else:
            return last_date

if __name__ == "__main__":
    dates = ['19450601', '19450602', '19450603', '19450604', '19450605', '19450606']
    temps = [24.0, 25.1, 24.9, 28.3, 27.3, 25.1, 23.2]

    # This will give 19450602, which is the first time 25.1 degrees is reached
    print(fake_index(temps, 25.1))

    # This function will give the last date that has a temperature over 24.9
    print(find_last_summerday(dates, temps))
