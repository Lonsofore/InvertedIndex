import grpc

from invertedindexproto import invertedindex_pb2
from invertedindexproto import invertedindex_pb2_grpc
 
 
class Client(object):
    """
    Client for accessing the gRPC functionality
    """
 
    def __init__(self, host, port):
        # host and the the port to which the client should connect to
        self.host = host
        self.server_port = port
 
        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port)
        )
 
        # bind the client to the server channel
        self.stub = invertedindex_pb2_grpc.InvertedIndexStub(self.channel)
        
    def add(self, text):
        request = invertedindex_pb2.Text(text=text)
        result = self.stub.add(request)
        return result.id
        
    def search(self, text):
        request = invertedindex_pb2.Text(text=text)
        result = self.stub.search(request)
        return result.id
        
    def delete(self, id):
        request = invertedindex_pb2.Id(id=id)
        result = self.stub.delete(request)
        return result.status
