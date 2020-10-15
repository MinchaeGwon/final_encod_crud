from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .serializers import PostSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def post_list(request):
    if request.method == 'GET':
        query_set = Post.objects.all()
        serializer = PostSerializer(query_set, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def post_detail(request, pk):

    post = Post.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if post.owner == request.user.username:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        else:
            print("error")
            return Response(status=400)


    elif request.method == 'DELETE':
        if post.owner == request.user.username:
            post.delete()
            return Response(status=204)
        else:
            print("error")
            return Response(status=400)


# from django.http import HttpResponse, JsonResponse
# from .models import Post
# from .serializers import PostSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.decorators import permission_classes, authentication_classes

# @csrf_exempt
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication, SessionAuthentication))
# def post_list(request):
#     if request.method == 'GET':
#         query_set = Post.objects.all()
#         serializer = PostSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication, SessionAuthentication))
# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)

#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'PUT':
#         if post.owner == request.user.username:
#             data = JSONParser().parse(request)
#             serializer = PostSerializer(post, data=data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=201)
#             return JsonResponse(serializer.errors, status=400)
#         else:
#             print("Error!!")
#             return HttpResponse(status=400)

#     elif request.method == 'DELETE':
#         if post.owner == request.user.username:
#             post.delete()
#             return HttpResponse(status=204)
#         else:
#             print("Error!!")
#             return HttpResponse(status=400)


# from rest_framework.viewsets import ModelViewSet
# from .models import Post
# from .serializers import PostSerializer
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.permissions import IsAuthenticated

# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [IsAuthenticated]

