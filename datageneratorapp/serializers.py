from rest_framework import serializers
from .models import *

class AllScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllScenario
        fields = '__all__'

    # def create(self, validated_data):
    #     channels_data = validated_data.pop('channel')
    #     uin_number = validated_data.get('uin_number')
    #     channels = [channel.objects.create(uin_number=uin_number, channel=channel_data) for channel_data in channels_data]
    #     return channels

# class ProposalCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = proposal_category
#         fields = '__all__'

# class MudrankStampDutySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = mudrank_stamp_duty
#         fields = '__all__'

# class EntryAgeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = entry_age
#         fields = '__all__'

# class ModesOfPremiumsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = modes_of_premiums
#         fields = '__all__'

# class PremiumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = premium
#         fields = '__all__'

# class BasicSASerializer(serializers.ModelSerializer):
#     class Meta:
#         model = basic_sa
#         fields = '__all__'

# class PolicyTermSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = policy_term
#         fields = '__all__'

# class MaturityAgeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = maturity_age
#         fields = '__all__'

# class GenderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = gender
#         fields = '__all__'

# class SmokerCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = smoker_category
#         fields = '__all__'

# class CaseTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = case_type
#         fields = '__all__'

# class StandardAgeProofSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = standard_age_proof
#         fields = '__all__'

# class PayerThirdPartyCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = payer_third_party_category
#         fields = '__all__'

# class FunctionalitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = functionality
#         fields = '__all__'
