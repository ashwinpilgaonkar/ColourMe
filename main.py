import cv2
import os
import shutil
import moviepy.editor as mp

extract_path = os.getcwd()+"\data"
img_path = extract_path+"\extract_img"

def extract():

    # Extract images (frames) from video file
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
        os.makedirs(img_path)

    else:
        shutil.rmtree(extract_path)
        os.remove("output.mp4")
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

def recompileVideo():
    os.system("ffmpeg.win32 -start_number 0 -i "+img_path+"\\frame%d.jpg -framerate 30 -vcodec h264 output_temp.mp4")
    os.system("ffmpeg.win32 -i "+extract_path+"\\audio.mp3 -i output_temp.mp4 -acodec copy -vcodec copy output.mp4")
    os.remove("output_temp.mp4")

def main():
    extract()
    recompileVideo()

if __name__ == '__main__':
    main()