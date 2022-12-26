import os

rootpath = r"D:\Onedrive\OneDrive - txsxcy\Project\FileManagement"
class MyDirectory:
    def __init__(self,path,parent=None):
        self.path = path
        self.pathname=path.replace(rootpath,'home')
        self.dirname= path.split('/')[-1]
        self.subdirname = []
        self.subdir=[]
        self.files=[]
        self.parent=parent
        temp = os.listdir(self.path)
        for i in temp:
            if(i.find('.')==-1):
                self.subdirname.append(i)
                self.subdir.append(MyDirectory(self.path+'/'+i,self))
            else:
                self.files.append(i)

    def get_files(self):
        return self.files

    def get_subdirname(self):
        return self.subdirname

    def get_parent(self):
        return self.parent

    def tree(self,level=0):
        if level==0:
            print(f"\033[34m{self.pathname}\033[0m")
        else:
            print('   '*level+f"\033[34m{self.dirname}\033[0m")
        for i in self.files:
            print('   '*(level+1)+i)
        for i in self.subdir:
            i.tree(level+1)

    def get_pathname(self):
        return self.pathname