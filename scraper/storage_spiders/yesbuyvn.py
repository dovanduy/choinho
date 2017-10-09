# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='infoProduct']/div[@class='title']/h1",
    'price' : "//strong[@class='sell_price']/span[@class='uc-price']",
    'category' : "//div[@class='breadcrumb']/span/a/span",
    'description' : "//div[@class='content_details']/div[@class='description_pci'] | //div[@class='content_details']/p",
    'images' : "//div[@class='imagePreview']/div[@id='images_preview']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'yesbuy.vn'
allowed_domains = ['yesbuy.vn']
start_urls = ['http://yesbuy.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+--\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+/[a-zA-Z0-9-]+($|\?page=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
