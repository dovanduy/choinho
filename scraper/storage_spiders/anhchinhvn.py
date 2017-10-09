# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='prod_content']/h1[@id='prod_title']",
    'price' : "//div[@class='final_price']/span[@id='special_price_box']",
    'category' : "//div[@class='bcr box breadcrumbs']/ul/li/a",
    'description' : "//div[@class='prod_details']",
    'images' : "//div[@id='prdMedia']/div[@id='img_large']/div/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'anhchinh.vn'
allowed_domains = ['anhchinh.vn']
start_urls = ['http://www.anhchinh.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_id+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_dm+\d+\.html'], deny=['\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
