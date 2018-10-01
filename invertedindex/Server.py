import grpc
import os
from concurrent import futures

from invertedindex import CONFIG_NAME
from .utility import get_config
from .Index import Index
from . import invertedindex_pb2
from . import invertedindex_pb2_grpc


CONFIG = get_config(CONFIG_NAME)
DB_WORDS_TO_DOCS = os.path.join(CONFIG['db']['path'], CONFIG['db']['words_to_docs'])
DB_DOCS_TO_WORDS = os.path.join(CONFIG['db']['path'], CONFIG['db']['docs_to_words'])


# create a class to define the server functions, derived from
# invertedindex_pb2_grpc.InvertedIndexServicer
class InvertedIndexServicer(invertedindex_pb2_grpc.InvertedIndexServicer):

    def __init__(self):
        self.index = Index(DB_WORDS_TO_DOCS, DB_DOCS_TO_WORDS)
                
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

    def __init__(self, port, max_workers=10):
        self.port = port
        self.max_workers = max_workers
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.max_workers))
        invertedindex_pb2_grpc.add_InvertedIndexServicer_to_server(
            InvertedIndexServicer(), self.server
        )
        self.server.add_insecure_port('[::]:{}'.format(self.port))
        
    def set_port(self, port):
        self.port = port
        self.server.add_insecure_port('[::]:{}'.format(self.port))
        
    def start(self):
        self.server.start()
        
    def stop(self):
        self.server.stop(0)
