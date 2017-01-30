from django.conf.urls import url, include
from django.contrib import admin
from app import views as app_view
from rest_framework import routers
from chatbot_api import views as api_view
from rest_framework.authtoken import views as rest_framework_views
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', api_view.UserViewSet)
router.register(r'groups', api_view.GroupViewSet)
router.register(r'qacorpus', api_view.QAViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', app_view.index_view, name='index_view'),
    url(r'^chat/$', app_view.chat_view, name='chat_view'),
    url(r'^train/$', app_view.train_view, name='train_view'),
    url(r'^api/chatterbot/', api_view.ChatterBotView.as_view(), name="chatbot"),
    url(r'^api/trainerbot/', api_view.FeedBackTrainView.as_view(), name="feedlearn"),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot')),
]
