# Auto generated by generator.py. Delete this line if you make modification.

from scraper.spiders.detail_site_map import DetailSiteMap
from scraper.storage_spiders import thegioididongcom

class Thegioididongcom(DetailSiteMap):

    name = thegioididongcom.name
    allowed_domains = thegioididongcom.allowed_domains
    start_urls = thegioididongcom.start_urls
    tracking_url = thegioididongcom.tracking_url
    sitemap_urls = thegioididongcom.sitemap_urls
    sitemap_rules = thegioididongcom.sitemap_rules
    sitemap_follow = thegioididongcom.sitemap_follow
    rules = thegioididongcom.rules
    
    def __init__(self, files=None):
        DetailSiteMap.__init__(self, thegioididongcom.XPATH, files)
    
