# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='productName']/h1",
    'price' : "//div[@class='productName']/div[@class='productPrice']/div/div[@class='main-price']",
    'category' : "//div[@class='col-md-10 col-xs-12 ']/span[@class='bc-one']/a",
    'description' : "//div[@class='productInfo']/div[@class='container']",
    'images' : "//div[@class='slick-track']/li/a/@data-large_img",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'vitaminshoppe.com'
allowed_domains = ['vitaminshoppe.com']
start_urls = ['https://www.vitaminshoppe.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/p/[a-zA-Z0-9-]+/[a-zA-Z]+-\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c/[a-zA-Z0-9-/]+($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]