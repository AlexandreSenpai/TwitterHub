import socket, os
from datetime import datetime
from TwitterAPI import TwitterAPI

class Twitter:
    def __init__(self, consumer_key, consumer_secret, acess_token_key, acess_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.acess_token_key = acess_token_key
        self.acess_token_secret = acess_token_secret

    def init_API(self):
        return TwitterAPI(self.consumer_key,
                         self.consumer_secret,
                         self.acess_token_key,
                         self.acess_token_secret)
    
    def request_POST(self, msg=''):
        request_info = {
            'IP': socket.gethostbyname(socket.gethostname()),
            'local_data': {
                'date': str(datetime.now().strftime('%d/%m/%Y')),
                'hour': str(datetime.now().strftime('%H:%M:%S'))
            },
            'status_data': {
                'name': os.getlogin(),
                'msg': msg
            }
        }
        print('Status atualizado.\nStatus: {}\nData: {}\nHorario: {}\nIP: {}'.format(request_info['status_data']['msg'], 
                                                                             request_info['local_data']['date'], 
                                                                             request_info['local_data']['hour'],
                                                                             request_info['IP']))
        api = self.init_API()
        api.request('statuses/update', {'status': request_info['status_data']['msg']})

    def request_POST_WITH_IMAGE(self, msg, IMAGE_PATH):
        request_info = {
            'IP': socket.gethostbyname(socket.gethostname()),
            'local_data': {
                'date': str(datetime.now().strftime('%d/%m/%Y')),
                'hour': str(datetime.now().strftime('%H:%M:%S'))
            },
            'status_data': {
                'name': os.getlogin(),
                'msg': msg
            }
        }
        file = open(IMAGE_PATH, 'rb')
        data = file.read()
        api = self.init_API()
        r = api.request('media/upload', None, {'media': data})
        print('IMAGE UPLOAD: SUCESSO' if r.status_code == 200 else 'IMAGE UPLOAD: FALHA -> ' + r.text)
        if r.status_code == 200:
            media_id = r.json()['media_id']
            r = api.request('statuses/update', {'status': msg, 'media_ids': media_id})
            print('Status atualizado.\nStatus: {}\nData: {}\nHorario: {}\nIP: {}'.format(request_info['status_data']['msg'], 
                                                                                         request_info['local_data']['date'], 
                                                                                         request_info['local_data']['hour'],
                                                                                         request_info['IP']))

    def search_TWEET(self, key='', stream=''):
        request_info = {
            'IP': socket.gethostbyname(socket.gethostname()),
            'search_data': {
                'key': key,
            }
        }
        print('Pesquisa realizada.\nKey: {}\nIP: {}'.format(request_info['search_data']['key'],
                                                            request_info['IP']))
        
        api = self.init_API()
        print(stream)
        if stream == 'y':
            print('Modo: Streaming.')
            request = api.request('statuses/filter', {'track': request_info['search_data']['key']})
        else:
            print('Modo: Fixo.')
            request = api.request('search/tweets', {'q': request_info['search_data']['key'], 'count':30})

        for item in request:
            print('#######################################################')
            print('Tweet: {}\nUsuário: {}\nLocal: {}\nData: {}\nLink: {}'.format(item['text'],
                                                                       item['user']['screen_name'],
                                                                       item['user']['location'],
                                                                       item['created_at'],
                                                                       'https://www.twitter.com/' + str(item['user']['screen_name']) + '/status/' + str(item['id_str'])))
            print('#######################################################')                                                            