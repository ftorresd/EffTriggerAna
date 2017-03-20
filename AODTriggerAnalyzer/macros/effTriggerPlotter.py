#!/usr/bin/env python

"""
Plotter for EffTriggerAna
"""

import ROOT, os

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(1)
ROOT.TH1.SetDefaultSumw2(True)
ROOT.gStyle.SetOptStat(0)

effFiles = {
	'DYJetsToLL_M-1to10' : ROOT.TFile('efficiency_DYJetsToLL_M-1to10.root'),
	# 'DYJetsToLL_M-10to50' : 'efficiency_DYJetsToLL_M-10to50.root',
	# 'DYJetsToLL_M-50' : 'efficiency_DYJetsToLL_M-50.root',
	'ZToJPsiGamma' : ROOT.TFile('efficiency_ZToJPsiGamma.root')
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


def plotEff(file, configNames, egCut):
	ROOT.gROOT.Reset()
	c1 = ROOT.TCanvas("c1","c1",200,10,1050,750);
	leg = ROOT.TLegend(0.9-.38,0.7,0.9,0.9);

	for index, config in enumerate(configNames):
		histo = effFiles[file].Get(config).Get("h_L1HLTRECO_"+config+"_EG_"+str(egCut))
		histo.Scale( 1./(effFiles[file].Get(config).Get("h_nEvtsHLTRECO_"+config).GetBinContent(1) ) )
		histo.SetTitle("")
		histo.SetMarkerStyle(24)
		histo.SetMarkerColor(index+1)
		histo.SetMinimum(0.0);
		histo.SetMaximum(1.15);
		histo.GetXaxis().SetRangeUser(0.0, 40.0)
  		leg.AddEntry(histo,translateConfigNameToLegend(config, egCut));
		histo.Draw("same")
		# print "oi"
		# histo.Print()
 
	# leg->SetHeader("The Legend Title","C"); // option "C" allows to center the header
	# leg->AddEntry(h1,"Histogram filled with random numbers","f");
	# leg->AddEntry("f1","Function abs(#frac{sin(x)}{x})","l");
	# leg->AddEntry("gr","Graph with error bars","lep");
	leg.Draw();
	c1.Update()
	c1.SaveAs("l1Plots/"+file+"/h_L1HLTRECO_EG_"+str(egCut)+".pdf");
	c1.SaveAs("l1Plots/"+file+"/h_L1HLTRECO_EG_"+str(egCut)+".png");

# loop over datasets file
os.system("rm -rf l1Plots ; mkdir l1Plots")
for file_ in effFiles:
	os.system("mkdir l1Plots/"+file_)
	for egCut in range(51):
		plotEff(file_, configNames, egCut)

