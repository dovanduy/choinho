# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='product-top']/h1",
    'price' : "//div[@class='PricesalesPrice']/span",
    'category' : "//div[@id='sp-pathway']/div/span[@class='breadcrumbs']/a",
    'description' : "//div/div[@class='product-short-description']",
    'images' : "//div[@class='main-image']/img[@id='medium-image']/@src | //div[@class='additional-images']/div//a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'binhminhmobile.com'
allowed_domains = ['binhminhmobile.com']
start_urls = ['http://binhminhmobile.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
