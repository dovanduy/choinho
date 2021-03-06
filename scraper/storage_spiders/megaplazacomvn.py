# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//meta[@property='og:title']/@content",
    'price' : "//div[@class='price_detail_1']/span[@class='price_pr']",
    'category' : "//div[@class='breadcrumb hidden-xs']/ul/li/a",
    'description' : "//div[@class='tab-content']//div[@class='rte']",
    'images' : "//meta[@property='og:image']/@content",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'megaplaza.com.vn'
allowed_domains = ['megaplaza.com.vn']
start_urls = ['http://megaplaza.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+$)'], deny=['/cart']), 'parse_item_and_links'),
]
