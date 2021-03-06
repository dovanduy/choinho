# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/td/div/font[@class='CTieuDeNhoNho']",
    'price' : "//div[@id='content']/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/font/div[5]/font[2]/b",
    'category' : "",
    'description' : "//tr/td/p[@class='textbody']",
    'images' : "//div[@id='content']/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table//tr/td[1]/table//tr[1]/td/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sachvidan.com'
allowed_domains = ['sachvidan.com']
start_urls = ['http://sachvidan.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/newsdetail.asp']), 'parse_item'),
    Rule(LinkExtractor(allow=['/ShowCat.asp']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
