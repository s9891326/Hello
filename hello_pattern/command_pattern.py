# 命令模式：用來給應用添加Undo操作
# 命令模式幫助我們把一個操作（undo，redo，copy，paste等）封裝成一個物件，通常是創建一個包含Operation所有邏輯和方法的類。
# 通過命令模式可以控制命令的執行時間和過程，還可以用來組織事務。 用一些檔操作類來說明命令模式的使用

import os


class RenameFile:
    
    def __init__(self, path_src, path_dest):
        """ 在init里保存一些必要信息，比如undo需要的老的和新的文件名 """
        self.src, self.dest = path_src, path_dest
    
    def execute(self, verbose=False):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)
    
    def undo(self, verbose=False):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


def delete_file(path, verbose=False):
    if verbose:
        print("deleting file '{}".format(path))
    os.remove(path)


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt
    
    def execute(self, verbose=False):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)
    
    def undo(self):
        delete_file(self.path)


class ReadFile:
    def __init__(self, path):
        self.path = path
    
    def execute(self, verbose=False):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')

def main():
    orig_name, new_name = 'file1', 'file2'
    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)
    [c.execute() for c in commands]
    
    answer = input('reverse the executed commands? [y/n] ')
    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()
    for c in reversed(commands):
        try:
            c.undo()   # 执行undo
        except AttributeError:
            pass

if __name__ == '__main__':
    main()
