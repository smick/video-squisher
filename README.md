# Video Squisher

This Python script uses FFmpeg to squish a video to fit a specified duration while keeping the audio in sync. The output video file will be created in the same folder as the input file with `_squish` added to the end of the file name.

## Requirements

- Python 3.6 or higher
- FFmpeg

## Installation

1. Install Python 3.6 or higher, if not already installed.
2. Install FFmpeg on your system. Follow the installation instructions on the [official FFmpeg website](https://www.ffmpeg.org/download.html). If you're on OS X you can use brew `brew install ffmpeg`.

## Usage

To use the script, open a terminal, navigate to the directory containing the `squish_video_ffmpeg.py` script, and run the following command:

`python squish_video_ffmpeg.py <input_file> <target_duration>`

Replace `<input_file>` with the path to the video file you want to squish, and `<target_duration>` with the desired duration in seconds.

For example:

`python squish_video_ffmpeg.py "/aliens/took/my/laptop/videos/SquirrelNinjaAcademy.mp4" 59`

This command will take the input video file, squish it to fit the 59-second duration, and save the result as a new file with `_squish` added to the end of the file name. The output video will have audio that is in sync with the adjusted video speed.

## License

This project is open source and available under the [MIT License](LICENSE).

