# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='home']/div/div/div[@class='pro_name']",
    'price' : "//div[@class='home_product_price']/span",
    'category' : "//div[@class='cat_pro_title']/a",
    'description' : "//div[@class='body_pro']/div/div[@id='description_1']",
    'images' : "//div[@id='home']/div/div/div/img/@src | //div[@id='home']/div/div/div/div/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'daiduongmobi.com'
allowed_domains = ['daiduongmobi.com']
start_urls = ['http://daiduongmobi.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
