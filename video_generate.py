import cv2
import os
from PIL import Image

# Path to the directory containing the images
image_folder = 'gan_images'
# Output video file name
video_name = 'gan_training.avi'

# Get all image filenames and sort them by epoch number
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort(key=lambda x: int(os.path.splitext(x)[0]))

# Determine the width and height from the first image
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)

    # Extract epoch number from the image filename
    epoch_number = os.path.splitext(image)[0]

    # Add text overlay to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'Learning after epoch {epoch_number}', (
        10, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    # Write the frame into the video
    video.write(frame)

# Release the video writer
video.release()

print(f'Video saved as {video_name}')
