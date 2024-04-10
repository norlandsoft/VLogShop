# 下载Youtube视频
import sys

from pytube import YouTube
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from youtubesearchpython import VideosSearch
from datetime import datetime, timedelta
import dateparser


def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining) / stream.filesize)
    percent = '{0:.1f}'.format(current * 100)
    progress = int(50 * current)
    sys.stdout.write("\r[%s%s] %s%%" % ('=' * progress, ' ' * (50 - progress), percent))


# 从视频中提取音频
def extract_audio(video_file, audio_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)


def download_video(url, output_path='.'):
    try:
        # 创建YouTube对象
        yt = YouTube(url)

        # 获取视频的最高分辨率流
        video_stream = yt.streams.get_highest_resolution()

        # 注册回调函数
        yt.register_on_progress_callback(progress_function)

        # 获取视频标题
        video_title = yt.title
        print(f'视频标题: {video_title}')

        # 下载视频
        video_stream.download(output_path)
        print(f'\n视频下载成功: {video_title}')
        return output_path + '/' + video_stream.default_filename
    except Exception as e:
        print(f'下载失败: {e}')
        return None


def search_and_sort_videos(query):
    # Perform YouTube search
    videos_search = VideosSearch(query, limit=50)

    # Get search results
    results = videos_search.result()

    # Extract video information
    video_list = results['result']

    # Get the current date and time
    now = datetime.now()

    # Calculate the date and time
    days_ago = now - timedelta(days=15)

    recent_videos = [video for video in video_list if
                     dateparser.parse(video['publishedTime']) is not None and dateparser.parse(
                         video['publishedTime']) >= days_ago]

    # Sort videos by published time
    sorted_videos = sorted(recent_videos,
                           key=lambda x: dateparser.parse(x['publishedTime']),
                           reverse=True)

    # Display sorted videos
    for video in sorted_videos:
        print(f"Title: {video['title']}")
        print(f"Published Time: {video['publishedTime']}")
        print(f"URL: {video['link']}")
        print("")


if __name__ == "__main__":
    video_file_path = download_video("https://www.youtube.com/watch?v=rUw4cs2MHwc", "/opt/VLogShop/workspace")
    if video_file_path is not None:
        # video_file_path文件扩展名替换为mp3
        audio_file_path = video_file_path.replace('.mp4', '.mp3')
        # 提取视频的音频
        extract_audio(video_file_path, audio_file_path)

        # Convert mp3 file to wav
        # audio = AudioSegment.from_mp3(audio_file_path)
        # wav_file_path = audio_file_path.replace('.mp3', '.wav')
        # audio.export(wav_file_path, format="wav")

        from audio_tool import audio_to_text
        audio_to_text(audio_file_path, "")



    # Specify the keywords you want to search for
    # search_keywords = "Prince Andrew Jeffrey Epstein"

    # Search and sort videos
    # search_and_sort_videos(search_keywords)

    # 替换为您要下载的YouTube视频的URL
    # video_url = 'https://www.youtube.com/watch?v=2KHpmMMXhlE'

    # 替换为您希望保存视频的目录
    # output_directory = './workspace/output/videos/cache'
    #
    # video_file_path = download_video(video_url, output_directory)
    # if video_file_path is not None:
    #     # video_file_path文件扩展名替换为mp3
    #     audio_file_path = video_file_path.replace('.mp4', '.mp3')
    #     # 提取视频的音频
    #     extract_audio(video_file_path, audio_file_path)