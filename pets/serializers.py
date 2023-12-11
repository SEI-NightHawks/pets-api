from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pet, Post, Following, Comment, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super(PetSerializer, self).create(validated_data)

# class PostSerializer(serializers.ModelSerializer):
#     pet = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all())

#     class Meta:
#         model = Post
#         fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    pet = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all())

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        pet_data = PetSerializer(instance.pet).data  # Assuming you have a PetSerializer defined
        representation['pet'] = pet_data
        return representation

    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    pet = PetSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
