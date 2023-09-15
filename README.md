# jittor-Labmem-Landscape
第三届计图人工智能挑战赛。使用jittor框架在风景图片数据集上训练模型，根据输入的mask和ref图，生成对应的gen图。

# jittor 计图挑战热身赛 Conditional GAN
![result](./select/385491480_17acdedabd_b.jpg)
          
## 简介
本项目包含了第三届计图人工智能挑战赛 - 计图挑战热身赛的代码实现。在数字图片数据集 MNIST 上训练 Conditional GAN 模型，通过输入一个随机向量 z 和额外的类别标签信息 y ，生成特定数字的图像。

## 安装

#### 运行环境

- ubuntu 20.04 LTS
- python >= 3.7
- jittor >= 1.3.0

#### 安装依赖

```bash
pip install -r requirements.txt # 本目录下的requirements.txt
```

#### 数据集

赛事训练数据集[由此下载](https://cloud.tsinghua.edu.cn/f/063e7fcfe6a04184904d/?dl=1)。

预训练模型采用的是 `Jittor` 框架自带的 `vgg19` 模型，无需额外下载，在代码运行的过程中会载入到内存里。

## 训练

在单卡上训练：

```bash
sh train.sh
```
此前需要修改train.sh，其内容为：
```bash
# train.sh
CUDA_VISIBLE_DEVICES="0" python train.py --input_path {训练数据集路径（即train_resized文件夹所在路径）}
```
## 测试

在单卡上进行测试：

```bash 
sh test.sh
```

此前需要：
1. 将label与img的映射关系（label_to_img.json）放置在gaugan目录下
2. 修改test.sh，其内容为：
```bash
CUDA_VISIBLE_DEVICES="0" python test.py  \
--input_path {测试数据集路径（即labels文件夹所在路径），它提供label mask图} \
--img_path {训练数据集的图片路径（即train_resized/imgs文件夹所在路径，它提供ref图）}
--which_epoch {使用的模型的epoch数目}
```


##致谢
本项目代码参考了jittor官方提供的[GauGAN](https://github.com/Jittor/JGAN/tree/master/models/gaugan)以及[SESAME](www.code.com)。
