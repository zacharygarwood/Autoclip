from datetime import datetime
import requests
import json
import time
import os

def get_clips():
    number_of_videos = 50
    period = 'day'
    language = 'en'
    url="https://api.twitch.tv/kraken/clips/top?limit="+str(number_of_videos)+"&language="+language+"&period="+period
    referrer = "google.com"
    client_id = '<client id goes here>'
    headers = {
        'Client-ID' : client_id,    
        'Accept': 'application/vnd.twitchtv.v5+json'
    }
    response = requests.get(url, headers=headers, timeout=10)
    clips=[]    
    paths=[]   
    response_dict = json.loads(response.content)
    temp = None;
    for item in response_dict['clips']:
        clip_slug = item['slug']
        clip_image = item['thumbnails']['medium']
        clip_url = item['url']
        clip_title = item['title']
        channel_url = item['broadcaster']['channel_url']
        clip_details = {'slug': clip_slug, 'url': clip_url, 'image': clip_image, 'title': clip_title[0:99], 'channel_url': channel_url};
        clips.append(clip_details)
    return clips