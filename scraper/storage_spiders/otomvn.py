# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@itemprop='offers']/p[@itemprop='price']//span[@class='amount']",
    'category' : "//nav[@itemprop='breadcrumb']/a",
    'description' : "//div[@itemprop='description']/div[@class='std']",
    'images' : "//div[@class='product_thumbnails']/div[1]/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'otom.vn'
allowed_domains = ['otom.vn']
start_urls = ['http://otom.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/shop/[\w-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/[\w-]+($|/page/\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
