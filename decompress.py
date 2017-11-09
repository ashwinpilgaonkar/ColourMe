import cv2
import os
import shutil
import moviepy.editor as mp

# Extract images (frames) from video file
extract_path = os.getcwd()+"\data"
img_path = extract_path+"\extract_img"

if not os.path.exists(extract_path):
    os.makedirs(extract_path)
    os.makedirs(img_path)

else:
    shutil.rmtree(extract_path)
    os.makedirs(extract_path)
    os.makedirs(img_path)

vidcap = cv2.VideoCapture('sampleVideo.mp4')
success,image = vidcap.read()
count = 0
success = True

while success:
  success,image = vidcap.read()
  print('Extracting frame: ', count)
  print(success)
  cv2.imwrite(os.path.join(img_path , "frame%d.jpg") % count, image) # save frame as JPEG file
  count += 1


# Extract audio track from video file
clip = mp.VideoFileClip("sampleVideo.mp4")
clip.audio.write_audiofile(os.path.join(extract_path , "audio.mp3"))