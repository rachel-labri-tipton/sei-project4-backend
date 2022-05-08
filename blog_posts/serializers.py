from rest_framework import serializers
from blog_categories.models import Category
from blog_posts.models import BlogPost
from users.models import CommunityUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ("first_name", "last_name", "id",)


class BlogPostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = BlogPost
        fields = '__all__'

    def create(self, data):
        author_data = data.pop("author")
        category_data = data.pop("categories")
        # blogpost = BlogPost(**data)
        blogpost = BlogPost(
            title=data['title'],
            excerpt=data['excerpt'],
            content=data['content'],
            status=data['status'],
        )

        if author_data:
            author = CommunityUser.objects.get(
                first_name=author_data["first_name"]
            )
            blogpost.author = author

        request = self.context.get("request")
        if request and hasattr(request, "user"):
            blogpost.author = request.user

        blogpost.save()

        if category_data:
            for name in category_data:
                newCategory, _created = Category.objects.get_or_create(**name)
                blogpost.categories.add(newCategory)

        return blogpost

    def update(self, blogpost, data):
        author_data = data.pop("author")
        category_data = data.pop("categories")

        blogpost.title = data.get("title", blogpost.title)
        blogpost.excerpt = data.get("excerpt", blogpost.excerpt)
        blogpost.content = data.get(
            "content", blogpost.content)
        blogpost.status = data.get("status", blogpost.status)

        if author_data:
            author, _created = CommunityUser.objects.get(
                first_name=author_data["first_name"])
            blogpost.author = author

        if category_data:
            for name in category_data:
                newCategory, _created = Category.objects.get_or_create(
                    **name)
            blogpost.locations.add(newCategory)

        # save to the database
        # blogpost.save()

        # render to the api
        return blogpost
