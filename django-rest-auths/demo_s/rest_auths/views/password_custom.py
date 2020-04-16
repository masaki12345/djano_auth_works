from rest_framework.generics import GenericAPIView
from ..serializers.password_custom import CustomPasswordResetSerializer


class PasswordResetView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomPasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Password reset e-mail has been sent.', status=200)
        return Response(serializer.errors, status=400)
