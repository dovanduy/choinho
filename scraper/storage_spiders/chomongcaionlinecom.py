# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='detail']/div/div[@class='info_product fl']/h2",
    'price' : "//div[@id='detail']/div/div[@class='info_product fl']/p/span[@class='money']",
    'category' : "//div[@id='message']/div/h3/a",
    'description' : "//div[@id='detail']/div/div[@id='TabView']/div[@class='Pages']",
    'images' : "//div[@id='detail']/div/span/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'chomongcaionline.com'
allowed_domains = ['chomongcaionline.com']
start_urls = ['http://chomongcaionline.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]/'], deny=['/vi/news/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
