from django.urls import path
from . import views

urlpatterns = [
    path('<int:num_page>/',views.num_page_view),
    path('<str:topic>/',views.news_view,name='topic-page'),
    #finance directly pani import gareko xu
    # path('finance_view/',views.finance_view),
]
