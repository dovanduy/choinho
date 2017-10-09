# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='box_main2']/div[@class='detail']/h3",
    'price' : "//div[@class='dt_text']/p/span/strong",
    'category' : "//div[@class='box2']/div[@class='box_tit2']/p",
    'description' : "//div[@id='pro_content_box']/div[@id='pro_content_desc']/ul/li | //div[@id='pro_content_desc']/p/img/@src",
    'images' : "//div[@class='dt_img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'avz.com.vn'
allowed_domains = ['avz.com.vn']
start_urls = ['http://avz.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/d_pro/+\d+/[a-zA-Z0-9-_]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/pro/+\d+/+\d+/[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
