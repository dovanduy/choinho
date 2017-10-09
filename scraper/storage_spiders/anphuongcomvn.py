# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//font[@class='display_title']",
    'price' : "",
    'category' : "//div[@class='main_title']/a[1]",
    'description' : "//div[@class='main_content']/div[2]",
    'images' : "//div[@class='main_content']/div[1]/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'anphuong.com.vn'
allowed_domains = ['anphuong.com.vn']
start_urls = ['http://anphuong.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(deny=['about', 'news','services','contact','training']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
