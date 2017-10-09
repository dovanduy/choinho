# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='ctl00_MainContent_divMainContent']/div[@class='primary-product group']/div[@class='col col-product-detail']/h1[@class='product-name']",
    'price' : "//div[@class='col col-product-detail']/div[@class='product-buy']/p[@class='product-row']/span[@id='total-money']",
    'category' : "//ol[@class='breadcrumb']/li/a/span",
    'description' : "//div[@id='ctl00_MainContent_divMainContent']/div[@class='second-product group']/div[@class='tab-content']/div[@id='tab0']",
    'images' : "//div[@class='col col-product-detail']/div[@class='product-buy']/p[@class='product-row']/span[@class='product-price']",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'ngocanhshop.com.vn'
allowed_domains = ['ngocanhshop.com.vn']
start_urls = ['http://ngocanhshop.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+s+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
