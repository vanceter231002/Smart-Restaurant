from django.urls import path
from . import views

app_name='smart_restaurant'
urlpatterns=[ 
    path('<int:table_no>',views.index,name="index"),
    path('menu/',views.menu,name="menu"),
    path('order/',views.order_details,name="order"),
    path('thanks/',views.thanks,name="thanks"),
    path('',views.redirection,name="redirection")
    #path('<int:pk>/results/',views.ResultsView.as_view(),name="results"),
    #path('<int:question_id>/vote/',views.vote,name="vote")
]