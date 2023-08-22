from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView

class Create_Api(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body) 
        print(type(data))
        value1 = data.get('value1')
        value2 = data.get('value2')
        value3= data.get('value3')
        print(1111111111111111111)
        print(data)
        print(value1, value2,value3)
        table_name = 'creation'
        column1_name = 'name'
        column2_name = 'rollnum'
        column3_name = 'student_id'
        
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO {table_name} ({column1_name}, {column2_name},{column3_name}) VALUES (%s, %s)", [value1, value2])
        return JsonResponse({'message': 'Item created successfully.'})

# class Get_data(APIView):
#     def get(self,request,id):
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM creation WHERE id = %s", [id])
#             row = cursor.fetchone()
#             if row:
#                 # Process the row data and create a dictionary
#                 item = {
#                     'id': row[0],
#                     'column1': row[1],
#                     'column2': row[2],
#                     # ...
#                 }
#                 return JsonResponse(item)
#             else:
#                 return JsonResponse({'message': 'Item not found.'}, status=404)
class Get_data(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM creation")
            rows = cursor.fetchall()
            
            names = [row[0] for row in rows]  # Extract the names from the fetched rows
            
            return JsonResponse({'names': names})
 
class Update_data(APIView):
    def post(self,request, id):
        if request.method == 'POST':
            data = request.data  # Use request.data for JSON data
            print(type(data),1111111111111111111)
            value1 = data.get('value1')
            value2 = data.get('value2')
            with connection.cursor() as cursor:
                cursor.execute("UPDATE creation SET name = %s, rollnum = %s WHERE id = %s", [value1,value2 ,id])
            return JsonResponse({'message': 'Item updated successfully.'})

        
class  Delete_data(APIView):
    def delete(self,request,id):
        if request.method == 'DELETE':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM creation WHERE id = %s", [id])
            return JsonResponse({'message': 'Item deleted successfully.'})
