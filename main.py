'''DETERMINE WHETHER ONE-TO-ONE CHARACTER MAPPING EXISTS 
FROM ONE STRING S1 TO S2

SOLUTION BY PANKTI SATISHKUMAR BARDOLIA
CONTACT pbardolia@albany.edu'''

#IMPORTS
import sys

#ONE-TO-ONE
def oneToOne(string1, string2):
	#CONDITION ONE
	#NO OF ELEMENTS IN DOMAIN SHOULD BE LESS THAN OR EQUAL TO NO OF CODOMAIN
	#RETURNS FALSE IF LENGTH(STRING1)> LENGTH(STRING2)
	if len(string1)> len(string2):
		return "false"
	#CHECK IF BOTH THE STRINGS HAVE SINGLE ONE TO ONE RELATION	
	else:
		hashMap= dict()
		i=0
		while i< len(string1):
			#CREATE HASHMAP
			if string1[i] not in hashMap:
				hashMap[string1[i]]= string2[i]
			else:
				#NOT MAPPED TO SAME ELEMENT				
				if hashMap[string1[i]] != string2[i]:
					return "false"
			i=i+1
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

