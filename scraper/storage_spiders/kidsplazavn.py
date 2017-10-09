# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='page-title']/h1",
    'price' : "//div[@class='lineprices php-in-stock']/div[@class='price-box php-orginal-price']/span[@class='regular-price']/span[@class='price']",
    'category' : "//div[@class='breadcrumb']/span/a",
    'description' : "//div[@id='product-description']/div[@class='desc']",
    'images' : "//meta[@property='og:image']/@content",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'kidsplaza.vn'
allowed_domains = ['kidsplaza.vn']
start_urls = ['http://www.kidsplaza.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html($|\?p=\d+$)'], deny=['seo_sitemap','/../']), 'parse_item_and_links'),
]
