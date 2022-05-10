from calendar import c
from rest_framework import serializers

from blog_categories.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class CategoryEditorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', )

    def validate(self, attrs):
        # request = self.context.get("request")
        # print("attributes", attrs)
        # if request and hasattr(request, "user"):
        #     if attrs['is_staff_writer'] == False:
        #         raise serializers.ValidationError({
        #             "error_message": "You're not allowed to perform this action."
        #         })

        print("attributes", attrs)

        return attrs

    def update(self, blogcategory, data):

        blogcategory.name = data.get("name", blogcategory.name)

        # save to the database
        blogcategory.save()

        # render to the api
        return blogcategory
