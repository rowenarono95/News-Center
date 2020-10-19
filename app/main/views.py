from flask import render_template
from ..request import get_sources,get_articles
from ..models import Sources
from .import main    

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome To News Center'
    
    business_news = get_sources('business')
    general_news = get_sources('general')
    entertainment = get_sources('entertainment')
    title = 'Welome To News Center'
    return render_template('index.html',title = title,business = business_news,general = general_news, entertainment = entertainment)


@main.route('/article/<article_id>')
def article(article_id):
    article = get_articles(article_id)

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',article = article) 

      