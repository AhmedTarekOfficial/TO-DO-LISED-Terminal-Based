import os 
import time 
import json
def Main_menu() : 
    os.system("clear")
    print("Hello to our todo list app do you wanna to be an Effective person not lazy then use us and organize you'r day :) "+"\n--------------------------")
    userchoice = input("1-Add Job\n2-delete job\n3-update job\n\nenter you'r choice : ")
    if userchoice == "1" : 
        addjob()
    elif userchoice == "2" :
        Remove_job()
    else : 
        Update_Job_information()
    
    
    
    
    
def addjob():
    
    os.system("clear")
    Job_title = input("please enter job title : ")
    os.system("clear")
    JOB_DESCRIPTION = input("PLEASE ENTER JOB DESCREPTION : ")
    os.system("clear")
    Job_period = input("enter the job period such as (10/24/2003 10:45 To 12/31/2020 10:40) IF you don't want period just click enter ")
    
    JOBS =  [] 
    
    
        
    if Job_period is None or Job_period == "" :
        JOBS.append({
        f"{Job_title}":[
            {
                "Descreption" : JOB_DESCRIPTION , 
            }
        ]
        
    })
    else :
        JOBS.append({
        f"{Job_title}":[
            {
                "Descreption" : JOB_DESCRIPTION , 
                 "Job_Period" : Job_period 
            }
        ]
        
    })
    with open("Jobs_information.json","w") as jobs : 
        json.dump(JOBS , jobs , indent=3)
        jobs.close()
        
    print(JOBS)
    
    

def Remove_job() :
    count = 0
    first_input = True
    with open("Jobs_information.json","r") as Remove_information_about_specific_job :
        data = json.load(Remove_information_about_specific_job) 
        
        for Elements in data :
            if first_input !=False :
                count = 0 
            else :
                count +=1
            
            first_input = False
            for parent_dict_key in Elements : 
                print("Job name  : "+parent_dict_key+"\n-------------------------------------")
                for Elements_of_sub_array in Elements[parent_dict_key] :
                    for Sub_dict_key in Elements_of_sub_array :
                        print("\t"+f"{Sub_dict_key} : \n\t\t{Elements_of_sub_array[Sub_dict_key]}")
    
    user_job_choice = input("please write the title of the job you want to delete it from the list of jobs : ")
    
    if user_job_choice in parent_dict_key :
    
       del data[count][user_job_choice]
       print("Done delete the key ")
       with open("Jobs_information.json" , "w") as rr :
           json.dump(data , rr , indent=3)
           rr.close()
       
                        
                    
                    
def display_Jobs() : 
      all_keys = {} 
      
    
      with open("Jobs_information.json","r") as Display_JOBS :
        data = json.load(Display_JOBS) 
        for Elements in data :
            for parent_dict_key in Elements : 
                all_keys["Parent_keys"] = parent_dict_key
                print("Job name  : "+parent_dict_key+"\n-------------------------------------")
                for Elements_of_sub_array in Elements[parent_dict_key] :
                    for Sub_dict_key in Elements_of_sub_array :
                        print("\t"+f"{Sub_dict_key} : \n\t\t{Elements_of_sub_array[Sub_dict_key]}")
                        all_keys["sub_keys"] = [Sub_dict_key]
                        
        return all_keys
    
    
    
                    
                    
def Update_Job_information():
    
    display_Jobs()
    
    
    

Main_menu()

                    
    


    
    



