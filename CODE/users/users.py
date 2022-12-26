import json
file = f"CODE/users/users.json"

class users:
    def __init__(self):
        self.j = json.load(open(file))


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


if __name__ == "__main__":
    u = users()
