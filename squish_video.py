import sys
import os
import subprocess

def squish_video(input_file, target_duration):
    # Calculate the speedup factor
    video_duration_cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        input_file
    ]
    video_duration = float(subprocess.check_output(video_duration_cmd).strip())
    speedup_factor = video_duration / target_duration

    # Generate the output file name
    input_file_name, input_file_ext = os.path.splitext(input_file)
    output_file = input_file_name + "_squish" + input_file_ext

    # Squish the video and audio using FFmpeg
    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        input_file,
        "-vf",
        f"setpts={1/speedup_factor}*PTS",
        "-af",
        f"atempo={speedup_factor}",
        "-y",
        output_file
    ]
    subprocess.run(ffmpeg_cmd)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python squish_video_ffmpeg.py <input_file> <target_duration>")
        sys.exit(1)

    input_file = sys.argv[1]
    target_duration = float(sys.argv[2])

    squish_video(input_file, target_duration)
