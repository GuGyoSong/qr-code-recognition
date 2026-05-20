# qr-code-recognition
# QR Vision ROS System

## 功能
- 接收任务请求（TaskRequest）
- 读取图像
- 二维码识别
- 输出结构化结果（TaskResult）

## 运行

```bash
roslaunch qr_vision_ros qr_system.launch

## launch
### qr_system.launch
<launch>
    <node pkg="qr_vision_ros"
          type="qr_node.py"
          name="qr_node"
          output="screen"/>
</launch>
