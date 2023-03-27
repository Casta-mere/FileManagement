import os
import json
# Modify the rootpath to your own path
rootpath = r"D:\Onedrive\OneDrive - txsxcy\Project\FileManagement"

class MyDirectory:
    def __init__(self, path, parent=None):
        self.path = path
        self.pathname = path.replace(rootpath, 'home')
        self.dirname = path.split('/')[-1]

        self.subdirname = []
        self.subdir = []

        self.filesname = []
        self.files = []

        self.parent = parent

        temp = os.listdir(self.path)
        for i in temp:
            if(i.find('.') == -1):
                self.subdirname.append(i)
                self.subdir.append(MyDirectory(self.path+'/'+i, self))
            elif(i == '.git'):
                self.filesname.append(i)
                self.files.append(MyFile(self.path+'/'+i, self))
            elif(not i.startswith('.')):
                self.filesname.append(i)
                self.files.append(MyFile(self.path+'/'+i, self))

    def get_files(self):
        return self.filesname

    def get_subdirname(self):
        return self.subdirname

    def get_filename(self):
        return self.filesname

    def get_parent(self):
        return self.parent

    def tree(self, level=0):
        if level == 0:
            print(f"\033[34m{self.pathname}\033[0m")
        else:
            print('   '*level+f"\033[34m{self.dirname}\033[0m")
        for i in self.filesname:
            print('   '*(level+1)+i)
        for i in self.subdir:
            i.tree(level+1)

    def mkdir(self, dirname):
        os.mkdir(self.path+'/'+dirname)
        self.subdirname.append(dirname)
        self.subdir.append(MyDirectory(self.path+'/'+dirname, self))

    def rmdir(self, dirname):
        self.subdir.remove(self.subdir[self.get_subdirname().index(dirname)])
        self.subdirname.remove(dirname)
        os.rmdir(self.path+'/'+dirname)

    def get_pathname(self):
        return self.pathname

    def chmod(self, username, filename, p):
        if(filename not in self.filesname):
            return "No such file or directory"
        if(username != "root" and username != self.files[self.get_filename().index(filename)].author):
            return "Permission denied"
        self.files[self.get_filename().index(filename)].chmod(p,0)

    def touch(self, username, filename):
        if(filename in self.filesname):
            return "File exists"
        self.filesname.append(filename)
        os.open(self.path+'/'+filename, os.O_CREAT)
        self.files.append(MyFile(self.path+'/'+filename, self, username))

    def rm(self, username, filename):
        # Determine if the file exists
        if(filename not in self.filesname):
            return "No such file or directory"

        # Determine if the user has permission to delete the file
        author, p1, p2, state = self.files[self.get_filename().index(
            filename)].get_p()

        p1 = int(p1)
        p1 = p1 & 2  # using xor to get write permission
        p1 = p1 and (username == author)

        p2 = int(p2)
        p2 = p2 & 2  # using xor to get write permission
        p2 = p2 and (username != author)

        if(username != "root" and not p1 and not p2):
            return "Permission denied"

        # Delete the file
        self.files[self.get_filename().index(filename)].rm()
        self.files.remove(self.files[self.get_filename().index(filename)])
        self.filesname.remove(filename)

    def mv(self, username, old, new):
        if(old not in self.filesname):
            return "No such file or directory"
        if(new in self.filesname):
            return "File exists"
        author, p1, p2, state = self.files[self.get_filename().index(
            old)].get_p()

        p1 = int(p1)
        p1 = p1 & 2
        p1 = p1 and (username == author)

        p2 = int(p2)
        p2 = p2 & 2
        p2 = p2 and (username != author)

        if(username != "root" and not p1 and not p2):
            return "Permission denied"

        oldpath = self.path+'/'+old
        newpath = self.path+'/'+new
        oldpermissionpath = f"{self.path}/.{old}.json"
        newpermissionpath = f"{self.path}/.{new}.json"

        self.files[self.get_filename().index(old)].path = newpath
        self.files[self.get_filename().index(old)].filename = new
        self.files[self.get_filename().index(
            old)].permissionsdir = newpermissionpath
        self.filesname[self.get_filename().index(old)] = new
        os.rename(oldpath, newpath)
        os.rename(oldpermissionpath, newpermissionpath)

    def cp(self, username, old, new):
        if(old not in self.filesname):
            return "No such file or directory"
        if(new in self.filesname):
            return "File exists"
        self.touch(username, new)

    def cat(self, username, filename):
        if(filename not in self.filesname):
            return "No such file or directory"
        author, p1, p2 ,state= self.files[self.get_filename().index(
            filename)].get_p()

        p1 = int(p1)
        p1 = p1 & 4
        p1 = p1 and (username == author)

        p2 = int(p2)
        p2 = p2 & 4
        p2 = p2 and (username != author)

        if (username != "root" and not p1 and not p2):
            return "Permission denied"

        return self.files[self.get_filename().index(filename)].cat()

    def echo(self, username, content, filename):
        if(filename in self.filesname):
            return "File alreadt exists!"
        self.touch(username, filename)
        self.files[self.get_filename().index(filename)].echo(content)

    def find(self, filename):
        if(filename in self.filesname):
            return self.pathname+'/'+filename
        for i in self.subdir:
            if(i.find(filename) != None):
                return i.find(filename)
        return None

    def vi(self, username, filename):
        # Determine if the file is being edited by another user
        author, p1, p2, state = self.files[self.get_filename().index(
            filename)].get_p()
        if state == "2":
            return "File is being edited by another user"

        # Determine if the user has permission to edit the file
        p1 = int(p1)
        p1 = p1 & 6
        p1 = p1 and (username == author)

        p2 = int(p2)
        p2 = p2 & 6
        p2 = p2 and (username != author)

        if(username != "root" and not p1 and not p2):
            return "Permission denied"

        if(filename not in self.filesname):
            return "No such file or directory"
        self.files[self.get_filename().index(filename)].vi()


class MyFile:
    def __init__(self, path, parent=None, author=None):
        self.path = path
        self.filename = path.split('/')[-1]
        self.parent = parent
        self.permissionsdir = f"{path[:-1*len(self.filename)]}.{self.filename}.json"
        self.author, self.p1, self.p2, self.state = self.get_p()
        # 0 - available
        # 1 - reading
        # 2 - writing
        if(author != None):
            self.author = author
            self.chmod((self.p1 + self.p2), self.state)

    def get_p(self):
        if os.path.exists(self.permissionsdir):
            pass
        else:
            with open(self.permissionsdir, 'w') as f:
                f.write('{"author":"root","p1": "7", "p2": "7","state": "0"}')

        j = json.load(open(self.permissionsdir))
        return j["author"], j["p1"], j["p2"], j["state"]

    def rm(self):
        try:
            os.remove(self.path)
            os.remove(self.permissionsdir)
        except:
            pass

    def chmod(self, p, state):
        self.p1 = p[0]
        self.p2 = p[1]
        with open(self.permissionsdir, 'w') as f:
            dict = {"author": self.author, "p1": self.p1,
                    "p2": self.p2, "state": state}
            json.dump(dict, f)

    def cat(self):
        with open(self.path.replace('/', r'\\'), 'r', encoding="utf-8") as f:
            return f.read()

    def echo(self, content):
        with open(self.path.replace('/', r'\\'), 'w', encoding="utf-8") as f:
            f.write(content)
            f.close()

    def vi(self):
        self.chmod((self.p1 + self.p2), "2")
        os.system("cls")
        print(self.cat())
        while(True):
            content = input()
            if(content == ":wq"):
                break
            self.echo(self.cat()+content+'\n')
        self.chmod((self.p1 + self.p2), "0")


# d = MyDirectory(os.path.abspath('.'))
# for i in d.files:
#     i.get_p()

if __name__ == '__main__':
    pass
