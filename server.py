import grpc
import assistant_on_demand_pb2
import assistant_on_demand_pb2_grpc
from bot_connection import BotConnection
from concurrent import futures


class AssistanceOnDemandServicer(assistant_on_demand_pb2_grpc.assistanceOnDemandServicer):
    def __init__(self):
        pass

    def getChannelMeta(self, request, context):
        b = BotConnection()
        print('getChannelMeta invoked \n')
        b.getchannelmeta(request.channel_id)
        return assistant_on_demand_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()

    def getPost(self, request, context):
        b = BotConnection()
        print('getPost invoked \n')
        b.getpost(request.channel_id, request.post_id)
        return assistant_on_demand_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()

    def getChannelSubs(self, request, context):
        b = BotConnection()
        print('getChannelSubs invoked \n')
        b.getchatmembers(request.channel_id)
        return assistant_on_demand_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()

    def getPostStat(self, request, context):
        b = BotConnection()
        print('getPostStat invoked \n')
        b.getpost(request.channel_id, request.post_id)
        return assistant_on_demand_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()

    def joinChannel(self, request, context):
        b = BotConnection()
        print('joinChannel invoked \n')
        b.joinchannel(request.invite_link)
        return assistant_on_demand_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    assistant_on_demand_pb2_grpc.add_assistanceOnDemandServicer_to_server(
        AssistanceOnDemandServicer(), server
    )
    server.add_insecure_port("[::]:50054")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
