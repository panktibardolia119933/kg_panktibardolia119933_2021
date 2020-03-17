'''DETERMINE WHETHER ONE-TO-ONE CHARACTER MAPPING EXISTS 
FROM ONE STRING S1 TO S2

SOLUTION BY PANKTI SATISHKUMAR BARDOLIA
CONTACT pbardolia@albany.edu'''

#IMPORTS
import sys

def oneToOne(string1, string2):
	#CONDITION ONE
	#NO OF ELEMENTS IN DOMAIN SHOULD BE LESS THAN OR EQUAL TO NO OF CODOMAIN
	#RETURNS FALSE IF LENGTH(STRING1)> LENGTH(STRING2)
	if len(string1)> len(string2):
		return "false"
	else:
		return "true"

#MAIN
def main():
	#CMDLINE SYS ARGS
	string1= str(sys.argv[1])
	string2= str(sys.argv[2])
	
	#ONE-TO-ONE
	result=	oneToOne(string1, string2)
	print(result)


if __name__ == "__main__":
    main()

