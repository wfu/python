# -*- coding: utf-8 -*- 
#cherrypick

# File: readline-example-1.py
#import sqlite3


sqlfile = open('keyword.sql','w')

kfile = open("keyword.txt")
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
