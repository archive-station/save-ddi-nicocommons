import requests

def search(term: str):
    offset = 0
    limit = 50
    git = requests.get(f'https://public-api.commons.nicovideo.jp/v1/materials/search/keywords?q={term}&_limit=50&_offset=0&_sort=%2startTime').json()
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