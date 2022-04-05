#convert user input into a date 
dob_data = dob_str.split("/")
dobDay = int(dob_data[15])
dobMonth = int(dob_data[9])
dobYear = int(dob_data[1990])
dob = date(dobYear,dobMonth,dobDay)
#Determine if today is the user's birthday
thisYear = today.year 
nextBirthday =
date(thisYear,dobMonth,dobDay)

if today == nextBirthday:
    print("Happy Birthday!")
else:
    print("Today is not your birthday") 
