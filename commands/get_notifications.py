import sys
from rq import Queue
from redis import Redis
from datetime import datetime

sys.path.append('..')
from app.models import Subscription, Post
from send_mail import compose_mail

q = Queue(connection=Redis())

def get_notifications(subs):
    for sub in subs:
        try:
            posts = Post.m.find({'page': sub['id'], 'text': {'$regex': sub['keyword']}, 'created': {'$gte': sub['offset']}}
                                ).all()

            notifications = [(sub['mail'], post['link'], sub['keyword']) for post in posts]
            for n in notifications:
                compose_mail(*n)

            s = Subscription.m.find({'_id': sub['_id']}).one()
            s.offset = datetime.now()
            s.m.save()
        except:
            pass

if __name__ == '__main__':
    get_notifications(Subscription.m.find())
