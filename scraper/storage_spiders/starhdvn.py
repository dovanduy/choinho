# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//span[@class='Product_Detail_Name']",
    'price' : "//span[@id='ctl00_cphMain_Detail1_uDetail_spnProduct']/span[@class='Product_Detail_Price']",
    'category' : "",
    'description' : "//div[@id='ctl00_cphMain_Detail1_uDetail_divAttributeAndContent']/p",
    'images' : "//div[@class='Product_Detail']//td[1]//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'starhd.vn'
allowed_domains = ['starhd.vn']
start_urls = ['http://starhd.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]