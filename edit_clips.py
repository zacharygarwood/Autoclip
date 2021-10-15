from moviepy.editor import *
import shutil

def edit_clips(clips):
    print('in edit clips')
    description = 'subscribe :)\n\n'
    title = ''
    total_duration = 600
    curr_duration = 0
    clip_list = []

    for clip in clips:
        if(curr_duration < total_duration):
            video = VideoFileClip('D:/zgarw/Documents/Projects/autoclip/tmp/' + clip['slug'] + '.mp4')
            transition = VideoFileClip('D:/zgarw/Documents/Projects/autoclip/transition/transition.mp4')
            clip_list.append(video.resize(width=1920,height=1080))
            clip_list.append(transition.resize(width=1920,height=1080))
            if(curr_duration%60 == 0):
                description += str(int(curr_duration/60)) + ':00' + ' - ' + clip['title'] + ' - ' + clip['channel_url'] + '\n'
            elif(int((curr_duration%60)/10) == 0):
                description += str(int(curr_duration/60)) + ':0' + str(curr_duration%60) + ' - ' + clip['title'] + ' - ' + clip['channel_url'] + '\n'
            else:
                description += str(int(curr_duration/60)) + ':' + str(curr_duration%60) + ' - ' + clip['title'] + ' - ' + clip['channel_url'] + '\n'
                
            video_duration = int(video.duration) + int(transition.duration)
            curr_duration += video_duration
    
    # removes the transition at the end
    clip_list.pop()
    main = concatenate_videoclips(clip_list, method='compose')

    file = open(r"D:\zgarw\Documents\Projects\autoclip\count.txt","r+")
    vid_num = int(file.read())
    title += 'Top Twitch Clips of the Day #' + str(vid_num)
    file.close()

    file = open(r"D:\zgarw\Documents\Projects\autoclip\count.txt","w+")
    file.write(str(vid_num+1))
    file.close()

    main.write_videofile(title + '.mp4')   
    shutil.move("D:/zgarw/Documents/Projects/autoclip/" + title + '.mp4', 'D:/zgarw/Documents/Projects/autoclip/fin/' + title + '.mp4')
    print(title)   
    print(description)
    print(curr_duration)
    return title, description 
    
        
