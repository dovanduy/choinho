# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/td[@class='pro_name']/strong",
    'price' : "//td/div/strong/span[@style='color:#FF4800'][1]",
    'category' : "//tr/td[@class='font home']/div[@class='addressdetail']/a",
    'description' : "//tr/td[@class='font home']/div[@id='homecontent_1']/table[@class='thuoctinh']",
    'images' : "//div[@class='m']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'fam.vn'
allowed_domains = ['fam.vn']
start_urls = ['http://fam.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['-d\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['-p\d+$','page=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
