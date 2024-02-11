"""
Tests for models.
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from .. import models


class ModelTests(TestCase):
    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        recipe = models.Recipe.objects.create(
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample receipe description.',
        )

        self.assertEqual(str(recipe), recipe.title)