import smtplib

carriers = {
	'att': '@mms.att.net',
	'tmobile': '@tmomail.net',
	'verizon': '@vtext.com',
	'sprint': '@page.nextel.com',
	'boost': '@sms.myboostmobile.com',
	'virgin': '@vmobl.com'
}

def send(message):
	#Enter contact numbers or emails in this variable, separated by a comma. Replace 'ten-digit-number' with 
  #the recipient phone number, and replace 'verizon' with the appropriate carrier:
	to_number = 'ten-digit-number{}'.format(carriers['verizon']), 'email_example@gmail.com'
	
  #Enter the sender's (your) email login information here:
	auth = ('your_email@address.com','your_password')
	
  #Your email provider's SMTP server info goes here. If using GMail, leave the server variable
  #as is. Else, replace it with your provider's info:
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(auth[0],auth[1])
	
	server.sendmail(auth[0],to_number,message)
