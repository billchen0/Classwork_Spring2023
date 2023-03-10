def interface():
    print('Blood Calculator')
    keep_running = True

    while keep_running:
        print('Options:')
        print('1 - HDL')
        print('2 - LDL')
        print('3 - Cholesterol')
        print('9 - Quit')

        choice = input('Select an option: ')
        
        if choice == '9':
            keep_running = False
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
        elif choice == '3':
            chol_driver()
    
    print('Program Ending')

def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)
    

def HDL_input():
    HDL_value = input("Enter the HDL result: ")
    HDL_value = int(HDL_value)
    return HDL_value

def HDL_analysis(HDL_int):
    if (HDL_int >= 60):
        answer = 'Normal'
    elif (40 <= HDL_int < 60):
        answer = 'Borderline Low'
    else:
        answer = 'Low'

    return answer

def HDL_output(HDL_value, HDL_analy):
    print(f'The HDL result of {HDL_value} is considered {HDL_analy}')
    return

def LDL_driver():
    LDL_in = LDL_input()
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_analy)

def LDL_input():
    LDL_value = input('Enter the LDL result: ')
    LDL_value = int(LDL_value)
    return LDL_value

def LDL_analysis(LDL_int):
    if (LDL_int < 130):
        answer = 'Normal'
    if (130 <= LDL_int < 159):
        answer = 'Borderline High'
    if (160 <= LDL_int < 189):
        answer = 'High'
    if (LDL_int >= 190):
        answer = 'Very High'

    return answer

def LDL_output(LDL_value, LDL_analy):
    print(f'The LDL result of {LDL_value} is considered {LDL_analy}')
    return 

def chol_driver():
    chol_in = chol_input()
    chol_analy = chol_analysis(chol_in)
    chol_output(chol_in, chol_analy)

def chol_input():
    chol_value = int(input('Enter the total cholestoral result: '))
    return chol_value

def chol_analysis(chol_int):
    if (chol_int < 200):
        answer = 'Normal'
    if (200 <= chol_int <= 239):
        answer = 'Borderline High'
    if (chol_int >= 240):
        answer = 'High'

    return answer

def chol_output(chol_value, chol_analy):
    print(f'The Total Cholestoral result of {chol_value} is considered {chol_analy}')
    return 

def check_fever(input_list):
    for temp in input_list:
        if temp > 100.5: 
            return True
        
    return False

if __name__ == "__main__":
    interface()