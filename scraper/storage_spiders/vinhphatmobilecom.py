# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='ty-product-bigpicture']/div[@class='ty-product-bigpicture__left']/div[@class='ty-product-bigpicture__left-wrapper']/h1[@class='ty-product-block-title']",
    'price' : "//div[@class='ty-product-block__price-actual']/span/span/span",
    'category' : "//div[@class='    ty-float-left']/ul[@class='ty-menu__items cm-responsive-menu']/li[@class='ty-menu__item ty-menu__item-nodrop ty-menu__item-active']/a[@class='ty-menu__item-link']",
    'description' : "//div[@id='content_product_tab_10']/div[@class='ty-wysiwyg-content']/ul/li",
    'images' : "//div[@class='ty-product-img cm-preview-wrapper']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'vinhphatmobile.com'
allowed_domains = ['vinhphatmobile.com']
start_urls = ['http://vinhphatmobile.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
