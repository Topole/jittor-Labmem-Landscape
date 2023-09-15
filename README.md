# jittor 风格及语义引导的风景图片生成
          
## 简介
本项目包含了第三届计图人工智能挑战赛 - 赛题一：风格及语义引导的风景图片生成的代码实现。

项目使用jittor框架在风景图片数据集上训练模型，根据输入的mask和ref图，生成对应的gen图。gen图需要考虑mask图的语义分割信息，以及ref图的（色调等）风格信息。



## 队伍成员及分工

* 陈柯文：负责算法 `GAUGAN + ColorLoss` 和 `OASIS Variant` 的实现与仓库维护
* 肖颂霖：负责算法 `DPGAN  Variant` 和 `GAUGAN + SESAME` 的实现与报告撰写

## 实现效果
我们在测试集上实现的效果如下（左一为风格参考图，左二为语义标签图，其余为各模型生成图像）：

<center>
<img src="./select/385491480_17acdedabd_b.jpg" />
</center>


## 算法背景
我们主要使用 $Jittor$ 实现了 $GAUGAN + ColorLoss$ 、 $GAUGAN + SESAME$ 、 $OASIS$ 、 $DP-GAN$ 的模型结构并成功跑通训练和测试流程。我们开源了效果最好的版本，即 `GAUGAN + SESAME`

![result](./select/385491480_17acdedabd_b.jpg)

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

请在赛事[官方网站](https://www.educoder.net/competitions/index/Jittor-4)下载训练数据集和测试数据集。

预训练模型采用的是 `Jittor` 框架自带的 `vgg19` 模型，无需额外下载，在代码运行的过程中会载入到内存里。

## 训练

```bash
sh train.sh
```
此前需要修改train.sh，其内容为：
```bash
# train.sh
CUDA_VISIBLE_DEVICES="0,1,2,3" mpirun -np 4 python -m train.py --input_path {训练数据集路径（即train_resized文件夹所在路径）}
```
## 推理

在单卡上进行测试：

```bash 
sh test.sh
```

此前需要：
1. 将label与img的映射关系（label_to_img.json）放置在目录下
2. 修改test.sh，其内容为：
```bash
CUDA_VISIBLE_DEVICES="0" python test.py  \
--input_path {测试数据集路径（即labels文件夹所在路径），它提供label mask图} \
--img_path {训练数据集的图片路径（即train_resized/imgs文件夹所在路径，它提供ref图）}
--which_epoch {使用的模型的epoch数目}
```


##致谢
本项目代码参考了jittor官方提供的[GauGAN](https://github.com/Jittor/JGAN/tree/master/models/gaugan)以及[SESAME]([www.code.com](https://github.com/entavelis/OpenSESAME)https://github.com/entavelis/OpenSESAME)。
