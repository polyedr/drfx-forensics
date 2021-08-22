from django.urls import path, include

from forensics.views import ForensicsDataList, ForensicsDataDetail

app_name = "forensics"

forensics_patterns = [
    path("forensics/", ForensicsDataList.as_view(), name="forensics_list",),
    path(
        "forensics/<int:pk>/", ForensicsDataDetail.as_view(), name="forensics_detail",
    ),
]


urlpatterns = [
    path("", include(forensics_patterns)),
]
