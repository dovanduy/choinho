# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//h3[@class='price_current']/span",
    'category' : "//div[@class='breadcrumb']/h2/a",
    'description' : "//div[@class='tab-content']/div[@class='tab-pane fade in active']",
    'images' : "//div[@id='MagicZoomPlus']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'digiworld.com.vn'
allowed_domains = ['digiworld.com.vn']
start_urls = ['http://digiworld.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-p\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/san-pham/[a-zA-Z0-9-]+-\d+(-page\d+)?\.html$'], deny=['/[/]+san-pham']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
