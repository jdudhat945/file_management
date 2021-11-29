# 21SOECE13013_jinal_dudhat_3ITA
import os
import pathlib
import shutil
path =input('Pleace enter folder path to convert in file manager ')
filelist = []
for root, dirs, files in os.walk(path):
	for file in files:
		filelist.append(os.path.join(root,file))
list=[]
temp=""
temp2=""
c=-1
for name in filelist:
    print(name)
for i in filelist:
    for j in range(len(i)-1,-1,-1):
        if(i[j]!='.'):
            temp=temp+i[j]
        else:
            break
    for k in range(len(temp)-1,-1,-1):
        temp2=temp2+temp[k]
    if(temp2 not in list and temp2.upper() not in list and temp2.lower() not in list):
        list.append(temp2)
    temp=""
    temp2=""
# print(list)
flag=0
directory=input('Pleace enter folder name. Your all file store in this folder .(example: FILE MANAGER) :  ')
parent_dir =input('Enter path where you create this folder ')
while True:
    try:
        print(directory)
        directory2=directory
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        parent_dir=parent_dir+directory2
        print("Directory '% s' created" % directory)
        for name in list:
            directory = name
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            for cp in filelist:
                split_tup = cp
                split_tup=pathlib.Path(cp).suffix
                if(name == split_tup[1:] or name==split_tup[1:].lower() or name ==split_tup[1:].upper()):
                    # print(cp)
                    original = cp
                    target = path+"\\"
                    # print(original)
                    # print(target)
                    shutil.copy(original, target)
            print("Directory '% s' created" % directory)
    except FileExistsError as e:
        print('this  file is already exists')
        new_name=input('Enter foldear name ')
        flag=1
        directory=new_name
        continue
    except Exception as e:
        print(e)
        parent_dir =input('Enter where you create your folder ')
        continue
    break
print('Done')