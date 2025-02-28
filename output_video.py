import cv2
import os
import numpy as np
import time

def write_video(out_path, output_img_list, avi_name):
    fps = 30
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(os.path.join(out_path, '{}.avi'.format(avi_name)), fourcc, fps, (512, 256))
    for i, image in enumerate(output_img_list):
        out.write(image)
        cv2.imshow("", image)
        cv2.waitKey(1)
        time.sleep(0.02)
    out.release()

if __name__ == '__main__':
    avi_name = "Beating_Heart_to_US"
    output_img_list = []
    image_path = "C:/Users/wangyuan/projects/sequence-model/pytorch-CycleGAN-and-pix2pix-master/results/heart2US_cyclegan/test_100/images"
    for img_num in range(14, 506):
        # print(os.path.join(image_path, '{}_real.png'.format(str(img_num).zfill(4))))
        realA = cv2.imread(os.path.join(image_path, '{}_real.png'.format(str(img_num).zfill(4))), cv2.IMREAD_COLOR)
        fakeB = cv2.imread(os.path.join(image_path, '{}_fake.png'.format(str(img_num).zfill(4))), cv2.IMREAD_COLOR)
        output_img_list.append(np.concatenate([realA, fakeB], axis=1))
    write_video(image_path, output_img_list, avi_name)