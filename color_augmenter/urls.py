from django.urls import path, include
# from rest_framework import routers

from color_augmenter.views import IllustrationSetList, IllustrationSetDetail

app_name = "color_augmenter"

color_augmenter_patterns = [
    path(
        "illustrations/",
        IllustrationSetList.as_view(),
        name="api_illustration_set_list",
    ),
    path(
        "illustrations/<int:pk>/",
        IllustrationSetDetail.as_view(),
        name="api_illustration_set_list_detail",
    ),
]


urlpatterns = [
    path("", include(color_augmenter_patterns)),
]
