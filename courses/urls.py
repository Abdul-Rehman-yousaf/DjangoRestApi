from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
        url(r'^$', views.ListCreateCourse.as_view(), name='course_list'),
        url(r'(?P<pk>\d+)/$',
            views.RetrieveUpdateDestroyCourse.as_view(),
            name='course_detail'),
        url(r'^(?P<course_pk>\d+)/reviews/$',
            views.ListCreateReview.as_view(),
            name='review_list'),
        url(r'^(?P<course_pk>\d+)/reviews/(?P<pk>\d+)/$',
            views.RetrieveUpdateDestroyReview,
            name='review_detail'),
        url(r'^home', TemplateView.as_view(template_name='courses/courses.html'), name='courses')
]
