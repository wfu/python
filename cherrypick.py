# -*- coding: utf-8 -*- 
#cherrypick

'''
cn fuweilin
h hash
cd datime
s msg
'''



path = '/var/www/';
afterDate = '2017-1-1';
authors = ['fuweilin','fuweilin2']


cmd = 'git log --pretty=format:%H  %cd %s';
for author in authors:
    cmd += '--author=' + author;



lfile = open("git.log")
templateName=''
while 1:
    line = kfile.readline()
    if not line:
        break
    if (templateName == ''):
        templateName = line.strip('\n')
        continue
    else:
        if line != '\n':
            sql = "insert or ignore into tb_keyword (templateName,keyword) values('" + templateName.strip('\n') + "','" + line.strip('\n') + "');"
            print sql
            print >> sqlfile, sql
#            cx.execute(sql)
        else:
            templateName=''
print >> sqlfile, '\n\n\n'
kfile.close()
sqlfile.close()
