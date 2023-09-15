import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', type=str, default='./train_datasets')

args = parser.parse_args()

print('训练生成数据存储在./checkpoints/bs4vae中')
subprocess.call(f'python spade_train.py --name sesame --dataset_mode custom --val_dir {args.input_path}/val --label_dir {args.input_path}/labels --image_dir {args.input_path}/imgs --label_nc 29 --no_instance --use_vae --batchSize 32 --netD sesamemultiscale --niter 100 --niter_decay 300 --no_inpaint --continue_train ', shell=True)
