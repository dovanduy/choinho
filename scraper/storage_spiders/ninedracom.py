# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='tskt']/h1",
    'price' : "//div[@class='prod_price']/span[@id='block_price']",
    'category' : "",
    'description' : "//div[@id='content']/div[@class='jshop_prod_description']",
    'images' : "//span[@id='list_product_image_middle']/a/@href",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'ninedra.com'
allowed_domains = ['ninedra.com']
start_urls = ['http://ninedra.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/san-pham-online/']), 'parse_item_and_links'),
]
