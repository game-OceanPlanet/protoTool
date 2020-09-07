import os, re

svntool = r'svn'

def update(svnPath):
    cmd = svntool + ' up ' + svnPath
    print (cmd)
    os.system(cmd)

def getVersion(svnPath):
    command=svntool + " log " + svnPath + ' -l 1'
    r = os.popen(command)
    info = r.read()
    return re.search('r(\d+)', info).group(1)

def getUrl(svnPath):
    cmd = svntool + ' info ' + svnPath
    r = os.popen(cmd)
    info = r.read()
    return re.search('URL:(.*)', info).group(1)
    
def commit(svnPath, message):
    cmd = svntool + ' commit ' + svnPath + ' --message \"' + message + '\"'
    print (cmd)
    os.system(cmd)

def revert(svnPath):
    cmd = svntool + ' revert ' + svnPath + ' -R'
    print (cmd)
    os.system(cmd)
    
def cleanup(svnPath):
    cmd = svntool + ' cleanup ' + svnPath
    print (cmd)
    os.system(cmd)
    
def copy(src, dst, msg, add) :
    cmd = svntool + ' copy ' + src + ' ' + dst + ' -m"' + msg + '"' + ' ' + add
    print (cmd)
    os.system(cmd)
    
def delete(src, msg, add) :
    cmd = svntool + ' delete ' + src + ' -m"' + msg + '"' + ' ' + add
    print (cmd)
    os.system(cmd)

def change(svnPath) :
    cmd = 'svn st ' + svnPath
    r = os.popen(cmd)
    print(cmd)
    info = r.readlines()
    for line in info:
        line = line.strip('\n').split('       ')
        one=line[0]
        tow=line[1]
        if one == '?':
            os.system('svn add %s' % tow )
        elif one == '!':
            os.system('svn delete %s' % tow)