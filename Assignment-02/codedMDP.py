# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 11:59:30 2021

@author: sreek
"""
"""Data structure for each state"""

class State:
    def __init__(self, x, y, d, action, reward, value):
        
        self.x = x
        self.y = y
        """(x,y) -> current tile in coordinate system notation (1->5)"""
        self.d = d
        """d -> facing direction; 1-> N; 2-> S; 3 -> W; 4 -> E;"""
        self.action = action
        """a -> next action"""
        self.reward = reward
        self.value = value

    def createState(x, y, d, action, reward, value):
        return State(x, y, d, action, reward, value)

# actionList = ["up", "doubleup", "left", "right"]

class MDP:
    def __init__(self):
        """Initialize a list of all the states - 100 in total"""
        self.initialStateList = self.initialize()
        
    def initialize(self):
        """Zeroth iteration/ initial state"""
        initialState = list()
        for x in range(1,6):
            for y in range(1,6):
                for d in range(1,5):
                    # """ For exit state, reward is 100"""
                    if (x == 5 and y == 5):
                        initialState.append(State.createState(x, y, d, None, 100, 0))
                        
                    # """for game over state, reward is -1000"""
                    elif (x == 4 and y == 4):
                        initialState.append(State.createState(x, y, d, None, -1000, 0))
                        
                    # """for all other states, reward is 0 initially"""
                    else:
                        initialState.append(State.createState(x, y, d, None, 0, 0))
                        
        return initialState
    
    def getActionList(self,currentState):
        """Generate list of possible actions"""
        actions = []  
        for action in range(1,5):
            if self.checkAction(currentState, action) == True:
                actions.append(action)     
        return actions    
        
    def checkAction(self, state, action):
        """Checks if the action is possible for that particular state"""
        """Initial check condition"""
        check = False 
        x = state.x
        y = state.y
        d = state.d
        
        # """Turning left in place"""
        if action == 3: 
            check=True
        
        # """Turning right in place"""        
        if action == 4:
            check=True
        
        # """Moving one step forward"""    
        if action == 1: 
            
            # """When facing north"""
            if d == 1:
                if (y == 5):
                   check = False
                elif (x == 5 and y == 3):
                    check = False
                elif (x == 3 and y == 1):
                    check = False
                elif (x == 2 and y == 1):
                    check = False
                else:
                    check = True

            # """When facing south"""                            
            if d == 2: 
                if (y == 1):
                   check = False
                elif (x == 5 and y == 4):
                    check = False
                elif (x == 2 and y == 4):
                    check = False
                elif (x == 3 and y == 3):
                    check = False
                else:
                    check = True
             
            # """When facing west"""        
            if d == 3: 
                if (x == 1):
                   check = False
                elif (x == 3 and y == 5):
                    check = False
                elif (x == 3 and y == 3):
                    check = False
                elif (x == 4 and y == 2):
                    check = False
                else:
                    check = True
                    
            # """When facing east"""                            
            if d == 4: 
                if (x == 5):
                    check = False
                elif (x == 1 and y == 2):
                    check = False
                elif (x == 1 and y == 3):
                    check = False
                elif (x == 2 and y == 5):
                    check = False
                else:
                    check = True          
                    
        # """Moving two steps forward""" 
        if action == 2: 
            
            # """When facing east"""  
            if d == 4: 
                if (x == 4 or x == 5):
                    check = False
                elif (x == 1 and y == 2):
                    check = False
                elif (x == 2 and y == 5): 
                    check = False
                elif (x == 1 and y == 5):
                    check = False
                elif (x == 1 and y == 3):
                    check = False
                else:
                    check = True

            # """When facing north"""                    
            if d == 1: 
                if (y == 5 or y == 4):
                   check = False
                elif (x == 2 and y == 1):
                    check = False
                elif (x == 3 and y == 1):
                    check = False
                elif (x == 5 and y == 2):
                    check = False
                elif (x == 5 and y == 3):
                    check = False
                else:
                    check = True
            
            # """When facing West"""                     
            if d == 3:
                if (x == 1 or x == 2):
                   check = False
                elif (x == 4 and y == 2):
                    check = False
                elif (x == 4 and y == 3):
                    check = False
                elif (x == 3 and y == 3):
                    check = False     
                elif (x == 5 and y == 2):
                    check = False  
                elif (y == 5 and x != 5):
                   check = False
                else:
                    check = True
                    
            # """When facing south"""          
            if d == 2: 
                if (y == 1 or y == 2):
                   check = False
                elif (x == 2):
                    check = False
                elif (x == 3 and y == 3):
                    check = False
                elif (x == 5 and y == 4):
                    check = False
                elif (x == 5 and y == 5):
                    check = False
                elif (x == 3 and y == 4):
                   check = False
                else:
                    check = True
            
        return check
    
 
    def getState(self, state, action):
        """Takes state and action. Performs the action. Returns the changed state orientation and position values."""
        x = state.x
        y = state.y
        d = state.d
        # reward = state.reward
        # newState = State.createState(x, y, d, action, reward, 0) 
        
        if self.checkAction(state, action) == True:
            # """What should happen when we move one step forward?"""
            if action == 1:
                if d == 1: 
                    y = y+1
                elif d == 2: 
                    y = y-1
                elif d == 3: 
                    x = x-1
                else: 
                    x = x+1
            
            # """What should happen when we move two steps forward?"""
            if action == 2:
                if d == 1: 
                    y = y+2
                elif d == 2: 
                    y = y-2
                elif d == 3: 
                    x = x-2
                else: 
                    x = x+2

            # """What should happen when we turn left?"""
            if action == 3: 
                if d == 1: 
                    d = 3
                elif d == 2: 
                    d = 4
                elif d == 3:
                    d = 2
                else:
                    d = 1

            # """What should happen when we turn right?"""
            if action == 4: 
                if d == 1: 
                    d = 4
                elif d == 2: 
                    d = 3
                elif d == 3:  
                    d = 1
                else: 
                    d = 2
            
        return x,y,d 
    
            
    def probableAction(self, state, action, noise):
        
        """ probableAction function for the MDP """
        plist = list();
        
        # """ If noise is zero, probability of taking a chosen action is 1"""
        if noise == 0:
            P = 1
            x,y,d = self.getState(state, action)
            plist = [P, x , y, d, action]
        
        # """ If noise is not zero, probability of taking a chosen action is 1-noise"""
        else:
            actionList = self.getActionList(state)
            P = 1-noise
            # """ The rest of the probability is split between the possible actions"""
            P1 = noise/(len(actionList)-1)
            # """ creating a list that contains probability, state and action"""
            for actions in actionList:
                if action != actions:
                    x,y,d = self.getState(state, actions)
                    plist.append([P1, x , y, d, actions])                    
                else:
                    x,y,d = self.getState(state, action)
                    plist.append([P, x , y, d, action])
            
        return plist        
    
    
    def cost(self, action):
    # """ Immediate cost/reward for making the action"""
        if action == 1:
            cost = -1.5
        elif action == 2:
            cost = -2
        elif action == 3:
            cost = -0.5
        elif action == 4:
            cost = -0.5
        return cost    

    
    def valueIteration(self, gamma, noise):
        """ Running value iteration for 100 iterations"""
        iterations = 100
        i = 1
        # epsilon = 0.001
        """ alternate list to store updated values"""
        updatedList= list()
        while (i<=iterations):
            updatedList.clear()
            if i<11:
                print("Iteration ", i)
            for state in self.initialStateList:
                
                aList = self.getActionList(state)
                val_dic = {}
                
                for action in aList:
                    val = 0
                    # """ When noise is zero, probability is not required"""
                    if noise == 0:
                        x,y,d = self.getState(state, action)
                        for stateIte in self.initialStateList:
                            if x == stateIte.x and y == stateIte.y and d == stateIte.d:
                                reward = self.cost(action)
                                val = (reward+stateIte.reward) + gamma * stateIte.value
                                val_dic[action]=val
                                
                    # """ When noise is not zero, probability function is required"""           
                    else:
                        for possibility in self.probableAction(state, action, noise):
                            reward = self.cost(possibility[4])
                            for stateIte in self.initialStateList:
                                if possibility[1] == stateIte.x and possibility[2] == stateIte.y and possibility[3] == stateIte.d:                                    
                                    val += possibility[0]*((reward+stateIte.reward) + gamma * stateIte.value)
                        val_dic[action]=val
                                            
                
                bestAction = max(val_dic, key=val_dic.get)
                value = val_dic[bestAction]
                
                if (state.x == 5 and state.y == 5) or (state.x ==4 and state.y ==4): 
                    # """Value for terminal sattes should not be updates"""
                    updatedList.append(State.createState(state.x, state.y, state.d, bestAction, state.reward, state.value))
                else:
                    # """The updates states are appended to the alternate list"""
                    updatedList.append(State.createState(state.x, state.y, state.d, bestAction, state.reward, value))
                
                if i<11:                 
                    print("state", (state.x,state.y,state.d), "V=",state.value, "; Best action is A",bestAction)
            # """ The state is updated with the updated values"""
            self.initialStateList.clear()
            self.initialStateList = updatedList.copy()
            i=i+1
            
        return 0
    
    def path(self, x, y, d):
        # """ Generates a path from an initial state to the goal """
        print("Generating path from initial state to the goal")        
        for state in self.initialStateList:
            if state.x == x and state.y == y and state.d == d:
                break
        print(state.x,state.y,state.d,state.action)
        path = [[state.x,state.y,state.d,state.action]] 
        
        while True:
            xn,yn,dn = self.getState(state,state.action)
            for stateIte in self.initialStateList:
                if (xn == stateIte.x and yn == stateIte.y and dn == stateIte.d):
                    break
            path.append([stateIte.x,stateIte.y,stateIte.d,stateIte.action])
            state = stateIte 
            print(stateIte.x,stateIte.y,stateIte.d,stateIte.action)
            if (state.x == 5 and state.y == 5):
                break

        print('Path generated')
        return 
    

# initialState = []            
# # init = MDP.initialize(initialState)
# init = MDP()
# # run = MDP.act(init,actionList)

# for object in init.initialState:
#     print(object.x, object.y, object.d, object.value, object.reward)
    


# def value_iteration(mdp, epsilon=0.001):

#     U1 = {s: 0 for s in mdp.states}
#     R, T, gamma = mdp.R, mdp.T, mdp.gamma
#     while True:
#         U = U1.copy()
#         delta = 0
#         for s in mdp.states:
#             U1[s] = R(s) + gamma * max(sum(p * U[s1] for (p, s1) in T(s, a))
#                                        for a in mdp.actions(s))
#             delta = max(delta, abs(U1[s] - U[s]))
#         if delta <= epsilon * (1 - gamma) / gamma:
#             return U
            

    
    


# class MDP:
#     def __init__(self, init, direction, actionList, terminals, probabillityActions = {}, reward = None, states = None, gamma=1):
#         self.init = init
#         self.direction = direction
        
        
#         self.terminals = terminals
#         self.probabillityActions = probabillityActions
#         self.gamma = gamma
#         if reward:
#             self.reward = reward
#         else:
#             self.reward = {s : 0 for s in self.states}
           

# class GridWorld(MDP):
#     def __init__(self, grid, terminals, init=(0, 0), direction=1, gamma=1):
#         grid.reverse()
#         reward = {}
#         states = set()

    # def value_iteration(self, state, epsilon=0.001):  
    #     self.state = state;
    #     for s in self.state:
    #         for a in actionList:
    #             s1 = list.append(self.act(s,a))

    # def act(self, currentState, action):
    #     if self.a == "up":
        