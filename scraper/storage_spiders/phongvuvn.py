# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='chitietsp']/h1",
    'price' : "//div[@class='chitietsp']/ul/li[@class='giasp']",
    'category' : "//div[@class='breadcrumb']/ul/li/a",
    'description' : "//div[@class='leftCont']/div[@class='motasanpham']",
    'images' : "//form[@class='shopping shoppingdetail']/div[@class='chitietsp']/p/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'phongvu.vn'
allowed_domains = ['phongvu.vn']
start_urls = ['http://phongvu.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+c\.html','/[a-zA-Z0-9-]+-\d+c+/cpage']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
