#! /usr/bin/env python 
#coding: utf-8

from Frontier import frontier as Frontier
from State import state
from Node import node
from Problem import problem

#Busca de custo uniforme

#Cria um no filho
#problem - Problema a ser resolvido
#parent - pai do no a ser criado
#action - String que representa a ação que vai ser executada no pai para que o filho seja gerado
#Return o no filho
def childNode(problem,parent,action):
	return node(
		problem.result(parent.state,action),
		parent,
		action,
		parent.pathCost+problem.stepCost(parent.state,action))
	

#Imprime a sequencia de estado que leva do estado incial a solução
def solution(node):
	resp=''
	if(node.parent is None):
		resp+=str(node.state)
	else:
		resp+=solution(node.parent)+" "+str(node.state)
	return resp

def AStar(problem):
	nod = problem.initialNode
	frontier=Frontier()
	frontier.put(nod)
	explored = set() 
	while(True):
		if(frontier.empty()):
			return "FAILURE"
		nod = frontier.get()
		if(problem.goalTest(nod.state)):
			return solution(child)
		explored.add(nod.state)
		for action in problem.actions(nod.state):
			child=childNode(problem,nod,action)
			if (child.state not in explored) or (child not in frontier):
				if(problem.goalTest(child.state)):
					return solution(child)
				frontier.put(child)
			frontier.updateCost(child)#Atualiza a fila se o child ja foi explorado e encontrou um child de custo maior 
#Main
problem=problem()
print AStar(problem)
