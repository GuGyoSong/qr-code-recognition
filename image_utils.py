!/usr/bin/env python3
 coding=utf-8

import rospy
import cv2

from qr_vision_ros.msg import TaskRequest, TaskResult
from image_utils import load_image
from qr_decoder import decode_qr
from qr_parser import parse_qr


class QRNode:

    def __init__(self):

        rospy.init_node("qr_node")

        self.sub = rospy.Subscriber(
            "/task_request",
            TaskRequest,
            self.callback
        )

        self.pub = rospy.Publisher(
            "/task_result",
            TaskResult,
            queue_size=10
        )

        rospy.loginfo("QR Node Started")

    def callback(self, msg):

        # 1. 读图
        img = load_image(msg.image_path)

        if img is None:
            rospy.logerr("Image load failed")
            return

        # 2. 解码二维码
        qr_list = decode_qr(img)

        # 3. 解析业务逻辑
        has_a, has_b, has_c, slot = parse_qr(qr_list)

        # 4. 输出结果
        result = TaskResult()
        result.task_id = msg.task_id
        result.has_a = has_a
        result.has_b = has_b
        result.has_c = has_c
        result.delivery_slot = slot

        self.pub.publish(result)

        rospy.loginfo("Published result")


if __name__ == "__main__":
    QRNode()
    rospy.spin()
