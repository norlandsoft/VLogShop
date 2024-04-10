import whisper
from pydub import AudioSegment
from pydub.silence import split_on_silence

# 加载 Whisper 模型
# model_path = '/opt/AirOne/machine/workspace/models/whisper-large-v3'
# whisper_model = whisper.load_model("large-v3", device="mps", download_root=model_path)


def audio_to_text(audio_path, output_file):
    """
    将音频文件转换为文本
    """
    # 音频文件拆分
    split_audio_by_silence(audio_path)
    # result = whisper_model.transcribe(audio_path)
    # print(result["text"])


def text_to_audio(text, output_file):
    """
    将文本转换为音频文件
    """
    pass


def split_audio_by_silence(input_file, silence_threshold=-50, min_silence_duration=100):
    audio = AudioSegment.from_file(input_file)

    # 根据静音拆分音频
    segments = split_on_silence(
        audio,
        min_silence_len=min_silence_duration,
        silence_thresh=silence_threshold
    )

    # 将每个段导出为单独的文件
    for i, segment in enumerate(segments, start=1):
        output_file = f"chunk_{i}.mp3"
        segment.export(output_file, format="mp3")

        # 打印每个片段的开始和结束时间
        chunk_start_time = (segment[0].frame_count() / segment.frame_rate) * 1000
        chunk_end_time = (segment[-1].frame_count() / segment.frame_rate) * 1000
        print(f"Chunk {i}: {chunk_start_time}ms to {chunk_end_time}ms")