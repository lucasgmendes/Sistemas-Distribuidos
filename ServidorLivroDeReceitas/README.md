# Hash table - TCP & gRPC #

Para rodar utilize `python3+`, primeiro instale as dependências com

    $ pip install -r requirements.txt

Use o seguinte comando para gerar o código Python:

    $ python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./service.proto
    
Por fim, caso queira rodar com a implementação **tcp** execute

    $ python server.py tcp
    $ python client.py tcp

Caso opte pela implementação **gRPC** execute

    $ python server.py grpc
    $ python client.py grpc
