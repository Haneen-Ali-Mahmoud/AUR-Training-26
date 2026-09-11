import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


class Turtle_client(Node):

    def __init__(self):
        super().__init__('Tutle_client')

        self.client = self.create_client(SetBool,'start_movement')
        self.service_called = False
        self.timer = self.create_timer(3.0,self.call_service)
        self.get_logger().info('Service client started.')
        self.get_logger().info('Waiting 3 seconds before starting movement')

    def call_service(self):
        if self.service_called:
            return

        if not self.client.wait_for_service(timeout_sec=0.1):
            self.get_logger().info('Waiting for start_movement service' )
            return

        request = SetBool.Request()
        request.data = True
        future = self.client.call_async(request)
        future.add_done_callback(self.service_response)
        self.service_called = True
        self.get_logger().info('Sending START request')

    def service_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Service response: '
                f'success={response.success}, '
                f'message={response.message}')

        except Exception as e:

            self.get_logger().error(f'Service call failed: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = Turtle_client()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()