class graph:
    def __init__(self,nodes,edges):
        self.nodes = set(nodes)
        self.edges = set()
        for (a,b) in edges:
            self.addedge((a,b))

    def addnode(self,node):
        self.nodes.add(node)

    def addedge(self,edge):
        (a,b) = edge
        if(a in self.nodes and b in self.nodes and a != b and (b,a) not in self.edges):
            self.edges.add(edge)

    def DFS(self,source):
        self.intDFS(source,set(),0,True,tree(self.nodes,[]))

    def intDFS(self,source,visited,lvl,verbose,tree):
        verbose and print(lvl*"   "+source)
        visited.add(source)
        for (a,b) in self.edges:
            if(a == source and b not in visited):
                tree.addedge((a,b))
                self.intDFS(b,visited,lvl+1,verbose,tree)
            elif(b == source and a not in visited):
                tree.addedge((a,b))
                self.intDFS(a,visited,lvl+1,verbose,tree)
        return tree

    def gettree(self,source):
        return self.intDFS(source,set(),0,False,tree(self.nodes,[]))

class tree(graph):
    def addedge(self,edge):
        (a,b) = edge
        if(a in self.nodes and b in self.nodes and a != b and (b,a) not in self.edges):
            self.edges.add(edge)
        if(self.hascycle()):
            self.edges.remove(edge)

    class FoundCycleException(Exception): pass

    def hascycle(self):
        for n in self.nodes:
            try:
                self.searchcycle(n,self.edges,set())
            except self.FoundCycleException:
                return True
        return False


    def searchcycle(self,source,remainingedges,visited):
        visited.add(source)
        for (a,b) in remainingedges:
            if(a == source):
                if(b not in visited):
                    self.searchcycle(b,(remainingedges - {(a,b)}),visited)
                else: raise self.FoundCycleException()
            elif(b == source):
                if(a not in visited):
                    self.searchcycle(a,(remainingedges - {(a,b)}),visited)
                else: raise self.FoundCycleException()

    def printtree(self,source):
        print(source)
        self.intprinttree(source,self.edges,"")

    def intprinttree(self,source,remainingedges,prefix):
        neighbours = [(a,b) for (a,b) in remainingedges if(source==a or source==b)]
        if(len(neighbours)!=0):
            for i in range(len(neighbours)-1):
                a,b = neighbours[i]
                if(a == source):
                    print(prefix+"   |___"+b)
                    self.intprinttree(b,(remainingedges-set(neighbours)),prefix+"   |")
                elif(b == source):
                    print(prefix+"   |___"+a)
                    self.intprinttree(a,(remainingedges-set(neighbours)),prefix+"   |")
            a,b = neighbours[len(neighbours)-1]
            if(a == source):
                print(prefix+"   |___"+b)
                self.intprinttree(b,(remainingedges-set(neighbours)),prefix+"    ")
            elif(b == source):
                print(prefix+"   |___"+a)
                self.intprinttree(a,(remainingedges-set(neighbours)),prefix+"    ")


friendships = [("Tanso","Chiara"),("Tanso","Fede"),("Fede","Sofia"),("Tanso","Grosso"),("Grosso","Chiara")]
grafo = graph(["Tanso","Chiara","Fede","Sofia","Grosso","Ferry","Della"],friendships)
grafo.addedge(("Grosso","Ferry"))
grafo.addedge(("Della","Fede"))
grafo.addnode("Tanso")
print(grafo.nodes)
grafo.addedge(("qoijrvoiwm","Tanso"))
grafo.addnode("Costa")
grafo.addedge(("Della","Costa"))
print("DFS, source: Della")
grafo.DFS("Della")
print("DFS, source: Grosso")
grafo.DFS("Grosso")
albero = grafo.gettree("Tanso")
print("Tree ottenuto da DFS(Tanso), source: Tanso")
albero.printtree("Tanso")
print("Tree ottenuto da DFS(Tanso), source: Della")
albero.printtree("Della")
print("Tree ottenuto da DFS(Tanso), source: Grosso")
albero.printtree("Grosso")
albero = grafo.gettree("Della")
print("Tree ottenuto da DFS(Della), source: Tanso")
albero.printtree("Tanso")
print("Tree ottenuto da DFS(Della), source: Della")
albero.printtree("Della")
print("Tree ottenuto da DFS(Della), source: Grosso")
albero.printtree("Grosso")
