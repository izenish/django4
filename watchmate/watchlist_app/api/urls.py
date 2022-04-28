from django.urls import path
# from watchlist_app.api import views
from watchlist_app.api.views import movie_detail,movie_list,WatchListAV,StreamPlatformAV,ReviewList


urlpatterns = [
    path('list/',movie_list),
    path('<int:pk>',movie_detail,name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view()),
    path('watchlist/',WatchListAV.as_view()),
    path('review/',ReviewList.as_view())
    
]
