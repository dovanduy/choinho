# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detailRight']/h1[@class='title']",
    'price' : "//div[@class='detailRight']/p[@class='price']/span[1]",
    'category' : "//div[@class='directory2']/div/a/span",
    'description' : "//div[@class='tabProductDetailList']/div[@class='tabProductDetail'][2]",
    'images' : "//div[@class='gallery_catalog']/div[@class='image_large']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'pth.vn'
allowed_domains = ['pth.vn']
start_urls = ['http://pth.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.htm']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+/','/list.php']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]