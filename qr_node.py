#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import cv2

from qr_vision_system.msg import (
    TaskRequest,
    TaskResult
)

from qr_decoder import decode_qr
from qr_parser import parse_qr


class QRNode:

    def __init__(self):

        rospy.init_node("qr_node")

        # 订阅任务
        self.sub = rospy.Subscriber(
            "/task_request",
            TaskRequest,
            self.callback,
            queue_size=1
        )

        # 发布结果
        self.pub = rospy.Publisher(
            "/task_result",
            TaskResult,
            queue_size=10
        )

        rospy.loginfo("QR Node Started")

    def callback(self, msg):

        rospy.loginfo(
            f"Receive Task: {msg.task_id}"
        )

        # 读取图片
        image = cv2.imread(msg.image_path)

        if image is None:

            rospy.logerr(
                "Image Load Failed"
            )

            return

        # 二维码识别
        qr_list = decode_qr(image)

        rospy.loginfo(
            f"QR Result: {qr_list}"
        )

        # 业务逻辑解析
        (
            has_a,
            has_b,
            has_c,
            delivery_slot
        ) = parse_qr(qr_list)

        # 封装结果
        result = TaskResult()

        result.task_id = msg.task_id

        result.has_a = has_a
        result.has_b = has_b
        result.has_c = has_c

        result.delivery_slot = delivery_slot

        # 发布结果
        self.pub.publish(result)

        rospy.loginfo(
            "Task Result Published"
        )


if __name__ == "__main__":

    QRNode()

    rospy.spin()
