import smtplib
my_email = "javedmomin99999@gmail.com"
password = "testing@123!"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # Above Code is to be used by default to send emails using gmail addresses.
    connection.starttls()
    #connection.starttls() increases security of message . i.e., your message is end-to-end encrypted TLS means Transport Layer Security
    connection.login(user = my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="javedmomin99@gmail.com",
                        msg="Subject : Hello \n\n Hiiii Javed, \n How are You? \n I hope you have received this Testing Message \n Have a Good Day Bro!!!! \n\n\n Regards, \n Md Javed Momin \n Data Analyst \n Azent Overseas Education Ltd"
                        )
    #connection.close()
