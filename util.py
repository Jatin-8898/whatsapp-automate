import pandas as panda

def filter_the_contacts(filename):

    all_contacts = panda.read_csv(filename)
    all_contacts = all_contacts[["Name", "Given Name"]]
 
    print("Instructions:" +  "\nTo break, Enter c")
    print("To keep it same as the given name present after  - , press k")

    wishing_contacts = dict()
    
    for index, row in all_contacts.iterrows():
        print(str(row['Name'])+"  -  "+str(row['Given Name']))
        y = input()
        
        if y == 'c':
            break
        
        if y == 'k':
            wishing_contacts[str(row['Name'])] = str(row['Given Name'])
        
        elif y != '':
            wishing_contacts[str(row['Name'])] = y

    return wishing_contacts



