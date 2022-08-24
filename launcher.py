import os
import sys
from TrajDBSCAN import *

#Get the configurations

with open('config.txt','r') as inf:
    config = eval(inf.read())

eps = int(config["eps"])
min_time = int(config["mintime"])

#print eps, min_time

#fork process for each input file to achieve some speedup

for file in config["filenames"]:
	#initialize the details
	initialize(eps,min_time)
	initialize_name([file])
	#execute the algorithm
	createSlowPointFiles()
	findPS()
	clusterPS()
	#whenever a cluster is created calculate the shared stops.
	#Thus we can have the shared stops found at any point before the completion of all the processes.
	createSharedStops()




