import cv2
import os

def cap_video_ffmpeg(input_path, out_path, args):
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    raw_jpg_dir = os.path.join(out_path, 'raw_jpgs')
    if not os.path.exists(raw_jpg_dir):
        os.makedirs(raw_jpg_dir)
    os.system('ffmpeg -loglevel panic -y -i ' + input_path + ' -r ' + str(
        fps) + ' -q:v 2 -f image2 ' + raw_jpg_dir + '/%d.jpg')
    with open(os.path.join(out_path,'fps.txt'), 'w') as f1:
        f1.write(str(fps))

def get_fps(input_video_path):
    cap = cv2.VideoCapture(input_video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    #    print(fps,'-------------------------------------------------------------')
    return fps

def resize(input_path, output_path, image_size=(256, 256)):
    input_imgs_paths = os.listdir(input_path)
    for img_name in input_imgs_paths:
        img = cv2.resize(cv2.imread(os.path.join(input_path, img_name)), image_size)
        # img = cv2.flip(img, -1)
        output_name = os.path.join(output_path, img_name)
        print(output_name)
        cv2.imwrite(output_name, img)
    return


if __name__ == '__main__':
    input_path = ".\dataset\heart\Heart-two_png"
    output_path = ".\dataset\heart\Heart-two_png256"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    resize(input_path, output_path)