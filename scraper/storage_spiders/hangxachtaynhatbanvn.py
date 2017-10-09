# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='primary_block']/div[@id='pb-left-column']/h1",
    'price' : "//div[@class='price']/p/span",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@id='more_info_block']/div[@id='more_info_sheets']/div[@id='idTab1']",
    'images' : "//span[@id='view_full_size']/img[@id='bigpic']/@src | //div[@id='thumbs_list']/ul/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hangxachtaynhatban.vn'
allowed_domains = ['hangxachtaynhatban.vn']
start_urls = ['http://www.hangxachtaynhatban.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/*.\html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]