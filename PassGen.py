import random

print("Generating Password")
uzunluk = input("Password Lenght: ")

charlist = "abcdefghıjklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!'^+%&/()=?>£#${[]}}|"
randomn = random.random()
axuarray = 0
passlist = []

while 3 == 3:
	axuarray = axuarray + 1
	if axuarray == int(uzunluk) + 1:
		break

	
	randomn1 = random.randint(0,len(charlist) -1)
	passlist.append(charlist[randomn1])

print("Generated Password: " + "".join(passlist))
input()



