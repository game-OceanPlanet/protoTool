#!/usr/bin/python
# -*- coding:utf-8 -*- 
import os
import sys
import json
import svn
from util import syscall
from fileUtil import FileUtil
#reload(sys)
#sys.setdefaultencoding("utf-8")

def _runCommand(cmd, logfile, cdPath, encode='utf-8'):
		# print('## cd ' + cdPath)
		os.chdir(cdPath) 
		logstr = syscall(cmd, True)
		if logfile.strip() != '':
			logbyte = FileUtil.read(cdPath + logfile)
			logstr = logbyte.decode(encode)
			# print(logstr)

currentPath = os.getcwd()
configName = sys.argv[1]

with open(currentPath + "/" + configName + ".json",'r',encoding= 'utf8') as fconfig:
	content = fconfig.read()
	content = content.replace('\\', '/')
	jConfig = json.loads(content)
	protoPath = jConfig['protoPath']
	codePath = jConfig['codePath']
	path = protoPath + "/message.proto"
	path1 = currentPath + "/proto_ts/MessageID.ts"
	path2 = currentPath + "/proto_ts/ProtoMsgTemplate.ts"
	newpath = codePath + "/src/com/breeze/game/server/"

print('runing')
# 更新proto
#svn.cleanup(protoPath)
#svn.revert(protoPath)
#svn.update(protoPath)

protofilePath = codePath + "/protobuf/protofile"
bundlesPath = codePath + "/protobuf/bundles"

# 删除原来的文件
print('deleting old files')
FileUtil.del_file(protofilePath)
FileUtil.del_file(bundlesPath)
print('copying proto files')
FileUtil.xcp(protoPath, protofilePath, 'proto')

# 根据proto生成js库
print('generating libs with proto, wait for a moment ...')
_runCommand('pb-egret generate', '', codePath + "/")

# 生成MessageID.ts,ProtoMsgIdMap.ts
print('generating ts files')
filename = "MessageID"
filename2 = "ProtoMsgIdMap"

contentstr = ""
classNames = []
file = open(path,"r",encoding= 'utf8')
str = file.readline()
str = file.readline()

# ����д�����˵�����ļ��ײ� ���Բ���ȡ
while str.find("}") == -1 :
	str = str.lstrip()
	str = str.rstrip() 
	str = str.replace("\t","")
	str = str.replace("\n","")
	if str == "" :
		str = file.readline()
		continue
	if str.find("=") == -1 :
		str = file.readline()
		continue
	if str.find("{") == -1 :
		if str.find("//") == 0 :
			str = file.readline()
			continue
		arr = str.split("=")
		arr0 = arr[0].rstrip()
		arr[1] = arr[1].rstrip()
		
		if arr0.find("S_") > -1:
			classNames.append(arr0)
		elif (arr0.find("SYNC_")) > -1:
			classNames.append(arr0)
			
		if arr[1].find("//") > -1:
			darr = arr[1].split("//")
			contentstr += "/** " + darr[1] + " */\n\t\t"
			contentstr += "public static " + arr0 + ":number =" + darr[0] + "\n\t\t"
		else :
			contentstr += "public static " + arr0 + ":number =" + arr[1] + "\n\t\t"
	str = file.readline()
	
# ����ӳ���ļ� MessageID.ts
file = open(path1,"r",encoding= 'utf8')
temp = file.read();
temp = temp.replace("$params$", contentstr)
newfile = open(newpath + filename + ".ts","w",encoding= 'utf8')
newfile.write(temp)
newfile.flush()
newfile.close()


# ����ӳ���ļ� ProtoMsgIdMap.ts
file = open(path2,"r",encoding= 'utf8')
temp = file.read();
params = ""

for i in range(0,len(classNames)):
	className = classNames[i]
	# print (className)
	params += "\t\t\tthis.msgIdMap[MessageID." + className + "] = com.message." + className + ";\n"

temp = temp.replace("$params$", params)
newfile2 = open(newpath + filename2 + ".ts","w",encoding= 'utf8')
newfile2.write(temp)
newfile2.flush()
newfile2.close()
file.close()
print("completed!")


