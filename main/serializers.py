from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    age = serializers.IntegerField(max_value= 96 , min_value = 17)
    workclass = serializers.CharField(max_length=100)
    fnlwgt = serializers.IntegerField(min_value = 0)
    education = serializers.CharField(max_length=100)
    education_num = serializers.IntegerField(min_value = 0)
    marital_status = serializers.CharField(max_length=100)
    occupation = serializers.CharField(max_length=100)
    relationship = serializers.CharField(max_length=100)
    race = serializers.CharField(max_length=100)
    sex = serializers.CharField(max_length=100)
    capital_gain = serializers.IntegerField(min_value = 0)
    capital_loss = serializers.IntegerField(min_value = 0)
    hours_per_week = serializers.IntegerField(min_value = 0)
    native_country = serializers.CharField(max_length=100)