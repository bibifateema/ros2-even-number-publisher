import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random


class RandomPublisher(Node):

    def __init__(self):
        super().__init__('random_publisher')
        self.publisher = self.create_publisher(Int32, 'random_number',10)

        self.timer= self.create_timer(1.0, self.publish_random)
        
    def publish_random(self):
        msg = Int32()

        msg.data =  random.randint(1, 100)

        self.publisher.publish(msg)
        self.get_logger().info(f'Random Number: {msg.data}')

def main(args = None):
    rclpy.init(args=args)
    node = RandomPublisher()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

