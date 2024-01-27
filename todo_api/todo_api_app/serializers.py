from datetime import datetime
from rest_framework import serializers


class DeedSerializer(serializers.Serializer):
    _id = serializers.CharField(max_length=36, default=1)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=2047, allow_null=True)
    hashtags = serializers.JSONField(default=[])
    user = serializers.CharField(default="todo_front")
    is_done = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(default=datetime.now())

