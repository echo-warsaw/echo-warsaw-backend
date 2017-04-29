import facebook

access_token = ''
graph = None
testing = True


def get_access_token():
    '''
        TODO: force renewing token
    '''
    return '129471194266873|o4ltMq1cg05Hn4HQ8Xj8HaKa6ZE'


def get_graph():
    global access_token
    global graph

    if not access_token:
        access_token = get_access_token()

    if not graph:
        graph = facebook.GraphAPI(access_token=access_token)

    return graph


def get_fb_ids_of_query(q, q_type='page', only_best=True):
    graph = get_graph()
    search_results = graph.request('search', {'q' : q, 'type': q_type})['data']

    if only_best:
        return search_results[0]['id']
    else:
        return [k['id'] for k in search_results]


def create_url_from_post_id(post_id):
    split_ids = post_id.split('_')
    return 'www.facebook.com/' + split_ids[0] + '/posts/' + split_ids[1]



def get_page_feed(id):
    posts = get_graph().get_connections(id=id, connection_name='posts')['data']
    return [(p['created_time'],
            p['message'],
            create_url_from_post_id(p['id'])
            ) for p in posts if 'message' in p]


def tests():
    '''
        Usage example:
    '''
    page_id = get_fb_ids_of_query('teatr rozmaitosci')
    # posts = get_page_feed(page_id)
    # print(posts)
    for post in get_page_feed(page_id):
        print(post)

