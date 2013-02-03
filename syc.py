import os

class FileSyc:
    def __init__(self):
        self.srcPath = ''
        self.destPath = r'C:\Users\ZH\Documents\∞Ÿ∂»‘∆\poj code\notebook'
        self.filelist = os.listdir(self.destPath)
        self.filemap = {}
        for f in self.filelist:
            self.filemap[f] = 1
    def copyFile(self,src,dest):
        f1 = open(src,'rb')
        f2 = open(dest,'wb')
        for line in f1:
            f2.write(line)
        f1.close()
        f2.close()
    def searchDir(self,sdir,func):
        contents = os.listdir(sdir)
        os.chdir(sdir)
        cwd = os.getcwd()
        for e in contents:
            #print e
            if os.path.isdir(e):
                self.searchDir(e,func)
                os.chdir(cwd)
            else:
                fullpath = os.path.join(cwd,e)
                func(fullpath)
    def sycSourceFile(self,path):
        ext = os.path.splitext(path)[1]
        fdir = os.path.split(path)[0]
        if(ext=='.cpp'):
            self.copy(path)
    def copy(self,src):
        fdir = os.path.split(src)[0]
        fileName = os.path.split(src)[1]
        pos = fdir.rfind(os.sep)
        pdir = fdir[pos+1:]
        if(self.filemap.has_key(pdir)):
            print '%s already exits'%pdir
            return
        newDir = self.destPath+os.sep+pdir
        print src
        print newDir+os.sep+fileName
        os.mkdir(newDir)
        self.copyFile(src,newDir+os.sep+fileName)

syc = FileSyc()
syc.searchDir(r'D:\My Program\POJ',syc.sycSourceFile)
        
