import os

def displayGraph (f):
	"""create the file robot.png which is a graphical
    	representation of robot.graph.  
	"""
	
	fileGraph = open(f, 'r')
	
	## dot file which describes the graph
	fileDot = open  (f+".dot",'w')
	
	## beginning of the dot file
	fileDot.write("graph G {\noverlap=false\n")
			
	for line in fileGraph:
       		lineContent = line.split(" ")
		
	    	## we only need to retrieve edges from the graph
		if "edge" in lineContent:
	       		id1 = lineContent[1]
	       		if len(lineContent) == 4:
	       		  id2 = lineContent[2]
	       		  weight = lineContent[3][:-1]
	       		else:
        		  id2 = lineContent[2][:-1]
			## we add the edge id1 -- id 2
        		edgeString=id1+" -- "+id2
			edgeString += ";\n"
			fileDot.write(edgeString)
	## end of the dot file 
	fileDot.write("}\n")		
	fileDot.close()
	## line command which creates the png file 
	os.system ("neato "+f+".dot -Tpng -o "+f+".png")

  
## graphviz.show_active_nodes( kcores, activated_nodes, filename, "IC_kcores" )
def show_active_nodes( initial_nodes, active_nodes, input_file, method ):
  fileGraph = open(input_file, 'r')
  ## dot file which describes the graph
  fileDot = open  (input_file+"_"+method+".dot",'w')
  ## beginning of the dot file
  fileDot.write("graph G {\noverlap=false\n")
  fileDot.write("{\nnode [style = bold, color=red]\n" )
  for node in initial_nodes:
    node_string = str(node) + "\n"
    fileDot.write(node_string)
  fileDot.write("}\n")
  fileDot.write("{\nnode [color=red]\n" )
  for node in active_nodes:
    if node not in initial_nodes:
      node_string = str(node) + "\n"
      fileDot.write(node_string)
  fileDot.write("}\n")
			
  for line in fileGraph:
    lineContent = line.split(" ")
  	## we only need to retrieve edges from the graph
    if "edge" in lineContent:
      id1 = lineContent[1]
      if len(lineContent) == 4:
	      id2 = lineContent[2]
	      weight = lineContent[3][:-1]
      else:
        id2 = lineContent[2][:-1]
			## we add the edge id1 -- id 2
      edgeString=id1+" -- "+id2
      edgeString += ";\n"
      fileDot.write(edgeString)
	## end of the dot file 
  fileDot.write("}\n")		
  fileDot.close()
	## line command which creates the png file 
  os.system ("neato "+input_file+"_"+method+".dot"+" -Tpng -o "+input_file+"_"+method+"_activated.png")
  return
  

def show_core_network( mst_tree, core, input_file, output_file ):
  if mst_tree <> [] and core <> []:
    ## dot file which describes the graph
    fileDot = open  (output_file,'w')
    ## beginning of the dot file
    fileDot.write("graph G {\noverlap=false\n")
    fileDot.write("{\nnode [style = bold, color=red]\n" )
    for node in core:
      node_string = str(node) + "\n"
      fileDot.write(node_string)
    fileDot.write("}\n")
    visitedLink = []
    for id1 in mst_tree:
      for id2 in mst_tree[id1]:
        if (id1,id2) not in visitedLink:
          if ( id1 in core and id2 in core[id1] ) or ( id2 in core and id1 in core[id2] ):
            edgeString=id1+" -- "+id2 + "[style = bold, color=red];" + "\n"
          else:
            edgeString=id1+" -- "+id2 + "[style = bold, color=blue];" + "\n"
          fileDot.write(edgeString)
          visitedLink.append((id1,id2))
          visitedLink.append((id2,id1))

    ## end of the dot file 
    fileDot.write("}\n")
    fileDot.close()
    ## line command which creates the png file
    os.system ("neato "+output_file+" -Tpng -o "+input_file+"_core.png")
  return
