from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes
# from drf_spectacular import OpenApiParameter, OpenApiResponse
from .serializers import ServerSerializer

server_update_docs = extend_schema(
    request=ServerSerializer,
    responses={200: ServerSerializer}
)

server_list_docs = extend_schema(
    responses={200: ServerSerializer(many=True)},
)

server_detail_docs = extend_schema(
    responses={200: ServerSerializer},
)

server_create_docs = extend_schema(
    request=ServerSerializer,
    responses={201: ServerSerializer}
)

server_delete_docs = extend_schema(
    responses={204: "No Content"}
)
