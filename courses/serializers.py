from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'
        )
        model = models.Review

    def validate_rating(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError(
            'Rating must an integer between 1 and 5')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        reviews = serializers.PrimaryKeyRelatedField(
                    many=True,
                    read_only=True,
        )
        fields = (
            'id',
            'title',
            'url',
            'reviews',
        )
        model = models.Course
