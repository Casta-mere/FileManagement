import json
file = f"CODE/users/users.json"
file2 = f"users/users.json"
class users:
    def __init__(self):
        try:
            self.j = json.load(open(file))

        except:
            self.j = json.load(open(file2))

    def validate(self, username, password):
        # 0: user not exist
        # 1: password wrong
        # 2: success
        if username in self.j:
            if self.j[username] == password:
                return 2
            else:
                return 1
        return 0

    def add_user(self, username, password):
        if(username in self.j):
            return f"User {username} already exist"
        self.j[username] = password
        self.writeback()
        return "Success"

    def remove_user(self, username):
        del self.j[username]
        self.writeback()

    def writeback(self):
        json.dump(self.j, open(file, "w"))
    
    def change_password(self, username, password):
        if self.validate(username, password) == 2:
            self.j[username] = input("New password: ")
            self.writeback()
            return "Success"
        else:
            return "Wrong password"

if __name__ == '__main__':
    pass
