'''
Created on Jan 18, 2014

@author: Edoardo Foco

Input: 
    -File.txt : Containing a list of names or surnames
    -names or surnames : names or surnames separated by a space. If these contain non-alphabetic characters,
                         the characters will be ignored
    
    Sample Input:  
    -python Program.py Jones Winton < surnames.txt

Output:
    The program outputs a list of names or surnames taken from the list, that match the sound of the input
    
    Sample Output:
     Jones: Jonas, Johns, Saunas
     Winton: Van Damme
    
    
Limitations & Enhancements:
  
    1. The algorithm could be enhanced by adding rules for multi-letter sequences that produce a single sound such as: 
        GH could be replaced with H => When it doesn't start a word
        GN could be replaced with N 
        KN could be replaced with N
        PH could be replaced with F
        MP could be replaced with M => When it is followed by S, Z, or T
        PS could be replaced with S => When it starts a word
        PF could be replaced with F => When it starts a word
        TCH could be replaced with CH
        
        Source: http://creativyst.com/Doc/Articles/SoundEx1/SoundEx1.htm#Enhancements
    
'''
import sys
import re

def validateInput():
    '''
    Validating Input:
        1. must contain one or more names
        2. must contain an input file
       
        Returns: names, namesInFile
    '''
    namesInFile = []
    
    #Handling Input Error: No names given
    if len(sys.argv) < 2:
        print "**Error: No names were specified"
        quit()
    names = sys.argv[1:]
    
    #Handling Input Error: No input file given
    if not sys.stdin.isatty():
        pass
    else:
        print "**Error: No input file was specified"
        quit()
    
    #Getting list of names from file
    for line in sys.stdin.readlines():
        line = line.strip('\n')
        namesInFile.append(line)

    return names, namesInFile 

def getCode(name):
    '''
    Creates Code from names using the following algorithm:
        1. Ignore non-alphabetic characters
        2. After the first letter, any of the following letters are discarded: A, E, I, H, O, U, W, Y.
        3. Replace letters with numbers according to sets:
            0 => A,E,I,O,U
            1 => C,G,J,K,Q,S,X,Y,Z
            2 => B,F,P,V,W
            3 => D,T
            4 => M,N
            5 => L
            6 => R
            7 => H
        4. Any consecutive occurrences of equivalent letters (after discarding letters in step 2) are 
           considered as a single occurrence
           
    Returns: code
    '''
    name = name.lower()
    # 1. Strip non-alphabetic chars
    code = re.sub(r'\W*\d*', '', name)
   
    # Handling Input error. If the name contains only invalid characters
    if code == '':
        print '**Error: Near "',name,'". This is not a name'
        quit()
        
    # 2. Strip vowels,w,y from name after first letter
    chars = '[aeihouwy]'
    tmp = re.sub(chars, '', code[1:] )
    code = code[0]+tmp
    
    # 3. Replace letters with numbers according to sets
    set0 = '[aeiou]'
    set1 = '[cgjkqsxyz]'
    set2 = '[bfpvw]'
    set3 = '[dt]'
    set4 = '[mn]'
    set5 = '[l]'
    set6 = '[r]'
    set7 = '[h]'
    
    code = re.sub(set0, '0', code)
    code = re.sub(set1, '1', code)
    code = re.sub(set2, '2', code)
    code = re.sub(set3, '3', code)
    code = re.sub(set4, '4', code)
    code = re.sub(set5, '5', code)
    code = re.sub(set6, '6', code)
    code = re.sub(set7, '7', code)
    
    # 4. Discard double occurrences
    for i in range(len(code)):
        if i+1 != len(code) and code[i] == code[i+1]:
            # Discarding double occurrences and adding a symbol to end of string to avoid out of index error
            code = code[:i] + code[i+1:] + '%'
    
    code = code.strip('%')       
    return code
    
def findSimilar(code, namesInListCodes):
    '''
    Performs a search on the dictionary comparing the codes
    
    Returns: array of similar names
    '''
    result = []
    for nameInList, codeInList in namesInListCodes.iteritems():
        if(codeInList == code):
            result.append(nameInList)
    
    result = sorted(result)    
    return result
       
        
if __name__ == '__main__':
    
    #Get Input
    names, namesInFile = validateInput()
    
    namesCodes = {} 
    namesInListCodes = {}
    result = {}
    
    #Get codes from input File
    for name in namesInFile:
        namesInListCodes[name] = getCode(name)
    
    #Get code from names given at input and perform search
    for name in names:
        # Get code of name
        namesCodes[name] = getCode(name)
        # Find similar names
        result[name] = findSimilar(namesCodes[name], namesInListCodes)
        
    
    for name in result:
        final_string = name+': '
        for i in range(len(result[name])):
            if i == len(result[name])-1:
                final_string+=result[name][i]+'\n'
                break
            final_string += result[name][i]+', '
        
        
        print final_string 
    

    
