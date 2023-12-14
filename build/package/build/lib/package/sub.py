import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class ImageSubscriberNode(Node):
    def __init__(self):
        super().__init__('image_subscriber_node')
        self.subscription = self.create_subscription(
            Image,
            'webcam_image',
            self.process_image,
            10
        )
        self.bridge = CvBridge()

    def process_image(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        edges = cv2.Canny(image, 100, 200)
        if len(image.shape) == 3 and len(edges.shape) == 2:
        # Convert edges to 3 dimensions for concatenation
         edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        # Stack the images horizontally
        stacked_image = np.hstack((image, edges))
        
        # Display the stacked image
        cv2.imshow("Webcam and Canny Images", stacked_image)
        
        # Handle keyboard input
        key = cv2.waitKey(1)
        if key == 27:  # Check if the Esc key is pressed
            cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
