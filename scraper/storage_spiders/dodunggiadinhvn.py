# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//p[@class='prod-price']/span[@class='price']",
    'category' : "//ol[@class='breadcrumb']/li/a",
    'description' : "//div[@class='col-md-12']/div/div[@class='tab-content']",
    'images' : "//ul[@class='slides']/li[1]/a/@data-image",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'dodunggiadinh.vn'
allowed_domains = ['dodunggiadinh.vn']
start_urls = ['http://dodunggiadinh.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['dodunggiadinh\.vn/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse_item_and_links'),
]
