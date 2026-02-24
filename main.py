from userFunc import user

# typePaswd = input("Masukkan Jenis Password yang ingin anda masukkan")
# userName = input("Masukkan Passowrd Anda")

typePaswd = "Telegram"
userName = "preman"
password = "Macanpekutuk"

NewUser = user.user(typePaswd,userName,password)
# NewUser.createAccount()
NewUser.editAccount("Telegram")
# NewUser.delAccount("dfjdlfjdlf")

# NewUser.seeAllAccount()


