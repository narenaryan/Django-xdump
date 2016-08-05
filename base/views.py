from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.shortcuts import render
from io import BytesIO
import xlsxwriter
# Create your views here.

class Home(View):
    template_name = "home.html"
    def get(self, request):
        return render(request,self.template_name,{})

class Userdump(View):
    def get(self, request):
        output = BytesIO()
        # Feed a buffer to workbook
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet("users")
        users = get_user_model().objects.all()
        bold = workbook.add_format({'bold': True})
        columns = ["user", "name", "email", "date_joined"]
        # Fill first row with columns
        row = 0
        for i,elem in enumerate(columns):
            worksheet.write(row, i, elem, bold)
        row += 1
        # Now fill other rows with columns
        for user in users:
            worksheet.write(row, 0, user.id)
            worksheet.write(row, 1, user.username)
            worksheet.write(row, 2, user.email)
            worksheet.write(row, 3, user.date_joined.ctime())
            row += 1
        # Close workbook for building file
        workbook.close()
        output.seek(0)
        response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        return response
