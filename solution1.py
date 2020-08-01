#defining solution function
def solution(str):
	#the following statement will only execute if the length of string is equal to 10 and string starts with 7 or 8 or 9 and string contains numbers
    if(len(str)==10  and str.isnumeric()  and (str.startswith('7') or str.startswith('8') or str.startswith('9'))) :
        print("VALID")
    #else this will get executed if it doesn't statisfy the above conditions
    else:
    	print("NOT VALID")






#taking input of mobile number from the user in string  
mobile_number=input("Please enter your mobile  number:")
#calling solution function 
solution(mobile_number)