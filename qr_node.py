import cv2

def load_image(image_path):
    """
    读取图像
    """
    img = cv2.imread(image_path)
    return img
