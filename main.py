import requests
def grab_info(url: str):
   url = url.split('nc')[1]
   git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/{url}').json()

   return git


def download(url: str):
    print(grab_info(url))


if __name__ == '__main__':
    download('nc15531')