#! /usr/bin/env python 
#coding: utf-8

import heapq

class frontier():

	def __init__(self,maxSize=0):
		self.maxSize = maxSize
		self.list=[]	
	
	def __contains__(self,key):
 		return key in self.list		
 	
 	def empty(self):
 		return len(self.list)==0
 		
 	def get(self):
 		return heapq.heappop(self.list) 
 	
 	def put(self,element):
 		heapq.heappush(self.list,element)
 	
 	#Atualiza a lista de prioridades se um no com menor custo do caminho for encontrado
	def updateCost(self,node):
		for index, item in enumerate(self.list):
			if(item==node):
				if(node.pathCost<item.pathCost):
					self.list[index]=node
 	
	def __str__(self):
		string=""
		string+=",".join(str(e) for e in self.list)
		return string
