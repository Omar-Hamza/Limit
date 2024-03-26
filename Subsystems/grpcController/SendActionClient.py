import grpc
import interfacecontroller_pb2
import interfacecontroller_pb2_grpc
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def sendAction(Action):
    try:
        print("Will try to send action to the server ...")

        with grpc.insecure_channel("localhost:50051") as channel:
            stub = interfacecontroller_pb2_grpc.webinterfaceStub(channel)
            response = stub.SendAction(interfacecontroller_pb2.actionRequest(name=Action))
            print("Greeter client received: " + response.message)
            return response.message  # Return the response message
    except Exception as e:
        print("Error sending action:", e)
        return "Error"

@app.route('/Subsystems/Interface/grpcpage/SendActionClient.py', methods=['POST'])
def call_python_function():
    try:
        data = request.get_json()
        result = sendAction('first')  # Call your Python function
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
