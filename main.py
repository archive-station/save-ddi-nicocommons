import requests


def grab_metadata(url: str):
   url = url.split('nc')[1]
   git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/{url}').json()
   # return
   return git

def download(url: str):
    metadata = grab_metadata(url)
    

if __name__ == '__main__':
    download('nc15531')