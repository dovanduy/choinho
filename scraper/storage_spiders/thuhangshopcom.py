# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/form[@id='aspnetForm']/div[3]/div[@class='bgwhite']/div[4]/table/tbody/tr[3]/td[4]/div[3]/table/tbody/tr/td[4]/div/div[@class='bgtextquangcao'][2]",
    'price' : "/html/body/form[@id='aspnetForm']/div[3]/div[@class='bgwhite']/div[4]/table/tbody/tr[3]/td[4]/div[3]/table/tbody/tr/td[4]/div[5]/div[@class='bgtextquangcao'][2]",
    'category' : "/html/body/form[@id='aspnetForm']/div[3]/div[@class='bgwhite']/div[4]/table/tbody/tr[3]/td[4]/div[3]/table/tbody/tr/td[4]/div[3]/div[@class='bgtextquangcao'][2]",
    'description' : "/html/body/form[@id='aspnetForm']/div[3]/div[@class='bgwhite']/div[4]/table/tbody/tr[3]/td[4]/div[3]/table/tbody/tr/td[4]/div[11]/div[@class='bgtextall']/p",
    'images' : "//div[@id='contenttab5']/span/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thuhangshop.com'
allowed_domains = ['thuhangshop.com']
start_urls = ['http://thuhangshop.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
