# -*- coding: utf-8 -*- 
#cherrypick

import os

path = 'c:/work/rc/Coding';
gitlog = 'c:/git.log';
gitscript = 'c:/git.txt';
afterDate = '2017-8-1';
authors = ['author1','author2']


cmd = 'git log --pretty=format:"%H %s" '
for author in authors:
    cmd += '--author=' + author +' '
cmd += '--after='+afterDate + ' > ' + gitlog
print cmd;
os.chdir(path)
os.system(cmd)

logfile = open(gitlog)
gitfile = open(gitscript, 'w')
while 1:
    line = logfile.readline()
    if not line:
        break
    hash = line.split(' ')[0]
    if hash.strip():
        str = 'git cherry-pick ' + hash
        print >> gitfile, str

logfile.close()
gitfile.close()
      
    
