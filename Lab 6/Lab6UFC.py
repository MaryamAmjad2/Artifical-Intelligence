class Node :

    def __init__(self,state,parent,actions,cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.cost=cost
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
def UFC():
    inital="Arad"
    goal="Neamt"
    graph={
        'Oradea' : Node('Oradea',None,['Zerind','Sibiu'],[71,151] ),
        'Zerind' : Node('Zerind',None,['Arad', 'Oradea'],[75,71 ]),
        'Arad' : Node('Arad',None,['Zerind','Timisoara','Sibiu'],[75,118,140] ),
        'Sibiu' : Node('Sibiu',None,['Fagaras','Rimnicu Vilcea','Oradea','Arad'],[99,80,151,140] ),
        'Fagaras' : Node('Fagaras',None,['Sibiu','Bucharest'],[99,211] ),
        'Bucharest' : Node('Bucharest',None,['Fagaras','Pitesti','Urziceni','Giurgiu'],[211,101,85,90] ),
        'Pitesti' : Node('Pitesti',None,['Rimnicu Vilcea','Bucharest','Craiova'],[97,101,138] ),
        'Urziceni' : Node('Urziceni',None,['Bucharest','Hirsova','Vaslui'],[85,98,142] ),
        'Hirsova' : Node('Hirsova',None,['Urziceni','Eforie'],[98,86] ),
        'Timisoara':Node('Timisoara',None,['Lugoj','Arad'],[111,118]),
        'Lugoj':Node('Lugoj',None,['Mehadia','Timisoara'],[70,111]),
        'Mehadia':Node('Mehadia',None,['Drobeta','Lugoj'],[75,70]),
        'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,['Sibiu','Pitesti'],[70,111]),
        'Drobeta' : Node('Drobeta',None,['Craiova','Mehadia'],[120,75] ),
        'Craiova' : Node('Craiova',None,['Pitesti','Rimnicu Vilcea'],[138,146] ),
        'Eforie' : Node('Eforie',None,['Hirsova'],[86] ),
        'Vaslui' : Node('Vaslui',None,['Urziceni','Iasi'],[142,92] ),
        'Iasi' : Node('Iasi',None,['Vaslui','Neamt'],[92,87] ),
        'Giurgiu' : Node('Giurgiu',None,[],[]),
        'Neamt' : Node('Neamt',None,[],[] ),
        }
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
      
sol=UFC()
print(sol)
                      
