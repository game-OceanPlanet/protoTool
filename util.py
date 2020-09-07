# -*- coding:utf-8 -*- 
import hashlib, subprocess, os, time, shlex
import encoding

def md5(s):
    return hashlib.md5(s).hexdigest()
    
def syscall(s, shll=False):
    encoding.log ('cmd:' + s)
    p = subprocess.Popen(shlex.split(s), stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = shll)
    return p.communicate()[0].decode('UTF-8', errors='ignore')

def combinedir(path, *paths):
    return os.path.abspath(os.path.join(path, *paths))

def getModifyTime(f):
    statinfo=os.stat(f)
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))
    
def combineurl(*parts):
    url = ''
    cnt = len(parts)
    for i in range(cnt-1):
        p = parts[i]
        url = url + p
        if not p.endswith('/'):
            url = url + '/'
    url = url + parts[cnt-1]
    return url