from django.urls import path, include

urlpatterns = [
    path('api/recipe/', include('recipe.urls')),
]