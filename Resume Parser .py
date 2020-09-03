#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from docx import Document
from docx import *
import re
import json
from docx import *
import re
import json
import mammoth
# result = mammoth.extract_raw_text(document)
# text = result.value
# email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]{3}",text, flags=re.IGNORECASE)
# phone_list=re.findall(r'[\+\(]?[0-9][0-9 .\%\(\)]{8,}[0-9]',text, flags=re.IGNORECASE)
# University_list=re.search(r'\bUniversity of ilorin\b|\bUniversity of Lagos\b',text,flags=re.IGNORECASE)
# Course_Of_study_list=re.search(r'\bEnglish\b|\bMATHEMATICS\b|\bAccountancy\b',text,flags=re.IGNORECASE)
# Age_list=re.search(r'\b1993\b|\b1994\b|\b1995\b',text,flags=re.IGNORECASE)


# In[ ]:


import os
entries = os.scandir(r'C:\Users\abdul\Downloads\RESUMES')
# for entry in entries:
#     with open(entry) as f_input:
#         print(f_input)


# In[ ]:


type(entries)


# In[ ]:


import glob
import errno
import mammoth
import pandas as pd
profiles=[]
path = r'C:\Users\abdul\Downloads\RESUMES\*.docx'
files = glob.glob(path)
for name in files:
        document=open(name,'rb')
        profiles.append((mammoth.extract_raw_text( document).value))


# In[ ]:


files


# In[ ]:


len(profiles)


# In[ ]:


all_Nigeria_uni ={'air force institute of technology','alex ekwueme university',
'federal university gashua','federal university dutse','federal university gusau ','federal university kashere','federal university lafia','federal university lokoja','federal university otuoke',

'federal university oye-ekiti','federal university wukari','michael okpara university ','national open university','nigeria police academy wudil', 'nigerian army university biu',

'nigerian defence academy kaduna','nigerian maritime university okerenkoko','achievers university owo','adeleke university ede','admiralty university, ibusa delta state','african university of science & technology, abuja',

'ajayi crowther university, ibadan','al-hikmah university','al-qalam university','anchor university ayobo lagos state','arthur javis university akpoyubo cross river state',

'atiba university oyo','augustine university','baze university','bells university of technology','benson idahosa university, benin city',

'bingham university','bowen university','caleb university, lagos','caritas university','chrisland university','christopher university mowe',

'clifford university owerrinta abia state','coal city university enugu state','crawford university igbesa','crescent university',

'crown hill university eiyenkorin','dominican university ibadan','dominion university ibadan','edwin clark university','eko university of medical and health sciences ijanikin',

'elizade university','evangel university','fountain unveristy','godfrey okoye university, ugwuomu-nike – enugu state',

'greenfield university kaduna','gregory university','hallmark university ogun','hezekiah university umudi','igbinedion university okada',

'joseph ayo babalola university','kings university ode omu','kola daisi university ibadan','kwararafa university wukari','landmark university omu-aran.',

'lead city university','legacy university okija anambra state','madonna university','mcpherson university ajebo','micheal & cecilia ibru university',

'mountain top university','nile university of nigeria','novena university','obong university obong ntak','oduduwa university ipetumodu ',

'pamo university of medical sciences','paul university awka ','precious cornerstone university','renaissance university','rhema university obeama-asa','ritman university ikot ekpene',

'salem university lokoja','samuel adegboyega university','skyline universit kano','southwestern university oku owa',

'spiritan university nneochi abia state','summit university','tansian university umunya','trinity university ogun state',

'university of mkar','veritas university abuja','wellspring university evbuobanosa ','wesley university of science & technology ondo',

'western delta university','westland university iwo','abia state university','adamawa state university mubi','akwa ibom state university',

'chukwuemeka odumegwu ojukwu university','bauchi state university','benue state university','yobe state university',

'cross river state university of technology calabar','gombe state univeristy','ignatius ajuru university of education','imo state university',

'sule lamido university','kano university of science & technology, wudil','kebbi state university of science and technology aliero',

'kogi state university anyigba','ondo state university of science and technology okitipupa','niger delta university yenagoa','plateau state university bokkos','tai solarin university of education ijebu ode','taraba state university, jalingo',

'sokoto state university','yusuf maitama sule university kano','oyo state technical university ibadan','ondo state university of medical sciences','edo university iyamo','eastern palm university ogboko','university of africa toru orua','bornu state university','moshood abiola university of science and technology abeokuta','gombe state university of science and technology','zamfara state university','bayelsa medical university','airforceinstituteoftechnology','alexekwuemeuniversity',
'federaluniversitygashua','federaluniversitydutse','federaluniversitygusau','federaluniversitykashere','federaluniversitylafia','federaluniversitylokoja','federaluniversityotuoke',

'federaluniversityoye-ekiti','federaluniversitywukari','michaelokparauniversity','nationalopenuniversity','nigeriapoliceacademywudil','nigerianarmyuniversitybiu',

'nigeriandefenceacademykaduna','nigerianmaritimeuniversityokerenkoko','achieversuniversityowo','adelekeuniversityede','admiraltyuniversity,ibusadeltastate','africanuniversityofscience&technology,abuja',

'ajayicrowtheruniversity,ibadan','al-hikmahuniversity','al-qalamuniversity','anchoruniversityayobolagosstate','arthurjavisuniversityakpoyubocrossriverstate',

'atibauniversityoyo','augustineuniversity','bazeuniversity','bellsuniversityoftechnology','bensonidahosauniversity,benincity',

'binghamuniversity','bowenuniversity','calebuniversity,lagos','caritasuniversity','chrislanduniversity','christopheruniversitymowe',

'clifforduniversityowerrintaabiastate','coalcityuniversityenugustate','crawforduniversityigbesa','crescentuniversity',

'crownhilluniversityeiyenkorin','dominicanuniversityibadan','dominionuniversityibadan','edwinclarkuniversity','ekouniversityofmedicalandhealthsciencesijanikin',

'elizadeuniversity','evangeluniversity','fountainunveristy','godfreyokoyeuniversity,ugwuomu-nike–enugustate',

'greenfielduniversitykaduna','gregoryuniversity','hallmarkuniversityogun','hezekiahuniversityumudi','igbinedionuniversityokada',

'josephayobabalolauniversity','kingsuniversityodeomu','koladaisiuniversityibadan','kwararafauniversitywukari','landmarkuniversityomu-aran.',

'leadcityuniversity','legacyuniversityokijaanambrastate','madonnauniversity','mcphersonuniversityajebo','micheal&ceciliaibruuniversity',

'mountaintopuniversity','nileuniversityofnigeria','novenauniversity','obonguniversityobongntak','oduduwauniversityipetumodu',

'pamouniversityofmedicalsciences','pauluniversityawka','preciouscornerstoneuniversity','renaissanceuniversity','rhemauniversityobeama-asa','ritmanuniversityikotekpene',

'salemuniversitylokoja','samueladegboyegauniversity','skylineuniversitkano','southwesternuniversityokuowa',

'spiritanuniversitynneochiabiastate','summituniversity','tansianuniversityumunya','trinityuniversityogunstate',

'universityofmkar','veritasuniversityabuja','wellspringuniversityevbuobanosa','wesleyuniversityofscience&technologyondo',

'westerndeltauniversity','westlanduniversityiwo','abiastateuniversity','adamawastateuniversitymubi','akwaibomstateuniversity',

'chukwuemekaodumegwuojukwuuniversity','bauchistateuniversity','benuestateuniversity','yobestateuniversity',

'crossriverstateuniversityoftechnologycalabar','gombestateuniveristy','ignatiusajuruuniversityofeducation','imostateuniversity',

'sulelamidouniversity','kanouniversityofscience&technology,wudil','kebbistateuniversityofscienceandtechnologyaliero',

'kogistateuniversityanyigba','ondostateuniversityofscienceandtechnologyokitipupa','nigerdeltauniversityyenagoa','plateaustateuniversitybokkos','taisolarinuniversityofeducationijebuode','tarabastateuniversity,jalingo',

'sokotostateuniversity','yusufmaitamasuleuniversitykano','oyostatetechnicaluniversityibadan','ondostateuniversityofmedicalsciences','edouniversityiyamo','easternpalmuniversityogboko','universityofafricatoruorua','bornustateuniversity','moshoodabiolauniversityofscienceandtechnologyabeokuta','gombestateuniversityofscienceandtechnology','zamfarastateuniversity','bayelsamedicaluniversity'}


# In[ ]:


profiles


# In[ ]:


profile_pdf = []
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()
    if text:
        return text
        profile_pdf.append(text)
if __name__ == '__main__':
    prof = []
    
    for PDFRESUMES,subfolders,files in os.walk(r"C:\Users\abdul\Desktop\PDFRESUMES"):
        for file in files:
            print(file)
            prof.append(extract_text_from_pdf(r"C:\Users\abdul\Desktop\PDFRESUMES\{}".format(file)))
# profile_pdf.append(text)
           


# In[ ]:


prof


# In[ ]:


len(prof)


# In[ ]:


combined_profiles = profiles + prof; combined_profiles


# In[ ]:


len(combined_profiles)


# In[ ]:


University_attened=[]
Defined_Honours=['Upper' 'Honours']
Candidate_Honour=[]
Masters=[]
Defined_Age = ['1993','1994','1995','1996','1997','1998']#define formula to produce this
Candidate_Age = []
Defined_Courses = ['B.Sc. Mathematics','B.Eng. Engineering','Mathematics','Bachelor','Statistics']
Candidate_course_of_study = []
Candidate_sof = []


# In[ ]:


# profile_list = re.split(',|\n',profiles[1].lower())
# profile_list[(20 - 4):(20 - 2)]
# print([s for s in profile_list[(20 - 4):(20 - 2)] if 'potential' in s])


# In[ ]:


CV_dict = {}
Candidate = {}
Defined_Age = ['1993','1994','1995','1996','1997','1998']#re-visit
second_class_lower_candidates =['second class lower','2.2','2:2','2ndclasslower', '2nd class lower','lowerdivision','2nd classlower','2ndclass lower','2(2)','secondclass lowerhonours','secondclasslowerhonours']
state_of_origin = ['state of origin', 'state oforigin', 'stateoforigin']
dob_string_list = ['date of birth', 'd o b', 'dob', 'd.o.b','d-o-b','dateofbirth','date ofbirth','dateof birth']#re-visit
course_list= ['BSC.','B.SC.','B.Sc.','b.sc.','BSC','B.SC','B.Sc','b.sc','bsc','bachelorofscience','bachelor of science',
              'bachelor ofscience','b.tech','btech', 'b.eng','beng','bachelor of technology','bachelor oftechnology',
              'bachelor of Engineering','bachelor ofEngineering','bachelor ofart','bachelor of arts',
              'bachelor of education','bedu','b.edu', 'bachelor of law', 'bachelor of history', 'bachelor ofhistory']
def main():
    
    '''    
        check if element exist in list using 'in'
        
    '''
    for profile in combined_profiles:
        email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]{3}",profile, flags=re.IGNORECASE)
        Candidate = {}
        profile_list = re.split(',|\n',profile.lower())
        counter = 0
        for letter in profile_list:
            for i in nig_unis:
                for k in profile_list:
                
                    if i in letter and i not in all_Nigeria_uni: #and  age in list(Defined_Age):
                        Candidate['University_attened'] = i
                    elif 'university' in k:
                        Candidate['University_attened'] = k
                        

            if any(s in letter for s in ['m.sc', 'masters', 'msc'] ):
                temp_master = letter
                Candidate['Masters'] = letter
                if 'university' in letter:
                    print(letter)
                    Candidate['Masters Uni'] = letter
                elif any('university' in s for s in profile_list[(counter - 4):(counter-1)]):
                    Candidate['Masters Uni'] = [s for s in profile_list[(counter - 4):(counter-1)] if 'university' in s].pop()
                elif 'university' in profile_list[counter + 2]:
                    Candidate['Masters Uni'] = profile_list[counter + 2]

            if any(s in letter for s in course_list):
                Candidate['Candidate_course_of_study'] = letter
          
            if any(s in letter for s in dob_string_list) and 'Candidate_Age' not in Candidate.keys():
#                 if any(s in letter.split() for s in Defined_Age) and len(profile_list[counter + 1]) == 4:
                Candidate['Candidate_Age'] = ''.join(profile_list[(counter): (counter + 2)])
#                 else:
#                     Candidate['Candidate_Age'] = "Can't read candidate's age"
            if counter == len(profile_list) and 'Candidate_Age' not in Candidate.keys():
                Candidate['Candidate_Age'] = "Candidate's DOB not provided"
            
            if any(s in letter for s in state_of_origin) and 'Candidate_sof' not in Candidate.keys():
#                 if any(s in letter.split() for s in Defined_Age) and len(profile_list[counter + 1]) == 4:
                Candidate['Candidate_sof '] = ''.join(profile_list[(counter): (counter + 2)])
            if counter == len(profile_list) and 'Candidate_sof' not in Candidate.keys():
                Candidate['Candidate_sof'] = "Candidate's sof not provided"

            degree_class = ['second class','2.1','2:1','first class','1stclass', '2ndclass','1st class', '2nd class','upperdivision','upper division','2(1)','firstclasshonours','secondclasshonours']
            if any(s in letter for s in degree_class):
                Candidate['Candidate_Honour'] = letter
            counter += 1
            temp = letter
        
        CV_dict[email_list[0]] =  Candidate
    return CV_dict
        
    '''    
        check if element NOT exist in list using 'in'
    '''
    if 'Polythecnic' not in combined_profiles[i].split():
        print("Yes, 'Polythecnic' NOT found in List") 

main()


# In[ ]:


df=pd.DataFrame( CV_dict).T;df.index.names =['mail'];df


# In[ ]:


q = "QUALIFIED"
not_q = "NOT QUALIFIED"
yob = {'1995','1996','1997','1998'}
nig_unis = {'anambra state university Uli','kaduna state university','olabisi onabanjo university',
            'imo state university','ambrose alli university','delta state university',
            'ebonyi state university','ekiti state university','nasarawa state university',
            'kwara state university','benue state university','adekunle ajasin university',
            'enugu state university','afe babalola university ','madonna university okija',
            'american university of nigeria','modibbo adama university','university of ibadan',
            'ibrahim badamasi babangida university','Umaru Musa Yar’Adua University',
            'umaru musa yaradua university','abubakar tafawa balewa university',
            'osun state university','rivers state university','lagos state university',
            'redeemers university mowe','redeemer’s university','pan african university',
            'covenant university','university of abuja','usman danfodio university',
            'university of calabar','bayero university kano','university of uyo',
            'nnamdi azikiwe university ','federal university of technology',
            'university of agriculture','university of maiduguri','university of port harcourt',
            'university of jos','ahmadu bello university','obafemi awolowo university',
            'university of benin','university of nigeria nsukka','babcock university',
            'university of ilorin','ladoke akintola university','university of lagos','universityofilorin','anambrastateuniversity Uli','kaduna state university','olabisi onabanjo university',
            'imostateuniversity','ambrosealliuniversity','deltastateuniversity',
            'ebonyistateuniversity','ekitistateuniversity','nasarawastateuniversity',
            'kwarastateuniversity','benuestateuniversity','adekunle ajasin university',
            'enugustateuniversity','afebabalolauniversity ','madonnauniversityokija',
            'americanuniversityofnigeria','modibboadamauniversity','universityofibadan',
            'ibrahimbadamasibabangidauniversity','UmaruMusaYar’AduaUniversity',
            'umarumusayaraduauniversity','abubakartafawabalewauniversity',
            'osunstateuniversity','riversstateuniversity','lagosstateuniversity',
            'redeemersuniversitymowe','redeemer’suniversity','panafricanuniversity',
            'covenantuniversity','universityofabuja','usmandanfodiouniversity',
            'universityofcalabar','bayerouniversitykano','universityofuyo',
            'nnamdiazikiweuniversity ','federaluniversityoftechnology',
            'universityofagriculture','universityofmaiduguri','universityofportharcourt',
            'universityofjos','ahmadubellouniversity','obafemiawolowouniversity',
            'universityofbenin','universityofnigeriansukka','babcockuniversity',
            'universityofilorin','ladokeakintolauniversity','universityoflagos','anambra state universityUli','kaduna stateuniversity','olabisi onabanjo university',
            'imo stateuniversity','ambrose alliuniversity','delta stateuniversity',
            'ebonyi stateuniversity','ekiti stateuniversity','nasarawa stateuniversity',
            'kwara stateuniversity','benue stateuniversity','adekunle ajasinuniversity',
            'enugu stateuniversity','afe babalolauniversity ','madonna universityokija',
            'american university ofnigeria','modibbo adamauniversity','university ofibadan',
            'ibrahim badamasi babangidauniversity','Umaru Musa Yar’AduaUniversity',
            'umaru musa yaraduauniversity','abubakar tafawa balewauniversity',
            'osun stateuniversity','rivers stateuniversity','lagos stateuniversity',
            'redeemers universitymowe','redeemer’s university','pan africanuniversity',
            'covenant university','university ofabuja','usman danfodiouniversity',
            'university ofcalabar','bayero university kano','university ofuyo',
            'nnamdi azikiweuniversity ','federal university oftechnology',
            'university of agriculture','university of maiduguri','university of portharcourt',
            'university ofjos','ahmadu bello university','obafemi awolowo university',
            'university ofbenin','university of nigeriansukka','babcock university',
            'university ofilorin','ladoke akintolauniversity','university oflagos','university of nigeriaenugu'}
masters_yob = {'1993', '1994'}
masters_strings = {'m.sc', 'masters', 'msc'}


# In[ ]:


results=[]
result_dict = {}
for profile in CV_dict.keys():
    out = not_q
    print(profile)
    if 'Candidate_Age' in CV_dict[profile].keys() and 'Candidate_Honour'in CV_dict[profile].keys():
        
        if any(s in CV_dict[profile]['Candidate_Age'] for s in yob):
            print("DOB under 24:", CV_dict[profile]['Candidate_Age'])
            if 'University_attened' in CV_dict[profile].keys():
                
                if any(s in CV_dict[profile]['University_attened'] for s in nig_unis) or                not any(s in CV_dict[profile]['University_attened'] for s in all_Nigeria_uni): 
                    print("University attened:", CV_dict[profile]['University_attened'])
                    out = q + " by age < 24 and University of First Degree"


        
        if any(s in CV_dict[profile]['Candidate_Age'] for s in masters_yob):
            print("DOB over 24:", CV_dict[profile]['Candidate_Age'])
            if 'Masters' in CV_dict[profile].keys() and 'Masters Uni' in CV_dict[profile].keys():
                if any(s in CV_dict[profile]['Masters'] for s in masters_strings) and                not any(s in CV_dict[profile]['Masters Uni'] for s in nig_unis):
                    print("Masters University:", CV_dict[profile]['Masters Uni'])
                    out = q + " by age > 24 and foreign masters uni"
    results.append(out) 
    result_dict[profile]=out
    print(out)
    print('*************************************************')

            
#         print(CV_dict[profile]['Candidate_Age'])


# In[ ]:


result_dict


# In[ ]:


df1 = pd.DataFrame(list(result_dict.items()));df1.columns=['mail','status'];df2=df1.set_index('mail')


# In[ ]:


df2


# In[ ]:


df_row = pd.merge(df,df2, on='mail');df_row


# In[ ]:


df_row.to_csv(r'C:\Users\iyaniwuraa\Desktop\hr_final.csv')


# In[ ]:


profile_pdf = []
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()
    if text:
        return text
        profile_pdf.append(text)
if __name__ == '__main__':
    prof = []
    
    for PDFRESUMES,subfolders,files in os.walk(r"C:\Users\abdul\Desktop\PDFRESUMES"):
        for file in files:
            
            prof.append(extract_text_from_pdf(r"C:\Users\abdul\Desktop\PDFRESUMES\{}".format(file)))
# profile_pdf.append(text)
           


# In[ ]:


prof


# In[ ]:


#TEST=extract_text_from_pdf('osuolalecv2pdf.pdf');TEST


# In[ ]:


#TEST.split(",")


# In[ ]:


list("QUALIFIED")[0:8]


# In[ ]:


#Status_dict = {}
#Candidate = {}
# University_attened=[]
# Defined_Honours=['Upper' 'Honours']
# Candidate_Honour=[]
# Masters=[]
Defined_Age = ['1993','1994','1995','1996','1997','1998']
# Candidate_Age=[]
# Defined_Courses= ['B.Sc. Mathematics','B.Eng. Engineering','Mathematics','Bachelor','Statistics']
# Candidate_course_of_study=[]
# i=0
def status():
    
    '''    
        check if element exist in list using 'in'
        
    '''
    for profile in profiles:
        #print('Yes')
        email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]{3}",profile, flags=re.IGNORECASE)
        print(email_list)
        if email_list[0] == 'anayochikwado@gmail.com':
            print("Checked and found as True")
        out = "NOT QUALIFIED"
        out_age = False
        out_uni = False
        out_masters =  False
        out_overage = False
        for letter in re.split(',|\n',profile.lower()):
#             Candidate = {}
            
            defined_university = ['anambra state university Uli','kaduna state university','olabisi onabanjo university','imo state university','ambrose alli university','delta state university','ebonyi state university','ekiti state university','nasarawa state university','kwara state university','benue state university','adekunle ajasin university','enugu state university','afe babalola university ','madonna university okija','american university of nigeria','modibbo adama university','ibrahim badamasi babangida university','Umaru Musa Yar’Adua University','umaru musa yaradua university','abubakar tafawa balewa university','osun state university','rivers state university','lagos state university','redeemers university mowe','redeemer’s university','pan african university','covenant university','university of abuja','usman danfodio university','university of calabar','bayero university kano','university of uyo','nnamdi azikiwe university '
                                  ,'federal university of technology','university of agriculture','university of maiduguri','university of port harcourt','university of jos','ahmadu bello university','obafemi awolowo university','university of benin',
                                  'university of nigeria nsukka','babcock university','university of ilorin','ladoke akintola university','university of lagos','university of ibadan']
            if any(s in letter for s in defined_university):
                out_uni = True
                              
                break
        Defined_Age = ['1995','1996','1997','1998']
        for letter in re.split(',|\n',profile.lower()):
            if any(s in letter for s in Defined_Age):
                out_age = True
                if email_list[0] == 'anayochikwado@gmail.com':
                    print("Age found to be in order")
             
                break
        Defined_Age_Masters = ['1993','1994']
        
        for letter in re.split(',|\n',profile.lower()):
            if any(s in letter for s in Defined_Age_Masters) :
                out_overage = True
                if email_list[0] == 'anayochikwado@gmail.com':
                    print("Checked and found as True")
            if any(s in letter for s in ['m.sc', 'masters', 'msc'] ):
                out_masters = True                    
                break
        if (out_uni and out_age) or (out_masters and out_overage):
            out = "QUALIFIED"
#             #len(re.findall(r"\bhonours|Second|Upper|First\b", letter, re.IGNORECASE)) > 0:
#                 Candidate['Candidate_Honour'] = letter
           # if 'university of ilorin' in letter :
               
        print(out)
                
#             if any(s not in letter for s  in defined_university):
#                 print("NOT QUALIFIED")
            
                #Candidate['University_attened'] = letter
#         if 'university of ilorin' not in letter and  letter not in list(Defined_Age):
#                 candidate ={}
#         print("NOT QUALIFIED")  #Candidate['University_attened'] = "Not found"
# if __name__ == '__status__':
status()


# In[ ]:


a = ['anambra state university Uli','kaduna state university','olabisi onabanjo university','imo state university','ambrose alli university','delta state university','ebonyi state university','ekiti state university','nasarawa state university','kwara state university','benue state university','adekunle ajasin university','enugu state university','afe babalola university ','madonna university okija','american university of nigeria','modibbo adama university','ibrahim badamasi babangida university','Umaru Musa Yar’Adua University','umaru musa yaradua university','abubakar tafawa balewa university','osun state university','rivers state university','lagos state university','redeemers university mowe','redeemer’s university','pan african university','covenant university','university of abuja','usman danfodio university','university of calabar','bayero university kano','university of uyo','nnamdi azikiwe university '
                                  ,'federal university of technology','university of agriculture','university of maiduguri','university of port harcourt','university of jos','ahmadu bello university','obafemi awolowo university','university of benin',
                                  'university of nigeria nsukka','babcock university','university of ilorin','ladoke akintola university','university of lagos','university of ibadan']
string = 'nnamdi azikiwe university – anambra state – b.eng electrical engineering (second class upper honours)'
any(s in string for s in a)
    


# In[ ]:


for profile in profiles:
    print('Yes')


# In[ ]:


# # # profiles[0]
# # len(profiles)
# sentence =  I am a very happy person
# dic = {}
# for i in sentence.split():
#     if i = 'am':
#         dic['Check_am'] = len(i)
#     else:
#         dic['Check_am'] = "None"
#     if i =
d = [2,4,6,8,0]
s = '1,4,7,54'
c = -1
# for i in d:
#     c+= 1
#     if str(i) in s.split(','):
#         print(True)
#         a = s.split(',')[c]
#     print(c)
        
    
# type(a)
# # print(s.split(','))
Candidate.keys()


# In[ ]:


s.split(',')


# In[ ]:


for index, letter in enumerate(profiles):
    print(index, letter)
    


# In[ ]:


profiles


# In[ ]:


len(profiles)


# In[ ]:


DIR=os.path.join( r'C:\Users\abdul\Downloads',"RESUMES")
file_list = glob.glob(DIR + "docx")
corpus = []
for file_path in file_list:
    with open(file_path) as f_input:
        corpus.append(f_input.read())
print(corpus)


# In[ ]:


profiles_pdf =[]
import PyPDF2
import re
import os

for PDFRESUMES,subfolders,files in os.walk(r"C:\Users\abdul\Desktop\PDFRESUMES"):
    for file in files:
        print(file)
        # open the pdf file
        object = PyPDF2.PdfFileReader(os.path.join(PDFRESUMES,file))
        print(object)

        # get number of pages
        NumPages = object.getNumPages()

        # define keyterms
        #String = "New York State Real Property Law"

        # extract text and do the search
        Text = ''
        for i in range(0, NumPages):
            PageObj = object.getPage(i)
#             if file == 'osuolalecv2.pdf':
#                 a= input('Checking osuolalecv2.pdf file. Press enter to continue')
                
            print("this is page " + str(i)) 
            Text += PageObj.extractText()
            
#             profiles_pdf.append(Text)
        profiles_pdf.append(Text)

#         profiles_pdf=''.join(profiles_pdf)
            # print(Text)
            #ResSearch = re.search(String, Text)
            #print(ResSearch)


# In[ ]:


profiles_pdf


# In[ ]:


len(profiles_pdf)


# In[ ]:




