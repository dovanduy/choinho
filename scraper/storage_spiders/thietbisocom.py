# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-form']/h2[@class='pname']",
    'price' : "//div[@class='p_info']/span/span[@class='price_format']",
    'category' : "//div[@class='breadcrumb']/span/a/span",
    'description' : "//div[@class='right']/div[@class='right-part2']",
    'images' : "//img[@id='fullimg_preview']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thietbiso.com'
allowed_domains = ['thietbiso.com']
start_urls = ['http://thietbiso.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/chi-tiet/']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/san-pham/'], deny = ['page=','/khuyen-mai/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]