import os
import json
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
        self.files[self.get_filename().index(filename)].chmod(p)

    def touch(self, username, filename):
        if(filename in self.filesname):
            return "File exists"
        self.filesname.append(filename)
        os.open(self.path+'/'+filename, os.O_CREAT)
        self.files.append(MyFile(self.path+'/'+filename, self, username))

    def rm(self, username, filename):
        if(filename not in self.filesname):
            return "No such file or directory"
        author, p1, p2 = self.files[self.get_filename().index(
            filename)].get_p()
        p1 = int(p1)
        p1 = p1 & 2
        p1 = p1 and (username == author)
        p2 = int(p2)
        p2 = p2 & 2
        p2 = p2 and (username != author)

        if(username != "root" and not p1 and not p2):
            return "Permission denied"

        self.files[self.get_filename().index(filename)].rm()
        self.files.remove(self.files[self.get_filename().index(filename)])
        self.filesname.remove(filename)


class MyFile:
    def __init__(self, path, parent=None, author=None):
        self.path = path
        self.filename = path.split('/')[-1]
        self.parent = parent
        self.permissionsdir = f"{path[:-1*len(self.filename)]}.{self.filename}.json"
        self.author, self.p1, self.p2 = self.get_p()
        if(author != None):
            self.author = author
            self.chmod((self.p1 + self.p2))

    def get_p(self):
        if os.path.exists(self.permissionsdir):
            pass
        else:
            with open(self.permissionsdir, 'w') as f:
                f.write('{"author":"root","p1": "7", "p2": "7"}')

        j = json.load(open(self.permissionsdir))
        return j["author"], j["p1"], j["p2"]

    def rm(self):
        try:
            os.remove(self.path)
            os.remove(self.permissionsdir)
        except:
            pass

    def chmod(self, p):
        self.p1 = p[0]
        self.p2 = p[1]
        with open(self.permissionsdir, 'w') as f:
            dict = {"author": self.author, "p1": self.p1, "p2": self.p2}
            json.dump(dict, f)


# d = MyDirectory(os.path.abspath('.'))
# for i in d.files:
#     i.get_p()
