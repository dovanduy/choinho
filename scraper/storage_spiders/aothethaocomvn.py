# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='vmMainPage']/table/tbody/tr[1]/td[2]/h1",
    'price' : "//span[@class='productPrice']",
    'category' : "",
    'description' : "",
    'images' : "//td[@class='vm-product-img']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'aothethao.com.vn'
allowed_domains = ['aothethao.com.vn']
start_urls = ['http://aothethao.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['\*.html']), 'parse_item'),
    Rule(LinkExtractor(deny=['/giao-dich/','/Lien-he/','/Tin-the-thao']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
