# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//table[1]//td[@class='contentc'][1]",
    'price' : "//span[@id='ctl00_ContentplaceholderMainPage_lblCostSaleOff'] | //tr[1]/td[2]/span[@id='ctl00_ContentplaceholderMainPage_lblCost'] | //span[@style='color:Red;font-size:14pt;font-weight:bold;']",
    'category' : "//div[@class='divBc']/a",
    'description' : "//span[@id='ctl00_ContentplaceholderMainPage_ltrDes']",
    'images' : "//span[@id='ctl00_ContentplaceholderMainPage_lblImage']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'afamilyshop.com'
allowed_domains = ['afamilyshop.com']
start_urls = ['http://www.afamilyshop.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/Product+/\d+/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/Product+/\d+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
