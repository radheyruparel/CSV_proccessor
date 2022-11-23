#
##Author: Radhey Ruparel
##Description: A program that reads into a CSV file with no column labels, and can compute an average, maximum and min.
##

#Required to import all the os functions and progam is able to locate the file
import os
os.chdir(os.path.dirname(__file__))

#Importing all the modules for the program execution  
import random #Importing the random module

def storing_the_data_from_file(file_selection):
    
    '''This function reads the data from the user selected CSV file. Then stores the data from
    the CSV file into a 2D list called numbers.
    The  parameter varaible for this function is file_selected, which is a string. Contains the name
    of the file which needs to be read.'''
    
    #Opening the user selected file for reading
    file_selected=open(file_selection,'r')
    
    #Declaring of the list
    numbers=[]
    
    #Iternating through CSV file line by line
    for number in file_selected:
        #This strips \n from the line and creates that line into a list
        number=number.rstrip('\n').split(',')
        #Appending a list to a list, making numbers 2D list
        numbers.append(number)
    
    #Returning the 2D list for futher processing
    return numbers

def processing_the_command(column_number,command_operation,file_selection):
    
    '''This function uses the 2D with the data, to process the desired command given by 
    the user. Such as average, minimum and maximum.
    The parameter varaible for this function is file_selected, which is a string. Contains the name
    of the file which needs to be read.
    Another varaible is column_number, which is a intger, the number of column with values, which user 
    selected to perform the command on.
    Other varaible is command_operation, which is a string, is the choice of operation the user wants
    to perform
    '''
    #Calling the function, for having the main 2D list in the funtion
    numbers=storing_the_data_from_file(file_selection)
    #This list will have the values of the column, which user selects
    column_selected=[]
    #For list indexing
    column_select=column_number-1
    #This loop will choice the value at the selected column and put into a new list, just the colum 
    for number_list in numbers:
        #coverting the number into float for futher numrical processing
        column_selected.append(float(number_list[column_select]))
    
    #For taking the average of the 
    if command_operation=='avg':
        #A varaible keeping the record of the total 
        total_submation=0
        #Using the loop to calcatue the summation of the items in the sliced list 
        for number in column_selected:
            total_submation+=float(number)
        #Callcuting the average
        average_column=total_submation/len(column_selected)
        #Printing the average for the user to know. 
        print('The average for column',column_number,'is:',average_column)
    
    #For finding the maximum value in the selected
    if command_operation=='max':
        #This will return the maximum value from the sliced list
        maximum_value=max(column_selected)
        #Printing the maximum value for the user to know. 
        print('The maximum value in column',column_number,'is:',maximum_value)
    
    #For finding the minimum value in the selected
    if command_operation=='min':
        #This will return the minimum value from the sliced list
        minimum_value=min(column_selected)
        #Printing the minimum value for the user to know. 
        print('The minimum value in column',column_number,'is:',minimum_value)

#Declaring the main function  
def main():
    #User inputs the CSV which needs to the read
    file_selection=input('Enter CSV file name:\n')
    #User selects the column for which the user wants the operation to be performed on. 
    column_number=int(input('Enter column number:\n'))
    #User selects one of the three operation avg, min and max.
    command_operation=input('Enter column operation:\n')
    #Calling the 
    processing_the_command(column_number,command_operation,file_selection)

#Calling the main function    
main()