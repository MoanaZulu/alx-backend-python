#!/usr/bin/env python3
"""
Main project URLs
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("messaging_app.chats.urls")),
    path("api-auth/", include("rest_framework.urls")),  # <-- add this line
]

