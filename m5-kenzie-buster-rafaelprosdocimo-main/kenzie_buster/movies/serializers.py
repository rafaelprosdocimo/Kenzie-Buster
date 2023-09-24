from rest_framework import serializers
from .models import Movie, MovieClassificationChoices
from movies.models import Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, allow_null=True, allow_blank=True, required=False
    )
    rating = serializers.ChoiceField(
        choices=MovieClassificationChoices.choices,
        default=MovieClassificationChoices.G,
        required=False,
    )
    synopsis = serializers.CharField(allow_blank=True, allow_null=True, default=None)
    added_by = serializers.SerializerMethodField(method_name="get_added_by")

    def get_added_by(self, obj: Movie) -> str:
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    buyed_by = serializers.SerializerMethodField()

    def get_buyed_by(self, obj: MovieOrder) -> str:
        return obj.buyed_by.email

    def create(self, validated_data) -> MovieOrder:
        print(validated_data)
        return MovieOrder.objects.create(**validated_data)
