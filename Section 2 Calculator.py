############# My calculator


import re


#This was my attempt at the calc before watching the video, I didn't know of the eval function
#which was essential really. Also after watching bits of the video, I got to a solid point but
#didn't apply any filters to the calc input, causing errors
def unassissted_calculator():
    boolean_control=1   #These were set globally in his examples
    a=0
    print ('Enter equation:')
    while boolean_control==1:
        if a==0:
            input_equation = input()
        else:
            input_equation = input(str())

        if input_equation == 'Toast':
            boolean_control = 0
        elif input_equation=='Clear':
            a=0
        else:

            input_numbers = re.sub('[^0-9]','',input_equation)
            print(input_numbers)

            a=a+1
    return


def calculator():
    boolean_control = 1  # These were set globally in his examples
    a = 0
    while boolean_control == 1:
        #on the first iteration, get equation prompt
        if a == 0:
            input_equation = input("Enter opalration:")
        #on following iterations, start prompt with the previous answer
        else:
            input_equation = input(str(a))

        if input_equation == 'Toast':
            boolean_control = 0
        elif input_equation == 'Clear':
            a = 0
        else:
            #apply filter to avoid breaking the eval function
            input_filtered=re.sub('[a-zA-Z,.()" "]','',input_equation)
            if a==0:
                a= eval(input_filtered)
            else:
                a=eval(str(a)+input_filtered)

    return


calculator()



