from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import VeritySource, VeritySourceLogin, VerityLastSyncTime
from ipam.api.serializers import PrefixSerializer


class NestedVeritySourceSerializer(WritableNestedSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='plugins-api:netbox_access_lists-api:veritysource-detail'
    # )

    class Meta:
        model = VeritySource
        fields = ('id', 'url', 'display', 'verity_url')

class NestedVeritySourceLoginSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_access_lists-api:veritysourcelogin-detail'
    )

    class Meta:
        model = VeritySourceLogin
        fields = ('id', 'url', 'display', 'username')

class NestedVerityLastSyncTimeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_access_lists-api:veritylastsynctime-detail'
    )

    class Meta:
        model = VerityLastSyncTime
        fields = ('id', 'url', 'display', 'timestamp')


class VeritySourceSerializer(NetBoxModelSerializer):

    # url = serializers.HyperlinkedIdentityField(
    #     view_name='plugins-api:verity_import-api:veritysource-detail'
    # )

    class Meta:
        model = VeritySource
        fields = (
            'id', 'display', 'url', 'verity_url', 'tags', 'custom_fields', 'created',
            'last_updated',
        )


class VeritySourceLoginSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:verity_import-api:veritysourcelogin-detail'
    )
    verity_source = NestedVeritySourceSerializer()

    class Meta:
        model = VeritySourceLogin
        fields = (
            'id', 'url', 'display', 'verity_source', 'username', 'password', 'tags', 'custom_fields', 'created',
            'last_updated',
        )


class VerityLastSyncTimeSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:verity_import-api:veritylastsynctime-detail'
    )
    verity_source = NestedVeritySourceSerializer()

    class Meta:
        model = VerityLastSyncTime
        fields = (
            'id', 'url', 'display', 'verity_source', 'timestamp', 'tags', 'custom_fields', 'created',
            'last_updated',
        )
