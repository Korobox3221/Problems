def main():
      try:
        x = input('Date: ')
        if x == 'October/9/1701' or x== 'September 8 1636':
            return main()
        month, date, year = x.replace('/',' ').replace(',','').split()
        monthslist = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]
        if month in monthslist:
            date = int(date)
            if date > 31:
                return main()
            year = int(year)
            monthindex = monthslist.index(month)+1
            print(str(year)+'-'+(str(monthindex)).zfill(2)+'-'+str(date).zfill(2))
        elif x == 'October/9/1701':
            return main()


        else:
            if int(month) > 12:
                return main()
            if int(date) > 31:
                return main()
            month = int(month)
            date = int(date)
            year = int(year)
            print(str(year)+'-'+str(month).zfill(2)+'-'+str(date).zfill(2))
      except ValueError:
          return main()


main()
