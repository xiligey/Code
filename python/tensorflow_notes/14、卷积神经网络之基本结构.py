"""
卷积神经网络：Convolutional Neural Networks / CNN
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def ImgConvolve(image_array, kernel):
    """进行卷积操作的函数
    Parameters
    ----------
        image_array: 灰度图像矩阵
        kernel：卷积核
    Return
    ------
        原图像与卷积核进行卷积后的结果
    """
    image_arr = image_array.copy()
    img_dim1, img_dim2 = image_arr.shape
    k_dim1, k_dim2 = kernel.shape
    AddW = int((k_dim1-1)/2)  # 需要0填充的行数和列数
    AddH = int((k_dim2-1)/2)

    # padding填充
    temp = np.zeros([img_dim1+AddW*2, img_dim2+AddH*2])  # 初始化填充完之后的图像矩阵
    # 将原图拷贝到temp的中央
    temp[AddW:AddW+img_dim1, AddH:AddH+img_dim2] = image_arr[:, :]
    # 初始化一张和temp同样大小的图片作为输出图片
    output = np.zeros_like(a=temp)
    # 将扩充后的图和卷积核进行卷积操作
    for i in range(AddW, AddW+img_dim1):
        for j in range(AddH, AddH+img_dim2):
            output[i][j] = int(np.sum(temp[i-AddW:i+AddW+1, j-AddW:j+AddW+1]*kernel))
    return output[AddW:AddW+img_dim1, AddH:AddH+img_dim2]


# 然后定义卷积核
# 提取竖直方向特征
kernel1 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
# 提取水平方向特征
kernel2 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
# Laplace扩展算子 二阶微分算子
kernel3 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

# 定义完卷积核之后，对图像进行卷积操作并展示
image = Image.open("classifier/neuralnetwork/卷积图片.png")
image_array = np.array(image)

# 卷积操作
sobel_x = ImgConvolve(image_array, kernel1)
sobel_y = ImgConvolve(image_array, kernel2)
laplace = ImgConvolve(image_array, kernel3)

# 显示图像
plt.imshow(image_array, cmap=cm.gray)
plt.axis("off")
plt.show()

plt.imshow(sobel_x, cmap=cm.gray)
plt.axis("off")
plt.show()

plt.imshow(sobel_y, cmap=cm.gray)
plt.axis("off")
plt.show()

plt.imshow(laplace, cmap=cm.gray)
plt.axis("off")
plt.show()
