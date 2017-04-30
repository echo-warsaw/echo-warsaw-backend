import sys
import facebook
from dateutil import parser

sys.path.append('..')
from app.models import Subscription, Post

token = '129471194266873|o4ltMq1cg05Hn4HQ8Xj8HaKa6ZE'

graph = facebook.GraphAPI(access_token=token)

def get_page_posts(url):
    try:
        id = url.split('/')[-1]
        posts = graph.get_connections(id=id, connection_name='posts')
        for post in posts['data']:
            id1, id2 = post['id'].split('_')
            data = {'link': 'www.facebook.com/{}/posts/{}'.format(id1, id2),
                    'created': parser.parse(post['created_time']), 'text': post['message'],
                    'page': url}
            if not Post.m.find(data).first():
                p = Post(data)
                p.m.save()
    except:
        pass

if __name__ == '__main__':
    for page_url in Subscription.m.distinct('url'):
        get_page_posts(page_url)
