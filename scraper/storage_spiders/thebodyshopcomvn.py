# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@itemprop='name']",
    'price' : "//div[@class='product-shop right']/div[@itemprop='offers']//span[@itemprop='price']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='product-shop right']/div[@class='product-infos']",
    'images' : "//div[@class='product-image']/a/img[@id='image']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : ""
}
name = 'thebodyshop.com.vn'
allowed_domains = ['thebodyshop.com.vn']
start_urls = ['https://www.thebodyshop.com.vn/vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[\w-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w-]+($|\?p=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]