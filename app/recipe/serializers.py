"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from recipe.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']