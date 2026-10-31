import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenPublisher(Node):
    def __init__(self):
        super().__init__('even_publisher')
        self.publisher = self.create_publisher(Int32, 'even_numbers', 10)
        self.number = 2

        self.timer = self.create_timer(1.0, self.publish_number)

    def publish_number(self):
        msg= Int32()
        msg.data = self.number
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing Even Numbers: {self.number}')
        self.number +=2

def main(args=None):
        rclpy.init(args=args)
        node = EvenPublisher()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
        main()
