# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='goods_details box thin_box']/div[@class='bd']/h1/span",
    'price' : "//ul[@class='basic clearfix']/li/em[@class='price']/span",
    'category' : "//p[@class='breadcrumbs']/a/span",
    'description' : "//div[@id='description']/div[@class='bd']",
    'images' : "//div[@id='gallery']/div[@class='cloud_zoom_wrap']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'congmua.com'
allowed_domains = ['congmua.com']
start_urls = ['http://congmua.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]