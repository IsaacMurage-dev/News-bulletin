import os
class Config:
    '''
     General configuration parent class
    '''

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    # SECRET_KEY = '4076f971e66749f19122871dd39d185d'

# @staticmethod
# def init_app(app):
#     pass



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}