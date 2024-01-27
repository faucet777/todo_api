from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .utils import collection_todo
from .serializers import DeedSerializer
from bson import ObjectId


class DeedAPIView(APIView):
    def get(self, request:Request):
        deeds = list(collection_todo.find({}))
        return Response({'posts': DeedSerializer(deeds, many=True).data})

    def post(self, request: Request):
        new_deed = collection_todo.insert_one(request.data)
        posted = collection_todo.find_one({'_id': new_deed.inserted_id})
        return Response({'posts': DeedSerializer(posted).data})

    def delete(self, request: Request):
        del_id = ObjectId(request.data["_id"])
        del_deed = collection_todo.delete_one({"_id": del_id})
        return Response({'posts': del_deed.raw_result})

    def put(self, request: Request):
        upd_id = ObjectId(request.data["_id"])
        print('put data>>>>>>>>>>', request.data)
        upd = request.data
        del upd["_id"]
        upd_deed = collection_todo.update_one({"_id": upd_id},
                                              {"$set": upd})
        return Response({'posts': upd_deed.raw_result})
