# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pd-name']/h1",
    'price' : "//div[@class='pd-price']/span[@class='sub1 txt_20 chudam']",
    'category' : "//div[@id='location_hunv']/div/a",
    'description' : "//div[@class='pcdetails']/div[@id='tab1']",
    'images' : "//div[@class='hbimg zoomp']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'yenphat.vn'
allowed_domains = ['yenphat.vn']
start_urls = ['http://yenphat.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['((/san-pham-)|(/may-)).*\d+.*\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['[^(/san-pham)]'], deny=['&']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]