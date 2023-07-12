###### !/usr/bin/env python3   

# import rclpy
# import cv2

# from rclpy.node import Node
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge, CvBridgeError
# from pyzbar.pyzbar import decode

# class camera_1:

#   def __init__(self):
#     self.node = rclpy.create_node('camera_read')
#     self.image_sub = self.node.create_subscription(Image, '/demo/camera/image_raw', self.callback, 10)
#     self.bridge = CvBridge()

#   def callback(self, data):
#     try:
#       cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
#     except CvBridgeError as e:
#       self.node.get_logger().error(e)

#     (rows,cols,channels) = cv_image.shape
    
#     image = cv_image

#     resized_image = cv2.resize(image, (360, 640)) 

#     gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
#     thresh = 40
#     img_bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]

#     #cv2.imshow("B&W Image", gray)
#     #cv2.imshow("B&W Image /w threshold", img_bw)

#     qr_result = decode(img_bw)

#     #print (qr_result)
    
#     qr_data = qr_result[0].data
#     print(qr_data)

#     (x, y, w, h) = qr_result[0].rect

#     cv2.rectangle(resized_image, (x, y), (x + w, y + h), (0, 0, 255), 4)

#     text = "{}".format(qr_data)
#     cv2.putText(resized_image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#     cv2.imshow("Camera output", resized_image)

#     cv2.waitKey(5)

# def main():
#   rclpy.init()
#   camera_1_node = camera_1()
#   try:
#     rclpy.spin(camera_1_node.node)
#   except KeyboardInterrupt:
#     camera_1_node.node.get_logger().info("Shutting down")
  
#   cv2.destroyAllWindows()
#   camera_1_node.node.destroy_node()
#   rclpy.shutdown()

# if __name__ == '__main__':
#   main()











# import rclpy
# import cv2

# from rclpy.node import Node
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge, CvBridgeError
# from pyzbar.pyzbar import decode

# class camera_1:

#   def __init__(self):
#     self.node = rclpy.create_node('camera_read')
#     self.image_sub = self.node.create_subscription(Image, '/demo/camera/image_raw', self.callback, 10)
#     self.bridge = CvBridge()

#   def callback(self, data):
#     try:
#       cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
#     except CvBridgeError as e:
#       self.node.get_logger().error(e)

#     (rows,cols,channels) = cv_image.shape
    
#     image = cv_image

#     resized_image = cv2.resize(image, (360, 640)) 

#     gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
#     thresh = 40
#     img_bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]

#     qr_result = decode(img_bw)

#     if len(qr_result) > 0:  # Check if a QR code was found
#         qr_data = qr_result[0].data
#         print(qr_data)

#         (x, y, w, h) = qr_result[0].rect

#         cv2.rectangle(resized_image, (x, y), (x + w, y + h), (0, 0, 255), 4)

#         text = "{}".format(qr_data)
#         cv2.putText(resized_image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#         cv2.imshow("QR Code", resized_image)  # Show the image with the QR code

#     cv2.waitKey(5)

# def main():
#   rclpy.init()
#   camera_1_node = camera_1()
#   try:
#     rclpy.spin(camera_1_node.node)
#   except KeyboardInterrupt:
#     camera_1_node.node.get_logger().info("Shutting down")
  
#   cv2.destroyAllWindows()
#   camera_1_node.node.destroy_node()
#   rclpy.shutdown()

# if __name__ == '__main__':
#   main()






#!/usr/bin/env python3
import cv2
from pyzbar import pyzbar
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class QRCodeReader(Node):
    def __init__(self):
        super().__init__('qr_code_reader')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/demo/camera/image_raw',
            self.image_callback,
            10
        )
        self.subscription

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        
        decoded_qrcodes = pyzbar.decode(gray_image)
        if len(decoded_qrcodes) > 0:
            for decoded_qrcode in decoded_qrcodes:
                x, y, w, h = decoded_qrcode.rect
                cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                qr_code_data = decoded_qrcode.data.decode('utf-8')
                print('QR Code:', qr_code_data)

            cv2.imshow('QR Code', cv_image)
            cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    qr_code_reader = QRCodeReader()
    rclpy.spin(qr_code_reader)
    qr_code_reader.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()