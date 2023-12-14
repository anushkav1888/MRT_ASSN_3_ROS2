import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class WebcamPublisherNode(Node):
    def __init__(self):
        super().__init__('webcam_publisher_node')
        self.publisher_ = self.create_publisher(Image, 'webcam_image', 10)
        self.bridge = CvBridge()

        self.capture = cv2.VideoCapture(0)

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.publish_image)

    def publish_image(self):
        ret, frame = self.capture.read()
        if ret:
            img_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.publisher_.publish(img_msg)

def main(args=None):
    rclpy.init(args=args)
    node = WebcamPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
