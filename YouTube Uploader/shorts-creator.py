import os
import random
from moviepy.video.io.VideoFileClip import VideoFileClip

# Function to extract a random 30-second clip from a video
def extract_random_clip(video_path, output_path):
    clip = VideoFileClip(video_path)
    duration = clip.duration
    start_time = random.uniform(0, duration - 30)  # Ensure at least 30 seconds left
    end_time = start_time + 30
    sub_clip = clip.subclip(start_time, end_time)
    sub_clip.write_videofile(output_path)
    clip.close()

# Function to generate a random title
def generate_title():
    titles = ["Exploring", "Adventure Time", "City Life", "Travel Diaries", "Nature's Beauty"]
    return random.choice(titles)

# Function to generate a random description
def generate_description():
    descriptions = ["Join me as I explore the world!", "Experience the thrill of adventure!", "Discover the beauty of the city!",
                    "Embark on a journey through nature!", "Let's travel together and make memories!"]
    return random.choice(descriptions)

# Main function
def main():
    video_path = "path_to_your_long_video.mp4"
    output_folder = "cutouts"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(10):  # Generate 10 random cutouts
        output_path = os.path.join(output_folder, f"cutout_{i}.mp4")
        extract_random_clip(video_path, output_path)
        title = generate_title()
        description = generate_description()
        with open(os.path.splitext(output_path)[0] + ".txt", "w") as f:
            f.write(f"Title: {title}\n\nDescription: {description}")

if __name__ == "__main__":
    main()

