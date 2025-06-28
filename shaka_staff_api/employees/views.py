from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Manager, Intern

class StaffRolesView(APIView):
    def get(self, request):
        data = []
        for staff in list(Manager.objects.all()) + list(Intern.objects.all()):
            data.append({
                "name": staff.name,
                "email": staff.email,
                "role": staff.get_role()
            })
        return Response(data)
