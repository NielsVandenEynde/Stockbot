from user import user
import userMapper, os
class userRepo:

    def __init__(self):
        os.chdir('C:\\Users\\niels\desktop\\scripts\\stonkbot\\domain')
        self.mapper=userMapper.userMapper()
        if os.path.getsize('users.json') > 0:
            self.users=self.mapper.load_users()
            
        else: self.users={}
        print(len(self.users))
        print(self.users)

    def add_user(self, id):
        usr=user(stocks=[])
        if not str(id) in self.users:
            self.users[str(id)]=usr
            self.save_users()
            return 0
        else:
            return 1
        
        
    def load_users(self):
        return self.mapper.load_users()

    def save_users(self):
        print(self.users)
        self.mapper.save_users(self.users)




        