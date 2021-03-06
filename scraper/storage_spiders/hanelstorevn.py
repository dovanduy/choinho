# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product-title']",
    'price' : "//div[@class='product-info']/div[@class='discount-price product-row']",
    'category' : "//div[@class='top']/h4/a",
    'description' : "//div[@id='tabs']/div[@class='tab_content']",
    'images' : "//div[@class='product-image-fashion']/div/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'hanelstore.vn'
allowed_domains = ['hanelstore.vn']
start_urls = ['http://www.hanelstore.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[\w\d-]+\.\d+\.aspx$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc-san-pham/[\w\d-]+\.aspx$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
