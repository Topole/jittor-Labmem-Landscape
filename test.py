import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', type=str, default='./val/val_A_labels_resized')
parser.add_argument('--img_path', type=str, default='./imgs')
parser.add_argument('--output_path', type=str, default='./result')
args = parser.parse_args()
cmd_str = f'python spade_test.py --name sesame --dataset_mode custom --label_dir {args.input_path} --image_dir {args.img_path} --label_nc 29 --no_instance --use_vae --which_epoch {400} --no_pairing_check --output_path {args.output_path}'
subprocess.call(cmd_str, shell=True)
