"""
Algorithm designed by Izzet Memmedov
Problem : Huffman
""" 
import heapq

sj=int(input("CODING:1 \nDECODİNG:2\ninput:"))

if sj==1:
    maps={}
    class node:
        def __init__(self, say, simbol, left=None, right=None):
            self.say = say
            self.simbol = simbol
            self.left = left
            self.right = right
            self.huff = ''
            
        def __lt__(self, nxt):
            return self.say < nxt.say
            
    def printNodes(node, val=''):
        qimet = val + str(node.huff)
        global maps
        if(node.left):
            printNodes(node.left, qimet)
        if(node.right):
            printNodes(node.right, qimet)
        if(not node.left and not node.right):
            print(f"{node.simbol} -> {qimet}")
            maps[node.simbol]=qimet


    
    info=input("input your string:")
    dic={}
    for keys in info:
        dic[keys]=dic.get(keys,0)+1
    dic=sorted(dic.items(),key=lambda x:x[1])

    nodes=[]
    for i in range(len(dic)):
        heapq.heappush(nodes,node(dic[i][1],dic[i][0]))
    
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
    
        left.huff = 1
        right.huff = 0
        newNode = node(left.say+right.say, left.simbol+right.simbol, left, right)
    
        heapq.heappush(nodes, newNode)
    

    printNodes(nodes[0])

    maplist=[]
    for i in info:
        maplist.append(maps[i])
    maplist=''.join(maplist)
    print(f"your code is {maplist}")
else:
    dic={}

    NoS=int(input("input number of symbols:"))

    for i in range(NoS):
        key=input(f"input {i+1}th symbol:")
        code=input("input code:")
        dic[code]=key
    info=input("input your information:")
    info=[*info]
    string=""
    cvb=""
    while len(info)!=0:
        string=string+str(info[0])
        info.pop(0)
        if string in dic.keys():
            cvb=cvb+dic[string]
            string=""

    print(f"your string is {cvb}")
