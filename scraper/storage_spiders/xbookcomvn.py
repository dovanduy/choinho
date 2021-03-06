# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div/font[@class='CTieuDeNhoNho']",
    'price' : "//table//tr/td[2]/font/div/font/b",
    'category' : "//div[@id='content']/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td[@class='CTieuDeNho']",
    'description' : "//div[@id='content']/table[1]/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/p",
    'images' : "//div[@id='content']/table//tr/td/table//tr[2]/td/table/tbody/tr[1]/td/table//tr/td[1]/table//tr[1]/td/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'xbook.com.vn'
allowed_domains = ['xbook.com.vn']
start_urls = ['http://www.xbook.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['CatId=', 'NewsId=']), 'parse_item'),
    Rule(LinkExtractor(allow=['CategoryLoai=+\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
