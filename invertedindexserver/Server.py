import grpc
import os
from concurrent import futures

from invertedindexproto import invertedindex_pb2
from invertedindexproto import invertedindex_pb2_grpc

from .Index import Index


# create a class to define the server functions, derived from
# invertedindex_pb2_grpc.InvertedIndexServicer
class InvertedIndexServicer(invertedindex_pb2_grpc.InvertedIndexServicer):

    def __init__(self, words_to_docs_path, docs_to_words_path):
        self.index = Index(words_to_docs_path, docs_to_words_path)
                
    def add(self, request, context):
        response = invertedindex_pb2.Id()
        response.id = self.index.add(request.text)
        return response
        
    def search(self, request, context):
        response = invertedindex_pb2.IdArray()
        result = self.index.search(request.text)
        response.id[:] = result
        return response
        
    def delete(self, request, context):
        response = invertedindex_pb2.Status()
        response.status = self.index.delete(request.id)
        return response

        
class Server:

    def __init__(self, port, max_workers, words_to_docs_path, docs_to_words_path):
        self.port = port
        self.max_workers = max_workers
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.max_workers))
        invertedindex_pb2_grpc.add_InvertedIndexServicer_to_server(
            InvertedIndexServicer(words_to_docs_path, docs_to_words_path), self.server
        )
        self.server.add_insecure_port('[::]:{}'.format(self.port))
        
    def set_port(self, port):
        self.port = port
        self.server.add_insecure_port('[::]:{}'.format(self.port))
        
    def start(self):
        self.server.start()
        
    def stop(self):
        self.server.stop(0)
