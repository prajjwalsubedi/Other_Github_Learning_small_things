import smtplib
import datetime as dt
import random

date = dt.datetime.now()
print(date.weekday())
if date.weekday() == 0:
    with open("quotes.txt") as quotes:
        data = quotes.readlines()
        quote = random.choice(data)
        print(quote)

    my_email = "tt8939892@gmail.com"
    my_password = "zdtvnvciadzgfhbl"
    send_to = "subediprajjwal@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.ehlo()
        connection.login(user=my_email, password=my_password)
        connection.ehlo()
        connection.sendmail(from_addr=my_email, to_addrs=send_to,
                            msg=f"subject:Monday Motivation\n\n{quote}")


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


