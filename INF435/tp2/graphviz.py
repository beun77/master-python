import os

def showShortestPath (pathList):
	"""create the file karate.png which
    	is a graphical representation of 
    	karate.graph.
    	The edges of pathList (which is a list of adjacent nodes)
    	are bolded in the graph
	"""
	
	fileGraph = open("karate.graph", 'r')
	
	## dot file which describes the graph
	fileDot = open  ("karate.dot",'w')
	
	## beginning of the dot file
	fileDot.write("graph G {\n")
			
	for line in fileGraph:
       		lineContent = line.split(" ")
		
	    	## we only need to retrieve edges from the graph
		if "edge" in lineContent:
	       		id1 = lineContent[1]
        		id2 = lineContent[2][:-1]
			## we add the edge id1 -- id 2
        		edgeString=id1+" -- "+id2
			## does the edge belongs to the path ?				
			if (id1 in pathList) and (id2 in pathList):
				## we now that the vertices belongs to the path 
				## but are they adjacent in the path ?
				index1=pathList.index(id1)
				index2=pathList.index(id2)					
				if ((index1-index2==1) or (index2-index1==1)):					
					## the edge belongs to the path, so we make it bolded
				  	edgeString+= "[style = bold]"					
			edgeString += ";\n"
			fileDot.write(edgeString)
	## end of the dot file 
	fileDot.write("}\n")		
	fileDot.close()
	## line command which creates the png file 
	os.system ("fdp karate.dot -Tpng -o karate.png")		
	

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
def showcheapestTree(tree):
	"""creates the file promotion.png and the file promotion.dot
	
	the edges of the cheapest tree are bolded and blue

    	"""    
	listofEdges=tree[1]		
#	if listofEdges<> []:
	fileGraph = open("promotion.graph", 'r')
	## dot file that describes the graph
	fileDot = open  ("promotion.dot",'w')

	## beginning of the dot file
	fileDot.write("graph G {\n")

	for line in fileGraph:

		lineContent = line.split(" ")

		## retrieve two ids and a value from file and create edge between them
		if "edge" in lineContent:
			id1 = lineContent[1]
			id2 = lineContent[2]
			weight = lineContent[3][:-1]			
			## we add the edge id1 -- id 2 with the weight as label
			edgeString=id1+" -- "+id2 + "[ len=5 "
			## uncomment the following line if you want to shwo weight on edges
			## edgeString+= ", fontsize=12, label= \" "+weight+"\""
			## does the edge belongs to the path ?				
			if ([id1,id2] in listofEdges) or ([id2,id1] in listofEdges):
				edgeString+= ",style = bold, color=blue"
			edgeString+= "];\n"
			fileDot.write(edgeString)
	## end of the dot file 
	fileDot.write("}\n")		
	fileDot.close()

	## line command which creates the png file 
	os.system ("neato promotion.dot -Tpng -o promotion.png")
	return ()

