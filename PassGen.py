import random

PasswordLenght = input("Password Lenght: ")

charlist = "abcdefghıjklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!'^+%&/()=?>£#${[]}}|"
GeneratedChars = 0
genpass = []

while 3 == 3:
	GeneratedChars = GeneratedChars + 1
	if GeneratedChars == int(PasswordLenght) + 1:
		break	

	GenerateChar = random.randint(0,len(charlist) -1)
	genpass.append(charlist[GenerateChar])

print("Generated Password: " + "".join(genpass))
