#!/usr/bin/env python

"""
Simple demo of a horizontal bar chart.
"""
import os
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt





configRates = {
		"L1_DoubleMu8_OS_EG10" : [45.1167, 7.5194],
		"L1_DoubleMu0_OS_EG9" : [ 2891.23, 60.194],
		"L1_Mu5_EG15" : [ 3943.95, 70.304],
		"L1_Mu5_EG20" : [ 1643, 45.37],
		"L1_Mu5_EG23" : [ 1022.64, 35.799],
		"L1_Mu5_IsoEG18" : [ 852.204, 32.680],
		"L1_Mu5_IsoEG20" : [ 637.9,  28.274],
		"L1_Mu12_EG10" : [ 1510.16, 43.503],
		"L1_Mu20_EG10" : [ 436.128, 23.378],
		"L1_Mu20_EG17" : [ 126.577, 12.594],
		"L1_Mu23_IsoEG10" : [ 120.311, 12.279],
		"L1_Mu23_EG10" : [ 330.856, 20.362],
		"L1_DoubleMu7_EG14" : [ 36.344,  6.7489],
		"L1_DoubleMu7_EG7" : [ 286.992, 18.965],
		"L1_DoubleMu7_OS" : [ 725.627, 30.15],
		"L1_DoubleMu7_OS_EG10" : [ 66.4218, 9.1237],
		"L1_DoubleMu7_OS_IsoEG10" : [ 30.0778, 6.139],
		"L1_DoubleMu6_OS_EG10" : [ 109.032, 11.689],
		"L1_DoubleMu5_OS_EG10" : [ 206.785, 16.098],
		"L1_DoubleMu4_OS_EG10" : [ 446.154, 23.646],
		"L1_DoubleMu3_OS_EG10" : [ 934.918, 34.229],
		"L1_DoubleMu2_OS_EG10" : [ 1799.65, 47.491],
		"L1_DoubleMu1_OS_EG10" : [ 2126.75, 51.626],
		"L1_DoubleMu0_OS_EG10" : [ 2126.75, 51.626],
		"L1_DoubleMu8_OS_IsoEG10" : [ 23.8116, 5.4627],
		"L1_DoubleMu6_OS_IsoEG10" : [ 37.5972, 6.8642],
		"L1_DoubleMu5_OS_IsoEG10" : [ 80.2074, 10.025],
		"L1_DoubleMu4_OS_IsoEG10" : [ 185.48,  15.246],
		"L1_DoubleMu3_OS_IsoEG10" : [ 407.303, 22.593],
		"L1_DoubleMu2_OS_IsoEG10" : [ 785.782, 31.381],
		"L1_DoubleMu1_OS_IsoEG10" : [ 946.197, 34.435],
		"L1_DoubleMu0_OS_IsoEG10" : [ 946.197, 34.435],
		"L1_DoubleMu7_OS_EG9" : [ 86.4736, 10.410],
		"L1_DoubleMu8_OS_EG9" : [ 57.6491, 8.499],
		"L1_DoubleMu7_OS_EG12" : [ 40.1037, 7.089],
		"L1_DoubleMu7_OS_EG11" : [ 48.8764, 7.8264],
		"L1_DoubleMu8_OS_EG11" : [ 31.331,  6.2662],
		"L1_DoubleMu8_OS_EG12" : [ 27.5713, 5.8782],
		"L1_DoubleMu6_OS_EG9" : [ 145.376, 13.497],
		"L1_DoubleMu6_OS_EG11" : [ 85.2204, 10.334],
		"L1_DoubleMu6_OS_EG12" : [ 72.688,  9.5444],
		"L1_DoubleMu5_OS_EG9" : [ 279.473, 18.714],
		"L1_DoubleMu5_OS_EG11" : [ 165.428, 14.398],
		"L1_DoubleMu5_OS_EG12" : [ 137.857, 13.144],
		"L1_DoubleMu4_OS_EG9" : [ 617.848, 27.826],
		"L1_DoubleMu4_OS_EG11" : [ 350.908, 20.970],
		"L1_DoubleMu4_OS_EG12" : [ 278.22,  18.672],
		"L1_DoubleMu3_OS_EG9" : [ 1279.56, 40.044],
		"L1_DoubleMu3_OS_EG11" : [ 723.12,  30.103],
		"L1_DoubleMu3_OS_EG12" : [ 562.705, 26.555],
		"L1_DoubleMu2_OS_EG9" : [ 2436.3,  55.256],
		"L1_DoubleMu2_OS_EG11" : [ 1363.53, 41.338],
		"L1_DoubleMu2_OS_EG12" : [ 1035.18, 36.018],
		"L1_DoubleMu1_OS_EG9" : [ 2891.23, 60.194],
		"L1_DoubleMu1_OS_EG11" : [ 1599.14, 44.767],
		"L1_DoubleMu1_OS_EG12" : [ 1216.9,  39.052],
		"L1_DoubleMu0_OS_EG11" : [ 1599.14, 44.767],
		"L1_DoubleMu0_OS_EG12" : [ 1216.9,  39.052],
		"L1_DoubleMu7_OS_IsoEG9" : [ 35.0908, 6.6315],
		"L1_DoubleMu7_OS_IsoEG11" : [ 22.5583, 5.3170],
		"L1_DoubleMu7_OS_IsoEG12" : [ 17.5454, 4.6892],
		"L1_DoubleMu8_OS_IsoEG9" : [ 26.3181, 5.7430],
		"L1_DoubleMu8_OS_IsoEG11" : [ 16.2921, 4.5186],
		"L1_DoubleMu8_OS_IsoEG12" : [ 12.5324, 3.9631],
		"L1_DoubleMu6_OS_IsoEG9" : [ 51.3829, 8.0246],
		"L1_DoubleMu6_OS_IsoEG11" : [ 28.8245, 6.0103],
		"L1_DoubleMu6_OS_IsoEG12" : [ 23.8116, 5.4627],
		"L1_DoubleMu5_OS_IsoEG9" : [ 112.792, 11.889],
		"L1_DoubleMu5_OS_IsoEG11" : [ 61.4088, 8.7726],
		"L1_DoubleMu5_OS_IsoEG12" : [ 46.3699, 7.6231],
		"L1_DoubleMu4_OS_IsoEG9" : [ 263.181, 18.161],
		"L1_DoubleMu4_OS_IsoEG11" : [ 139.11,  13.203],
		"L1_DoubleMu4_OS_IsoEG12" : [ 105.272, 11.486],
		"L1_DoubleMu3_OS_IsoEG9" : [ 560.199, 26.496],
		"L1_DoubleMu3_OS_IsoEG11" : [ 305.791, 19.576],
		"L1_DoubleMu3_OS_IsoEG12" : [ 224.33,  16.767],
		"L1_DoubleMu2_OS_IsoEG9" : [ 1079.04, 36.773],
		"L1_DoubleMu2_OS_IsoEG11" : [ 577.744, 26.908],
		"L1_DoubleMu2_OS_IsoEG12" : [ 419.836, 22.938],
		"L1_DoubleMu1_OS_IsoEG9" : [ 1313.4,  40.571],
		"L1_DoubleMu1_OS_IsoEG11" : [ 688.029, 29.364],
		"L1_DoubleMu1_OS_IsoEG12" : [ 500.043, 25.033],
		"L1_DoubleMu0_OS_IsoEG9" : [ 1313.4,  40.571],
		"L1_DoubleMu0_OS_IsoEG11" : [ 688.029, 29.364],
		"L1_DoubleMu0_OS_IsoEG12" : [ 500.043, 25.033],
	}

DoubleMu_X_OS_EG_Y = {
		"L1_DoubleMu8_OS_EG10" : [45.1167, 7.5194],
		"L1_DoubleMu0_OS_EG09" : [ 2891.23, 60.194],
		"L1_DoubleMu7_EG14" : [ 36.344,  6.7489],
		"L1_DoubleMu7_EG07" : [ 286.992, 18.965],
		"L1_DoubleMu7_OS_EG10" : [ 66.4218, 9.1237],
		"L1_DoubleMu6_OS_EG10" : [ 109.032, 11.689],
		"L1_DoubleMu5_OS_EG10" : [ 206.785, 16.098],
		"L1_DoubleMu4_OS_EG10" : [ 446.154, 23.646],
		"L1_DoubleMu3_OS_EG10" : [ 934.918, 34.229],
		"L1_DoubleMu2_OS_EG10" : [ 1799.65, 47.491],
		"L1_DoubleMu1_OS_EG10" : [ 2126.75, 51.626],
		"L1_DoubleMu0_OS_EG10" : [ 2126.75, 51.626],
		"L1_DoubleMu7_OS_EG09" : [ 86.4736, 10.410],
		"L1_DoubleMu8_OS_EG09" : [ 57.6491, 8.499],
		"L1_DoubleMu7_OS_EG12" : [ 40.1037, 7.089],
		"L1_DoubleMu7_OS_EG11" : [ 48.8764, 7.8264],
		"L1_DoubleMu8_OS_EG11" : [ 31.331,  6.2662],
		"L1_DoubleMu8_OS_EG12" : [ 27.5713, 5.8782],
		"L1_DoubleMu6_OS_EG09" : [ 145.376, 13.497],
		"L1_DoubleMu6_OS_EG11" : [ 85.2204, 10.334],
		"L1_DoubleMu6_OS_EG12" : [ 72.688,  9.5444],
		"L1_DoubleMu5_OS_EG09" : [ 279.473, 18.714],
		"L1_DoubleMu5_OS_EG11" : [ 165.428, 14.398],
		"L1_DoubleMu5_OS_EG12" : [ 137.857, 13.144],
		"L1_DoubleMu4_OS_EG09" : [ 617.848, 27.826],
		# "L1_DoubleMu4_OS_EG11" : [ 350.908, 20.970],
		# "L1_DoubleMu4_OS_EG12" : [ 278.22,  18.672],
		# "L1_DoubleMu3_OS_EG9" : [ 1279.56, 40.044],
		# "L1_DoubleMu3_OS_EG11" : [ 723.12,  30.103],
		# "L1_DoubleMu3_OS_EG12" : [ 562.705, 26.555],
		# "L1_DoubleMu2_OS_EG9" : [ 2436.3,  55.256],
		# "L1_DoubleMu2_OS_EG11" : [ 1363.53, 41.338],
		# "L1_DoubleMu2_OS_EG12" : [ 1035.18, 36.018],
		# "L1_DoubleMu1_OS_EG9" : [ 2891.23, 60.194],
		# "L1_DoubleMu1_OS_EG11" : [ 1599.14, 44.767],
		# "L1_DoubleMu1_OS_EG12" : [ 1216.9,  39.052],
		# "L1_DoubleMu0_OS_EG11" : [ 1599.14, 44.767],
		# "L1_DoubleMu0_OS_EG12" : [ 1216.9,  39.052],
	}


def ratePlotter(configList, configName, sortBy):
	plt.rcdefaults()
	plt.figure(num=None, figsize=(99, 6), dpi=300, facecolor='w', edgecolor='k')
	fig, ax = plt.subplots()
	# Example data
	y_pos = np.arange(len(configList))
	rates = []
	errors = []
	labels = []
	for config in configList:
		labels.append(config)
		rates.append(configList[config][0])
		errors.append(configList[config][1])

	if (sortBy == "rate"):
		rates, errors, labels = zip(*sorted(zip(rates, errors, labels)))
	if (sortBy == "label"):
		labels, rates, errors  = zip(*sorted(zip(labels, rates, errors)))		

	ax.barh(y_pos, rates, height=0.8, xerr=errors, align='center', color='steelblue', ecolor='black')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(labels)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Rate (Hz)')
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
	    label.set_fontsize("small")


	plt.tight_layout()
	plt.savefig("l1Rates/rates_"+configName+"_"+sortBy+".png")
	plt.savefig("l1Rates/rates_"+configName+"_"+sortBy+".pdf")

os.system("rm -rf l1Rates ; mkdir l1Rates")
ratePlotter(configRates, "total", "rate")
ratePlotter(configRates, "total", "label")
ratePlotter(DoubleMu_X_OS_EG_Y, "DoubleMu_X_OS_EG_Y", "rate")
ratePlotter(DoubleMu_X_OS_EG_Y, "DoubleMu_X_OS_EG_Y", "label")