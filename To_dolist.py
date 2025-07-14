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
       os.system("clear")
       print("Removing task in progress..")
       time.sleep(1)
       os.system("clear")
       print("Done delete the Task ")
       
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
    task_chooser = input("Please write the name of the taks you want to update it : ")
    with open("Jobs_information.json" , "r") as updateinformation :
         data = json.load(updateinformation)
         for index ,  elments in enumerate(data) : 
             for keys in elments : 
                 if task_chooser in keys : 
    
                  update_taske_choose =input("what is the inormation you want to update ?\n1-Title\n2-Details\n\n")
    if update_taske_choose == "1" : 
        os.system("clear")
        new_Task_name  = input("could you please enter the new title do you want to replace with older ? : ")
        elments[f"{new_Task_name}"] = elments.pop(task_chooser)
        with open("Jobs_information.json","w") as updateinformation : 
            json.dump(data , updateinformation , indent=3 )
            print("SUCCESSFULLY UPDATE TASKS INFORMATION")
            updateinformation.close()
    elif update_taske_choose == "2":
        Sub_keys = []
        for Sub_keyss in elments[keys] : 
            for index ,  Elements in enumerate(Sub_keyss) :   
             Sub_keys.append(Elements)
             print(Elements+"\n")
             specific_details = int(input("Which  specific information you want to update ? : "
                                 +"\n"))-1
             if Sub_keys[specific_details] :
                new_key_value = input("please enter the new value : ")
                Sub_keyss[Elements] = new_key_value 
                time.sleep(1)
                print("Sucessfully update the value ")
                
                with open("Jobs_information.json" , "w") as updateinformation : 
                    json.dump(data , updateinformation , indent=3)
                                      
                
            
            
            
            
         
        
        
        
                         
                      
                        
                       
                     
                     
           
                    
                    
                    
                
                
          
    
    
    
    
    

Main_menu()

                    
    


    
    



