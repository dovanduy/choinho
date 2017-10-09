# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='price']/p[@class='our_price_display']/span[@id='our_price_display']",
    'category' : "//div[@class='breadcrumb clearfix']/a",
    'description' : "//div[@id='short_description_block']/div[@class='rte align_justify']|//section[@class='page-product-box']",
    'images' : "//img[@id='bigpic']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = '3456.vn'
allowed_domains = ['3456.vn']
start_urls = ['https://3456.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+/\d+/[a-zA-Z0-9-]+-3456vn\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/\d+/[a-zA-Z0-9-]+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
