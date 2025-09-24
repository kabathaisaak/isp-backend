from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .service import get_api, add_pppoe_user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def status(request):
    return Response({'status': 'ok', 'message': 'MikroTik integration ready'})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user(request):
    data = request.data
    host = data.get('host')
    username = data.get('username')
    password = data.get('password')
    user = data.get('user')
    passwd = data.get('pass')
    api = get_api(host, username, password)
    add_pppoe_user(api, user, passwd)
    return Response({'added': user})
