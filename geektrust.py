import sys

def get_bill(bedrooms, corp, bore, no_of_guests_in_month):  
    
    if bedrooms == 2:
        alloted_liters = 900  # 3*10*30 = 900 liters Normally alloted for a 2BHK  every month.
    else:
        alloted_liters = 1500  # 5*10*30 = 1500 liters Normally alloted for a 3BHK  every month.  

    
    no_of_liters_from_tanker = no_of_guests_in_month*10*30 # extra liters used from tanker

    total_liters = alloted_liters+no_of_liters_from_tanker  # Total no.of liters consumed in a month.
    
    corp_bill = (corp/(corp+bore))*alloted_liters*1       # using given ratio and calculating corporation_water and borewell_water bills 
    bore_bill = (bore/(corp+bore))*alloted_liters*1.5  
    

    if no_of_liters_from_tanker <= 500:                     # Depending on slabs tanker_water bill is calculated 
        tanker_bill = 2 * no_of_liters_from_tanker
    elif no_of_liters_from_tanker <= 1500:
        tanker_bill = 1000 + 3*(no_of_liters_from_tanker-500)
    elif no_of_liters_from_tanker <= 3000:
        tanker_bill = 4000 + 5*(no_of_liters_from_tanker-1500)
    elif no_of_liters_from_tanker > 3000:
        tanker_bill = 11500 + 8*(no_of_liters_from_tanker - 3000) 

 
    total_bill = corp_bill + bore_bill + tanker_bill

    return total_liters,int(total_bill)     #converting the total bill from float to integer as asked in the problem



def main():
    input_file = open(sys.argv[1])
    
    commands_list=[]       
    for command in input_file:
        commands_list+=[command]

    guests_commands_list=[]
    for item in commands_list[1:-1]:
        guests_commands_list.append(int(item.split()[1]))

    no_of_guests_in_month=sum(guests_commands_list)    #Total guests in a month.

    

    command, no_of_bedrooms, ratio = commands_list[0].split()
    no_of_bedrooms = int(no_of_bedrooms)
    corp,bore =[int(char) for char in ratio.split(":")]     # unpacking the integers in the rario of corporaion_water:borewell_water
    

    print(*get_bill(no_of_bedrooms, corp, bore, no_of_guests_in_month)) # unpacking and printing the water_used_in_liters and bill using *

    return None

    
    
    

if __name__ == "__main__":
    main()
