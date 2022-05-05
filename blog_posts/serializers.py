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
        fields = ("username",)


class BlogPostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    author_name = AuthorSerializer()

    class Meta:
        model = BlogPost
        fields = '__all__'

    def create(self, data):
        author_data = data.pop("author_name")
        category_data = data.pop("category")
        # blogpost = BlogPost(**data)
        blogpost = BlogPost(
            title=data['title'],
            excerpt=data['excerpt'],
            content=data['content'],
            status=data['status'],
            slug=data['slug']
        )

        if author_data:
            author, _created = CommunityUser.objects.get_or_create(
                **author_data)
            blogpost.author = author

        request = self.context.get("request")
        if request and hasattr(request, "user"):
            blogpost.creator = request.user

        blogpost.save()

        if category_data:
            for name in category_data:
                newCategory, _created = Category.objects.get_or_create(**name)
                blogpost.categories.add(newCategory)

        return blogpost

# def update(self, blogpost, data):
    # author_data = data.pop("author")
    # location_data = data.pop("locations")

    # book.title = data.get("title", book.title)
    #  book.rating = data.get("rating", book.rating)
    #   book.year_of_publication = data.get(
    #        "year_of_publication", book.year_of_publication)

    #    if author_data:
    #         author, _created = Author.objects.get_or_create(**author_data)
    #         book.author = author

    #     if location_data:
    #         for location in location_data:
    #             newLocation, _created = Location.objects.get_or_create(
    #                 **location)
    #             book.locations.add(newLocation)

    #     # save to the database
    #     book.save()

    #     # render to the api
    #     return book
