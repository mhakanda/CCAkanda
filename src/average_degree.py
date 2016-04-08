'''
Python 3 (more specifically 3.4) is used to run the program. Running with Python 2 will genrate errors.
This program reads twitters sequentially from a file and extract corresponding time and hastags.
The information is used to form hashtag graph and then compute and write average degree of vertex (adv) in file.
As more twitters come in, graph (maintaing it in a 60 sec window) changes and so the adv.
April 08, 2016, Mohammad H Akanda (mhakanda1@yahoo.com)
'''
import json, itertools, math, sys
from datetime import datetime
from collections import defaultdict
from itertools import chain
#MyGraph class: Add, remove nodes and computing average degree of vertex in a Twitter hashtag graph
class MyGraph():
    def __init__(self):
        self._Mygraph = defaultdict(list)
    def add(self, nodes):
        w2=itertools.permutations(set(nodes),2)
        for k,v in w2:
            self._Mygraph[k].append(v)
    def remove(self, nodes):
        w4=itertools.permutations(set(nodes),2)
        for k,v in w4:
            self._Mygraph[k].remove(v)
        if not(all(self._Mygraph.values())):
            for ii in [jj for jj in self._Mygraph.keys() if len(self._Mygraph[jj])==0]:
                self._Mygraph.pop(ii)
    def avg(self):
        v1=[len(set(v)) for v in self._Mygraph.values()]
        try:
            av=sum(v1)/len(v1)
            return "%.2f" % (math.floor(av*100)/100)
        except ZeroDivisionError:
            av=0
            return "%.2f" % av
#-------------------------------------------------
def main():
    r1 = open(sys.argv[1],'r')
    w1 = open(sys.argv[2],'w')
    d,g=defaultdict(list),MyGraph()#initialization
    while 1:
        p1=r1.readline()
        if len(p1)==0:#It means EOF
            break
        else:
            j1=json.loads(p1)
            if ('created_at' in j1.keys() and 'entities' in j1.keys()):
                aa=datetime.strptime(j1['created_at'],'%a %b %d %H:%M:%S %z %Y')#Must need python3 to make datetime object
                bb=[i['text'] for i in j1['entities']['hashtags']]#Hastags extraction
                d[aa].append(bb)# d is the dictionary of of datetime and hashtags 
                b1=bb #To be added to the graph
                q1=[]# To be removed from the graph
                #Updating d with exclusive 60 sec window
                if (max(d.keys())-min(d.keys())).total_seconds()>=60:#Out of window condition
                    pp=[i for i in d.keys() if (max(d.keys())-i).total_seconds()>=60]#removing index
                    q1=list(chain.from_iterable([d[j] for j in pp]))# To be removed from the graph
                    #Updating d
                    for j in pp:
                        d.pop(j)
                #updating the Graph g with 60 sec window
                if len(b1)>=2:
                    g.add(b1)
                for j in q1:
                    if len(j)>=2:
                        g.remove(j)
                w1.write(g.avg()+'\n')#Get the average degree and write
    r1.close()
    w1.close()
if __name__ == "__main__":
    main()
