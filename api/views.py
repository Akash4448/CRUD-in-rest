from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print('--------partial update')
        print('basename : ',self.basename)
        print('Action : ',self.action)
        print('Detail : ',self.detail)
        print('suffix : ',self.suffix)
        print('Name : ',self.name)
        print('Description : ',self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        print('--------partial update')
        print('basename : ',self.basename)
        print('Action : ',self.action)
        print('Detail : ',self.detail)
        print('suffix : ',self.suffix)
        print('Name : ',self.name)
        print('Description : ',self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data) 
           
            

    def create(self,request):
        print('--------partial update')
        print('basename : ',self.basename)
        print('Action : ',self.action)
        print('Detail : ',self.detail)
        print('suffix : ',self.suffix)
        print('Name : ',self.name)
        print('Description : ',self.description)
        serializer = StudentSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def update(self,request,pk):
        print('--------partial update')
        print('basename : ',self.basename)
        print('Action : ',self.action)
        print('Detail : ',self.detail)
        print('suffix : ',self.suffix)
        print('Name : ',self.name)
        print('Description : ',self.description)
        id = pk
        # id = request.data.get('id') 
        stu = Student.objects.get(pk=id) 
        serializer = StudentSerializer(stu,data=request.data,partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def partial_update(self,request,pk):
        print('--------partial update')
        print('basename : ',self.basename)
        print('Action : ',self.action)
        print('Detail : ',self.detail)
        print('suffix : ',self.suffix)
        print('Name : ',self.name)
        print('Description : ',self.description)
        id = pk
        # id = request.data.get('id') 
        stu = Student.objects.get(pk=id) 
        serializer = StudentSerializer(stu,data=request.data,partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data is updated'})
        return Response(serializer.errors)   

    def delete(self,request,pk): 
        id = pk
        # id = request.data.get('id')
        stu = Student.objects.get(pk=id)  
        stu.delete()
        return Response({'msg':'data is deleted'})   

                













































# from django.shortcuts import render
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import GenericAPIView 
# from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin
# # from rest_framework.mixins import CreateModelMixin

# # Create your views here.

# # List & Create no need pk----
# class LCStudentList(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)   

# #-------Retrieve , Update , Delete------------
# class RUDStudentRetrieve(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)        


#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs) 


#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)         