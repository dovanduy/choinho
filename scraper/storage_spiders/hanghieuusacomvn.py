# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail_r_tile noresize']/h1",
    'price' : "//div[@class='rowgia']/div/span[@id='price']",
    'category' : "//section/div[@class='brecum']/ul/li/a",
    'description' : "//div[@class='tabpanel fl']/div[@id='cont_ct']",
    'images' : "//ul[@id='etalage']/li/div/img/@src | //div[@class='detail_r_img fl']//img/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'hanghieuusa.com.vn'
allowed_domains = ['hanghieuusa.com.vn']
start_urls = ['http://hanghieuusa.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['\.html']), 'parse_item_and_links'),
]