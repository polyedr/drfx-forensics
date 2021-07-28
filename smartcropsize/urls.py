from django.urls import path, include
from smartcropsize.views import SmartcropImageList, SmartcropImageDetail

app_name = "smartcrop"

smartcrop_patterns = [
    path(
        "smartcrops/",
        SmartcropImageList.as_view(),
        name="api_smartcrop_list",
    ),
    path(
        "smartcrops/<int:pk>/",
        SmartcropImageDetail.as_view(),
        name="api_smartcrop_detail",
    ),
]


urlpatterns = [
    path("", include(smartcrop_patterns)),
]
