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
                paswdJson[self.account] ={'username':self.name, 'password': self.password}

                with open(path,'w') as f :
                    f.write(json.dumps(paswdJson))

        
        except:
            paswdJson[self.account] = {'username':self.name, 'password': self.password}
            with open(path,'a') as f:
                f.write(json.dumps(paswdJson))


    # Melihat list Akun yang sudah disimpan
    def seeAllAccount(self):
        with open (path,'r') as f :
            paswdJson = json.loads(f.read())
            print("-----Koleksi Akun----")
            for i in list(paswdJson):
                print("Tipe Akun : ",i)
                print("- Username :  ",paswdJson[i]['username'])
                print("- Password :  ",paswdJson[i]['password'])

