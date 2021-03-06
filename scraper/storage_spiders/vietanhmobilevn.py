# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='content']/div[@class='detail-product']/div[@class='detail']/h1",
    'price' : "//div[@class='detail-product']/div[@class='detail']/div[@class='group-bottom']/p[@class='price']",
    'category' : "//body/div[@id='main']/div[@class='inner breadcrumbs']/a",
    'description' : "//div[@class='content']/div[@class='col-main fl']/div[@class='tabbed_area']/div[@id='content_1']",
    'images' : "//div[@class='img br']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'vietanhmobile.vn'
allowed_domains = ['vietanhmobile.vn']
start_urls = ['http://www.vietanhmobile.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/'], deny=['\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
