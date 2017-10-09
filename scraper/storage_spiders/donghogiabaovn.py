# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/td[@class='ten-slide']/h1",
    'price' : "//div[@class='product_bc']/div[@class='nd']//tr[6]/td[@class='ten-slide']",
    'category' : "",
    'description' : "//table[@class='table-technical']",
    'images' : "//tr/td/img[@id='myimage']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'donghogiabao.vn'
allowed_domains = ['donghogiabao.vn']
start_urls = ['http://donghogiabao.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/loai-dong-ho/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
