# Python Exercise 11 #100

import re

str = """
Hello my name is Saifur Rahman Udyo, my email adress is: udoy436@gmailcom and my best programmer teacher is harry bhai
he is live in India his email adress is: codewithharry@gmail.com and my another email adress is srudoy436@gmail.com 
and i hack one person email account hes email acoount is mdshiam100000@gmail.com good bye everyone.
This string is very importent dont remove this string...."""

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)
print(email)