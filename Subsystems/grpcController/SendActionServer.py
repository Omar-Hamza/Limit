from concurrent import futures

import logging

import grpc
import time
import interfacecontroller_pb2
import interfacecontroller_pb2_grpc


class webinterface(interfacecontroller_pb2_grpc.webinterfaceServicer):
    def SendAction(self, request, context):
        return interfacecontroller_pb2.actionReply(message="Action, %s!" % request.name)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    interfacecontroller_pb2_grpc.add_webinterfaceServicer_to_server(webinterface(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()



if __name__ == "__main__":
    logging.basicConfig()
    serve()
