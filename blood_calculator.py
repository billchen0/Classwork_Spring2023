def interface():
    print('Blood Calculator')
    keep_running = True

    while keep_running:
        print('Options:')
        print('1 - HDL')
        print('2 - LDL')
        print('9 - Quit')

        choice = input('Select an option: ')
        
        if choice == '9':
            keep_running = False
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
    
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

def LDL_input():
    LDL_value = input('Enter the LDL result: ')
    LDL_value = int(LDL_value)
    return LDL_value



    
interface()