# -*- coding: utf-8 -*-
# Python 2
#run it from cron like: subprocess.run(["C:\Python27\python.exe", "C:\dev\echo-warsaw-backend\commands\send_sms.py", "511661676", "trump", "www.facebook.com/21/posts/37"])
import sys

from smsapi.client import SmsAPI
from smsapi.responses import ApiError


def send_sms(number, keyword, url):
    api = SmsAPI()
    api.auth_token = 'ombgS9YCMn0N6Do6iav1kwWlYwGocV6NbRIQAs5r'

    try:
        api.service('sms').action('send')

        api.set_content(u'Welcome, recently keyword: [%1%] appeared on page you are following. Go to post: [%2%] $echo-warsaw team')
        api.set_params(keyword, url)
        api.set_to(str(number))
        # api.set_from('$echo-warsaw')
        result = api.execute()

        for r in result:
            print r.id, r.points, r.status

    except ApiError, e:
        print '%s - %s' % (e.code, e.message)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        send_sms(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print "usage: send_sms.py number, keyword, url"
        exit(1)
