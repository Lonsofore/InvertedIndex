# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import invertedindex_pb2 as invertedindex__pb2


class InvertedIndexStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.add = channel.unary_unary(
        '/invertedindex.InvertedIndex/add',
        request_serializer=invertedindex__pb2.Text.SerializeToString,
        response_deserializer=invertedindex__pb2.Id.FromString,
        )
    self.search = channel.unary_unary(
        '/invertedindex.InvertedIndex/search',
        request_serializer=invertedindex__pb2.Text.SerializeToString,
        response_deserializer=invertedindex__pb2.IdArray.FromString,
        )
    self.delete = channel.unary_unary(
        '/invertedindex.InvertedIndex/delete',
        request_serializer=invertedindex__pb2.Id.SerializeToString,
        response_deserializer=invertedindex__pb2.Status.FromString,
        )


class InvertedIndexServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def add(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def search(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InvertedIndexServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'add': grpc.unary_unary_rpc_method_handler(
          servicer.add,
          request_deserializer=invertedindex__pb2.Text.FromString,
          response_serializer=invertedindex__pb2.Id.SerializeToString,
      ),
      'search': grpc.unary_unary_rpc_method_handler(
          servicer.search,
          request_deserializer=invertedindex__pb2.Text.FromString,
          response_serializer=invertedindex__pb2.IdArray.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=invertedindex__pb2.Id.FromString,
          response_serializer=invertedindex__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'invertedindex.InvertedIndex', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
