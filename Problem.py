#! /usr/bin/env python 
#coding: utf-8

from State import state
from Node import node

from Edge import edge

class problem:
	
	def __init__(self):
		self.graph = {
		'A': [edge('B',5),edge('C',4)],
		'B': [edge('A',5),edge('F',10)],
		'C': [edge('A',4),edge('D',8)],
		'D': [edge('C',8),edge('F',2),edge('E',3)],
		'E': [edge('D',3),edge('G',2)],
		'F': [edge('B',10),edge('D',2),edge('G',3),edge('H',8)],
		'G': [edge('E',2),edge('F',3),edge('H',1)],
		'H': [edge('G',1),edge('F',8)]}
	
		self.meta=state('H')
		self.initialNode = node(state('A'),None,None,0)

	#Checa se o node tem o estado meta 
	#State - Estado recebido
	#Return true se o no tem o estado meta senão retorna false
	def goalTest(self,state):
		return(state==self.meta)
			
	#Metodo que cria uma lista de action que um no pode realizar 
	#State - Estado recebido
	#Return a lista de ações possiveis de ser realizado por aquele state
	def actions(self,state):
		l=self.graph[state.sName]
		resp=[]
		for i in range(len(l)):
			resp.append(l[i].sDestiny)
		return resp
			
	#Cria um novo estado baseado nos parametros dados
	#stat - Estado que vai sofrer a ação
	#action - Ação que vai ser executada no state
	#Return um novo estado resultado da ação de action aplicada no estado state
	def result(self,stat,action):
		return state(action)
	
	#state - Estado que vai ter o custo calculado
	#action - Ação que vai ser executada no state
	#Return o inteiro que representa o custo de fazer essa ação nesse estado
	def stepCost(self,state,action):
		paths=self.graph[state.sName]#state.SName - cidade origem
		for city in paths:
			if city.sDestiny==action:
				return city.iCost
		return 	0
	
	
