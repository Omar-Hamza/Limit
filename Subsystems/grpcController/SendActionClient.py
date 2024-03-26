import logging

import grpc
import time
import interfacecontroller_pb2
import interfacecontroller_pb2_grpc

Acc = 25
Action = "Forward" + str (Acc)
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to send action to the server ...")

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = interfacecontroller_pb2_grpc.webinterfaceStub(channel)
        response = stub.SendAction(interfacecontroller_pb2.actionRequest(name=Action))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    
    while True:
        logging.basicConfig()
        run()
        time.sleep(1)
