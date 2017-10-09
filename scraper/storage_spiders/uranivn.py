# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='mainbox-title']",
    'price' : "//span[contains(@id,'sec_discounted_price')]",
    'category' : "//div[@class='breadcrumbs']/a",
    'description' : "//div[@id='tabs_content']",
    'images' : "//a[contains(@id,'detailed_href')]/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'urani.vn'
allowed_domains = ['urani.vn']
start_urls = ['http://www.urani.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['.html$']), 'parse_item'),
    Rule(LinkExtractor(allow = ['.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]