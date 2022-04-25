# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
# # Create your views here.


# def movie_list(request):
#     movies=Movie.objects.all()
#     # print(movies.values())
#     data={'movie':list(movies.values())}

#     'Querys set lai python dictionary ma convert garera last ma Json form ma return gareko'
#     return JsonResponse(data)