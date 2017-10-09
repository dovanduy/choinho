# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//title",
    'price' : "/html/body//div[@id='idPrint']/p[@class='Title']",
    'category' : "/html/body//div/p[@class='New_Title'][1]",
    'description' : "/html/body//table[@class='TableProduct']//tr[1]/td[2]",
    'images' : "//div[@class='Content_New']/table//tr/td/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'beboiphao.com'
allowed_domains = ['beboiphao.com']
start_urls = ['http://beboiphao.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
