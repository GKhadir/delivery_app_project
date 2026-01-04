from rest_framework import serializers
from .models import UsersData,delivary_partner_details,addresses,user_profiles

class UsersDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersData
        fields = ['id', 'username', 'email', 'phone', 'password', 'role', 'is_active', 'is_verified' , 'created_at']

    def create(self, validated_data):
        # Use your custom manager to ensure password is hashed
        user = UsersData.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Handle password hashing on update
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class user_profilesSerializer(serializers.ModelSerializer):
    class Meta:
        model= user_profiles
        fields='__all__'

class addressesSerializer(serializers.ModelSerializer):
    class Meta:
        model= addresses
        fields='__all__'

class delivary_partner_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=delivary_partner_details
        fields='__all__'