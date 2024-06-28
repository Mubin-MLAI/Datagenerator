from django.db import models

# Create your models here.
# models.py

# class channel(models.Model):
#     uin_number = models.CharField(max_length=100)
#     channel = models.CharField(max_length=100)  # Considering multiple channels are selected

#     def __str__(self):
#         return self.uin_number
# class proposal_category(models.Model):
#     uin_number = models.CharField(max_length=100)
#     proposal_category = models.CharField(max_length=100)  # Considering multiple proposal categories are selected

#     def __str__(self):
#         return self.uin_number
# class mudrank_stamp_duty(models.Model):
#     uin_number = models.CharField(max_length=100)    
#     mudrank_stamp_duty = models.CharField(max_length=100, blank=True, null=True)
#     # gst = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.uin_number    
# class entry_age(models.Model):
#     uin_number = models.CharField(max_length=100)  
#     min_entry_age = models.IntegerField(blank=True, null=True)
#     max_entry_age = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return self.uin_number
# class modes_of_premiums(models.Model):
#     uin_number = models.CharField(max_length=100)
#     modes_of_premiums = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple modes are selected

#     def __str__(self):
#         return self.uin_number
# class premium(models.Model):
#     uin_number = models.CharField(max_length=100)    
#     min_premium = models.FloatField(blank=True, null=True)
#     max_premium = models.FloatField(blank=True, null=True)

#     def __str__(self):
#         return self.uin_number
# class basic_sa(models.Model):
#     uin_number = models.CharField(max_length=100)
#     min_basic_sa = models.FloatField(blank=True, null=True)
#     max_basic_sa = models.FloatField(blank=True, null=True)

#     def __str__(self):
#         return self.uin_number
# class policy_term(models.Model):
#     uin_number = models.CharField(max_length=100)
#     min_policy_term = models.IntegerField(blank=True, null=True)
#     max_policy_term = models.IntegerField(blank=True, null=True)
#     specific_ppt = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.uin_number
# class maturity_age(models.Model):
#     uin_number = models.CharField(max_length=100)
#     min_maturity_age = models.IntegerField(blank=True, null=True)
#     max_maturity_age = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return self.uin_number
# class gender(models.Model):
#     uin_number = models.CharField(max_length=100)
#     gender = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.uin_number
# class smoker_category(models.Model):
#     uin_number = models.CharField(max_length=100)
#     smoker_category = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.uin_number
# class case_type(models.Model):
#     uin_number = models.CharField(max_length=100)    
#     case_type = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple case types are selected

#     def __str__(self):
#         return self.uin_number
# class standard_age_proof(models.Model):
#     uin_number = models.CharField(max_length=100)    
#     standard_age_proof = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple proofs are selected

#     def __str__(self):
#             return self.uin_number
# class payer_third_party_category(models.Model):
#     uin_number = models.CharField(max_length=100)    
#     payer_third_party_category = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple categories are selected

#     def __str__(self):
#         return self.uin_number
# class functionality(models.Model):
#     uin_number = models.CharField(max_length=100)    
#     functionality = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple functionalities are selected

#     def __str__(self):
#         return self.uin_number


from django.db import models

# Create your models here.
# models.py

class AllScenario(models.Model):
    uin_number = models.CharField(max_length=100)

    # Channel fields
    channel = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple channels are selected

    # Proposal category fields
    proposal_category = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple proposal categories are selected

    # Mudrank stamp duty fields
    mudrank_stamp_duty = models.CharField(max_length=100, blank=True, null=True)
    # gst = models.CharField(max_length=100, blank=True, null=True)  # Uncomment if needed

    # Entry age fields
    entry_age = models.CharField(max_length=100, blank=True, null=True)
    min_entry_age = models.IntegerField(blank=True, null=True)
    max_entry_age = models.IntegerField(blank=True, null=True)

    # Modes of premiums fields
    modes_of_premiums = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple modes are selected

    # Premium fields
    premium = models.CharField(max_length=100, blank=True, null=True)
    min_premium = models.FloatField(blank=True, null=True)
    max_premium = models.FloatField(blank=True, null=True)

    # Basic SA fields
    basic_sa = models.CharField(max_length=100, blank=True, null=True)
    min_basic_sa = models.FloatField(blank=True, null=True)
    max_basic_sa = models.FloatField(blank=True, null=True)

    # Policy term fields
    policy_term = models.CharField(max_length=100, blank=True, null=True)
    min_policy_term = models.IntegerField(blank=True, null=True)
    max_policy_term = models.IntegerField(blank=True, null=True)

    # Policy term fields
    ppt = models.CharField(max_length=100, blank=True, null=True)
    min_ppt = models.IntegerField(blank=True, null=True)
    max_ppt = models.IntegerField(blank=True, null=True)

    # Maturity age fields
    maturity_age = models.CharField(max_length=100, blank=True, null=True)
    min_maturity_age = models.IntegerField(blank=True, null=True)
    max_maturity_age = models.IntegerField(blank=True, null=True)

    # Gender fields
    gender = models.CharField(max_length=100, blank=True, null=True)

    # Smoker category fields
    smoker_category = models.CharField(max_length=100, blank=True, null=True)

    # Case type fields
    case_type = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple case types are selected

    # Standard age proof fields
    standard_age_proof = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple proofs are selected

    # Payer third party category fields
    payer_third_party_category = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple categories are selected

    # Functionality fields
    functionality = models.CharField(max_length=100, blank=True, null=True)  # Considering multiple functionalities are selected

    def __str__(self):
        return self.uin_number

