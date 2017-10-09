# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/td/h1[@id='product_name']",
    'price' : "//td/div[@class='product_right']/div/span[@class='price_display']",
    'category' : "//td/div[@class='product_detail']/div[@class='categoryPath']/a",
    'description' : "//tr/td/div[@id='content_tab_hunv']/div[@id='content_1']",
    'images' : "//div[@id='img_large']/a[@id='Zoomer']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'songhongcamera.com'
allowed_domains = ['songhongcamera.com']
start_urls = ['http://songhongcamera.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['_id+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['_dm+\d+\.html($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
