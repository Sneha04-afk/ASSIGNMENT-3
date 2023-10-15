from django.urls import path
from recipes import views
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, UserRecipeListView, RecipeSearchView

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('search/', RecipeSearchView.as_view(), name='recipe_search'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<str:username>/', UserRecipeListView.as_view(), name='user_recipes'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('about/', views.about, name='about'),
]