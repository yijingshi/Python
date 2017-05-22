def main():
    get_date = raw_input ("Please enter a date in form of mm/dd/yy: ")
    print ('the date you enter is: ', get_date)
    date_list = get_date.split('/')
    print ('month: ', date_list [0])
    print ('day: ', date_list [1])
    print ('year: ', date_list [2])
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]

    if month > "12" or month < "01":
        print ('Month has to be in between 1~12, please enter again!')
        return main()
    if day > "31" or day < "01":
        print ('Day has to be in between 1~31, please enter again!')
        return main()
    elif len(year)>2:
        print ("The length must be two digits, in YY")
        return main()
    elif year != "13":
        print ('Year must be 2013!')
        return main()
    else:
        date_output(month,day,year)

def date_output(month,day,year):
    if month == '01':
        month = 'January'
    if month == '02':
        month = 'February'
    if month == '03':
        month = 'March'
    if month == '04':
        month = 'April'
    if month =='05':
        month = 'May'
    if month == '06':
        month = 'June'
    if month == '07':
        month = 'July'
    if month == '08':
        month = 'August'
    if month == '09':
        month = 'September'
    if month =='10':
        month = 'October'
    if month == '11':
        month = 'November'
    if month == '12':
        month = 'December'

    print (month +" "+ day + "," + year)
main()
