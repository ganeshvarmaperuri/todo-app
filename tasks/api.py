from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)


class TaskList(APIView):
    def get(self, request):
        model = task.objects.all()
        serializer = taskserializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskUpdate(APIView):
    def get_task_id(self, pk):
        try:
            model = task.objects.get(id=pk)
            return model
        except task.DoesNotExist:
            return


    def get(self, request, pk):
        if not self.get_task_id(pk):
            return Response(f'task with {pk} is not found in Database', status=status.HTTP_404_NOT_FOUND)
        serializer = taskserializer(self.get_task_id(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        if not self.get_task_id(pk):
            return Response(f'task with {pk} is not found in Database', status=status.HTTP_404_NOT_FOUND)
        serializer = taskserializer(self.get_task_id(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not self.get_task_id(pk):
            return Response(f'task with {pk} is not found in Database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_task_id(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)