#! /usr/bin/env python 
#coding: utf-8

class state:

	def __init__(self,sName):
			self.sName=sName
		
	def __eq__(self,other):
		return (self.sName==other.sName)
	
	def __ne__(self,other):
		return not(__eq__(self,other))
	
	def __hash__(self):
		return hash(self.sName)
		
	def __str__(self):
		return str(self.sName)

