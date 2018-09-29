import scrapy
from Naukri.items import MemberItem
from scrapy.loader import ItemLoader

class MemberDetails(scrapy.Spider):
	name='naukri_details'
	start_urls=['http://www.naukri.com/data-analytics-jobs-in-delhi-ncr']

	def parse(self,response):
		jobs_list=response.css('div[type=tuple].row')
		for member in jobs_list:
			member_loader=ItemLoader(MemberItem(),selector=member)
			member_loader.add_css('Job_Title','ul > li.desig::text')
			member_loader.add_css('Experience_Required','span.exp::text')
			member_loader.add_css('Location','span.loc > span::text')
			member_loader.add_css('Company_Name','span.org::text')
			member_loader.add_css('Link','a::attr(href)')
			member_loader.add_css('Keyskills','span.skill::text')
			member_loader.add_css('Job_Description','span.desc::text')
			member_loader.add_css('Salary','div.other_details > span.salary::text')
			member_loader.add_css('Posted_By','div.other_details > div.rec_details > a.rec_name::text')
			member_loader.add_css('Posted_On','div.other_details > div.rec_details > span.date::text')

			yield member_loader.load_item()
