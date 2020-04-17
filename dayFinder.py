months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def useBigBrainToCalculateTheDay(year, month, day):

    totalDaysPassed = (year - 2) * 365.2422222
    for i in range(month):
        totalDaysPassed += months[i]
    totalDaysPassed += day
    dayNumber = (int) (totalDaysPassed % 7)
    return daysOfTheWeek[dayNumber - 1]

def main():
    print("Obviously if you don't input only numbers when asked to do so program will not work.")
    year = (int)(input("year: "))
    month = (int)(input("month(number): " ))
    day = (int)(input("day"))
    # if you were to input a month greater than 12 this program would crash so dont. 
    print(useBigBrainToCalculateTheDay(year, month, day))

main()