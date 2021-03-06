# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='overview']/div[@class='product-name']/h1",
    'price' : "//div[@class='prices']/div[@class='product-price']/span",
    'category' : "//div[@class='breadcrumb']/ul/li/span/a/span",
    'description' : "//div[@class='full-description']/p",
    'images' : "//div[@class='picture-thumbs']/div/a/@href | //div[@class='gallery']/div[@class='picture-thumbs']//a/@href | //img[@id='productImage']/@data-zoom-image",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'alozo.vn'
allowed_domains = ['alozo.vn']
start_urls = ['http://alozo.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
