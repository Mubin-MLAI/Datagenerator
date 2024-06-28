import ast
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AllScenario
from .serializers import *
import pandas as pd 
from datetime import datetime
from dateutil.relativedelta import relativedelta
# Create your views here.

def home(request):
    return render(request, 'form.html')


from rest_framework.renderers import JSONRenderer


def downloadcsvfunc(request, uin_number):
    uinlist = []
    datalist = []
    channellist = []
    case_typelist = []
    modeofpremlist = []
    entry_agelist = []
    standard_age_prooflist  = []
    payer_third_party_categorylist = []
    functionalitylist = []
    premiumlist =  []
    basic_salist =  []
    policy_termlist =  []
    maturity_agelist =  []
    genderlist =  []
    smoker_categorylist =  []
    pptlist =  []
    proposal_categorylist =[]
    if uin_number:
        modelss = AllScenario.objects.filter(uin_number=uin_number)
        serializer = AllScenarioSerializer(modelss, many=True)
        data = serializer.data
        
        # Modify the channel data to include "check with" before each channel name
        df = pd.DataFrame(data)
        channel = df['channel'].to_list()
        case_type = df['case_type'].to_list()
        modes_of_premiums = df['modes_of_premiums'].to_list()
        entry_age = df['entry_age'].to_list()
        standard_age_proof = df['standard_age_proof'].to_list()
        payer_third_party_category = df['payer_third_party_category'].to_list()
        functionality = df['functionality'].to_list()   
        premium = df['premium'].to_list()
        basic_sa = df['basic_sa'].to_list() 
        policy_term = df['policy_term'].to_list()
        maturity_age = df['maturity_age'].to_list()
        gender = df['gender'].to_list()
        smoker_category = df['smoker_category'].to_list()
        ppt = df['ppt'].to_list()     
        proposal_category = df['proposal_category'].to_list()       

        set_string = channel[0]
        set_string_case_type = case_type[0]
        set_string_modes_of_premiums = modes_of_premiums[0]
        set_string_entry_age = entry_age[0]
        set_string_standard_age_proof = standard_age_proof[0]
        set_string_payer_third_party_category = payer_third_party_category[0]
        set_string_functionality = functionality[0]
        set_string_premium = premium[0]
        set_string_basic_sa = basic_sa[0] 
        set_string_policy_term = policy_term[0]
        set_string_maturity_age = maturity_age[0]
        set_string_gender = gender[0]
        set_string_smoker_category = smoker_category[0]
        set_string_ppt = ppt[0]
        set_string_proposal_category = proposal_category[0]
        # Convert the string representation of the set into an actual set using ast.literal_eval
        actual_set = ast.literal_eval(set_string)
        actual_set_case_type = ast.literal_eval(set_string_case_type)
        actual_set_modes_of_premiums = ast.literal_eval(set_string_modes_of_premiums)
        actual_set_entry_age = ast.literal_eval(set_string_entry_age)
        actual_set_string_standard_age_proof = ast.literal_eval(set_string_standard_age_proof)
        actual_set_string_payer_third_party_categorye = ast.literal_eval(set_string_payer_third_party_category)
        actual_set_string_functionality = ast.literal_eval(set_string_functionality)
        actual_set_string_premium = ast.literal_eval(set_string_premium)
        actual_set_string_basic_sa = ast.literal_eval(set_string_basic_sa)
        actual_set_string_policy_term = ast.literal_eval(set_string_policy_term)
        actual_set_string_maturity_age = ast.literal_eval(set_string_maturity_age)
        actual_set_string_gender = ast.literal_eval(set_string_gender)
        actual_set_string_smoker_category = ast.literal_eval(set_string_smoker_category)
        actual_set_string_ppt = ast.literal_eval(set_string_ppt)
        actual_set_string_proposal_category = ast.literal_eval(set_string_proposal_category)
        

        # Convert the set to a list if needed
        separated_elements = list(actual_set)
        separated_elements_case_type = list(actual_set_case_type)
        eparated_elements_modes_of_premiums = list(actual_set_modes_of_premiums)
        separated_elements_entry_age = list(actual_set_entry_age)
        separated_elements_standard_age_proof = list(actual_set_string_standard_age_proof)
        separated_elements_payer_third_party_category = list(actual_set_string_payer_third_party_categorye)
        separated_elements_functionality = list(actual_set_string_functionality)
        separated_elements_premium = list(actual_set_string_premium)
        separated_elements_basic_sa = list(actual_set_string_basic_sa)
        separated_elements_policy_term = list(actual_set_string_policy_term)
        separated_elements_maturity_age = list(actual_set_string_maturity_age)
        separated_elements_gender = list(actual_set_string_gender)
        separated_elements_smoker_category = list(actual_set_string_smoker_category)
        separated_elements_ppt = list(actual_set_string_ppt)
        separated_elements_proposal_category = list(actual_set_string_proposal_category)
        
        # Print the result

        for i in separated_elements: 
            channelstr =  'Check With The ' + str(i)
            channellist.append(channelstr)
            # case_typestr =  'Check With The ' + str(j)
            # case_typelist.append(case_typestr)
        for j in separated_elements_case_type: 
            case_typestr =  'Check With The ' + str(j)
            case_typelist.append(case_typestr)
        for k in eparated_elements_modes_of_premiums: 
            modes_of_premiumsstr =  'Check With The ' + str(k)
            modeofpremlist.append(modes_of_premiumsstr)
        for l in separated_elements_entry_age: 
            entry_agestr =   str(l)
            entry_agelist.append(entry_agestr)
        for m in separated_elements_standard_age_proof: 
            standard_age_proofstr =  'Check With The ' + str(m)
            standard_age_prooflist.append(standard_age_proofstr)
        for n in separated_elements_payer_third_party_category: 
            payer_third_party_categorystr =  'Check With The ' + str(n)
            payer_third_party_categorylist.append(payer_third_party_categorystr)
        for o in separated_elements_functionality: 
            functionalitystr =  'Check With The ' + str(o)
            functionalitylist.append(functionalitystr)
        for p in separated_elements_premium: 
            premiumstr =  str(p)
            premiumlist.append(premiumstr)
        for q in separated_elements_basic_sa: 
            basic_sastr =  str(q)
            basic_salist.append(basic_sastr)
        for r in separated_elements_policy_term: 
            policy_termstr =  str(r)
            policy_termlist.append(policy_termstr)
        for s in separated_elements_maturity_age: 
            maturity_agestr =  str(s)
            maturity_agelist.append(maturity_agestr)
        for t in separated_elements_gender: 
            genderstr =  'Check With The ' + str(t)
            genderlist.append(genderstr)
        for u in separated_elements_smoker_category: 
            smoker_categorystr = 'Check With The ' +   str(u)
            smoker_categorylist.append(smoker_categorystr)
        for v in separated_elements_ppt: 
            pptstr = 'Check With The ' +  str(v)
            pptlist.append(pptstr)
        for w in separated_elements_proposal_category: 
            proposal_categorystr = 'Check With The ' +  str(w)
            proposal_categorylist.append(proposal_categorystr)
        uinlist.append(uin_number)

        lenchan =  len(channellist + proposal_categorylist + case_typelist + modeofpremlist + entry_agelist
                    + standard_age_prooflist + payer_third_party_categorylist + functionalitylist + premiumlist + basic_salist +
                    policy_termlist + pptlist + maturity_agelist + genderlist + smoker_categorylist)
        print(lenchan)
        dictn = {
            'Uin No': uinlist, 
            'Channel':  channellist,
            'Proposal_Category':proposal_categorylist,
            'Case_Type': case_typelist,
            'Modes_of_premium':  modeofpremlist,
            'Entry_Age':  entry_agelist,
            'Standard_age_proof': standard_age_prooflist,
            'Payer_third_party_category' : payer_third_party_categorylist,
            'Functionality': functionalitylist,
            'Premium': premiumlist,
            'Basic_Sa': basic_salist,
            'Policy_Term': policy_termlist,
            'PPT': pptlist,
            'Maturity_Age': maturity_agelist,
            'Gender': genderlist,
            'Smoker_Category': smoker_categorylist,
            
            
        }

        # Flatten the dictionary into the desired format
        flattened_list = []
        # total = 'TOTAL SCENARIO GENERATED : ' + str(lenchan)
        for key, values in dictn.items():
            # flattened_list.append([key])
            for value in values:
                flattened_list.append([value])
        # flattened_list.append([total])

        # Create a DataFrame from the flattened list
        # df = pd.DataFrame(flattened_list, columns=['Key_Value'])


        # # max_length = max(len(v) for v in dictn.values())
        # # df_dict = {k: (v + [None]*(max_length - len(v))) for k, v in dictn.items()}

        # # df =  pd.DataFrame(df_dict)
        # path =  'output.csv'


        # # Save the DataFrame to a CSV file
        # filepath =  df.to_csv(path, index=True, header=False)

        # Create a DataFrame from the flattened list
        df = pd.DataFrame(flattened_list, columns=['Key_Value'])

        # Create a response object
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename= "{}.csv"'.format(uin_number)
        
        df.index = df.index + 1
        # Write DataFrame to CSV file in memory and attach to response
        df.to_csv(path_or_buf=response, index=True, header=False)

    return response




def insert_values(lst, start_val, end_val):
    lst.insert(0, start_val)  # Insert at the beginning
    lst.append(end_val)  # Append at the end
    return lst

def calculate_date(age, operation):
    current_date = datetime.now().date()
    if operation == 'subtract':
        return current_date - relativedelta(years=age)
    elif operation == 'add':
        return current_date - relativedelta(years=age)
    

def entryagefunc(request, min_entry_age,max_entry_age):
    min_age = []
    
    min_age.append(min_entry_age)
    start_value = int(min_age[0]) - 1
    end_value = int(min_age[0]) + 1
    result_list1 = insert_values(min_age, start_value, end_value)
    # print(result_list1)

    min_age = []
    
    min_age.append(max_entry_age)
    start_value = int(min_age[0]) - 1
    end_value = int(min_age[0]) + 1
    result_list2 = insert_values(min_age, start_value, end_value)
    # print(result_list2)

    new_lst = result_list1 + result_list2


    # Modify the list for specific cases
    for i in range(len(new_lst)):
        age_str = new_lst[i]
        age = int(age_str)
        if age == (int(min_entry_age) - 1):
            newlistdate = calculate_date(age, 'subtract')
            new_lst[i] =  'Min Fail Case ' + str(newlistdate)
        elif age == (int(max_entry_age) - 1):
            newlistdate3 = calculate_date(age, 'subtract')
            new_lst[i] =  'Max Pass Case ' + str(newlistdate3)
        if age == (int(min_entry_age)):
            newlistdate1 = calculate_date(age, 'subtract')
            new_lst[i] =  'Min Pass Case ' + str(newlistdate1)
        elif age == (int(max_entry_age)):
            newlistdate4 = calculate_date(age, 'subtract')
            new_lst[i] =  'Max Pass Case ' + str(newlistdate4)
        if age == (int(min_entry_age) + 1):
            newlistdate2 = calculate_date(age, 'subtract')
            new_lst[i] =  'Min Pass Case ' + str(newlistdate2)
        elif age == (int(max_entry_age) + 1):
            newlistdate5 = calculate_date(age, 'subtract')
            new_lst[i] =  'Max Fail Case ' + str(newlistdate5)
        
            
        # elif age in [int(max_entry_age) - 1, int(max_entry_age), int(max_entry_age) + 1]:
        #     new_lst[i] = calculate_date(age, 'add')

    # Print the modified list focusing only on dates
    # date_str_list = [date.strftime('%Y-%m-%d') for date in new_lst]

    return new_lst

def premiumfunc(request, a,b):
    min_age = []
    min_age.append(a)
    start_value = 'Min Fail Case ' + str(int(min_age[0]) - 1)
    end_value = 'Min Pass Case ' +  str(int(min_age[0]) + 1)
    result_list1 = insert_values(min_age, start_value, end_value)
    # print(result_list1)

    min_age = []
    min_age.append(b)
    start_value = 'Max Pass Case ' + str(int(min_age[0]) - 1)
    end_value = 'Max Fail Case ' + str(int(min_age[0]) + 1)
    result_list2 = insert_values(min_age, start_value, end_value)
    # print(result_list2)

    new_lst = result_list1 + result_list2

    # Modify the list for specific cases
    for i in range(len(new_lst)):
        if new_lst[i] == a:
            new_lst[i] = 'Min Pass Case ' + str(a)
        elif new_lst[i] == b:
            new_lst[i] = 'Max Pass Case ' + str(b)

    return new_lst

class ChannelAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # Assuming uin_number is passed in the query parameters
        uin_number = request.data.get('uin_number')

        return Response({"error": "UIN Number is required"}, status=status.HTTP_400_BAD_REQUEST)


        
    def post(self, request):
        uin_number = request.POST.get('uin_number')
        selected_channels = request.POST.getlist('channel')
        case_type_ip = request.POST.getlist('case_type')
        modes_of_premiums_ip = request.POST.getlist('modes_of_premiums')
        standard_age_proof_ip = request.POST.getlist('standard_age_proof')
        payer_third_party_category_ip = request.POST.getlist('payer_third_party_category')
        functionality_ip = request.POST.getlist('functionality')
        proposal_category_ip = request.POST.getlist('proposal_category')
        gender_ip = request.POST.getlist('gender')
        smoker_category_ip = request.POST.getlist('smoker_category')
        min_entry_age = request.POST.get('min_entry_age')
        max_entry_age = request.POST.get('max_entry_age')
        min_premium = request.POST.get('min_premium')
        max_premium = request.POST.get('max_premium')
        min_basic_sa = request.POST.get('min_basic_sa')
        max_basic_sa = request.POST.get('max_basic_sa')
        min_policy_term = request.POST.get('min_policy_term')
        max_policy_term = request.POST.get('max_policy_term')
        min_maturity_age = request.POST.get('min_maturity_age')
        max_maturity_age = request.POST.get('max_maturity_age')
        min_ppt = request.POST.get('min_ppt')
        max_ppt = request.POST.get('max_ppt')

        
        if not uin_number:
            return Response({"error": "UIN Number is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not selected_channels:
            return Response({"error": "At least one channel is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        entryagedatelist =  entryagefunc(request, min_entry_age,max_entry_age)
        premiumlist =  premiumfunc(request, min_premium,max_premium)
        basicsalist =  premiumfunc(request, min_basic_sa,max_basic_sa)
        policy_termlist =  premiumfunc(request, min_policy_term,max_policy_term)
        pptlist =  premiumfunc(request, min_ppt,max_ppt)
        maturity_agelist =  entryagefunc(request, min_maturity_age,max_maturity_age)


        channel_obj = AllScenario.objects.create(uin_number=uin_number, 
                                                channel=selected_channels,
                                                case_type=case_type_ip,
                                                modes_of_premiums =  modes_of_premiums_ip,
                                                entry_age = entryagedatelist,
                                                min_entry_age= min_entry_age,
                                                max_entry_age = max_entry_age,
                                                premium = premiumlist,
                                                min_premium = min_premium,
                                                max_premium = max_premium,
                                                standard_age_proof =  standard_age_proof_ip,
                                                payer_third_party_category =  payer_third_party_category_ip,
                                                functionality =  functionality_ip,
                                                proposal_category = proposal_category_ip,
                                                min_basic_sa = min_basic_sa,
                                                max_basic_sa = max_basic_sa,
                                                basic_sa = basicsalist,
                                                min_policy_term = min_policy_term,
                                                max_policy_term = max_policy_term,
                                                policy_term = policy_termlist,
                                                min_maturity_age = min_maturity_age,
                                                max_maturity_age = max_maturity_age,
                                                maturity_age = maturity_agelist,
                                                gender =  gender_ip,
                                                smoker_category = smoker_category_ip,
                                                min_ppt = min_ppt,
                                                max_ppt =  max_ppt,
                                                ppt = pptlist)
        channel_obj.save()

        # uin_number = request.data.get('uin_number')

        datasave =  downloadcsvfunc(request, uin_number)
        

        
        return datasave
