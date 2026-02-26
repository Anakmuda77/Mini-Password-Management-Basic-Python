from userFunc import user

print("=====SISTEM PENGELOLAAN PASSWORD=====")
a = True
while a == True:
    print("Silahkan Pilih Pilihan Berikut : ")
    print("1. Membuat Akun Baru ")
    print("2. Melihat Akun Yang Sudah Ada ")
    print("3. Mengedit Akun Yang sudah Ada")
    print("4. Mencari Akun Yang sudah Ada")
    print("5. Menghapus Akun Yang sudah Ada")
    print("6. Keluar dari Sistem")
    try:
       i = int(input("Silahkan Pilih Nomor Pilihan Anda: "))
       if(i == 1):
           print("")
           typeAccount = input("Masukkan Nama akun ke dalam sistem : ")
           userName = input("Masukkan username akun anda : ")
           password = input("Masukkan password akun anda : ")
           newUser =user.user(typeAccount,userName,password)
           newUser.createAccount()
           print('')

       elif(i==2):
           print("")
           print("")
           print("===Melihat Semua Account===")
           user.seeAllAccount()
           print("")

       elif(i==3):
           print("")
           account = str(input("Masukkan Akun yang ingin diedit : "))
           user.editAccount(account)
           print("")

       elif(i==4):
           print("")
           account = str(input("Masukkan Akun yang ingin dicari : "))
           user.searchAccount(account)
           print("")

       elif(i==5):
           print("")
           account = str(input("Masukkan Akun yang ingin dihapus : "))
           user.delAccount(account)
           print("")

       elif(i==6):
           print("")
           a = False
           print("===Anda Keluar dari sistem===")
           break
       
       else:
           print('')
           print("Mohon Masukkan Angka sesuai Pilihan")
           print("")
           continue
           
           
           
    except:
        print("")
        print("Mohon Masukkan Angka Pilihan Dengan benar")
        print("")
        continue




