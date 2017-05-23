#!/usr/bin/env python


# from  ROOT import *
import sys, math, csv, os, ROOT
from array import array


ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(1)
ROOT.TH1.SetDefaultSumw2(True)
ROOT.gStyle.SetOptStat(0)
# ROOT.gStyle.SetPalette(ROOT.kBird)


ratesToPlot = {}
with open(sys.argv[1], 'rb') as csvfile:	
	reader = csv.DictReader(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		# print row
		ratesToPlot.update({row["HLT Path"] : [float(row["Rate_2p0E34"]), float(row["Rate_2p0E34 Error"])]})

effsToPlot = {}
with open(sys.argv[2], 'rb') as csvfile:	
	reader = csv.DictReader(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		# print row
		effsToPlot.update({row["HLT Path"] : [float(row["Efficiency"]), float(row["Efficiency_Error"])]})


def plotRateEff(ratesToPlot, effsToPlot, minRate, maxRate, minEff, maxEff):
	ROOT.gROOT.Reset()
	# c1 = ROOT.TCanvas("c1","c1",200,10,1050,750)
	c1 = ROOT.TCanvas("c1","c1",4000,2350)
	# c1.DrawFrame(minEff-0.1, minRate-0.1, maxEff+0.1, maxRate+0.1);				
	baseGraph = ROOT.TMultiGraph();

	index = 0
	for config in effsToPlot:
		if config in ratesToPlot:
			rate = ratesToPlot[config][0]
			ratesError = ratesToPlot[config][1]
			efficiency = effsToPlot[config][0]
			efficiencyError = effsToPlot[config][1]

			if ((minEff <= efficiency <= maxEff) and (minRate <= rate <= maxRate)):
				index += 1
				# print efficiency, rate
				x = [efficiency]
				y = [rate]
				ex = [0]
				ey = [ratesError]
				# gr = ROOT.TGraphErrors(len(x),array('d',x),array('d',y),array('d',ex),array('d',ey))
				gr = ROOT.TGraphErrors(len(x),array('d',x),array('d',y))
				gr.SetTitle(config)
				if (index == 10): index += 1
				gr.SetMarkerColor(index)
				gr.SetMarkerStyle(20)
				gr.SetMarkerSize(4)
				gr.SetLineColor(0)
				gr.SetFillColor(0)
				baseGraph.Add(gr,"PMC");
				# gr.SetTitle("")
				# gr.GetXaxis().SetTitle("Efficiency")
				# gr.GetYaxis().SetTitle("Unprescaled Rate (at 2E34 cm^-2 s^-1) [Hz]")
				# gr.GetXaxis().SetRangeUser(minEff-0.1, maxEff+0.1)
				# gr.GetYaxis().SetRangeUser(minRate-0.1, maxRate+0.1)
				# gr.SetMarkerColor(index+1)
				# gr.SetMarkerColor(ROOT.kBlue)
				# gr.SetMarkerStyle(20)
				# gr.Draw("P")
	baseGraph.SetTitle("; Efficiency ; Unprescaled Rate (at 2E34 cm^-2 s^-1) [Hz]")
	baseGraph.Draw("A PMC")
	# ROOT.TGaxis.SetMaxDigits(2)
	ROOT.gPad.BuildLegend(0.6,0.10,1,0.9)
	ROOT.gStyle.SetLegendTextSize(0.025)
	ROOT.gStyle.SetOptTitle(0)
	# title = ROOT.TPaveLabel(.11,.95,.35,.99,"new title","brndc")
	# title.Draw()
	# c1.Range(0.6221116,0.8803213,0.8752612,5.375513)
   	c1.SetRightMargin(0.4)
   	c1.SetGrid()
	c1.Update()
	c1.SaveAs("hltRatesEffTree/ratesEffPlot_"+str(minRate)+"_"+str(maxRate)+"_"+str(minEff)+"_"+str(maxEff)+".png")
	c1.SaveAs("hltRatesEffTree/ratesEffPlot_"+str(minRate)+"_"+str(maxRate)+"_"+str(minEff)+"_"+str(maxEff)+".pdf")
	# c1.SaveAs("hltRatesEffTree/ratesEffPlot_"+str(minRate)+"_"+str(maxRate)+"_"+str(minEff)+"_"+str(maxEff)+".root")
	# c1.SaveAs("hltRatesEffTree/ratesEffPlot_"+str(minRate)+"_"+str(maxRate)+"_"+str(minEff)+"_"+str(maxEff)+".svg")

os.system("rm -rf hltRatesEffTree ; mkdir hltRatesEffTree")

# plotRateEff(ratesToPlot, effsToPlot, 0.1, 30.0, 0.0, 1.0)
# # plotRateEff(ratesToPlot, effsToPlot, 0.1, 10.0, 0.5, 1.0)
# plotRateEff(ratesToPlot, effsToPlot, 0.1, 18.0, 0.6, 1.0)
# plotRateEff(ratesToPlot, effsToPlot, 0.1, 4.5, 0.6, 1.0)
# plotRateEff(ratesToPlot, effsToPlot, 0.1, 4.5, 0.71, 1.0)

plotRateEff(ratesToPlot, effsToPlot, 0.0, 30.0, 0.0, 1.0)

plotRateEff(ratesToPlot, effsToPlot, 0.1, 3.0, 0.1, 1.0)

plotRateEff(ratesToPlot, effsToPlot, 1.5, 2.0, 0.65, 1.0)

plotRateEff(ratesToPlot, effsToPlot, 1.5, 2.0, 0.7, 1.0)

plotRateEff(ratesToPlot, effsToPlot, 1.5, 2.0, 0.76, 1.0)

plotRateEff(ratesToPlot, effsToPlot, 1.45, 2.0, 0.76, 1.0)

plotRateEff(ratesToPlot, effsToPlot, 1.5, 3.0, 0.76, 1.0)

plotRateEff(ratesToPlot, effsToPlot, 0.0, 2.0, 0.73, 1.0)








