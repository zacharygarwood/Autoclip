from get_clips import get_clips
from download_clips import download_clips

if __name__ == "__main__":
    clips = get_clips()
    downloaded_clips = download_clips(clips)
    print('done')