import matplotlib.pyplot as plt
import numpy as np
import paddle
from PIL import Image
from PIL.Image import Resampling


# img_path = './example_0.jpg'
# # 读取原始图像并显示
# im = Image.open('./example_0.jpg')
# plt.imshow(im)
# plt.show()
# # 将原始图像转为灰度图
# im = im.convert('L')
# print('原始图像shape: ', np.array(im).shape)
# # 使用Image.ANTIALIAS方式采样原始图片
# im = im.resize((28, 28), Image.ANTIALIAS)
# plt.imshow(im)
# plt.show()
# print("采样后图片shape: ", np.array(im).shape)

# 读取一张本地的样例图片，转变成模型输入的格式

#再次定义MNIST 避免对train.py中的内容进行执行
class MNIST(paddle.nn.Layer):
    def __init__(self):
        super(MNIST, self).__init__()

        # 定义一层全连接层，输出维度是1
        self.fc = paddle.nn.Linear(in_features=784, out_features=1)

    # 定义网络结构的前向计算过程
    def forward(self, inputs):
        outputs = self.fc(inputs)
        return outputs

if __name__ == "__main__":
    def load_image(img_path):
        # 从img_path中读取图像，并转为灰度图
        im = Image.open(img_path).convert('L')
        print(np.array(im))
        im = im.resize((28, 28), Resampling.LANCZOS)
        im = np.array(im).reshape(1, -1).astype(np.float32)
        # 图像归一化，保持和数据集的数据范围一致
        im = 1 - im / 255
        return im
    # 定义预测过程
    model = MNIST()
    params_file_path = 'mnist.pdparams'
    img_path = './example_0.jpg'
    # 加载模型参数
    param_dict = paddle.load(params_file_path)
    model.load_dict(param_dict)
    # 灌入数据
    model.eval()
    tensor_img = load_image(img_path)
    result = model(paddle.to_tensor(tensor_img))
    print('result',result)
    #  预测输出取整，即为预测的数字，打印结果
    print("本次预测的数字是", result.numpy().astype('int32'))