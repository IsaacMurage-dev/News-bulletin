import urllib.request
import json
from .models import Sources, Articles

# Get  API KEY
api_key ='4076f971e66749f19122871dd39d185d'

# Get news base url
base_url = None


def configure_request(app):
    global api_key, base_url, articles_base_url
    api_key ='4076f971e66749f19122871dd39d185d'
    base_url = app.config['NEWS_API_BASE_URL']
    articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']

def get_sources():
    """
    Function to retrieve news sources list from the News api
    """

    get_sources_url = "https://newsapi.org/v2/sources?apiKey=4076f971e66749f19122871dd39d185d"
    

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    """Function that process the results list and transforms them into a list of objects
    Args: sources_list: A list of dictionaries that contains news sources details
    Returns:
    sources_results: a list of news sources objects"""

    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        source_object = Sources(id, name, description, url, category)
        sources_results.append(source_object)

    return sources_results


def get_articles(id):
    '''
    Function to get a source and it's articles
    '''
    get_articles_url =articles_base_url.format(
        id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(article_list):
    '''
    Function that processes the article results and transform them to a list of objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []

    for article_item in article_list:
        source = article_item.get('source')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        urlToArticle = article_item.get('url')
        publishedAt = article_item.get('publishedAt')

        article_object = Articles(
            source, title, description, urlToImage, urlToArticle, publishedAt)
        article_results.append(article_object)

    return article_results
