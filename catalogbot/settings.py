# Scrapy settings for catalogbot project

BOT_NAME = 'catalogbot'

SPIDER_MODULES = ['catalogbot.spiders']
NEWSPIDER_MODULE = 'catalogbot.spiders'

ITEM_PIPELINES = [
  'scrapy_rethinkdb.RethinkDBPipeline',
]

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'

DOWNLOAD_DELAY = 5

#EXTENSIONS = {
#    'catalogbot.extensions.storestats.storestats': 500
#}

RETHINKDB_TABLE = 'catalog'

RETHINKDB_CONNECTION = {
    'db': 'catalog'
}

RETHINKDB_INSERT_OPTIONS = {
    'upsert': True
}
