import pymysql
from config import CONFIG
import csv

db = pymysql.connect(**CONFIG)   # name of the database
cur = db.cursor()
city = {}
city_index = 0
index = 0

with open('Naukri/tmp/naukri_dataanalytics.csv','r') as f:
	data = list(csv.reader(f))
	for row in data[1:]:
		if len(row)==0:
			continue
		(company, experience, description, job_title, keyskills, link, location, Posted_by, posted_on, salary) = row
		salary = salary.strip()
		string = 'INSERT INTO DataAnalyst_ncr(Job_Title,Experience,Company_Name,Link,Keyskills,Description,Salary) VALUES("%s","%s","%s","%s","%s","%s","%s");'%(job_title, experience, company, link, keyskills, description, salary)
		print(string)
		cur.execute(string)
		db.commit()
		if location not in city:
			string = 'INSERT INTO location_jobs(Job_id,location) VALUES(%d,"%s");'%(index+1,location)
			print(string)
			cur.execute(string)
			db.commit()
			city_index+=1
		index+=1
cur.close()		
db.close()
print("connected")
