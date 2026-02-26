import json
path = r'C:\Users\advan\Documents\Pemrograman\Python\Basic Exercise\Mini Password Manager/passwords.json'


class user:
    # Constructor method
    def __init__(self,account,name,password):
        self.account = account
        self.name = name
        self.password = password

    # Method untuk membuat Akun baru
    def createAccount(self):
        paswdJson = dict()
        # Mengecek apakah sudah terdapat file dengan nama tersebut atau tidak
        try:
            with open(path,'r') as f:
                # Mengubah Json jadi dictionary
                paswdJson = json.loads(f.read())

                if(self.account in paswdJson):
                    print(self.account," Akun sudah ada dalam sistem")
                else:
                    paswdJson[self.account] ={'username':self.name, 'password': self.password}
                    with open(path,'w') as f :
                        f.write(json.dumps(paswdJson))

                    print("Akun Berhasil Ditambahkan")

        
        except FileNotFoundError:
            paswdJson[self.account] = {'username':self.name, 'password': self.password}
            with open(path,'w') as f:
                f.write(json.dumps(paswdJson))
            print("Akun Berhasil Ditambahkan")



   
def seeAllAccount():
    with open (path,'r') as f :
        paswdJson = json.loads(f.read())
        print("-----Koleksi Akun----")
        for i in list(paswdJson):
            print("Tipe Akun : ",i)
            print("- Username :  ",paswdJson[i]['username'])
            print("- Password :  ",paswdJson[i]['password'])


# Mencari Akun 
def searchAccount(account):
    # Membuka file Json 
    with open (path,'r') as f:
        paswdJson = json.loads(f.read())
    # Mencari key dari akun yang ingin di cari
        if account in list(paswdJson):
            print("- Username : ",paswdJson[account]['username'])
            print("- Pasword : ",paswdJson[account]['password'])

        else:
            print("Akun tidak ditemukan ")

# Edit Account
def editAccount(account):
    # Membuka file Json
    with open (path,'r') as f:
        paswdJson = json.loads(f.read())

    # Mengecek apakah akun ada atau tidak
    if account in list(paswdJson):
        print("Username lama anda adalah : ",paswdJson[account]['username'])
        print("Password lama anda adalah : ",paswdJson[account]['password'])
        print("----Silahkan masukkan username dan password baru anda----")
        newUserName = str(input("Masukkan username baru anda : "))
        newPasword  = str(input("Masukkan password baru anda : "))

        paswdJson[account]['username'] = newUserName
        paswdJson[account]['password'] = newPasword

        # Menulis ulang json file dengan akun yang sudah diedit
        with open (path,'w') as f:
            f.write(json.dumps(paswdJson))

        print("Berhasil diperbaharui")

    else:
        print(account, "Akun tidak ditemukan")


# Menghapus Akun yang ada
def delAccount(account):
    # Mengambil Data Json Terlebih Dahulu
    with open (path,'r') as f:
        paswdJson = json.loads(f.read())
    
    # Mengecek apakah akun yang dicari ada atau tidak
    if account in list(paswdJson):
        del paswdJson[account]
        # Timpa File Yang sudah di hapus dengan Dictionary baru.
        with open (path,'w') as f :
            f.write(json.dumps(paswdJson))
        print("Akun ",account," Berhasil di hapus ")

    else :
        print(account, "Tidak berhasil di temukan")
            
