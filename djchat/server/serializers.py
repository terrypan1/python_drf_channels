from django.conf import settings
from rest_framework import serializers
from .models import Server, Category,Channel
from django.contrib.auth import get_user_model

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"

class ServerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # 添加这行来显示 id 字段
    name = serializers.CharField(max_length=100)
    owner = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    # 確保已經從相應模塊導入了 Category
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    description = serializers.CharField(max_length=250, allow_blank=True, required=False)
    member = serializers.PrimaryKeyRelatedField(many=True, queryset=get_user_model().objects.all(), required=False)
    # num_members = serializers.SerializerMethodField()
    def create(self, validated_data):
        members_data = validated_data.pop('member', [])  # 使用預設空列表以避免KeyError
        server = Server.objects.create(**validated_data)
        server.member.set(members_data)
        return server

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)

        # 假设仅当提供了新的成员信息时才更新描述
        if 'member' in validated_data:
            members_data = validated_data.pop('member')
            instance.member.set(members_data)
        
        # 假设我们根据成员的更新来决定是否更新描述
        # 注意：这里需要根据您的实际业务逻辑进行调整
            if 'description' in validated_data:
                instance.description = validated_data.get('description')
        instance.save()
        return instance
    
    def get_num_members(self, obj):
        # 获取成员数量
        return obj.member.count()
    




