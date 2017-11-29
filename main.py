import cv2
import os
import shutil
import moviepy.editor as mp
from PIL import Image

extract_path = os.getcwd()+"\data"
img_path = extract_path+"\extract_img"
img_resize_path = extract_path+"\\resize_img"
fps = 0

def extract():

    global fps

    # Extract images (frames) from video file
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
        os.makedirs(img_path)
        os.makedirs(img_resize_path)

    else:
        shutil.rmtree(extract_path)
        os.makedirs(extract_path)
        os.makedirs(img_path)
        os.makedirs(img_resize_path)

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

    duration = clip.duration
    fps = count/duration

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
 
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.save(output_image_path)

def recompileVideo():
    os.system("ffmpeg.win32 -start_number 0 -i "+img_path+"\\frame%d.jpg -framerate -vcodec h264 fps=29 output_temp.mp4")
    os.system("ffmpeg.win32 -i "+extract_path+"\\audio.mp3 -i output_temp.mp4 -acodec copy -vcodec copy output.mp4")
    
    if os.path.exists(os.getcwd()+"\output_temp.mp4"):
        os.remove(os.getcwd()+"\output_temp.mp4")

def main():
    extract()

    num=0
    for filename in os.listdir(img_path):
        if filename.endswith(".jpg"): 
            resize_image(input_image_path=img_path+"\\frame"+str(num)+".jpg",
                output_image_path=img_resize_path+"\\frame"+str(num)+".jpg",
                size=(400, 400))
            num = num + 1
            continue
        else:
            continue

    recompileVideo()

if __name__ == '__main__':
    main()