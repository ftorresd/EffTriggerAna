#!/usr/bin/env python

"""
Plotter for EffTriggerAna
"""

import ROOT, os

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(1)
ROOT.TH1.SetDefaultSumw2(True)
ROOT.gStyle.SetOptStat(0)
	
effFilesXSec = {
	'ZeroBias' : [
				(ROOT.TFile('efficiency_ZeroBias.root'), 1.0), #pb
				],
	'QCD_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-15to20_MuEnrichedPt5.root'), 1.27E+09), #pb
				(ROOT.TFile('efficiency_QCD_Pt-20to30_MuEnrichedPt5.root'), 5.59E+08), #pb
				(ROOT.TFile('efficiency_QCD_Pt-30to50_MuEnrichedPt5.root'), 1.40E+08), #pb
				(ROOT.TFile('efficiency_QCD_Pt-50to80_MuEnrichedPt5.root'), 1.92E+07), #pb
				(ROOT.TFile('efficiency_QCD_Pt-80to120_MuEnrichedPt5.root'), 2.76E+06), #pb
				(ROOT.TFile('efficiency_QCD_Pt-120to170_MuEnrichedPt5.root'), 4.70E+05) #pb
				],
	'QCD_Pt-15to20_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-15to20_MuEnrichedPt5.root'), 1.27E+09) #pb
				],
	'QCD_Pt-20to30_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-20to30_MuEnrichedPt5.root'), 5.59E+08) #pb
				],
	'QCD_Pt-30to50_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-30to50_MuEnrichedPt5.root'), 1.40E+08), #pb
				],
	'QCD_Pt-50to80_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-50to80_MuEnrichedPt5.root'), 1.92E+07), #pb
				],
	'QCD_Pt-80to120_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-80to120_MuEnrichedPt5.root'), 2.76E+06), #pb
				],
	'QCD_Pt-120to170_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-120to170_MuEnrichedPt5.root'), 4.70E+05) #pb
				],
	'DYJetsToLL_M-1to10' : [
				(ROOT.TFile('efficiency_DYJetsToLL_M-1to10.root'), 1.757E+05) #pb
				],
	'DYJetsToLL_M-10to50' : [
				(ROOT.TFile('efficiency_DYJetsToLL_M-10to50.root'), 1.614E+04) #pb
				],
	'DYJetsToLL_M-50' : [
				(ROOT.TFile('efficiency_DYJetsToLL_M-50.root'), 4.895E+03) #pb
				],									
	'DYJetsToLL' : [
				(ROOT.TFile('efficiency_DYJetsToLL_M-1to10.root'), 1.757E+05), #pb
				(ROOT.TFile('efficiency_DYJetsToLL_M-10to50.root'), 1.614E+04), #pb
				(ROOT.TFile('efficiency_DYJetsToLL_M-50.root'), 4.895E+03) #pb
				],
	'ZToJPsiGamma' : [
				(ROOT.TFile('efficiency_ZToJPsiGamma.root'), 1.881E0) #pb
				]
			}

configSets = {
			# "Zerobias": ["Zerobias"],
			"DoubleMu": ["DoubleMu_X", "DoubleMu_X_OS", "DoubleMu_X_EG_Y", "DoubleMu_X_OS_EG_Y", "DoubleMu_X_IsoEG_Y", "DoubleMu_X_OS_IsoEG_Y"],
			"Mu_9": ["Mu_9_X", "Mu_9_X_OS", "Mu_9_X_EG_Y", "Mu_9_X_OS_EG_Y", "Mu_9_X_IsoEG_Y", "Mu_9_X_OS_IsoEG_Y"],
			"Mu_10": ["Mu_10_X", "Mu_10_X_OS", "Mu_10_X_EG_Y", "Mu_10_X_OS_EG_Y", "Mu_10_X_IsoEG_Y", "Mu_10_X_OS_IsoEG_Y"],
			"Mu_11": ["Mu_11_X", "Mu_11_X_OS", "Mu_11_X_EG_Y", "Mu_11_X_OS_EG_Y", "Mu_11_X_IsoEG_Y", "Mu_11_X_OS_IsoEG_Y"],
			"Mu_12": ["Mu_12_X", "Mu_12_X_OS", "Mu_12_X_EG_Y", "Mu_12_X_OS_EG_Y", "Mu_12_X_IsoEG_Y", "Mu_12_X_OS_IsoEG_Y"],
			"Mu_13": ["Mu_13_X", "Mu_13_X_OS", "Mu_13_X_EG_Y", "Mu_13_X_OS_EG_Y", "Mu_13_X_IsoEG_Y", "Mu_13_X_OS_IsoEG_Y"],
			"Mu_8": ["Mu_8_X", "Mu_8_X_OS", "Mu_8_X_EG_Y", "Mu_8_X_OS_EG_Y", "Mu_8_X_IsoEG_Y", "Mu_8_X_OS_IsoEG_Y"],
			"Mu_7": ["Mu_7_X", "Mu_7_X_OS", "Mu_7_X_EG_Y", "Mu_7_X_OS_EG_Y", "Mu_7_X_IsoEG_Y", "Mu_7_X_OS_IsoEG_Y"],
			"Mu_6": ["Mu_6_X", "Mu_6_X_OS", "Mu_6_X_EG_Y", "Mu_6_X_OS_EG_Y", "Mu_6_X_IsoEG_Y", "Mu_6_X_OS_IsoEG_Y"],
			"Mu_5": ["Mu_5_X", "Mu_5_X_OS", "Mu_5_X_EG_Y", "Mu_5_X_OS_EG_Y", "Mu_5_X_IsoEG_Y", "Mu_5_X_OS_IsoEG_Y"],
			"Mu_4": ["Mu_4_X", "Mu_4_X_OS", "Mu_4_X_EG_Y", "Mu_4_X_OS_EG_Y", "Mu_4_X_IsoEG_Y", "Mu_4_X_OS_IsoEG_Y"],
			"Mu_3": ["Mu_3_X", "Mu_3_X_OS", "Mu_3_X_EG_Y", "Mu_3_X_OS_EG_Y", "Mu_3_X_IsoEG_Y", "Mu_3_X_OS_IsoEG_Y"]
			}

selectionSequences = [
		"",
		# "HLT",
		"RECO",
		"HLTRECO"
]

# needs to be rewriten
def translateConfigNameToLegend(config, egCut):
	if (config == "DoubleMu_X"):
		return "DoubleMu_X"
	if (config == "DoubleMu_X_OS"):
		return "DoubleMu_X_OS"		
	if (config == "DoubleMu_X_EG_Y"):
		return "DoubleMu_X_EG_"+str(egCut)
	if (config == "DoubleMu_X_OS_EG_Y"):
		return "DoubleMu_X_OS_EG_"+str(egCut)
	if (config == "DoubleMu_X_IsoEG_Y"):
		return "DoubleMu_X_IsoEG_"+str(egCut)
	if (config == "DoubleMu_X_OS_IsoEG_Y"):
		return "DoubleMu_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_3_X"):
		return "Mu_3_X"
	if (config == "Mu_3_X_OS"):
		return "Mu_3_X_OS"		
	if (config == "Mu_3_X_EG_Y"):
		return "Mu_3_X_EG_"+str(egCut)
	if (config == "Mu_3_X_OS_EG_Y"):
		return "Mu_3_X_OS_EG_"+str(egCut)
	if (config == "Mu_3_X_IsoEG_Y"):
		return "Mu_3_X_IsoEG_"+str(egCut)
	if (config == "Mu_3_X_OS_IsoEG_Y"):
		return "Mu_3_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_4_X"):
		return "Mu_4_X"
	if (config == "Mu_4_X_OS"):
		return "Mu_4_X_OS"		
	if (config == "Mu_4_X_EG_Y"):
		return "Mu_4_X_EG_"+str(egCut)
	if (config == "Mu_4_X_OS_EG_Y"):
		return "Mu_4_X_OS_EG_"+str(egCut)
	if (config == "Mu_4_X_IsoEG_Y"):
		return "Mu_4_X_IsoEG_"+str(egCut)
	if (config == "Mu_4_X_OS_IsoEG_Y"):
		return "Mu_4_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_5_X"):
		return "Mu_5_X"
	if (config == "Mu_5_X_OS"):
		return "Mu_5_X_OS"		
	if (config == "Mu_5_X_EG_Y"):
		return "Mu_5_X_EG_"+str(egCut)
	if (config == "Mu_5_X_OS_EG_Y"):
		return "Mu_5_X_OS_EG_"+str(egCut)
	if (config == "Mu_5_X_IsoEG_Y"):
		return "Mu_5_X_IsoEG_"+str(egCut)
	if (config == "Mu_5_X_OS_IsoEG_Y"):
		return "Mu_5_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_6_X"):
		return "Mu_6_X"
	if (config == "Mu_6_X_OS"):
		return "Mu_6_X_OS"		
	if (config == "Mu_6_X_EG_Y"):
		return "Mu_6_X_EG_"+str(egCut)
	if (config == "Mu_6_X_OS_EG_Y"):
		return "Mu_6_X_OS_EG_"+str(egCut)
	if (config == "Mu_6_X_IsoEG_Y"):
		return "Mu_6_X_IsoEG_"+str(egCut)
	if (config == "Mu_6_X_OS_IsoEG_Y"):
		return "Mu_6_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_7_X"):
		return "Mu_7_X"
	if (config == "Mu_7_X_OS"):
		return "Mu_7_X_OS"		
	if (config == "Mu_7_X_EG_Y"):
		return "Mu_7_X_EG_"+str(egCut)
	if (config == "Mu_7_X_OS_EG_Y"):
		return "Mu_7_X_OS_EG_"+str(egCut)
	if (config == "Mu_7_X_IsoEG_Y"):
		return "Mu_7_X_IsoEG_"+str(egCut)
	if (config == "Mu_7_X_OS_IsoEG_Y"):
		return "Mu_7_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_8_X"):
		return "Mu_8_X"
	if (config == "Mu_8_X_OS"):
		return "Mu_8_X_OS"		
	if (config == "Mu_8_X_EG_Y"):
		return "Mu_8_X_EG_"+str(egCut)
	if (config == "Mu_8_X_OS_EG_Y"):
		return "Mu_8_X_OS_EG_"+str(egCut)
	if (config == "Mu_8_X_IsoEG_Y"):
		return "Mu_8_X_IsoEG_"+str(egCut)
	if (config == "Mu_8_X_OS_IsoEG_Y"):
		return "Mu_8_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_9_X"):
		return "Mu_9_X"
	if (config == "Mu_9_X_OS"):
		return "Mu_9_X_OS"		
	if (config == "Mu_9_X_EG_Y"):
		return "Mu_9_X_EG_"+str(egCut)
	if (config == "Mu_9_X_OS_EG_Y"):
		return "Mu_9_X_OS_EG_"+str(egCut)
	if (config == "Mu_9_X_IsoEG_Y"):
		return "Mu_9_X_IsoEG_"+str(egCut)
	if (config == "Mu_9_X_OS_IsoEG_Y"):
		return "Mu_9_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_10_X"):
		return "Mu_10_X"
	if (config == "Mu_10_X_OS"):
		return "Mu_10_X_OS"		
	if (config == "Mu_10_X_EG_Y"):
		return "Mu_10_X_EG_"+str(egCut)
	if (config == "Mu_10_X_OS_EG_Y"):
		return "Mu_10_X_OS_EG_"+str(egCut)
	if (config == "Mu_10_X_IsoEG_Y"):
		return "Mu_10_X_IsoEG_"+str(egCut)
	if (config == "Mu_10_X_OS_IsoEG_Y"):
		return "Mu_10_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_11_X"):
		return "Mu_11_X"
	if (config == "Mu_11_X_OS"):
		return "Mu_11_X_OS"		
	if (config == "Mu_11_X_EG_Y"):
		return "Mu_11_X_EG_"+str(egCut)
	if (config == "Mu_11_X_OS_EG_Y"):
		return "Mu_11_X_OS_EG_"+str(egCut)
	if (config == "Mu_11_X_IsoEG_Y"):
		return "Mu_11_X_IsoEG_"+str(egCut)
	if (config == "Mu_11_X_OS_IsoEG_Y"):
		return "Mu_11_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_12_X"):
		return "Mu_12_X"
	if (config == "Mu_12_X_OS"):
		return "Mu_12_X_OS"		
	if (config == "Mu_12_X_EG_Y"):
		return "Mu_12_X_EG_"+str(egCut)
	if (config == "Mu_12_X_OS_EG_Y"):
		return "Mu_12_X_OS_EG_"+str(egCut)
	if (config == "Mu_12_X_IsoEG_Y"):
		return "Mu_12_X_IsoEG_"+str(egCut)
	if (config == "Mu_12_X_OS_IsoEG_Y"):
		return "Mu_12_X_OS_IsoEG_"+str(egCut)
	if (config == "Mu_13_X"):
		return "Mu_13_X"
	if (config == "Mu_13_X_OS"):
		return "Mu_13_X_OS"		
	if (config == "Mu_13_X_EG_Y"):
		return "Mu_13_X_EG_"+str(egCut)
	if (config == "Mu_13_X_OS_EG_Y"):
		return "Mu_13_X_OS_EG_"+str(egCut)
	if (config == "Mu_13_X_IsoEG_Y"):
		return "Mu_13_X_IsoEG_"+str(egCut)
	if (config == "Mu_13_X_OS_IsoEG_Y"):
		return "Mu_13_X_OS_IsoEG_"+str(egCut)


def plotEff(dataset, filesXSec, configNames, egCut, selectionSequence):
	ROOT.gROOT.Reset()
	c1 = ROOT.TCanvas("c1","c1",200,10,1050,750);
	leg = ROOT.TLegend(0.9-.38,0.7,0.9,0.9);

	for index, config in enumerate(configNames):
		histoToPlot = filesXSec[0][0].Get(config).Get("h_L1"+selectionSequence+"_"+config+"_EG_"+str(egCut))
		normFactor = (filesXSec[0][1]/filesXSec[0][0].Get(config).Get("h_nEvts_"+config).GetBinContent(1))
		histoToPlot.Scale( normFactor )
		nEvtsEff = normFactor * ( filesXSec[0][0].Get(config).Get("h_nEvts"+selectionSequence+"_"+config).GetBinContent(1))
		for fileXSec in filesXSec[1:]:
			histo = fileXSec[0].Get(config).Get("h_L1"+selectionSequence+"_"+config+"_EG_"+str(egCut))
			histo.Scale( normFactor )
			histoToPlot.Add(histo)
			nEvtsEff += normFactor * ( fileXSec[0].Get(config).Get("h_nEvts"+selectionSequence+"_"+config).GetBinContent(1) )

		if (nEvtsEff > 0):
			histoToPlot.Scale(1.0/nEvtsEff)
			histoToPlot.SetTitle("")
			histoToPlot.SetMarkerStyle(24)
			histoToPlot.SetMarkerColor(index+1)
			histoToPlot.SetMinimum(0.0);
			histoToPlot.SetMaximum(1.15);
			histoToPlot.GetXaxis().SetRangeUser(0.0, 40.0)
	  		leg.AddEntry(histoToPlot,translateConfigNameToLegend(config, egCut));
			histoToPlot.Draw("same")

	leg.Draw();
	c1.Update()
	# c1.SaveAs("l1Plots/"+dataset+"/L1"+selectionSequence+"/"+configName+"/h_L1"+selectionSequence+"_EG_"+str(egCut)+".pdf");
	c1.SaveAs("l1Plots/"+dataset+"/L1"+selectionSequence+"/"+configName+"/h_L1"+selectionSequence+"_EG_"+str(egCut)+".png");

# loop over datasets file
os.system("rm -rf l1Plots ; mkdir l1Plots")
for dataset in effFilesXSec:
	os.system("mkdir l1Plots/"+dataset)
	for selectionSequence in selectionSequences:
		os.system("mkdir l1Plots/"+dataset+"/L1"+selectionSequence)
		for configName in configSets:
			os.system("mkdir l1Plots/"+dataset+"/L1"+selectionSequence+"/"+configName)
			# for egCut in range(51):
			for egCut in [0,5,6,7,8,9,10,11,12,13,14,15]:
				plotEff(dataset, effFilesXSec[dataset], configSets[configName], egCut, selectionSequence)


				