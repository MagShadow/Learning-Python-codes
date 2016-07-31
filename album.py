#设计一个通讯录程序
#数据存放在同一目录下的“album.dat”文件中
class person:
    '''Represents a person,containing his/her personal info'''
    def __init__(self,name,pnum='',email=''):
        '''Use 3 arguments to initialize'''
        self.name=name
        self.pnum=pnum
        self.email=email
    def __str__(self):
        return(self.name+' '+self.pnum+' '+self.email)
#p=person("Yang","13051220808","1500011342@pku.edu.cn")
class album:
    '''Represents the album I need'''
    #应当有查找、新建、修改、删除等功能
    def __init__(self):
        '''Almost nothing to init'''
        self.n=0
        self.plist=[]
        print("Album-Init")
    def search(self,target=''):
        if self.n==0:
            print("Now the album is empty!")
            return
        else:
            rslt=0
            for i in self.plist:
                if (target in i.name) or (target in i.pnum) or (target in i.email):
                    rslt+=1
                    print(rslt,i)
            if rslt==0:
                print("No such info found!")
                return
            else:
                print("Totally {0} results found!".format(rslt))
                ch=input("What to do next?Modify(m)/Delete(d)/Return(r)-->")
                if ch=='r':
                    return
                elif ch=='d':
                    index=int(input("Input the index you want to delete:"))
                    temp=0
                    for i in self.plist:
                        if (target in i.name) or (target in i.pnum) or (target in i.email):
                            temp+=1
                            if temp==index:
                                del i
                                print("Successfully deleted!")
                elif ch=='m':
                    index=int(input("Input the index you want to modify:"))
                    print(index)
                    n_ch=input("Input the name:")
                    p_ch=input("Input the phone number:")
                    e_ch=input("Input the email:")
                    temp=0
                    for i in self.plist:
                        if (target in i.name) or (target in i.pnum) or (target in i.email):
                            temp+=1
                            if temp==index:
                                i.name=n_ch
                                i.pnum=p_ch
                                i.email=e_ch
                                print("Successfully Modified!")
                else:
                    print("No such command!")
    def add(self,name='',pnum='',email=''):
        p=person(name,pnum,email)
        self.n+=1
        self.plist.append(p)
    def showdetail(self):
        print("Totally {0} records.".format(self.n))
        temp=0
        for i in self.plist:
            temp+=1
            print(temp,i)
#myalbum=album()
#myalbum.search("Yang")
#p=person("Yang","13051220808","1500011342@pku.edu.cn")
#myalbum.add("Yang","13051220808","1500011342@pku.edu.cn")
#myalbum.search("Yang")
import os
import pickle

if os.path.exists('album.dat'):
    f=open('album.dat','rb')
    myalbum=pickle.load(f)
    f.close()
else:
    myalbum=album()
    #使用之前必须实例化！

class TooLessArgExcp(Exception):
    '''Nothing to init'''

try:
    while True:
        ch=input("Input the command(-help for info):")
        clist=ch.split()
        if clist[0]=="-help":
            print("-help/-save/-list/-exit/-search XXX/-add XXX XXX XXX")
        elif clist[0]=="-save":
            f=open('album.dat','wb')
            pickle.dump(myalbum,f)
            f.close()
        elif clist[0]=="-list":
            myalbum.showdetail()
        elif clist[0]=="-exit":
            break
        elif clist[0]=="-search":
            if len(clist)<2:
                print("Too less arguments were given!")
                continue
            myalbum.search(clist[1])
        elif clist[0]=="-add":
            if len(clist)<4:
                print("Too less arguments were given!")
                continue
            myalbum.add(clist[1],clist[2],clist[3])
        else:
            print("No such command!(-help for info)")
except TooLessArgExcp:
    print("Too less arguments are given!")
except:
    print("Unknown Error!")
