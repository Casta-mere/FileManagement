import os
from directory import dir
from users import users


class Control:
    def __init__(self):
        self.d = dir.MyDirectory(os.path.abspath('.'))
        self.rootdir = self.d
        self.u = users.users()
        self.username = ""
        self.login()
        self.interface()

    def ls(self):
        f = self.d.get_files()
        d = self.d.get_subdirname()
        total = f+d
        total.sort()
        for i in total:
            if i in f:
                print(f"\033[32m{i}\033[0m")
            else:
                print(f"\033[34m{i}\033[0m")

    def login(self):
        while True:
            os.system('cls')
            username = input("Username: ")
            password = input("Password: ")
            if self.u.validate(username, password) == 2:
                self.username = username
                os.system('cls')

                return True
            elif self.u.validate(username, password) == 1:
                print("Wrong password")
                os.system('pause')
            else:
                print("User not exist")
                if input("Do you want to create a new user? (y/n): ") == "y":
                    self.u.add_user(username, password)
                    self.username = username
                    return True

    def interface(self):
        print(f"{self.username}@{self.d.get_pathname()}:~$ ", end="")
        while True:
            cmd = input().split(' ')
            if cmd[0] == "ls":
                self.ls()
            elif cmd[0] == "cd":
                try:
                    self.cd(cmd[1])
                except:
                    pass
            elif cmd[0] == "tree":
                self.tree()
            elif cmd[0] == "exit":
                return
            elif cmd[0] == "clear":
                os.system('cls')
            elif cmd[0] == "mkdir":
                try:
                    self.d.mkdir(cmd[1])
                except:
                    print("Invalid dir name!")
            elif cmd[0] == "rmdir":
                try:
                    self.d.rmdir(cmd[1])
                except:
                    print(f"Dir {cmd[1]} not exist")
            elif cmd[0] == "chmod":
                try:
                    temp = self.d.chmod(self.username, cmd[1], cmd[2])
                    if temp is not None:
                        print(temp)
                except:
                    print("Command not complete")
            elif cmd[0] == "touch":
                try:
                    result = self.d.touch(self.username, cmd[1])
                    if (result is not None):
                        print(result)
                except:
                    print("Error!")
            elif cmd[0] == "rm":
                try:
                    result = self.d.rm(self.username, cmd[1])
                    if (result is not None):
                        print(result)
                except:
                    print("Error!")
            elif cmd[0] == "logout":
                self.login()
            elif cmd[0] == "":
                pass
            else:
                symbol = " "
                print(f"Command {symbol.join(cmd)} not found")
            print(f"{self.username}@{self.d.get_pathname()}:~$ ", end="")

    def cd(self, path):
        if path == "..":
            if self.d.get_parent() != None:
                self.d = self.d.get_parent()
        else:
            p = path.split('/')
            temp = self.d
            for i in p:
                if i in temp.get_subdirname():
                    temp = temp.subdir[temp.get_subdirname().index(i)]
                else:
                    print("No such file or directory")
                    return
            self.d = temp

    def tree(self):
        self.d.tree()


os.system('cls')
c = Control()
