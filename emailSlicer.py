userInput = input("Masukan alamat email anda : \n")

if '@' in userInput:
    # Split the email into username and domain
    username, domain = userInput.split('@')
else: 
    username = " "
    domain = " "

print("Username:", username)
print("Domain : ", domain)    