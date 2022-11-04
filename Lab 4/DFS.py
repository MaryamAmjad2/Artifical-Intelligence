class Node :
 
    def __init__(self,state,parent,actions,cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.cost=cost

def actionSequence(graph,inital,goal):
    sol=[goal]
    cp=graph[goal].parent
    while cp!=None:
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol


def DFS():
    inital='A'
    goal='D'
    graph={
        'A' : Node('A',None,['B','E',"C"],None ),
        'B' : Node('B',None,['D', 'E',"A"],None ),
        'C' : Node('C',None,['A','F','G'],None ),
        'D' : Node('D',None,['B','E'],None ),
        'E' : Node('E',None,['A','B','D'],None ),
        'F' : Node('F',None,['C'],None ),
        'G' : Node('G',None,['C'],None ),}
    front =[inital]
    exp=[]
    while(len(front)!=0):
         cNode=front.pop(len(front)-1)
         print (cNode)
         exp.append(cNode)
         cChild=0
         
         for i in graph[cNode].actions :
            if i not in front and i not in exp : 
                graph[i].parent==cNode
                if graph[i].state==goal:
                    print(exp)
                    return actionSequence(graph,inital,goal)
                cChild=cChild+1
                front.append(i)
         if cChild==0:
            del exp[len(exp)-1]

sol=DFS()
print(sol)
          


    




