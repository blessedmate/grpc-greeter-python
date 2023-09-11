import greet_pb2_grpc
import greet_pb2
import time
import grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Server Side Streaming")
        print("3. ChattyClientSaysHello - Client Side Streaming")
        print("4. InteractingHello - Both Streaming")
        rpc_call = input("Which RPC would you like to call: ")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting="Bonjour", name="YouTube")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello response received:")
            print(hello_reply)

        elif rpc_call == "2":
            print("Not Implemented")

        elif rpc_call == "3":
            print("Not Implemented")

        elif rpc_call == "4":
            print("Not Implemented")


if __name__ == "__main__":
    run()
