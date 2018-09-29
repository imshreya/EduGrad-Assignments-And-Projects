import scrapy

class MemberItem(scrapy.Item):
	Job_Title=scrapy.Field()
	Experience_Required=scrapy.Field()
	Location=scrapy.Field()
	Company_Name=scrapy.Field()
	Link=scrapy.Field()
	Keyskills=scrapy.Field()
	Job_Description=scrapy.Field()
	Salary=scrapy.Field()
	Posted_By=scrapy.Field()
	Posted_On=scrapy.Field()
