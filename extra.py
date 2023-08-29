import requests

def hit_sender(card,message,chat_id):
    bot_token = '6501623476:AAHQMeqbE18Fky2c-ME_3D2blUMq8mKVj5U' #ganti sesuai selera
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
