#!/usr/bin/env python
#coding:utf-8

__author__ ="Nick"
__repository__ ="liuwenlong"
__SysErrCode__ =128
#################### 

import sys,time,os,re

#################### 

class GIT_CMD:
    print ('''

    #################################################
    #   Automate deployment scripts for Git Manage  #
    #          (c)nick_liuwenlong@163.com           #
    #  https://github.com/longwenliu/ProjManage.git #
    #   Copyright Author Nick.All Rights Reserved.  #
    #################################################

    ''')
    print("\r\n###---Nick DEMO---###\r\n")
    print("\r\nGit Auto Manage Tool\r\n")

    def _init_(self,Root,U_Name,U_PWD,RemoteRepos,LocalRepos):
        
        self.Root = ""
        self.U_Name = ""
        self.U_PWD = ""
        self.RemoteRepos = ""
        self.LocalRepos = ""
        self.Type = ""
        
    def RootInput(self,fileRootPath):
        self.Root = fileRootPath + "//"

    def Pull(self):
        raw_input('Notice : GIT PULL will be run !!! ')
        os.system('git pull')

    def Push(self):
        raw_input('Notice : GIT PULL will be run !!! ')
        os.system('git push')

    def AddAll(self):
        raw_input('Notice : GIT ADD will be run !!! ')
        R_Sta = True
        self.LocalRepos = raw_input('Please input the git remote repository name: ')
        if "" == self.LocalRepos:
            self.LocalRepos = "test"
        try:
            R_Sta = os.system('cd '+ self.Root + self.LocalRepos + "//")
            R_Sta = os.system('git add -A https://www.github.com/'+ self.U_Name + "/test " + self.Root + self.LocalRepos + ".git ")
            #R_Sta = os.system('git add -A https://www.github.com/' + self.U_Name + "/"  + self.LocalRepos + ".git ")
            #R_Sta = os.system('git add -A ' + self.Root + self.LocalRepos)
            
            #print ("Sta - >%d")%R_Sta
            #TODO 生成装饰器，避免重复代码编写
            if R_Sta == __SysErrCode__:
                print("\r\n############---Warning---#################\r\n")
                print ("#################################################")            
                print (">> git Work Path ->[%s]")%self.Root
                print (">> git remote user name ->[%s]")%self.U_Name
                print (">> git remote repository name ->[%s]")%self.RemoteRepos
                print (">> git Local repository name ->[%s]")%self.LocalRepos
                print ("#################################################")  
                raw_input('\r\nPlease check Input message is all right!')               

        except ZeroDivisionError,e:
            print("\r\n############---Error---#################\r\n")
            print ("#################################################")            
            print (">> git Work Path ->[%s]")%self.Root
            print (">> git remote user name ->[%s]")%self.U_Name
            print (">> git remote repository name ->[%s]")%self.RemoteRepos
            print (">> git Local repository name ->[%s]")%self.LocalRepos
            print ("#################################################")  
            raw_input('\r\nPlease check Input message is all right!')            
            R_Sta = __SysErrCode__  
        return R_Sta 

    def Commit(self):
        raw_input('Notice : GIT COMMIT will be run !!! ')
        GIT_Message = raw_input('Warning : Please input release notes !!! ')
        
        if "" != GIT_Message:
            os.system('git commit -m ' + GIT_Message)
        else:
            GitCommit(self)
        
    def Clone(self):
        R_Sta = True
        self.RemoteRepos = raw_input('Please input the git remote repository name: ')
        if "" == self.RemoteRepos:
            self.RemoteRepos = "test"
            
        self.LocalRepos = raw_input('Please input the git Local repository name: ')
        if "" == self.LocalRepos:
            self.LocalRepos = self.RemoteRepos
        
        try:
            R_Sta = os.system('git clone https://www.github.com/' + self.U_Name + "/"  + self.RemoteRepos + ".git " + self.Root + self.LocalRepos)
            #print ("Sta - >%d")%R_Sta
            #TODO 生成装饰器，避免重复代码编写
            if R_Sta == __SysErrCode__:
                print("\r\n############---Warning---#################\r\n")
                print ("#################################################")            
                print (">> git Work Path ->[%s]")%self.Root
                print (">> git remote user name ->[%s]")%self.U_Name
                print (">> git remote repository name ->[%s]")%self.RemoteRepos
                print (">> git Local repository name ->[%s]")%self.LocalRepos
                print ("#################################################")  
                raw_input('\r\nPlease check Input message is all right!')               

        except ZeroDivisionError,e:
            print("\r\n############---Warning---#################\r\n")
            print ("#################################################")            
            print (">> git Work Path ->[%s]")%self.Root
            print (">> git remote user name ->[%s]")%self.U_Name
            print (">> git remote repository name ->[%s]")%self.RemoteRepos
            print (">> git Local repository name ->[%s]")%self.LocalRepos
            print ("#################################################")  
            raw_input('\r\nPlease check Input message is all right!')             
            R_Sta = __SysErrCode__
        return R_Sta 
    def AutoPush(self):
        fileroot = sys.path[0] + "//"
        GitAddAll()
        GitCommit()
        GitPush()
        
        


def mkdir(path):

    path += "\\"
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        try :
            os.makedirs(path) 
        except ZeroDivisionError,e:
            # NowTime = time.strftime('%m-%d[%H.%M.%S]',time.localtime(time.time()))
            # path = "Exception_" + NowTime
            # mkdir(path)
            return False            
        return True
    else:
        # 如果目录存在则创建附加时间戳
        # NowTime = time.strftime('%m-%d[%H.%M.%S]',time.localtime(time.time()))
        # path += "_" + NowTime
        # mkdir(path)
        return False
        
def welcome():

    print ('''

    #################################################
    #   Automate deployment scripts for Git Manage  #
    #          (c)nick_liuwenlong@163.com           #
    #  https://github.com/longwenliu/ProjManage.git #
    #   Copyright Author Nick.All Rights Reserved.  #
    #################################################

    ''')

def IntheEnd():
    #os.system('python Resources/Py27_AutoCreateProj_DEMO.py')
    print ('Have a fun!!!')

def NewCreate(path):
    #raw_input('\r\nPlease confirm that the input is correct!\r\n')
    try:
        return mkdir(path)
    finally:
        print ("Create OK,->%s")%path  

def GitManage(GIT):

    GIT_CMD.Type = raw_input('''
Please Input Git CMD,As follows:
>> [A/a]:add;
>> [C]:clone;
>> [c]:commit;
>> [P]:pull;
>> [p]:push;
''')
    fileRootPath = sys.path[0]
    GIT_CMD.RootInput(GIT,fileRootPath)
    if GIT_CMD.Type == "A" or GIT_CMD.Type == "a": 
        return GIT_CMD.AddAll(GIT)
    elif GIT_CMD.Type == "C":
        return GIT_CMD.Clone(GIT)
    elif GIT_CMD.Type == "c":
        return GIT_CMD.Commit(GIT)
    elif GIT_CMD.Type == "P":
        return GIT_CMD.Pull(GIT)
    elif GIT_CMD.Type == "p":
        return GIT_CMD.Push(GIT)
    else:
        print "Input Error!\r\n"
        return GitManage()        
        
def GitAutoManage(DEMO_Author):
    GIT = GIT_CMD()#类实例化
    if DEMO_Author == "Nick":
        # fileroot = sys.path[0] + "\\Resources\\ProjDemoArchitecture-V2.txt"
        # ProjDemo = open(fileroot,"r")
        # ProjDemoLines = ProjDemo.readlines()
        GIT.U_Name = "longwenliu"
    else:
        DEMO_Author = raw_input('Please input the git remote user name: ')
        if DEMO_Author == __repository__:
            DEMO_Author = "longwenliu"
        GIT.U_Name = DEMO_Author
    R_Sta = __SysErrCode__
    while (R_Sta == __SysErrCode__):
        R_Sta = GitManage(GIT)
        
if __name__ == "__main__":

    DEMO_Author = __author__
    GitAutoManage(DEMO_Author)      

