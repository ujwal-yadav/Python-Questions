class graph:
    def __init__(self,edges):
        self.edges=edges
        
        self.dict={}
        
        for s,e in routes:
            if s in self.dict:
                self.dict[s].append(e)
            else:
                self.dict[s]=[e]
        print(self.dict)

    def getPath(self,s,e,path=[]):
        path=path+[s]
        if s==e:
            return [path]
        
        if s not in self.dict:
            return []
        paths=[]   
        for node in self.dict[s]:
            if node not in path:
                new_path=self.getPath(node,e,path)
                for i in new_path:
                    paths.append(i)
                
        return paths
        
               
routes=[
    ("Mumbai","Paris"),
    ("Mumbai","Dubai"),
    ("Paris","Dubai"),
    ("Paris","New York"),
    ("Dubai","New York"),
    ("New York","Toronto")
    ]
    
r=graph(routes)

x=r.getPath("Mumbai","New York")
print("Possible Paths are : ",x)
