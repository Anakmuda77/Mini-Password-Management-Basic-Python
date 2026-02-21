import json
paswdJson = dict()
path = r'C:\Users\advan\Documents\Pemrograman\Python\Basic Exercise\Mini Password Manager/passwords.json'


class user:
    def __init__(self,account,name,password):
        self.account = account
        self.name = name
        self.password = password

    def createAccount(self):
        paswdJson[self.account] = {'username':self.name, 'password': self.password}
        with open(path,'a') as f:
            f.write(json.dumps(paswdJson))


