from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from .serializers import ServerSerializer,ChannelSerializer
from .models import Server, Channel
from rest_framework.response import Response
from .schema import server_update_docs,server_list_docs,server_detail_docs,server_create_docs,server_delete_docs
from rest_framework.exceptions import AuthenticationFailed, ValidationError


"""以下是繼承APIView的視圖"""


class ServerListAPIView(APIView):
    """列表視圖"""
    @server_list_docs
    def get(self, request):
        """查詢所有"""
        qs = Server.objects.all()
        serializer = ServerSerializer(instance=qs, many=True)
        print(serializer.data)
        response = Response(serializer.data)
        print(response.data)  # 響應對象未渲染處理的數據
        # print(response.content)  # 處理後要響應給前端的數據
        return Response(serializer.data)
    @server_create_docs
    def post(self, request):
        """新增"""
        # 獲取前端傳入的請求體數據
        data = request.data
        # 創建序列化器進行反序列化
        serializer = ServerSerializer(data=data)
        # 調用序列化器的is_validz方法進行校驗
        serializer.is_valid(raise_exception=True)
        # 調用序列化器的save方法進行執行create方法
        serializer.save()
        # 響應
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ServerDetailAPIView(APIView):
    """詳情視圖"""
    @server_detail_docs
    def get(self, request, pk):
        # 查詢pk指定的模型對象
        try:
            server = Server.objects.get(id=pk)
        except Server.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 創建序列化器進行序列化
        serializer = ServerSerializer(instance=server)
        # 查询与此服务器相关的频道数据
        channels = Channel.objects.filter(server=server)
        channel_serializer = ChannelSerializer(instance=channels, many=True)
        # 将频道数据添加到响应数据中
        data = serializer.data
        data['channels_server'] = channel_serializer.data
         # 添加num_members字段
        data['num_members'] = server.member.count()
        # 響應
        return Response(data)

    @server_update_docs
    def put(self, request, pk):
        # 查詢pk所指定的模型對象

        try:
            server = Server.objects.get(id=pk)
        except Server.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 獲取前端傳入的請求體數據
        # 創建序列化器進行反序列化
        serializer = ServerSerializer(instance=server, data=request.data)
        print(request.data)
        # 校驗
        serializer.is_valid(raise_exception=True)
        # save--->update
        serializer.save()
        # 響應
        return Response(serializer.data)
    @server_delete_docs
    def delete(self, request, pk):
        # 查詢pk所指定的模型對象
        try:
            server = Server.objects.get(id=pk)
        except Server.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # member.delete()# 物理刪除(真正從數據庫刪除)
        # 刪除模型對象
        server.is_activate = False
        server.save()  # (邏輯刪除)
        # 響應: 刪除時不需要有響應體但是要指定狀態碼為 204
        return Response(status=status.HTTP_204_NO_CONTENT)
