import pandas as pd 
import smtplib

df = pd.read_excel("mailinglist1.xls", sheet_name=0)
print(df)
e = df[['Emails']]
n = df[['Names']]
c = df[['Cities']]
u = df[['Unis']]

liste = list(df['Emails'])
listn = list(df['Names'])
listc = list(df['Cities'])
listu = list(df['Unis'])
length = len(e)

with smtplib.SMTP('smtp.EMAILPROVIDER.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login("YOUR EMAIL HERE","YOUR PASSWORD HERE")

	subject = "Masters Application Questions 11" 
	

	for i in range(length):
		body = "Subject: {}\n\n{}".format(subject, '''Good morning/afternoon {}, I am interested in joining one of the masters programs you offer at {}, I\'ve checked your website for all the details but I\'d like to ask a few more questions.

1- When do you consider a student to be \"In-state\"?
2- Are there specific prerequisite courses I should\'ve taken in university before applying for a masters at your school?
3- What is the GPA required to be competitive with other applicants?
4- Do you offer any benefits for working students?
5- Do you offer conditional acceptances and can I know more about what scolarships you provide?

If you offer inperson visits or tours I will be in {} from mid June until the end of August.

Thank You

NAME'''.format(listn[i], listu[i], listc[i]))
		smtp.sendmail('EMAIL \@ EMAILPROVIDER', liste[i] , body)
	smtp.quit




