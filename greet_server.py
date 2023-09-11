from concurrent import futures
import time

import grpc
import greet_pb2
import greet_pb2_grpc


class GreeterService(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return super().SayHello(request, context)

    def ParrotSaysHello(self, request, context):
        return super().ParrotSaysHello(request, context)

    def ChattyClientSaysHello(self, request_iterator, context):
        return super().ChattyClientSaysHello(request_iterator, context)

    def InteractingHello(self, request_iterator, context):
        return super().InteractingHello(request_iterator, context)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()