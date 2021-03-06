# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product_detail']/div[@class='content']/div[@id='lblName']",
    'price' : "//td[@class='pricevn']/span[@id='lblPrice']",
    'category' : "//div[@class='navigator']/a",
    'description' : "//div[@class='body_box']/div[5]",
    'images' : "//div[@id='imageSlider']/div[@class='ws_images']/ul/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hangnhapusa.vn'
allowed_domains = ['hangnhapusa.vn']
start_urls = ['http://hangnhapusa.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/chi-tiet-san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
