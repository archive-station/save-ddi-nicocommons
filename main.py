import requests

def search(url: str):
    git = requests.get('https://public-api.commons.nicovideo.jp/v1/materials/search/keywords?q=%E3%81%A9%E3%81%93%E3%81%A7%E3%82%82%E3%81%84%E3%81%A3%E3%81%97%E3%82%87&_limit=50&_offset=0&_sort=%2BstartTime').json()
    print(git)

def grab_metadata(url: str):
   url = url.split('nc')[1]
   git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/{url}').json()
   # return
   return git



def download(url: str):
    metadata = grab_metadata(url)
    

if __name__ == '__main__':
    search('help')
    download('nc15531')