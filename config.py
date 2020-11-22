import os
class Config:
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey=24b7239693044b00888fd8bc7e3173a0'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey=24b7239693044b00888fd8bc7e3173a0'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}