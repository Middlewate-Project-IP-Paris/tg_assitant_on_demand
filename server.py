import grpc
import assistant_on_demand_pb2
import assistant_on_demand_pb2_grpc
import bot_connection

class AssistanceOnDemandServicer(assistant_on_demand_pb2_grpc.assistanceOnDemandServicer):
    def getChannelMeta(self, request, context):
        pass
