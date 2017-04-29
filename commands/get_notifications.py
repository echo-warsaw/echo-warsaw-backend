import sys
from datetime import datetime

sys.path.append('..')
from app.models import Subscription, Post


def get_notifications(subs):
    for sub in subs:
        posts = Post.m.find({'page': sub['url'], 'text': {'$regex': sub['keyword']}, 'created': {'$gte': sub['offset']}}
                            ).all()

        notifications = [(sub['mail'], post['link']) for post in posts]
        print('notifications', notifications)
        s = Subscription.m.find({'_id': sub['_id']}).one()
        s.offset = datetime.now()
        s.m.save()

if __name__ == '__main__':
    get_notifications(Subscription.m.find())
