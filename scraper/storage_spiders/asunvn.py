# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//title|//h1[@class='product-name']",
    'price' : "//ul[@class='product-list']/li/strong",
    'category' : "//ul[@class='breadcrumb']/li/a",
    'description' : "//div[@class='tab-content clearfix']//p",
    'images' : "//li[@class='active-slide']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'asun.vn'
allowed_domains = ['asun.vn']
start_urls = ['http://asun.vn/index.php']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[\w\d-]+-\d+\.htm$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+-[\w\d-]+$','allproducts\.php\?cID=\d+&limit=20.start=\d+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
