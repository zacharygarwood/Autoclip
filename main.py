from get_clips import get_clips
from download_clips import download_clips
from upload_clips import upload_clips

if __name__ == "__main__":
    clips = get_clips()
    download_clips(clips)
    upload_clips(clips)

    print('done')