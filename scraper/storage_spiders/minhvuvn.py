# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-info-box']/h1[@class='proname']",
    'price' : "//div[@class='product-info-box']/p/span[@class='priceview']",
    'category' : "//div[@id='barlist']/div[@class='title']/a[@class='link2']",
    'description' : "//div[@class='contents cf']/div[5]",
    'images' : "//div[@class='boximglager']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'minhvu.vn'
allowed_domains = ['minhvu.vn']
start_urls = ['http://minhvu.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/detail-product-view+-[a-zA-Z0-9-_]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/menu-product+-[a-zA-Z0-9-_]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
