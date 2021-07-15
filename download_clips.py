import os
import sys
import urllib.request

def download_clips(clips):
    client_id = 'owmbz8hmskjc1qccso5ocjotg870xc'
    basepath = 'tmp/'
    
    for clip in clips:
        mp4_url = clip['image'].split('-preview',1)[0] + ".mp4"
        out_filename = clip['slug'] + ".mp4"
        output_path = basepath + out_filename
        print("mp4 url: " + mp4_url)
        print("out filename " + out_filename)
        # create the basepath directory
        if not os.path.exists(basepath):
            os.makedirs(basepath)

        try:
            urllib.request.urlretrieve(mp4_url, output_path)
        except:
            print("An exception occurred")
        print('done')



