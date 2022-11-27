from thlr_automata import *

Automata = ENFA([0,1,2,3,4,5,6],[0,3,4],[5],["a","b","c"],[(0,"a",1),(1,"b",2),(2,"c",5),(3,"b",3),(4,"c",4),(0,"a",0),(3,"a",6),(6,"c",5),(4,"c",5)])
Automata.export("A")


print("get accessible states")
#Q3
def get_accessible_states(A,origin):
	incoming = []
	tested = []
	alphabet = A.alphabet
	incoming.append(origin)
	tested.append(origin)
	#print("the original status are")
	#print(incoming)
	#print(tested)
	while (incoming!=[]):
		temp = incoming.pop()
		for letter in alphabet:
			successor = A.get_successors(temp, letter)
			while(successor!=set()):
				i = 0
				temp2 = successor.pop()
				while (i<len(tested) and temp2!= None):
					if (temp2 == tested[i]):
						temp2 = None
					i+=1
				if(temp2!=None and i==len(tested)):
					incoming.append(temp2)
					tested.append(temp2)
					#print("the list of successor is")
					#print(tested)
					#print("the list of things to test is")
					#print(incoming)
	return tested			
			

print(get_accessible_states(Automata,0))	

print("is accessible")
def is_accessible(A,state):
	res = False
	for start in A.initial_states:
		temp = get_accessible_states(A, start)
		for futur in temp:
			if (state == futur):
				res == True
	return res
	
print(is_accessible(Automata,0))

print("is co accessible")
def is_co_accessible(A,state):
	successor = get_accessible_states(A,state)
	res = False
	for ends in A.final_states:
		print("l'etat de fin analyse est")
		print(ends)
		for nexts in successor:
			print("le successeur analyse est")
			print(nexts)
			if (ends == nexts):
				res = True
				
	return res 
	
print(is_co_accessible(Automata,0))
