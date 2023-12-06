import moviepy.editor as mp
import os
import sys

def convert_mp4_to_gif(input_path, output_path, fps=10):
    clip = mp.VideoFileClip(input_path)
    clip.write_gif(output_path, fps=fps)

# Example usage
if __name__ == '__main__':
    input_video_path = sys.argv[1]
    output_gif_path = 'assets/' + os.path.basename(input_video_path).split('.')[0] + '.gif'

    convert_mp4_to_gif(input_video_path, output_gif_path)

