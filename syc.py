import os

class FileSyc:
    def __init__(self):
        self.srcPath = ''
        self.destPath = ''
    def copyFile(self,fileName):
        srcfile = self.srcPath+'/'+fileName
        destfile = self.destPath+'/'+fileName
        f1 = open(srcfile,'rb')
        f2 = open(destfile,'wb')
        
        
