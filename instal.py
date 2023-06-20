import json
import requests

def instadownload(link):
    import requests

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "41b74d8d18msh3eb9b566d913b1dp17a57fjsnb686d2f40544",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:
        dict = {}
        if rest['Type'] == 'Post-Image':
            dict['type']= 'image'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type']= 'video'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type']= 'carousel'
            dict['media']=rest['media']
            return dict
        else:
            return 'Bad'