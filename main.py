from userFunc import user

# typePaswd = input("Masukkan Jenis Password yang ingin anda masukkan")
# userName = input("Masukkan Passowrd Anda")

typePaswd = "Instagram"
userName = "Dito"
password = "Macanpekutuk"

NewUser = user.user(typePaswd,userName,password)
NewUser.createAccount()
