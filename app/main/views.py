from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome To News Center'
     # Getting popular movie
    business_news = get_news('business')
    general_news = general_news('general')
    entertainment = entertainment_news('entertainment')
    title = 'Welome To News Center'
    return render_template('index.html',title = title,business = business_news,general = general_news, entertainment = entertainment_news)


@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id) 

      