import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import VeritySource, VeritySourceLogin, VerityLastSyncTime


class VeritySourceTable(NetBoxTable):

    class Meta(NetBoxTable.Meta):
        model = VeritySource
        fields = ('pk', 'verity_url', 'actions')
        default_columns = ('verity_url')


class VeritySourceLoginTable(NetBoxTable):

    verity_source = tables.Column(
        linkify=True
    )

    def render_password(self, value):
        return "********"  # Always return a masked value

    class Meta(NetBoxTable.Meta):
        model = VeritySourceLogin
        fields = ('pk', 'verity_source', 'username', 'password', 'actions')
        default_columns = ('pk', 'verity_source', 'username', 'password')


class VerityLastSyncTimeTable(NetBoxTable):

    verity_source = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = VerityLastSyncTime
        fields = ('pk', 'verity_source', 'timestamp')
        default_columns = ('pk', 'verity_source', 'timestamp')
        exclude = ('actions',)
