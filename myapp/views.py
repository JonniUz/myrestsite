from rest_framework import viewsets
from myapp.models import Member
from myapp.serializers import MemberSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

#
# class MemberPagination(PageNumberPagination):
#     page_size = 2


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = LimitOffsetPagination


"""

FOURTH lesson

"""

"""
from rest_framework import generics
from .models import Member
from .serializers import MemberSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
"""

"""

Third Lesson

"""

"""
from rest_framework import mixins, generics
from myapp.serializers import MemberSerializer
from myapp.models import Member


class MemberList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class MemberDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

"""

"""

SECOND LESSON

"""

'''

from .models import Member
from .serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class MemberList(APIView):

    def get(self, request):
        students = Member.objects.all()
        serializer = MemberSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetail(APIView):

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        member = self.get_object(pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk):
        member = self.get_object(pk=pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        member = self.get_object(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

"""

FIRST LESSON
 
"""
# from .models import Member
# from .serializers import MemberSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
#
#
# @api_view(['GET', 'POST'])
# def member_list(request):
#     if request.method == "GET":
#         members = Member.objects.all()
#         serializer = MemberSerializer(members, many=True)
#         return Response(serializer.data)
#
#     if request.method == "POST":
#         serializer = MemberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def member_detail(request, pk):
#     try:
#         member = Member.objects.get(pk=pk)
#     except Member.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = MemberSerializer(member)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = MemberSerializer(member, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         member.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# #
