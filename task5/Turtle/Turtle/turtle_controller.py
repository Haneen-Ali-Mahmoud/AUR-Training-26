import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.pose_sub = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        
        self.timer = self.create_timer(0.5, self.publish_velocity)

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f'Turtle Pose -> X: {msg.x:.2f}, Y: {msg.y:.2f}, Theta: {msg.theta:.2f}')

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 2.0   
        msg.angular.z = 1.0  
        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()