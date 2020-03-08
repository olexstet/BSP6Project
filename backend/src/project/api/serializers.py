from rest_framework import serializers
from project.models import Question1

class Question1Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Question1
        fields = ('word','definitionWord','definitionOther1','definitionOther2','definitionOther3','definitionOther4')