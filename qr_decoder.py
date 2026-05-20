from pyzbar.pyzbar import decode

def decode_qr(image):
    """
    输入: OpenCV图像
    输出: QR内容列表
    """
    results = decode(image)
    return [r.data.decode("utf-8") for r in results]
