import logging
import coloredlogs
import requests

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO')


class error(Exception):
    pass


class line:
    def __init__(self, token):
        self.base_url = 'https://notify-api.line.me/api/'
        self.headers = {
            'Authorization': 'Bearer {token}'.format(token=token)}

    def send_message(self, text):
        data = {
            'message': text}
        url = self.base_url + 'notify'
        r = requests.post(url, data=data, headers=self.headers)
        return self.resp(r)

    def send_photo(self, photo, text=None, thumbnail=None):
        # TODO url 偵測
        if type(photo) == str:
            if 'http' in photo:
                file = photo
            else:
                try:
                    file = open(photo, 'rb')
                except:
                    raise
            if thumbnail == None:
                thumbnail = 'https://p176.p0.n0.cdn.getcloudapp.com/items/qGuyQLX1/loading.jpeg'

        elif type(photo) == bytes:
            file = photo
        if text == None:
            text = '傳送圖片'
        url = self.base_url + 'notify'

        params = {'message': text}
        if type(file) == str:
            files = {'imageFullsize': file,
                     'imageThumbnail': thumbnail}
            r = requests.post(url, params=params, data=files,
                              headers=self.headers)
            return self.resp(r)
        else:
            files = {'imageFile': file}
            r = requests.post(url, params=params,
                              files=files, headers=self.headers)
            return self.resp(r)

    def resp(self, response):
        if response.status_code != 200:
            logger.critical(response.text)
            raise error(response.text)
        else:
            return response.json()
