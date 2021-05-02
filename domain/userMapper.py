import json, os
import user
import stock
class userMapper:
    
    def save_users(self,users):
        os.chdir('.')
        print(users)
        with open('users.json',mode='w') as json_file:
            lost=[]
            for key in users:
                results = {}
                results[key]=users[key].as_dict()
                lost.append(results)
            jsdata = json.dumps({"users": lost})
            json_file.write(jsdata)

    def load_users(self):
        os.chdir('.')
        with open('users.json',mode='r+') as json_file:
            data= json.load(json_file)['users']
            usrdic={}
            for obj in data:
                key=list(obj.keys())[0]
                usrdic[key]=user.user([])
                for stonk in obj[key]['stocks']:
                    usrdic[key].stocks.append(stock.stock(stonk['ticker'],stonk['amount'],stonk['costbase']))
            return usrdic
            
