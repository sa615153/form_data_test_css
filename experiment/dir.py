import os

GIT_ROOT=r'M:\gitroot\\'
GIT_ROOT_IP=r'\\163.184.167.120\qa\gitroot'

git_dir = "Pangy"

git_path = GIT_ROOT +'\\'+git_dir
print "Path: "+git_path

retval = os.getcwd()
os.chdir(GIT_ROOT)
log = os.popen('dir /b/d').read()
#`git log --pretty=format:%h -n 1`
os.chdir(retval)
dir_list = log.split('\n')
print log
print dir_list

if git_dir in dir_list:
    print "ok"
else:
    print "false"
print "------------------------------------------------------"







if os.path.exists(git_path):
    print "exists"








if os.path.exists(git_path):
    retval = os.getcwd()
    os.chdir(git_path)
    log = os.popen('git log --pretty=format:"%an,%h,%cr,%cd,%s" -1').read()
    #`git log --pretty=format:%h -n 1`
    os.chdir(retval)

    print log
