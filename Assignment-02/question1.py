# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 17:39:05 2021

@author: sreek
"""
import codedMDP

def runMDP():    
    plan = codedMDP.MDP()
    """ for question B"""
    plan.valueIteration(1, 0)
    
    """ uncomment for question D"""
    # plan.valueIteration(0.8,0)
    """ uncomment for question E"""
    # plan.valueIteration(0.2, 0)
    """ uncomment for question F """
    # plan.valueIteration(0.9, 0.2)
    
    """"Path planner for all questions"""
    plan.path(1,1,4)
         
runMDP()                
                