import os
import sys
import urllib.request

def download_clips(clips):
    tmp = 'D:/zgarw/Documents/Projects/autoclip/tmp/'
    img = 'D:/zgarw/Documents/Projects/autoclip/img/'
    
    for clip in clips:
        mp4_url = clip['image'].split('-preview',1)[0] + ".mp4"
        img_url = clip['image']
        out_filename_vid = clip['slug'] + ".mp4"
        out_filename_img = clip['slug'] + ".jpg"

        output_path_vid = tmp + out_filename_vid
        output_path_img = img + out_filename_img
        # create the basepath directory

        try:
            #move files to output path
            urllib.request.urlretrieve(mp4_url, output_path_vid)
            urllib.request.urlretrieve(img_url, output_path_img)
        except:
            print("An exception occurred")




