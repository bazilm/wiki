import re


username_regex = '([a-zA-Z0-9-_]{3,16}$)'
password_regex = '([a-zA-Z0-9-_]{6,20}$)'
email_regex = '(.{1,16})@(.{3,10}).com'
message = None

def validate(username,password,verify=None,email=None):
	username_match=re.match(username_regex,username)
	global message
	
	if username_match:
		password_match = re.match(password_regex,password)

		if password_match:
			if verify:
				if password==verify:
					if email:
						email_match = re.match(email_regex,email)

						if  email_match:
							pass
						else:
							message = "Invalid email"

				else:
					message="Passwords doesn't match"
		else:
			message = "Invalid Password"

	else:
		message = "Invalid Username"

	return message
