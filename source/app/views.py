"""
This file contains the base app API functions
-------------------------------------------------------------------------------
"""

from django.shortcuts import render, redirect
from .models.organizations import Organization, OrganizationType
from .models.projects import Project
from .models import DataFile
from rest_framework import status
from rest_framework.response import Response
from .serializers import FileSerializer






def home_page(request):
    return render(request, "index.html")


def organization_list(request):
    context = {}
    organization_all = Organization.objects.all()
    context["organization_list"] = organization_all
    return render(request, "organizations.html", context)


def project_list(request):
    context = {}
    project_all = Project.objects.all()
    context["project_list"] = project_all
    return render(request, "projects.html", context)


def data_files(request):
    """
    Call this function List all uploaded data files.
    Post to upload the file to the endpoint.
    """
    if request.method == "GET":
        if request.user.groups.filter(name="Researcher").exists():
            files = DataFile.objects.all()
            serializer = FileSerializer(files, many=True)

            if "text/html" in request.META.get("HTTP_ACCEPT", ""):
                return render(request, "data_files.html", {"files": serializer.data})

            return Response(serializer.data)
        else:
            return Response(
                "You are not authorized to use this API",
                status=status.HTTP_401_UNAUTHORIZED,
            )

    elif request.method == "POST":
        if request.user.groups.filter(name="Researcher").exists():
            file_serializer = FileSerializer(data=request.FILES)

            if file_serializer.is_valid():
                file_serializer.save()

                if "text/html" in request.META.get("HTTP_ACCEPT", ""):
                    return redirect("data_files")

                return Response(file_serializer.data, status=status.HTTP_201_CREATED)

            else:
                if "text/html" in request.META.get("HTTP_ACCEPT", ""):
                    files = DataFile.objects.all()
                    return render(
                        request,
                        "data_files.html",
                        {"files": files, "error": file_serializer.errors},
                    )

                return Response(
                    file_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                "You are not authorized to use this API",
                status=status.HTTP_401_UNAUTHORIZED,
            )
