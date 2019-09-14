print ('This is the main script to find temperature data')
print ('We are going to start by defining some basic parametres...')
print ('')
print ('Select mode')
print ('''Mode 1 = We gather a certain number of data points
Mode 2 = We gather data over a certain time frame''')

Mode1 = 'we gather a certain number of data points'
Mode2 = 'we gather data over a certain time frame'

choice = input('Please select the mode by typing the the mode number: ')

def checkChoice(choice):
    if choice == '1':
        Mode = Mode1
        return Mode
    elif choice == '2':
        Mode = Mode2
        return Mode
    else:
        print ('Sorry I didnt quite catch that. Could you please re-enter one of the two options.')
        choice = input('Please select the mode by typing the the mode number: ')
        checkChoice(choice)

Mode = checkChoice(choice)

print ('')
print ('We are currently in mode',choice, 'where', Mode)

#=============================================================================================================================================
##Defining Modes and what they do

#Mode1

import time
from datetime import datetime

def Mode1Script():
    nDataPoints = int(input('How many data points would you like?: '))
    tDataPoints = int(input('What is wanted frequency of the data points? (s): '))
    n=1
    h=1
    Data2 = []
    start_time = time.time()
    elapsed_time = time.time() - start_time
    while n < nDataPoints:
        elapsed_time = time.time() - start_time
        Data2.append([n**2,elapsed_time,datetime.now()])
        n=n+1
        time.sleep(tDataPoints)
    return Data2

#Mode2

def Mode2Script():
    tDataPoints = int(input('How long would you like the script to run for? (s): '))
    nDataPoints = int(input('How many data points would you like?: '))
    frequency = nDataPoints / tDataPoints
    Data2 = []
    t = []
    n=0
    start_time = time.time()
    elapsed_time = time.time() - start_time
    while elapsed_time < tDataPoints:
        n=n+1
        elapsed_time = time.time() - start_time
        time.sleep(frequency)
        Data2.append([n**2,elapsed_time,datetime.now()])
    return Data2

#=============================================================================================================================================
#Defining filename

Y=1
N=2

print('')
ans = input('Would you like to give the new file a specific name? (Y/N): ')
 
if ans=="Y":
    name = input('What would you like the name to be?: ')
else:
    name = "Data"

fileName = str(dt_string + name)


print('The filename is now', fileName)

#=============================================================================================================================================
#Actual steps of the script

if choice == '1':
    Data2 = Mode1Script()
else: Data2= Mode2Script()

Data2 = "\n".join(["\t".join([str(y) for y in x]) for x in Data2])

#=============================================================================================================================================
#Obtaining current time and date for savefile


# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%Y_%m_%d__%H_%M__")


#=============================================================================================================================================
#Saving data into a file

print('')
print('Initialising save')

import os

def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()
    
def readFile(filePath):
    if not fileExists(filePath):
        print('The file, ' + filePath + ' does not exist - cannot read it.')
        return ""

    fileHandle = open(filePath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data

DATA_FILE_PATH = f'{fileName}.txt' # path to the file as a constant   'Data.txt'
Data = f'{Data2}'      #Data going in the file

writeFile(DATA_FILE_PATH,Data)

Data2 = readFile(DATA_FILE_PATH)
print('The file contains: ', Data2)

print ('')
print ('Save succesful.')

#=============================================================================================================================================
