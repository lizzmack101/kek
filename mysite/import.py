import csv, sys, os

project_dir ="/root/Desktop/djangoher/mysite/mysite"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from News.models import Student

data = csv.reader(open("/root/Desktop/djangoher/mysite/2.csv"), delimiter = ",")

for row in data:
    if row[0] != 'name':
        student = Student()
        print(row[0])
        student.name = u'row[0]'
        student.number = row[1]
        student.birthdata = row[2]
        student.email = row[3]
        student.save()
