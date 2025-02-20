from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from .models import Author, Category, Post


class AuthorSerializer(serializers.ModelSerializer):

    # license = serializers.HyperlinkedIdentityField(view_name='license-detail')
    """показывает ссылку на объект. показывает ссылку на объект с тем же id что и у объекта связанного с ним моделя"""

    posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='post-detail')
    """показывает выбранное поле объекта, но так как связь OneToOneField и у одного объекта этого моделя не может быть
       несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    user = serializers.StringRelatedField(read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
    моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = Author
        fields = ('id', 'user', 'profile_picture', 'posts')


class CategorySerializer(serializers.ModelSerializer):

    # driver = serializers.HyperlinkedIdentityField(view_name='driver-detail')
    """показывает ссылку на объект. показывает ссылку на объект с тем же id что и у объекта связанного с ним моделя"""
    """Не обязательно чтобы переменная была связывающей переменной между моделями, нужно лишь название самого моделя"""

    posts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    """показывает выбранное поле объекта, но так как связь OneToOneField и у одного объекта этого моделя не может быть
       несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    # driver = serializers.StringRelatedField(read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
    моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = Category
        fields = ('id', 'title', 'subtitle', 'slug', 'thumbnail', 'posts')



class PostSerializer(serializers.ModelSerializer):

    # books = serializers.HyperlinkedIdentityField(view_name='book-detail')
    """можно использовать, но работать будет некорректно, так как HyperlinkedIdentityField предназначен для связи
       моделей OneToOneField. покажет ссылку объекта с тем же id что и у объекта связанного с ним моделя, даже если
       такого объекта не существует он все ровно покажет ссылку"""

    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    """показывает выбранное поле объекта"""

    author = serializers.HyperlinkedRelatedField(read_only=True, view_name='author-detail')
    """показывает ссылки на все объекты"""

    # books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """показывает id объектов"""

    # books = serializers.StringRelatedField(many=True, read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
       моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'overview', 'author', 'timestamp', 'content', 'categories', 'featured')
