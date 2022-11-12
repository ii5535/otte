from rest_framework import serializers
from main.models import Comment, Home,Category

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'home', 'user','cate', 'created_at','comment')

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'name', 'images', 'Monthly_rent', 'administration_cost','room','floor','hitter','parking','Veranda','address','number','distance','option')
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')