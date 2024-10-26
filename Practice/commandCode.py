import os

class moveFileCommand(object):
    def  __init__(self,src, dst):
        self.src = src
        self.dst = dst
        os.rename(self.src, self.dst)

    def undoCommand(self):
        os.rename(self.dst, self.src)



stack = []
command = moveFileCommand('main.txt','temp.txt')


stack.append(command)


            

