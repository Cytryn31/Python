This is an implementation of the Phonetic Search algorithm
===========================================================

Author: Edoardo Foco
Date: 19/01/2014

------------
Description
------------

The algorithm is designed to return a list of phonetically similar surnames to the ones inputted by the user.

--------------------
System Requirements
--------------------

Any operating system with a base installation of Python 2.7
It may be required to add python to the system path

-------------
Requirements
-------------

1. The program shall read a list of surnames from standard input.
2. The command-line arguments to the program shall be one or more surnames.
3. For each of those surnames the program shall print out all the names in the input list that match those on the command-line.

--------------
The Algorithm
--------------

1. All non-alphabetic characters are ignored2. Word case is not significant3. After the first letter, any of the following letters are discarded: A, E, I, H, O, U, W, Y.4. The following sets of letters are considered equivalent	A,E,I,O,U	C,G,J,K,Q,S,X,Y,Z	B,F,P,V,W	D,T	M,N	All others have no equivalent5. Any consecutive occurrences of equivalent letters (after discarding letters in step 3) are considered as a single occurrence

------
Usage
------

The input must contain the following:
    -surnames : one or more surnames separated by a space. If these contain non-alphabetic characters, the characters will be ignored.
    -input file : a file containing a list of surnames separated by a new line

Sample Input from terminal (assuming python is in the system path):  
    
	$python Program.py Jones Winton < surnames.txt

--------
Testing
--------

Tested on:
	1. Mac OSX
	2. Debian 5
	3. Windows 7

1. User Input - Some tests have been run to verify the correct exception handling of the user input such as inserting only invalid characters or not specifying surnames or the input file. The program is able to handle incorrect user input but the command line sometimes stops the program from executing because it interprets command line arguments.
	E.g. (Using Mac OSX)
	$python Program.py winton' < surname.txt -> Fails because the command line interprets ' as a command

2. Algorithm Results - The algorithm performs correctly but it should be enhanced to return more accurate results. 
	The tests were performed on the following files:
		i. surnames.txt -> the given set of surnames contained in the specification
		ii. FemaleNames-4725entries.txt -> containing 4275 entries of female names
		iii. uk_surnames -> containing 3704 common uk surnames

-----------------------------
Limitations and Enhancements
-----------------------------
  
1. The algorithm could be enhanced by adding rules for multi-letter 	sequences that produce a single sound such as: 
        GH could be replaced with H => When it doesn't start a word
        GN could be replaced with N 
        KN could be replaced with N
        PH could be replaced with F
        MP could be replaced with M => When it is followed by S, Z, or T
        PS could be replaced with S => When it starts a word
        PF could be replaced with F => When it starts a word
        TCH could be replaced with CH
        
Source: http://creativyst.com/Doc/Articles/SoundEx1/SoundEx1.htm#Enhancements
