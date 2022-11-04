'''
0,0,0,0,0,GOAL,0,0
0,J,K,L,M,N,O,0
0,I,0,0,0,0,P,0
0,H,0,START,0,Q,R,0
0,G,0,A,0,0,S,0
0,F,0,B,0,T,U,0,
0,E,D,C,V,W,X,0,
0,0,0,0,0,0,0,0
'''
   

class Node :

    def __init__(self,state,parent,actions,cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.cost=cost  
def BFSCost():
    inital="START"
    goal="GOAL"
    
    graph={
        'START' : Node('START',None,['A'],[] ),
        'A' : Node('A','START',['START','B'],[]),
        'B' : Node('B','A',['A','C'],[] ),
        'C' : Node('C','B',['B','D','V'] ,[]),
        'D' : Node('D','C',['C','E'],[] ),
        'E' : Node('E','D',['D','F'],[] ),
        'F' : Node('F','E',['E','G'],[] ),
        'G' : Node('G','F',['F','H',],[] ),
        'H' : Node('H','G',['G','I'],[] ),
        'I':Node('I','H',['H','J'],[]),
        'J':Node('J','I',['I','K'],[]),
        'K':Node('K','J',['J','L'],[]),
        'L':Node('L','K',['K','M'],[]),
        'M' : Node('M','L',['N','L'],[120,75] ),
        'N' : Node('N','M',['GOAL','M','0'],[138,146] ),
        'O' : Node('O','N',['N','P'],[86] ),
        'P' : Node('P','O',['O','R'],[142,92] ),
        'Q' : Node('Q','R',['R'],[92,87] ),
        'R' : Node('R','P',['Q','S'],[]),
        'S' : Node('S','R',['R','U'],[] ),
        'T' : Node('T','U',['W','U'],[] ),
        'U' : Node('U','S',['S','T','X'],[] ),
        'V' : Node('V','C',['C','W'],[] ),
        'W' : Node('W','T',['V','T','X'],[] ),
        'X' : Node('X','U',['W','U'],[] ),
        'GOAL' : Node('GOAL','N',['N'],[] ),
        }
    front=[inital]
    exp=[]
   
    while(len(front)!=0) : 
          cNode=front.pop(0)
          exp.append(cNode)
          
          if cNode==goal:
              break
          for i in graph[cNode].actions :
              if i not in front and i not in exp : 
                  graph[i].parent==cNode
                  if graph[i].state==goal:
                      return actionSequence(graph,inital,goal)
                  front.append(i)
def actionSequence(graph,inital,goal):
    sol=[goal]
    cp=graph[goal].parent
    while cp!=None:
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol
sol=BFSCost()
print(sol)
