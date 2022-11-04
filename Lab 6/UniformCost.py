class Node :

    def __init__(self,state,parent,actions,cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.cost=cost
import math
def findMIn(front):
    minv=math.inf
    node=''
    for i in front:
        if(minv>front[i][1]):
           minV=front[i][1]
           node=i
    return node
def actionsequence(graph,inital,goal):
    sol=[goal]
    cp=graph[goal].parent
    while(cp !=None):
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol
def UCS():
    inital="C"
    goal="B"
    graph={'A': Node("A",None,[("B",6),('C',9),("E",1)],0),
           'B': Node("B",None,[("A",6),('D',3),("E",4)],0),
           'C': Node("C",None,[("A",9),('F',2),("G",3)],0),
           'D': Node("D",None,[("B",3),('E',5),("F",7)],0),
           'E': Node("E",None,[("A",1),('B',4),("D",5),('F',6)],0),
           'F': Node("F",None,[("C",2),('E',6),("D",7)],0),
           'G': Node("G",None,[("C",3)],0)}
    front=dict()
    front=[inital]
    exp=[]
    while(len(front)!=0):
        cnode=findMIn(front)
        del front[cnode]
        if(graph[cnode].state==goal):
            return actionsequence(graph,inital,goal)
        exp.append(cnode)
        for child  in graph[cnode].actions:
            ccost=[child][1]+graph[cnode].cost
            if child[0] not in front and child[0] not in exp:
                graph[child[0]].parent=cnode
                graph[child[0]].cost=ccost
                front[child[0]]=(graph[child[0]].parent,graph[child[0]].cost)
            elif child[0] in front:
                if front[child[0]][1]<ccost:
                    graph[child[0]].parent=front[child[0]][0]
                    graph[child[0]].cost=front[child[0]][1]
                else:
                    front[child[0]]=(cnode,ccost)

                    graph[child[0]].parent=front[child[0]][0]
                    graph[child[0]].cost=front[child[0]][1]
        
sol=UCS()
print(sol)
                      
