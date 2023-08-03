from cisc108 import assert_equal



def parse_date_month(date: string) -> int:
    '''
    Consumes a 'date' string and produces an integer
    which is the month from the date.
    
    Args:
        date (str): The string of text that show the date, which
            includes the month, date, and year.
    Returns:
        int: The month as an integer value.
    '''
    if '/' in date:  
        month = date[:(date.index('/'))]
        month_Int = int(month)
        if month_Int >= 1 and month_Int <= 12:
            result = month_Int
        else:
            result = -1
    else:
        result = -1
    return result

assert_equal(parse_date_month("1/27/20"),1)
assert_equal(parse_date_month("5/8/14"),5)
assert_equal(parse_date_month("12/10/04"),12)
assert_equal(parse_date_month("03/2/18"),3)
assert_equal(parse_date_month("-4/18/20"),-1)
assert_equal(parse_date_month("17/21/19"),-1)
assert_equal(parse_date_month("0/0/0000"),-1)




def parse_date_day(date: string) -> int:
    '''
    Consumes a 'date' string and produces an integer
    which is the day from the date.
    
    Args:
        date (str): The string of text that show the date, which
            includes the month, date, and year.
    Returns:
        int: The day as an integer value.
    '''
    if '//' in date:
        result = -1
    elif '/' in date:
        indexOfFirstSlash = date.index('/')
        indexOfSecondSlash = date.find('/', (date.find('/')+1))
        day = date[(indexOfFirstSlash+1):indexOfSecondSlash]
        day_Int = int(day)
        if day_Int >= 1 and day_Int <= 31:
            result = day_Int
        else:
            result = -1
    else:
        result = -1
    return result

assert_equal(parse_date_day("1/27/20"),27)
assert_equal(parse_date_day("1/1/20"),1)
assert_equal(parse_date_day("1/31/20"),31)
assert_equal(parse_date_day("1/-9/20"),-1)
assert_equal(parse_date_day("1/333/20"),-1)
assert_equal(parse_date_day("0/0/0000"),-1)
assert_equal(parse_date_day("1/32/10"),-1)
assert_equal(parse_date_day("1//20"),-1) 




def parse_date_year(date: str) -> int:
    '''
    Consumes a 'date' string and produces an integer
    which is the year from the date.
    
    Args:
        date (str): The string of text that show the date, which
            includes the month, date, and year.
    Returns:
        int: The year as an integer value.
    '''
    if '/' in date:
        indexOfSecondSlash = date.find('/', (date.find('/')+1))
        year = date[(indexOfSecondSlash+1):]
        if len(year) == 2:
            year = "20" + year
            result = int(year)
        elif len(year) == 4:
            result = int(year)
        else:
            result = -1
    else:
        result = -1
    return result
        
assert_equal(parse_date_year("1/27/2020"),2020)
assert_equal(parse_date_year("1/27/1998"),1998)
assert_equal(parse_date_year("1/27/10"),2010)
assert_equal(parse_date_year("1/27/05"),2005)
assert_equal(parse_date_year("1/27/304"),-1)




def is_date(date: str) -> bool:
    '''
    Consumes a 'date' string and produces a boolean
    value that determines if the date is valid.  
    
    Args:
        date (str): The string of text that show the date, which
            includes the month, date, and year.
    Returns:
        bool: Determines whether or not the given date is valid.
    '''
    return parse_date_month(date) != -1 and parse_date_day(date) != -1 and parse_date_year(date) != -1

assert_equal(is_date("1/27/2020"),True)
assert_equal(is_date("2/14/02"),True)
assert_equal(is_date("-1/27/2020"),False)
assert_equal(is_date("1/50/2020"),False)
assert_equal(is_date("1/27/303"),False)
assert_equal(is_date("1/32/10"),False)




def earlier(dateOne: str, dateTwo: str) -> str:
    '''
    Consumes a 'dateOne' string and a 'dateTwo' whose
    year, month, and day are compared to each other
    in order to determine the earlier date, and the
    earlier date is returned as a string. If the date
    is invalid, the string that is produced is 'error';
    and if the dates are exactly the same, the string that
    is produced is 'equal'.
    
    Args:
        dateOne (str): The first string that shows the date, which
            includes the month, date, and year.
        dateTwo (str): The second string that shows the date, which
            includes the month, date, and year.
    Returns:
        str: The date that is earlier, or 'equal'
            if the two dates are the same, or 'error'
            if either date is invalid. 
    '''
    if is_date(dateOne) and is_date(dateTwo):
        if parse_date_year(dateOne) < parse_date_year(dateTwo):
            return dateOne
        elif parse_date_year(dateOne) > parse_date_year(dateTwo):
            return dateTwo
        else:
            if parse_date_month(dateOne) < parse_date_month(dateTwo):
                return dateOne
            elif parse_date_month(dateOne) > parse_date_month(dateTwo):
                return dateTwo
            else:
                if parse_date_day(dateOne) < parse_date_day(dateTwo):
                    return dateOne
                elif parse_date_day(dateOne) > parse_date_day(dateTwo):
                    return dateTwo
                else:
                    return "equal"
    else:
        return "error"
                 
assert_equal(earlier("1/15/06","3/30/10"),"1/15/06")
assert_equal(earlier("1/15/20","3/30/02"),"3/30/02")
assert_equal(earlier("2/15/19","8/30/19"),"2/15/19")
assert_equal(earlier("9/15/18","4/30/18"),"4/30/18")
assert_equal(earlier("5/20/17","5/22/17"),"5/20/17")
assert_equal(earlier("5/30/16","5/8/16"),"5/8/16")
assert_equal(earlier("1/2/3000","1/32/2013"),"error")
assert_equal(earlier("7/8/1999","7/8/1999"),"equal")