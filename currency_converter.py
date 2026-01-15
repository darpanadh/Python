# Currency converter 

def conversion():
    try:

        amt=float(input("Enter the amount: "))
        source=(input("Source currency (USD,NRS,INR): ").upper()).strip()
        target=(input("Target currency (USD,NRS,INR): ").upper()).strip()
        
        rate={
            ("USD","NRS"):142,
            ("USD","INR"):90,
            
            ("NRS","USD"):1/142,
            ("NRS","INR"):1/1.6,
            
            ("INR","NRS"):1.6,
            ("INR","USD"):1/90
        }
        
        if source == target:
            print(f"{amt}{source} is equal to {amt}{target}")
        
        elif (source,target) in rate:
            final_val=amt*rate[source,target]
            print(f"{amt}{source} is equal to {final_val}{target}")
        
        else:
            print("Conversion not available.")
                
    except ValueError:
        print("Enter the valid amount.")

def again():
    while True:
        
        choice=input("Convert again (y/n) ?").lower()
        if choice =='n':
            exit()
        elif (choice == 'y'):
            break
        else:
            print("Enter valid choice (y/n).")

while True:
    conversion()
    again()
