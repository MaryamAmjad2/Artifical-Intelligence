class Node :
 
    def __init__(self,state,parent,actions,cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.cost=cost
graph={
    'A' : Node('A',None,['B','E',"C"],None ),
    'B' : Node('B',None,['A', 'E',"D"],None ),
    'C' : Node('C',None,['F','G','A'],None ),
    'D' : Node('D',None,['E','B'],None ),
    'E' : Node('E',None,['A','B','D'],None ),
    'F' : Node('F',None,['C'],None ),
    'G' : Node('G',None,['C'],None ),}
def BFS():


    
    print(graph.keys())
    vi=[]
    q=[]
    n='A'
    goal="F"
    while q :
       vi.append(n)
       q.append(n)
       current=q.pop(0)
       for c in graph[current].actions:
           if c not in vi and c not in q:
               graph[c].parent=n
               if graph[c].state==goal :
                   return actionSequence(graph,n,goal)
               q.append(c)
def actionSequence (graph,n,goal):
    solution=[goal]
    currentparent=graph[goal].parent
    while currentparent!= None :
        solution.append(currentparent)
        currentparent=graph[currentparent].parrent
    solution.reverse()
    return solution
    
solution =BFS()
print(actionSequence (graph,'B','F'))

print(solution)
           
       
