# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/form[@id='aspnetForm']/div[@class='ie6']/div[@class='container_28']/div[@class='clearfix bgw']/div[@class='left-col']/div[@class='prddt-desc']/h1[@class='prddt-name']",
    'price' : "/html/body/form[@id='aspnetForm']/div[@class='ie6']/div[@class='container_28']/div[@class='clearfix bgw']/div[@class='left-col']/div[@class='prddt-desc']/span[@class='price']",
    'category' : "/html/body/form[@id='aspnetForm']/div[@class='ie6']/div[@class='container_28']/div[@class='clearfix bgw']/div[@class='left-col']/div[@class='breadcrum']/a",
    'description' : "//div[@class='tab-contents']/div[@id='tabs1']/div",
    'images' : "/html/body/form[@id='aspnetForm']/div[@class='ie6']/div[@class='container_28']/div[@class='clearfix bgw']/div[@class='left-col']/div[@class='prddt-img']/div[@class='grid_pro alpha']/div[@id='prdmimg']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'shoplinhlan.com'
allowed_domains = ['shoplinhlan.com']
start_urls = ['http://www.shoplinhlan.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/\d+/\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
