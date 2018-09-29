class NullFixPipeline(object):
	def process_item(self,item,spider):
		try:
			item['Job_Title']
		except KeyError:
			item['Job_Title']='N/A'
		try:
			item['Experience_Required']
		except KeyError:
			item['Experience_Required']='N/A'
		try:
			item['Location']
		except KeyError:
			item['Location']='N/A'
		try:
			item['Company_Name']
		except KeyError:
			item['Company_Name']='N/A'
		try:
			item['Link']
		except KeyError:
			item['Link']='N/A'
		try:
			item['Keyskills']
		except KeyError:
			item['keyskills']='N/A'
		try:
			item['Job_Description']
		except KeyError:
			item['Job_Description']='N/A'
		try:
			item['Posted_By']
		except KeyError:
			item['Posted_By']='N/A'
		try:
			item['Salary']
		except KeyError:
			item['Salary']='N/A'	
		return item
#class SalaryFixPipeline(object):
#	def process_item(self,item,spider):
#		if item['Salary']=='Not disclosed':
#			item['Salary']='N/A'
#		return item
