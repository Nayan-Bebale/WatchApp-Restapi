from restWatch_app.models import WatchList, StreamPlatform
from rest_framework import serializers

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        exclude = ["created",]

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"  # This will include all fields in the model
