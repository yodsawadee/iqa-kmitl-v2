import xlrd
from django.contrib.auth.models import User


#exec(open('C:/iqa_website_test/IQA-Website-for-KMITL-master/myvenv/Scripts/iqa_web/study_program/importDataScript/createUser.py',encoding="utf8").read())


#faculties_list = [ 'aai','adm','agi','agt','ami','arc','chp','eir','eng','icx','ide','itx','lba','med','mse','nnt','sci' ]
faculties_list = [ 'aai','adm','agi','ami','arc','chp','eir','eng','icx','ide','itx','lba','med','mse','nnt','sci' ]
for faculty in faculties_list:
    User.objects.create_user(username = faculty, password = faculty)
    print("user:", faculty,"has been created.")