import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_fil_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path' : disk_fil_path, 'owerwrite' : 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str, filename):
        href = self.get_upload_link(disk_fil_path=file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Succes')


if __name__ == '__main__':
    path_to_file = 'random_file.txt'
    token =
    ya = YaUploader(token=token)
    ya.upload(file_path=path_to_file, filename='random_file.txt')


