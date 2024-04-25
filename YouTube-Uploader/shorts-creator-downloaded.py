import cv2
import numpy as np
import moviepy.editor as mp
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def process_video(local_file_path, output_modifier="modified"):
    try:
        # Check if the file exists
        if not os.path.exists(local_file_path):
            print(f"The file '{local_file_path}' does not exist.")
            return

        custom_filename = os.path.basename(local_file_path)

        # renamer
        reversed_string = custom_filename[::-1]
        index = reversed_string.find('|')
        if index != -1:
            sliced_reversed_string = reversed_string[:index]
        else:
            sliced_reversed_string = reversed_string

        final_name = sliced_reversed_string[::-1]

        resolution = "Unknown Resolution"

        print(f'{custom_filename} Video loaded successfully!')
        print('Resolution:', resolution)
        print("working")

        output_video = f'{output_modifier}_{final_name}'
        cap = cv2.VideoCapture(local_file_path)
        if not cap.isOpened():
            print("Error: Couldn't open video file.")
            return

        target_width, target_height = 1080, 1920

        # Get input video properties
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Calculate the aspect ratios
        aspect_ratio_input = width / height
        aspect_ratio_target = target_width / target_height

        # Calculate the new size
        if aspect_ratio_input > aspect_ratio_target:
            # Fit width
            new_width = target_width
            new_height = int(new_width / aspect_ratio_input)
        else:
            # Fit height
            new_height = target_height
            new_width = int(new_height * aspect_ratio_input)

        # Calculate margins
        margin_top = (target_height - new_height) // 2
        margin_bottom = target_height - new_height - margin_top
        margin_left = (target_width - new_width) // 2
        margin_right = target_width - new_width - margin_left

        # Create black background canvas
        black_background = np.zeros((target_height, target_width, 3), dtype=np.uint8) * 255

        # Create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify codec
        out = cv2.VideoWriter(output_video, fourcc, fps, (target_width, target_height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Resize the frame
            resized_frame = cv2.resize(frame, (new_width, new_height))

            # Add the resized frame to the black background canvas
            black_background[margin_top:margin_top + new_height, margin_left:margin_left + new_width] = resized_frame

            # Write the black background with the resized frame to the output video
            out.write(black_background)

        # Release VideoCapture and VideoWriter
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        print(f'Output file "{output_video}" created successfully.')

        # Extract audio and merge it with the modified video
        audio_clip = mp.AudioFileClip(local_file_path)
        audio_clip.write_audiofile(f'{output_modifier}_audio.mp3')

        final_video_clip = mp.VideoFileClip(output_video)
        final_video_clip.write_videofile(f'{output_modifier}_with_audio.mp4', audio=f'{output_modifier}_audio.mp3')

        os.rename(f'{output_modifier}_with_audio.mp4', f'{final_name}_edited.mp4')
        os.remove(f'{output_modifier}_audio.mp3')
        os.remove(f'{local_file_path}')
        os.remove(f'{output_video}')
        print('Audio extracted and merged with the modified video successfully.')

        ##############################
        # Create output folder if it doesn't exist
        namewithoutextentoin = final_name.replace(".mp4", '')

        video_path = f'{final_name}_edited.mp4'
        output_folder = f'{namewithoutextentoin}_shorts'
        os.makedirs(output_folder, exist_ok=True)

        # Open the video file
        video = VideoFileClip(video_path)

        # Calculate the duration of the video in seconds
        duration = video.duration

        # Calculate the number of clips and duration of each clip
        num_clips = int(duration // 30) + 1
        clip_duration = 30

        # Extract each clip
        for i in range(num_clips):
            # Set start and end times for the clip
            start_time = i * clip_duration
            end_time = min((i + 1) * clip_duration, duration)
            outro = VideoFileClip("outro.mp4")
            # Extract and save the clip
            clip1 = video.subclip(start_time, end_time)
            clip = concatenate_videoclips([clip1, outro])
            clip_name = f"{namewithoutextentoin} Shorts {i + 1}.mp4"
            clip_path = os.path.join(output_folder, clip_name)
            clip.write_videofile(clip_path, codec='libx264', audio_codec="aac")

        # Close the video file
        video.close()
    except Exception as e:
        print(f"An error occurred while processing the video '{local_file_path}': {e}")
        return

# Example usage:
video_paths = [
    "Downloaded-Videos\VLOG 11.mp4",
    # Add more paths as needed
]
for path in video_paths:
    process_video(path, output_modifier='modified')
