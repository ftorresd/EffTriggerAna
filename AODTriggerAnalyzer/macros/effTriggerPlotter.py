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
	'QCD_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-15to20_MuEnrichedPt5'), 1.27E+09), #pb
				(ROOT.TFile('efficiency_QCD_Pt-20to30_MuEnrichedPt5'), 5.59E+08), #pb
				(ROOT.TFile('efficiency_QCD_Pt-30to50_MuEnrichedPt5'), 1.40E+08), #pb
				(ROOT.TFile('efficiency_QCD_Pt-50to80_MuEnrichedPt5'), 1.92E+07), #pb
				(ROOT.TFile('efficiency_QCD_Pt-80to120_MuEnrichedPt5'), 2.76E+06), #pb
				(ROOT.TFile('efficiency_QCD_Pt-120to170_MuEnrichedPt5'), 4.70E+05) #pb
				],
	'QCD_Pt-15to20_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-15to20_MuEnrichedPt5') 1.27E+09) #pb
				],
	'QCD_Pt-20to30_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-20to30_MuEnrichedPt5') 5.59E+08) #pb
				],
	'QCD_Pt-30to50_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-30to50_MuEnrichedPt5') 1.40E+08), #pb
				],
	'QCD_Pt-50to80_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-50to80_MuEnrichedPt5') 1.92E+07), #pb
				],
	'QCD_Pt-80to120_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-80to120_MuEnrichedPt5') 2.76E+06), #pb
				],
	'QCD_Pt-120to170_MuEnrichedPt5' : [
				(ROOT.TFile('efficiency_QCD_Pt-120to170_MuEnrichedPt5') 4.70E+05) #pb
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

configNames = [
		# "Zerobias",
		"DoubleMu_X",
		"DoubleMu_X_OS",
		"DoubleMu_X_EG_Y",
		"DoubleMu_X_OS_EG_Y",
		"DoubleMu_X_IsoEG_Y",
     	"DoubleMu_X_OS_IsoEG_Y"
]

selectionSequences = [
		"",
		"HLT",
		"RECO",
		"HLTRECO"
]

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


def plotEff(dataset, filesXSec, configNames, egCut, selectionSequence):
	ROOT.gROOT.Reset()
	c1 = ROOT.TCanvas("c1","c1",200,10,1050,750);
	leg = ROOT.TLegend(0.9-.38,0.7,0.9,0.9);

	for index, config in enumerate(configNames):
		histoToPlot = filesXSec[0][0].Get(config).Get("h_L1"+selectionSequence+"_"+config+"_EG_"+str(egCut))
		# histoToPlot.Scale( (filesXSec[0][1]/filesXSec[0][0].Get(config).Get("h_nEvts_"+config).GetBinContent(1))/(filesXSec[0][0].Get(config).Get("h_nEvts"+selectionSequence+"_"+config).GetBinContent(1) ) )
		normFactor = (filesXSec[0][1]/filesXSec[0][0].Get(config).Get("h_nEvts_"+config).GetBinContent(1))
		histoToPlot.Scale( normFactor )
		nEvtsEff = normFactor * ( filesXSec[0][0].Get(config).Get("h_nEvts"+selectionSequence+"_"+config).GetBinContent(1))
		for fileXSec in filesXSec[1:]:
			histo = fileXSec[0].Get(config).Get("h_L1"+selectionSequence+"_"+config+"_EG_"+str(egCut))
			# histo.Scale( (fileXSec[1]/fileXSec[0].Get(config).Get("h_nEvts_"+config).GetBinContent(1))/(fileXSec[0].Get(config).Get("h_nEvts"+selectionSequence+"_"+config).GetBinContent(1) ) )
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
			# print "oi"
			# histo.Print()
 
	# leg->SetHeader("The Legend Title","C"); // option "C" allows to center the header
	# leg->AddEntry(h1,"Histogram filled with random numbers","f");
	# leg->AddEntry("f1","Function abs(#frac{sin(x)}{x})","l");
	# leg->AddEntry("gr","Graph with error bars","lep");
	leg.Draw();
	c1.Update()
	c1.SaveAs("l1Plots/"+dataset+"/L1"+selectionSequence+"/h_L1"+selectionSequence+"_EG_"+str(egCut)+".pdf");
	c1.SaveAs("l1Plots/"+dataset+"/L1"+selectionSequence+"/h_L1"+selectionSequence+"_EG_"+str(egCut)+".png");

# loop over datasets file
os.system("rm -rf l1Plots ; mkdir l1Plots")
for dataset in effFilesXSec:
	os.system("mkdir l1Plots/"+dataset)
	for selectionSequence in selectionSequences:
		os.system("mkdir l1Plots/"+dataset+"/L1"+selectionSequence)
		for egCut in range(51):
			plotEff(dataset, effFilesXSec[dataset], configNames, egCut, selectionSequence)