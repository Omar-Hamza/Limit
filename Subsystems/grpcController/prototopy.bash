echo "Please enter directory path and don't use \ use only /: "
read DIR

python -m grpc_tools.protoc \
  -I${DIR} \
  --python_out=${DIR} \
  --pyi_out=${DIR} \
  --grpc_python_out=${DIR} \
  ${DIR}\interfacecontroller.proto