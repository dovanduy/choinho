# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='prd-info']/div[@class='box-inner']/div[@class='prd-content']/h1[@id='prdTitle']",
    'price' : "//div[@class='_price']/span[@id='valuePrice']",
    'category' : "//div[@id='breadCrumb']/ul/li/a/span",
    'description' : "//div[@class='prd-description']/p",
    'images' : "//div[@class='prd-moreImagesListContainer sli-thumbnail']/ul/li/a/@data-zoom-image",
    'canonical' : "",
    'base_url' : "",
    'brand' : "//div[@class='prd-manufacturer flt']/a"
}
name = 'vala.vn'
allowed_domains = ['vala.vn']
start_urls = ['https://vala.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-sach-san-pham/-/catalog/[a-zA-Z0-9-]+($|\?cur=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
