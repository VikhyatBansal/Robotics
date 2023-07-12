#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class My_Cam(Node):
    def __init__(self):
        super().__init__('my_cam')
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(
            Image,
            '/demo/camera/image_raw',
            self.callback,
            10
        )

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        except cv2.CvBridgeError as e:
            self.get_logger().error(str(e))

        image = cv_image

        resized_image = cv2.resize(image, (360, 640))

        # cv2.imshow("Camera output normal", image)
        cv2.imshow("Camera output resized", resized_image)

        cv2.waitKey(3)


def main(args=None):
    rclpy.init(args=args)
    camera_node = My_Cam()

    try:
        rclpy.spin(camera_node)
    except KeyboardInterrupt:
        pass

    camera_node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
