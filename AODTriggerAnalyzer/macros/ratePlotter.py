#!/usr/bin/env python


# from  ROOT import *
import sys, math, csv, os

import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt




# plot rates
def ratePlotter(configList, configName, sortBy, minRate, maxRate, plotError):
	plt.rcdefaults()
	# plt.figure(num=None, figsize=(99, 6), dpi=300, facecolor='w', edgecolor='k')
	fig, ax = plt.subplots()
	fig.set_figheight(40)
	fig.set_figwidth(40)
	# Example data
	# y_pos = np.arange(len(configList))
	rates = []
	errors = []
	labels = []
	for config in configList:
		if ((minRate <= configList[config][0] <= maxRate) and (configList[config][0] != 0)):
		# if ((minRate <= configList[config][0] <= maxRate)):
			labels.append(config)
			rates.append(configList[config][0])
			if (plotError):
				errors.append(configList[config][1])
			else:
				errors.append(0)
	
	y_pos = np.arange(len(rates))			
	if (sortBy == "rate"):
		rates, errors, labels = zip(*sorted(zip(rates, errors, labels)))
	if (sortBy == "label"):
		labels, rates, errors  = zip(*sorted(zip(labels, rates, errors)))		

	ax.barh(y_pos, rates, height=0.8, xerr=errors, align='center', color='steelblue', ecolor='black')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(labels)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Rate @ 2E34 (Hz)', fontsize=35)
	# fig.suptitle('test title', fontsize=35)
	# ax.set_title('How fast do you want to go today?')
	# plt.figure(figsize=(1, 1), dpi=300)
	ax.grid(True)


	ticklines = ax.get_xticklines() + ax.get_yticklines()
	gridlines = ax.get_xgridlines() + ax.get_ygridlines()
	ticklabels = ax.get_xticklabels() + ax.get_yticklabels()

	for line in ticklines:
	    line.set_linewidth(3)

	for line in gridlines:
	    line.set_linestyle('-.')

	for label in ticklabels:
	    label.set_color('orangered')
	    # label.set_fontsize('medium')
	    label.set_fontsize(25)
 
	plt.xticks(range(int(minRate)-1,int(maxRate)+1))
	plt.xlim([minRate,maxRate])
	plt.tight_layout()
	plt.savefig("hltRates/rates_"+configName+"_"+sortBy+"_"+str(minRate)+"_to_"+str(maxRate)+".png")
	plt.savefig("hltRates/rates_"+configName+"_"+sortBy+"_"+str(minRate)+"_to_"+str(maxRate)+".pdf")


ratesToPlot = {}
with open(sys.argv[1], 'rb') as csvfile:	
	reader = csv.DictReader(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		# print row
		ratesToPlot.update({row["HLT Path"] : [float(row["Rate_2p0E34"]), float(row["Rate_2p0E34 Error"])]})
	# print ratesToPlot


os.system("rm -rf hltRates ; mkdir hltRates")

ratePlotter(ratesToPlot, "allPaths", "rate", 1.5, 2., False)
ratePlotter(ratesToPlot, "allPaths", "label", 1.5, 2., False)

ratePlotter(ratesToPlot, "allPaths", "rate", 1.75, 2., False)
ratePlotter(ratesToPlot, "allPaths", "label", 1.75, 2., False)


ratePlotter(ratesToPlot, "allPaths", "rate", 0, 30, True)
ratePlotter(ratesToPlot, "allPaths", "label", 0, 30, True)



# ratePlotter(ratesToPlot, "allPaths", "rate", 0.1, 7.0)
# ratePlotter(ratesToPlot, "allPaths", "label", 0.1, 7.0)

# ratePlotter(ratesToPlot, "allPaths", "rate", 0.1, 4.5)
# ratePlotter(ratesToPlot, "allPaths", "label", 0.1, 4.5)



