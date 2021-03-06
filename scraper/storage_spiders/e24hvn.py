# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='mainbox-title']",
    'price' : "//div[@class='float-left product-prices']/p[@class='actual-price']/span/span/span | //p[@class='actual-price']/span/span/span[1]",
    'category' : "//div[@class='breadcrumbs clearfix']/span/a/span",
    'description' : "//div[@id='tabs_content']/div[@id='content_description']",
    'images' : "//div[@class='product-main-info']/div/div/div[@class='cm-image-wrap']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'e24h.vn'
allowed_domains = ['e24h.vn']
start_urls = ['http://www.e24h.vn/buy/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/[a-zA-Z0-9-]+/+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
