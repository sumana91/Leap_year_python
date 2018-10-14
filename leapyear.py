import sys
import datetime

Feb = 2
TwentyNine = 29

def dayOfDate(date):
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    dayNumber = date.weekday()
    return days[dayNumber]


def checkLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def findNearestLeapYears(year):
    years = []
    if year % 4 == 0:
        years.append(year-4)
        years.append(year+4)
    elif year % 4 == 2:
        if (checkLeapYear(year+2)):
            years.append(year+2)
        else:
            years.append(year+6)

        if(checkLeapYear(year-2)):
            years.append(year-2)
        else:
            years.append(year-6)
    elif year % 4 == 1:
        if(checkLeapYear(year-1)):
            years.append(year-1)
        else:
            years.append(year+3)
    else:
        if(checkLeapYear(year+1)):
            years.append(year+1)
        else:
            years.append(year-3)
    return years


def yearFunction(year):
    if((len(year) == 4) and (int(year[0]) > 0)):
        year = int(year)
        print("input :")
        print(year)
        # Check Leap Year
        isLeapYear = checkLeapYear(year)
        if isLeapYear:
            extraDay = datetime.date(year, Feb, TwentyNine)
            print("Output :")
            print("Its a leap year")
            print("Day : "+dayOfDate(extraDay))
        else:
            nearestLeapYears = findNearestLeapYears(year)
            print("Output :")
            print("This is not a leap year")
            print("Nearest leap years :")
            for y in nearestLeapYears:
                extraDay = datetime.date(y, Feb, TwentyNine)
                print("Year : "+str (y))
                print("Day : "+dayOfDate(extraDay))
    else:
        print("Invalid Year Input")


if __name__ == "__main__":
    y = (sys.argv[1])
    if(y):
        yearFunction(y)
    else:
        print("Invalid Year Input")
