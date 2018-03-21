def assign_free_room(lab_system_details):
#     print(lab_system_details)
    for name,lab in lab_system_details.items():
        for k,v in lab.items() :
            if v[0]=='Free' and v[1]=='Good' :
                v[1]='allocated'
                print(name+" - "+ k)
                return
    print("not available ")

        
if __name__ == "__main__":
    lab_system_details = {'C Lab':{'1':['Free','Good'],'2':['Allocated','Repair'],'3':['Free','Good'] }, 'Cisco Lab':{'1':['Free','Good'],'2':['Free','Good'],'3':['Allocated','Repair']}}
    Student_list = {'Raja': 701, 'Teja': 702, 'Suraj': 770, 'manikant': 800}
    for student in sorted(Student_list.items(),key=lambda x:x[1]):
        print(student[0] + " - " + str(student[1]) ,end= " - " ) 
        assign_free_room(lab_system_details)