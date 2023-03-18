import argparse
import cv2
import matplotlib.pyplot as plt

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='', type=str, help='file path of input video (.mp4)')
    parser.add_argument('--output', default='outputs/', type=str, help='directry path for outputs')
    parser.add_argument('--mode', default='rgb', type=str, help='rgb or mask')
    parser.add_argument('--threshold', default=150, type=int, help='for binarization')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()

    video = cv2.VideoCapture(args.input)
    print(f'num frame: {video.get(cv2.CAP_PROP_FRAME_COUNT)}')

    i=0
    while video.isOpened():
        _ret, frame = video.read()
        if args.mode == 'rgb':
            save_path = args.output + 'rgb/' + args.input.split('.')[0].split('/')[-1] + '_mask%04d.png'%i
            print(save_path)
            plt.imsave(save_path, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        elif args.mode == 'mask':
            save_path = args.output + 'mask/' + args.input.split('.')[0].split('/')[-1] + '_mask%04d.png'%i
            print(save_path)
            _ret, mask = cv2.threshold(frame, args.threshold, 255, cv2.THRESH_BINARY)
            plt.imsave(save_path, mask, cmap='gray')
        i += 1
