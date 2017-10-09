# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='section book-detail']/h2",
    'price' : "//div[@class='section book-detail']/div/span[@class='price'] | //div[@class='section book-detail']/div/span[@class='price']",
    'category' : "",
    'description' : "//div[@class='section book-detail']/div[@class='intro']",
    'images' : "//div[@class='cover']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'alezaa.com'
allowed_domains = ['m.alezaa.com']
start_urls = ['http://m.alezaa.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/view.php+\?+id=[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/browse.php+.*'], deny=['next=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
