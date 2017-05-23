#!/usr/bin/env python

"""
Plotter for EffTriggerAna
"""

import ROOT, os, math
import csv

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(1)
ROOT.TH1.SetDefaultSumw2(True)
ROOT.gStyle.SetOptStat(0)


def plotEff(numerator,denominator,configName, effName, saveDir, fileToWrite):
	ROOT.gROOT.Reset()
	c1 = ROOT.TCanvas("c1","c1",200,10,1050,750)

	numClone = numerator.Clone()
	denClone = denominator.Clone()
	# if (effName != "total" and effName != "2d"):
		# numClone.Rebin(2)
		# denClone.Rebin(2)

	# if (effName == "2d"):
		# numClone.Rebin2D(2)
		# denClone.Rebin2D(2)

	# numClone.Print("base")
	# denClone.Print("base")
	
	h_Eff = ROOT.TEfficiency(numClone,denClone)
	if (effName == "2d"):
		h_Eff.Draw("COLZ")
	else:
		h_Eff.Draw("AP")
	c1.Update()

	if (effName == "purity"):
		h_Eff.SetTitle(configName+";  ; Purity")
		h_Eff.GetPaintedGraph().GetYaxis().SetRangeUser(0.0, 1.05)
		fileToWrite.write(configName+": "+str(h_Eff.GetEfficiency(1))+"\n") 

	if (effName == "total"):
		h_Eff.SetTitle(configName+";  ; Efficiency")
		h_Eff.GetPaintedGraph().GetYaxis().SetRangeUser(0.0, 1.05)
		fileToWrite.write(configName+": "+str(h_Eff.GetEfficiency(1))+"\n")

	if (effName == "muon"):
		h_Eff.SetTitle(configName+"; Leading Muon pT (GeV) ; Efficiency")
		h_Eff.GetPaintedGraph().GetXaxis().SetRangeUser(0.0, 45.0)
		h_Eff.GetPaintedGraph().GetYaxis().SetRangeUser(0.0, 1.05)

	if (effName == "photon"):
		h_Eff.SetTitle(configName+";  Photon pT (GeV) ; Efficiency")
		h_Eff.GetPaintedGraph().GetXaxis().SetRangeUser(0.0, 60.0)
		h_Eff.GetPaintedGraph().GetYaxis().SetRangeUser(0.0, 1.05)

	if (effName == "2d"):
		h_Eff.SetTitle(configName+";  Photon pT (GeV) ; Leading Muon pT (GeV)")
		# h_Eff.GetPaintedGraph().SetRangeUser(0.0, 60.0)
		h_Eff.GetPaintedHistogram().GetXaxis().SetRangeUser(0.0, 60.0)
		h_Eff.GetPaintedHistogram().GetYaxis().SetRangeUser(0.0, 45.0)

	c1.Update()
	c1.SaveAs(saveDir+"/"+configName+"/"+effName+"_"+configName+".png")





# cuts
AND = " && "

# hltCut = "hlTrigger.TestBitNumber(2)"
hltCut = {
	"HLT_DoubleMu5_5_Mass0to30_Photon12_v1" : "hlTrigger.TestBitNumber(1)",
	"HLT_DoubleMu5_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(2)",
	"HLT_DoubleMu6_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(3)",
	"HLT_DoubleMu7_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(4)",
	"HLT_DoubleMu8_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(5)",
	"HLT_DoubleMu9_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(6)",
	"HLT_DoubleMu12_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(7)",
	"HLT_DoubleMu13_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(8)",
	"HLT_DoubleMu13_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(9)",
	"HLT_DoubleMu14_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(10)",
	"HLT_DoubleMu14_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(11)",
	"HLT_DoubleMu14_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(12)",
	"HLT_DoubleMu15_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(13)",
	"HLT_DoubleMu15_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(14)",
	"HLT_DoubleMu15_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(15)",
	"HLT_DoubleMu15_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(16)",
	"HLT_DoubleMu16_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(17)",
	"HLT_DoubleMu16_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(18)",
	"HLT_DoubleMu16_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(19)",
	"HLT_DoubleMu16_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(20)",
	"HLT_DoubleMu16_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(21)",
	"HLT_DoubleMu17_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(22)",
	"HLT_DoubleMu17_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(23)",
	"HLT_DoubleMu17_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(24)",
	"HLT_DoubleMu17_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(25)",
	"HLT_DoubleMu17_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(26)",
	"HLT_DoubleMu18_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(27)",
	"HLT_DoubleMu18_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(28)",
	"HLT_DoubleMu18_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(29)",
	"HLT_DoubleMu18_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(30)",
	"HLT_DoubleMu18_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(31)",
	"HLT_DoubleMu19_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(32)",
	"HLT_DoubleMu19_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(33)",
	"HLT_DoubleMu19_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(34)",
	"HLT_DoubleMu19_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(35)",
	"HLT_DoubleMu19_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(36)",
	"HLT_DoubleMu20_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(37)",
	"HLT_DoubleMu20_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(38)",
	"HLT_DoubleMu20_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(39)",
	"HLT_DoubleMu20_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(40)",
	"HLT_DoubleMu20_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(41)",
	"HLT_DoubleMu21_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(42)",
	"HLT_DoubleMu21_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(43)",
	"HLT_DoubleMu21_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(44)",
	"HLT_DoubleMu21_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(45)",
	"HLT_DoubleMu21_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(46)",
	"HLT_DoubleMu22_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(47)",
	"HLT_DoubleMu22_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(48)",
	"HLT_DoubleMu22_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(49)",
	"HLT_DoubleMu22_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(50)",
	"HLT_DoubleMu22_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(51)",
	"HLT_DoubleMu23_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(52)",
	"HLT_DoubleMu23_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(53)",
	"HLT_DoubleMu23_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(54)",
	"HLT_DoubleMu23_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(55)",
	"HLT_DoubleMu23_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(56)",
	"HLT_DoubleMu24_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(57)",
	"HLT_DoubleMu24_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(58)",
	"HLT_DoubleMu24_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(59)",
	"HLT_DoubleMu24_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(60)",
	"HLT_DoubleMu24_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(61)",
	"HLT_DoubleMu25_5_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(62)",
	"HLT_DoubleMu25_6_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(63)",
	"HLT_DoubleMu25_7_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(64)",
	"HLT_DoubleMu25_8_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(65)",
	"HLT_DoubleMu25_9_Mass0to30_Photon14_v1" : "hlTrigger.TestBitNumber(66)",
	"HLT_DoubleMu5_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(67)",
	"HLT_DoubleMu6_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(68)",
	"HLT_DoubleMu7_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(69)",
	"HLT_DoubleMu8_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(70)",
	"HLT_DoubleMu9_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(71)",
	"HLT_DoubleMu12_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(72)",
	"HLT_DoubleMu13_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(73)",
	"HLT_DoubleMu13_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(74)",
	"HLT_DoubleMu14_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(75)",
	"HLT_DoubleMu14_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(76)",
	"HLT_DoubleMu14_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(77)",
	"HLT_DoubleMu15_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(78)",
	"HLT_DoubleMu15_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(79)",
	"HLT_DoubleMu15_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(80)",
	"HLT_DoubleMu15_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(81)",
	"HLT_DoubleMu16_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(82)",
	"HLT_DoubleMu16_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(83)",
	"HLT_DoubleMu16_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(84)",
	"HLT_DoubleMu16_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(85)",
	"HLT_DoubleMu16_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(86)",
	"HLT_DoubleMu17_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(87)",
	"HLT_DoubleMu17_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(88)",
	"HLT_DoubleMu17_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(89)",
	"HLT_DoubleMu17_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(90)",
	"HLT_DoubleMu17_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(91)",
	"HLT_DoubleMu18_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(92)",
	"HLT_DoubleMu18_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(93)",
	"HLT_DoubleMu18_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(94)",
	"HLT_DoubleMu18_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(95)",
	"HLT_DoubleMu18_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(96)",
	"HLT_DoubleMu19_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(97)",
	"HLT_DoubleMu19_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(98)",
	"HLT_DoubleMu19_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(99)",
	"HLT_DoubleMu19_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(100)",
	"HLT_DoubleMu19_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(101)",
	"HLT_DoubleMu20_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(102)",
	"HLT_DoubleMu20_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(103)",
	"HLT_DoubleMu20_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(104)",
	"HLT_DoubleMu20_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(105)",
	"HLT_DoubleMu20_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(106)",
	"HLT_DoubleMu21_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(107)",
	"HLT_DoubleMu21_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(108)",
	"HLT_DoubleMu21_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(109)",
	"HLT_DoubleMu21_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(110)",
	"HLT_DoubleMu21_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(111)",
	"HLT_DoubleMu22_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(112)",
	"HLT_DoubleMu22_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(113)",
	"HLT_DoubleMu22_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(114)",
	"HLT_DoubleMu22_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(115)",
	"HLT_DoubleMu22_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(116)",
	"HLT_DoubleMu23_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(117)",
	"HLT_DoubleMu23_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(118)",
	"HLT_DoubleMu23_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(119)",
	"HLT_DoubleMu23_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(120)",
	"HLT_DoubleMu23_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(121)",
	"HLT_DoubleMu24_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(122)",
	"HLT_DoubleMu24_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(123)",
	"HLT_DoubleMu24_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(124)",
	"HLT_DoubleMu24_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(125)",
	"HLT_DoubleMu24_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(126)",
	"HLT_DoubleMu25_5_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(127)",
	"HLT_DoubleMu25_6_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(128)",
	"HLT_DoubleMu25_7_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(129)",
	"HLT_DoubleMu25_8_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(130)",
	"HLT_DoubleMu25_9_Mass0to30_Photon15_v1" : "hlTrigger.TestBitNumber(131)",
	"HLT_DoubleMu5_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(132)",
	"HLT_DoubleMu6_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(133)",
	"HLT_DoubleMu7_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(134)",
	"HLT_DoubleMu8_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(135)",
	"HLT_DoubleMu9_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(136)",
	"HLT_DoubleMu12_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(137)",
	"HLT_DoubleMu13_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(138)",
	"HLT_DoubleMu13_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(139)",
	"HLT_DoubleMu14_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(140)",
	"HLT_DoubleMu14_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(141)",
	"HLT_DoubleMu14_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(142)",
	"HLT_DoubleMu15_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(143)",
	"HLT_DoubleMu15_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(144)",
	"HLT_DoubleMu15_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(145)",
	"HLT_DoubleMu15_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(146)",
	"HLT_DoubleMu16_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(147)",
	"HLT_DoubleMu16_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(148)",
	"HLT_DoubleMu16_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(149)",
	"HLT_DoubleMu16_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(150)",
	"HLT_DoubleMu16_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(151)",
	"HLT_DoubleMu17_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(152)",
	"HLT_DoubleMu17_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(153)",
	"HLT_DoubleMu17_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(154)",
	"HLT_DoubleMu17_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(155)",
	"HLT_DoubleMu17_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(156)",
	"HLT_DoubleMu18_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(157)",
	"HLT_DoubleMu18_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(158)",
	"HLT_DoubleMu18_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(159)",
	"HLT_DoubleMu18_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(160)",
	"HLT_DoubleMu18_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(161)",
	"HLT_DoubleMu19_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(162)",
	"HLT_DoubleMu19_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(163)",
	"HLT_DoubleMu19_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(164)",
	"HLT_DoubleMu19_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(165)",
	"HLT_DoubleMu19_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(166)",
	"HLT_DoubleMu20_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(167)",
	"HLT_DoubleMu20_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(168)",
	"HLT_DoubleMu20_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(169)",
	"HLT_DoubleMu20_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(170)",
	"HLT_DoubleMu20_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(171)",
	"HLT_DoubleMu21_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(172)",
	"HLT_DoubleMu21_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(173)",
	"HLT_DoubleMu21_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(174)",
	"HLT_DoubleMu21_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(175)",
	"HLT_DoubleMu21_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(176)",
	"HLT_DoubleMu22_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(177)",
	"HLT_DoubleMu22_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(178)",
	"HLT_DoubleMu22_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(179)",
	"HLT_DoubleMu22_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(180)",
	"HLT_DoubleMu22_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(181)",
	"HLT_DoubleMu23_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(182)",
	"HLT_DoubleMu23_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(183)",
	"HLT_DoubleMu23_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(184)",
	"HLT_DoubleMu23_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(185)",
	"HLT_DoubleMu23_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(186)",
	"HLT_DoubleMu24_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(187)",
	"HLT_DoubleMu24_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(188)",
	"HLT_DoubleMu24_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(189)",
	"HLT_DoubleMu24_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(190)",
	"HLT_DoubleMu24_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(191)",
	"HLT_DoubleMu25_5_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(192)",
	"HLT_DoubleMu25_6_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(193)",
	"HLT_DoubleMu25_7_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(194)",
	"HLT_DoubleMu25_8_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(195)",
	"HLT_DoubleMu25_9_Mass0to30_Photon16_v1" : "hlTrigger.TestBitNumber(196)",
	"HLT_DoubleMu5_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(197)",
	"HLT_DoubleMu6_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(198)",
	"HLT_DoubleMu7_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(199)",
	"HLT_DoubleMu8_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(200)",
	"HLT_DoubleMu9_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(201)",
	"HLT_DoubleMu12_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(202)",
	"HLT_DoubleMu13_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(203)",
	"HLT_DoubleMu13_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(204)",
	"HLT_DoubleMu14_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(205)",
	"HLT_DoubleMu14_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(206)",
	"HLT_DoubleMu14_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(207)",
	"HLT_DoubleMu15_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(208)",
	"HLT_DoubleMu15_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(209)",
	"HLT_DoubleMu15_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(210)",
	"HLT_DoubleMu15_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(211)",
	"HLT_DoubleMu16_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(212)",
	"HLT_DoubleMu16_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(213)",
	"HLT_DoubleMu16_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(214)",
	"HLT_DoubleMu16_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(215)",
	"HLT_DoubleMu16_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(216)",
	"HLT_DoubleMu17_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(217)",
	"HLT_DoubleMu17_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(218)",
	"HLT_DoubleMu17_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(219)",
	"HLT_DoubleMu17_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(220)",
	"HLT_DoubleMu17_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(221)",
	"HLT_DoubleMu18_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(222)",
	"HLT_DoubleMu18_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(223)",
	"HLT_DoubleMu18_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(224)",
	"HLT_DoubleMu18_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(225)",
	"HLT_DoubleMu18_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(226)",
	"HLT_DoubleMu19_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(227)",
	"HLT_DoubleMu19_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(228)",
	"HLT_DoubleMu19_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(229)",
	"HLT_DoubleMu19_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(230)",
	"HLT_DoubleMu19_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(231)",
	"HLT_DoubleMu20_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(232)",
	"HLT_DoubleMu20_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(233)",
	"HLT_DoubleMu20_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(234)",
	"HLT_DoubleMu20_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(235)",
	"HLT_DoubleMu20_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(236)",
	"HLT_DoubleMu21_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(237)",
	"HLT_DoubleMu21_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(238)",
	"HLT_DoubleMu21_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(239)",
	"HLT_DoubleMu21_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(240)",
	"HLT_DoubleMu21_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(241)",
	"HLT_DoubleMu22_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(242)",
	"HLT_DoubleMu22_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(243)",
	"HLT_DoubleMu22_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(244)",
	"HLT_DoubleMu22_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(245)",
	"HLT_DoubleMu22_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(246)",
	"HLT_DoubleMu23_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(247)",
	"HLT_DoubleMu23_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(248)",
	"HLT_DoubleMu23_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(249)",
	"HLT_DoubleMu23_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(250)",
	"HLT_DoubleMu23_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(251)",
	"HLT_DoubleMu24_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(252)",
	"HLT_DoubleMu24_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(253)",
	"HLT_DoubleMu24_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(254)",
	"HLT_DoubleMu24_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(255)",
	"HLT_DoubleMu24_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(256)",
	"HLT_DoubleMu25_5_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(257)",
	"HLT_DoubleMu25_6_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(258)",
	"HLT_DoubleMu25_7_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(259)",
	"HLT_DoubleMu25_8_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(260)",
	"HLT_DoubleMu25_9_Mass0to30_Photon17_v1" : "hlTrigger.TestBitNumber(261)",
	"HLT_DoubleMu5_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(262)",
	"HLT_DoubleMu6_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(263)",
	"HLT_DoubleMu7_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(264)",
	"HLT_DoubleMu8_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(265)",
	"HLT_DoubleMu9_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(266)",
	"HLT_DoubleMu12_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(267)",
	"HLT_DoubleMu13_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(268)",
	"HLT_DoubleMu13_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(269)",
	"HLT_DoubleMu14_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(270)",
	"HLT_DoubleMu14_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(271)",
	"HLT_DoubleMu14_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(272)",
	"HLT_DoubleMu15_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(273)",
	"HLT_DoubleMu15_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(274)",
	"HLT_DoubleMu15_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(275)",
	"HLT_DoubleMu15_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(276)",
	"HLT_DoubleMu16_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(277)",
	"HLT_DoubleMu16_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(278)",
	"HLT_DoubleMu16_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(279)",
	"HLT_DoubleMu16_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(280)",
	"HLT_DoubleMu16_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(281)",
	"HLT_DoubleMu17_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(282)",
	"HLT_DoubleMu17_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(283)",
	"HLT_DoubleMu17_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(284)",
	"HLT_DoubleMu17_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(285)",
	"HLT_DoubleMu17_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(286)",
	"HLT_DoubleMu18_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(287)",
	"HLT_DoubleMu18_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(288)",
	"HLT_DoubleMu18_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(289)",
	"HLT_DoubleMu18_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(290)",
	"HLT_DoubleMu18_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(291)",
	"HLT_DoubleMu19_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(292)",
	"HLT_DoubleMu19_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(293)",
	"HLT_DoubleMu19_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(294)",
	"HLT_DoubleMu19_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(295)",
	"HLT_DoubleMu19_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(296)",
	"HLT_DoubleMu20_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(297)",
	"HLT_DoubleMu20_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(298)",
	"HLT_DoubleMu20_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(299)",
	"HLT_DoubleMu20_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(300)",
	"HLT_DoubleMu20_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(301)",
	"HLT_DoubleMu21_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(302)",
	"HLT_DoubleMu21_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(303)",
	"HLT_DoubleMu21_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(304)",
	"HLT_DoubleMu21_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(305)",
	"HLT_DoubleMu21_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(306)",
	"HLT_DoubleMu22_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(307)",
	"HLT_DoubleMu22_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(308)",
	"HLT_DoubleMu22_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(309)",
	"HLT_DoubleMu22_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(310)",
	"HLT_DoubleMu22_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(311)",
	"HLT_DoubleMu23_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(312)",
	"HLT_DoubleMu23_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(313)",
	"HLT_DoubleMu23_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(314)",
	"HLT_DoubleMu23_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(315)",
	"HLT_DoubleMu23_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(316)",
	"HLT_DoubleMu24_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(317)",
	"HLT_DoubleMu24_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(318)",
	"HLT_DoubleMu24_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(319)",
	"HLT_DoubleMu24_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(320)",
	"HLT_DoubleMu24_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(321)",
	"HLT_DoubleMu25_5_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(322)",
	"HLT_DoubleMu25_6_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(323)",
	"HLT_DoubleMu25_7_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(324)",
	"HLT_DoubleMu25_8_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(325)",
	"HLT_DoubleMu25_9_Mass0to30_Photon18_v1" : "hlTrigger.TestBitNumber(326)",
	"HLT_DoubleMu5_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(327)",
	"HLT_DoubleMu6_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(328)",
	"HLT_DoubleMu7_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(329)",
	"HLT_DoubleMu8_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(330)",
	"HLT_DoubleMu9_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(331)",
	"HLT_DoubleMu12_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(332)",
	"HLT_DoubleMu13_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(333)",
	"HLT_DoubleMu13_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(334)",
	"HLT_DoubleMu14_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(335)",
	"HLT_DoubleMu14_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(336)",
	"HLT_DoubleMu14_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(337)",
	"HLT_DoubleMu15_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(338)",
	"HLT_DoubleMu15_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(339)",
	"HLT_DoubleMu15_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(340)",
	"HLT_DoubleMu15_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(341)",
	"HLT_DoubleMu16_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(342)",
	"HLT_DoubleMu16_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(343)",
	"HLT_DoubleMu16_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(344)",
	"HLT_DoubleMu16_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(345)",
	"HLT_DoubleMu16_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(346)",
	"HLT_DoubleMu17_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(347)",
	"HLT_DoubleMu17_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(348)",
	"HLT_DoubleMu17_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(349)",
	"HLT_DoubleMu17_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(350)",
	"HLT_DoubleMu17_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(351)",
	"HLT_DoubleMu18_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(352)",
	"HLT_DoubleMu18_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(353)",
	"HLT_DoubleMu18_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(354)",
	"HLT_DoubleMu18_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(355)",
	"HLT_DoubleMu18_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(356)",
	"HLT_DoubleMu19_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(357)",
	"HLT_DoubleMu19_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(358)",
	"HLT_DoubleMu19_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(359)",
	"HLT_DoubleMu19_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(360)",
	"HLT_DoubleMu19_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(361)",
	"HLT_DoubleMu20_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(362)",
	"HLT_DoubleMu20_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(363)",
	"HLT_DoubleMu20_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(364)",
	"HLT_DoubleMu20_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(365)",
	"HLT_DoubleMu20_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(366)",
	"HLT_DoubleMu21_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(367)",
	"HLT_DoubleMu21_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(368)",
	"HLT_DoubleMu21_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(369)",
	"HLT_DoubleMu21_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(370)",
	"HLT_DoubleMu21_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(371)",
	"HLT_DoubleMu22_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(372)",
	"HLT_DoubleMu22_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(373)",
	"HLT_DoubleMu22_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(374)",
	"HLT_DoubleMu22_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(375)",
	"HLT_DoubleMu22_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(376)",
	"HLT_DoubleMu23_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(377)",
	"HLT_DoubleMu23_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(378)",
	"HLT_DoubleMu23_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(379)",
	"HLT_DoubleMu23_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(380)",
	"HLT_DoubleMu23_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(381)",
	"HLT_DoubleMu24_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(382)",
	"HLT_DoubleMu24_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(383)",
	"HLT_DoubleMu24_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(384)",
	"HLT_DoubleMu24_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(385)",
	"HLT_DoubleMu24_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(386)",
	"HLT_DoubleMu25_5_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(387)",
	"HLT_DoubleMu25_6_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(388)",
	"HLT_DoubleMu25_7_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(389)",
	"HLT_DoubleMu25_8_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(390)",
	"HLT_DoubleMu25_9_Mass0to30_Photon19_v1" : "hlTrigger.TestBitNumber(391)",
	"HLT_DoubleMu5_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(392)",
	"HLT_DoubleMu6_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(393)",
	"HLT_DoubleMu7_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(394)",
	"HLT_DoubleMu8_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(395)",
	"HLT_DoubleMu9_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(396)",
	"HLT_DoubleMu12_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(397)",
	"HLT_DoubleMu13_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(398)",
	"HLT_DoubleMu13_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(399)",
	"HLT_DoubleMu14_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(400)",
	"HLT_DoubleMu14_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(401)",
	"HLT_DoubleMu14_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(402)",
	"HLT_DoubleMu15_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(403)",
	"HLT_DoubleMu15_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(404)",
	"HLT_DoubleMu15_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(405)",
	"HLT_DoubleMu15_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(406)",
	"HLT_DoubleMu16_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(407)",
	"HLT_DoubleMu16_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(408)",
	"HLT_DoubleMu16_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(409)",
	"HLT_DoubleMu16_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(410)",
	"HLT_DoubleMu16_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(411)",
	"HLT_DoubleMu17_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(412)",
	"HLT_DoubleMu17_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(413)",
	"HLT_DoubleMu17_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(414)",
	"HLT_DoubleMu17_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(415)",
	"HLT_DoubleMu17_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(416)",
	"HLT_DoubleMu18_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(417)",
	"HLT_DoubleMu18_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(418)",
	"HLT_DoubleMu18_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(419)",
	"HLT_DoubleMu18_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(420)",
	"HLT_DoubleMu18_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(421)",
	"HLT_DoubleMu19_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(422)",
	"HLT_DoubleMu19_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(423)",
	"HLT_DoubleMu19_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(424)",
	"HLT_DoubleMu19_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(425)",
	"HLT_DoubleMu19_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(426)",
	"HLT_DoubleMu20_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(427)",
	"HLT_DoubleMu20_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(428)",
	"HLT_DoubleMu20_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(429)",
	"HLT_DoubleMu20_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(430)",
	"HLT_DoubleMu20_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(431)",
	"HLT_DoubleMu21_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(432)",
	"HLT_DoubleMu21_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(433)",
	"HLT_DoubleMu21_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(434)",
	"HLT_DoubleMu21_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(435)",
	"HLT_DoubleMu21_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(436)",
	"HLT_DoubleMu22_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(437)",
	"HLT_DoubleMu22_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(438)",
	"HLT_DoubleMu22_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(439)",
	"HLT_DoubleMu22_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(440)",
	"HLT_DoubleMu22_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(441)",
	"HLT_DoubleMu23_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(442)",
	"HLT_DoubleMu23_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(443)",
	"HLT_DoubleMu23_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(444)",
	"HLT_DoubleMu23_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(445)",
	"HLT_DoubleMu23_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(446)",
	"HLT_DoubleMu24_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(447)",
	"HLT_DoubleMu24_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(448)",
	"HLT_DoubleMu24_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(449)",
	"HLT_DoubleMu24_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(450)",
	"HLT_DoubleMu24_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(451)",
	"HLT_DoubleMu25_5_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(452)",
	"HLT_DoubleMu25_6_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(453)",
	"HLT_DoubleMu25_7_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(454)",
	"HLT_DoubleMu25_8_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(455)",
	"HLT_DoubleMu25_9_Mass0to30_Photon20_v1" : "hlTrigger.TestBitNumber(456)",
	"HLT_DoubleMu5_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(457)",
	"HLT_DoubleMu6_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(458)",
	"HLT_DoubleMu7_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(459)",
	"HLT_DoubleMu8_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(460)",
	"HLT_DoubleMu9_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(461)",
	"HLT_DoubleMu12_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(462)",
	"HLT_DoubleMu13_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(463)",
	"HLT_DoubleMu13_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(464)",
	"HLT_DoubleMu14_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(465)",
	"HLT_DoubleMu14_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(466)",
	"HLT_DoubleMu14_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(467)",
	"HLT_DoubleMu15_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(468)",
	"HLT_DoubleMu15_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(469)",
	"HLT_DoubleMu15_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(470)",
	"HLT_DoubleMu15_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(471)",
	"HLT_DoubleMu16_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(472)",
	"HLT_DoubleMu16_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(473)",
	"HLT_DoubleMu16_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(474)",
	"HLT_DoubleMu16_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(475)",
	"HLT_DoubleMu16_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(476)",
	"HLT_DoubleMu17_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(477)",
	"HLT_DoubleMu17_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(478)",
	"HLT_DoubleMu17_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(479)",
	"HLT_DoubleMu17_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(480)",
	"HLT_DoubleMu17_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(481)",
	"HLT_DoubleMu18_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(482)",
	"HLT_DoubleMu18_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(483)",
	"HLT_DoubleMu18_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(484)",
	"HLT_DoubleMu18_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(485)",
	"HLT_DoubleMu18_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(486)",
	"HLT_DoubleMu19_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(487)",
	"HLT_DoubleMu19_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(488)",
	"HLT_DoubleMu19_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(489)",
	"HLT_DoubleMu19_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(490)",
	"HLT_DoubleMu19_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(491)",
	"HLT_DoubleMu20_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(492)",
	"HLT_DoubleMu20_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(493)",
	"HLT_DoubleMu20_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(494)",
	"HLT_DoubleMu20_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(495)",
	"HLT_DoubleMu20_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(496)",
	"HLT_DoubleMu21_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(497)",
	"HLT_DoubleMu21_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(498)",
	"HLT_DoubleMu21_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(499)",
	"HLT_DoubleMu21_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(500)",
	"HLT_DoubleMu21_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(501)",
	"HLT_DoubleMu22_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(502)",
	"HLT_DoubleMu22_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(503)",
	"HLT_DoubleMu22_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(504)",
	"HLT_DoubleMu22_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(505)",
	"HLT_DoubleMu22_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(506)",
	"HLT_DoubleMu23_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(507)",
	"HLT_DoubleMu23_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(508)",
	"HLT_DoubleMu23_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(509)",
	"HLT_DoubleMu23_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(510)",
	"HLT_DoubleMu23_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(511)",
	"HLT_DoubleMu24_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(512)",
	"HLT_DoubleMu24_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(513)",
	"HLT_DoubleMu24_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(514)",
	"HLT_DoubleMu24_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(515)",
	"HLT_DoubleMu24_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(516)",
	"HLT_DoubleMu25_5_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(517)",
	"HLT_DoubleMu25_6_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(518)",
	"HLT_DoubleMu25_7_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(519)",
	"HLT_DoubleMu25_8_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(520)",
	"HLT_DoubleMu25_9_Mass0to30_Photon21_v1" : "hlTrigger.TestBitNumber(521)",
	"HLT_DoubleMu5_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(522)",
	"HLT_DoubleMu6_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(523)",
	"HLT_DoubleMu7_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(524)",
	"HLT_DoubleMu8_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(525)",
	"HLT_DoubleMu9_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(526)",
	"HLT_DoubleMu12_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(527)",
	"HLT_DoubleMu13_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(528)",
	"HLT_DoubleMu13_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(529)",
	"HLT_DoubleMu14_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(530)",
	"HLT_DoubleMu14_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(531)",
	"HLT_DoubleMu14_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(532)",
	"HLT_DoubleMu15_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(533)",
	"HLT_DoubleMu15_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(534)",
	"HLT_DoubleMu15_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(535)",
	"HLT_DoubleMu15_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(536)",
	"HLT_DoubleMu16_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(537)",
	"HLT_DoubleMu16_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(538)",
	"HLT_DoubleMu16_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(539)",
	"HLT_DoubleMu16_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(540)",
	"HLT_DoubleMu16_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(541)",
	"HLT_DoubleMu17_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(542)",
	"HLT_DoubleMu17_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(543)",
	"HLT_DoubleMu17_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(544)",
	"HLT_DoubleMu17_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(545)",
	"HLT_DoubleMu17_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(546)",
	"HLT_DoubleMu18_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(547)",
	"HLT_DoubleMu18_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(548)",
	"HLT_DoubleMu18_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(549)",
	"HLT_DoubleMu18_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(550)",
	"HLT_DoubleMu18_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(551)",
	"HLT_DoubleMu19_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(552)",
	"HLT_DoubleMu19_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(553)",
	"HLT_DoubleMu19_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(554)",
	"HLT_DoubleMu19_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(555)",
	"HLT_DoubleMu19_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(556)",
	"HLT_DoubleMu20_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(557)",
	"HLT_DoubleMu20_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(558)",
	"HLT_DoubleMu20_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(559)",
	"HLT_DoubleMu20_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(560)",
	"HLT_DoubleMu20_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(561)",
	"HLT_DoubleMu21_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(562)",
	"HLT_DoubleMu21_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(563)",
	"HLT_DoubleMu21_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(564)",
	"HLT_DoubleMu21_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(565)",
	"HLT_DoubleMu21_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(566)",
	"HLT_DoubleMu22_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(567)",
	"HLT_DoubleMu22_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(568)",
	"HLT_DoubleMu22_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(569)",
	"HLT_DoubleMu22_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(570)",
	"HLT_DoubleMu22_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(571)",
	"HLT_DoubleMu23_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(572)",
	"HLT_DoubleMu23_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(573)",
	"HLT_DoubleMu23_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(574)",
	"HLT_DoubleMu23_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(575)",
	"HLT_DoubleMu23_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(576)",
	"HLT_DoubleMu24_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(577)",
	"HLT_DoubleMu24_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(578)",
	"HLT_DoubleMu24_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(579)",
	"HLT_DoubleMu24_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(580)",
	"HLT_DoubleMu24_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(581)",
	"HLT_DoubleMu25_5_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(582)",
	"HLT_DoubleMu25_6_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(583)",
	"HLT_DoubleMu25_7_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(584)",
	"HLT_DoubleMu25_8_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(585)",
	"HLT_DoubleMu25_9_Mass0to30_Photon22_v1" : "hlTrigger.TestBitNumber(586)",
	"HLT_DoubleMu5_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(587)",
	"HLT_DoubleMu6_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(588)",
	"HLT_DoubleMu7_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(589)",
	"HLT_DoubleMu8_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(590)",
	"HLT_DoubleMu9_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(591)",
	"HLT_DoubleMu12_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(592)",
	"HLT_DoubleMu13_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(593)",
	"HLT_DoubleMu13_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(594)",
	"HLT_DoubleMu14_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(595)",
	"HLT_DoubleMu14_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(596)",
	"HLT_DoubleMu14_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(597)",
	"HLT_DoubleMu15_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(598)",
	"HLT_DoubleMu15_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(599)",
	"HLT_DoubleMu15_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(600)",
	"HLT_DoubleMu15_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(601)",
	"HLT_DoubleMu16_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(602)",
	"HLT_DoubleMu16_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(603)",
	"HLT_DoubleMu16_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(604)",
	"HLT_DoubleMu16_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(605)",
	"HLT_DoubleMu16_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(606)",
	"HLT_DoubleMu17_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(607)",
	"HLT_DoubleMu17_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(608)",
	"HLT_DoubleMu17_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(609)",
	"HLT_DoubleMu17_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(610)",
	"HLT_DoubleMu17_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(611)",
	"HLT_DoubleMu18_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(612)",
	"HLT_DoubleMu18_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(613)",
	"HLT_DoubleMu18_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(614)",
	"HLT_DoubleMu18_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(615)",
	"HLT_DoubleMu18_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(616)",
	"HLT_DoubleMu19_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(617)",
	"HLT_DoubleMu19_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(618)",
	"HLT_DoubleMu19_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(619)",
	"HLT_DoubleMu19_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(620)",
	"HLT_DoubleMu19_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(621)",
	"HLT_DoubleMu20_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(622)",
	"HLT_DoubleMu20_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(623)",
	"HLT_DoubleMu20_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(624)",
	"HLT_DoubleMu20_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(625)",
	"HLT_DoubleMu20_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(626)",
	"HLT_DoubleMu21_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(627)",
	"HLT_DoubleMu21_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(628)",
	"HLT_DoubleMu21_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(629)",
	"HLT_DoubleMu21_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(630)",
	"HLT_DoubleMu21_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(631)",
	"HLT_DoubleMu22_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(632)",
	"HLT_DoubleMu22_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(633)",
	"HLT_DoubleMu22_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(634)",
	"HLT_DoubleMu22_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(635)",
	"HLT_DoubleMu22_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(636)",
	"HLT_DoubleMu23_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(637)",
	"HLT_DoubleMu23_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(638)",
	"HLT_DoubleMu23_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(639)",
	"HLT_DoubleMu23_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(640)",
	"HLT_DoubleMu23_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(641)",
	"HLT_DoubleMu24_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(642)",
	"HLT_DoubleMu24_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(643)",
	"HLT_DoubleMu24_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(644)",
	"HLT_DoubleMu24_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(645)",
	"HLT_DoubleMu24_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(646)",
	"HLT_DoubleMu25_5_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(647)",
	"HLT_DoubleMu25_6_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(648)",
	"HLT_DoubleMu25_7_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(649)",
	"HLT_DoubleMu25_8_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(650)",
	"HLT_DoubleMu25_9_Mass0to30_Photon23_v1" : "hlTrigger.TestBitNumber(651)",
	"HLT_DoubleMu5_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(652)",
	"HLT_DoubleMu6_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(653)",
	"HLT_DoubleMu7_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(654)",
	"HLT_DoubleMu8_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(655)",
	"HLT_DoubleMu9_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(656)",
	"HLT_DoubleMu12_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(657)",
	"HLT_DoubleMu13_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(658)",
	"HLT_DoubleMu13_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(659)",
	"HLT_DoubleMu14_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(660)",
	"HLT_DoubleMu14_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(661)",
	"HLT_DoubleMu14_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(662)",
	"HLT_DoubleMu15_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(663)",
	"HLT_DoubleMu15_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(664)",
	"HLT_DoubleMu15_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(665)",
	"HLT_DoubleMu15_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(666)",
	"HLT_DoubleMu16_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(667)",
	"HLT_DoubleMu16_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(668)",
	"HLT_DoubleMu16_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(669)",
	"HLT_DoubleMu16_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(670)",
	"HLT_DoubleMu16_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(671)",
	"HLT_DoubleMu17_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(672)",
	"HLT_DoubleMu17_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(673)",
	"HLT_DoubleMu17_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(674)",
	"HLT_DoubleMu17_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(675)",
	"HLT_DoubleMu17_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(676)",
	"HLT_DoubleMu18_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(677)",
	"HLT_DoubleMu18_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(678)",
	"HLT_DoubleMu18_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(679)",
	"HLT_DoubleMu18_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(680)",
	"HLT_DoubleMu18_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(681)",
	"HLT_DoubleMu19_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(682)",
	"HLT_DoubleMu19_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(683)",
	"HLT_DoubleMu19_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(684)",
	"HLT_DoubleMu19_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(685)",
	"HLT_DoubleMu19_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(686)",
	"HLT_DoubleMu20_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(687)",
	"HLT_DoubleMu20_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(688)",
	"HLT_DoubleMu20_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(689)",
	"HLT_DoubleMu20_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(690)",
	"HLT_DoubleMu20_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(691)",
	"HLT_DoubleMu21_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(692)",
	"HLT_DoubleMu21_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(693)",
	"HLT_DoubleMu21_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(694)",
	"HLT_DoubleMu21_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(695)",
	"HLT_DoubleMu21_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(696)",
	"HLT_DoubleMu22_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(697)",
	"HLT_DoubleMu22_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(698)",
	"HLT_DoubleMu22_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(699)",
	"HLT_DoubleMu22_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(700)",
	"HLT_DoubleMu22_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(701)",
	"HLT_DoubleMu23_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(702)",
	"HLT_DoubleMu23_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(703)",
	"HLT_DoubleMu23_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(704)",
	"HLT_DoubleMu23_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(705)",
	"HLT_DoubleMu23_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(706)",
	"HLT_DoubleMu24_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(707)",
	"HLT_DoubleMu24_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(708)",
	"HLT_DoubleMu24_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(709)",
	"HLT_DoubleMu24_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(710)",
	"HLT_DoubleMu24_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(711)",
	"HLT_DoubleMu25_5_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(712)",
	"HLT_DoubleMu25_6_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(713)",
	"HLT_DoubleMu25_7_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(714)",
	"HLT_DoubleMu25_8_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(715)",
	"HLT_DoubleMu25_9_Mass0to30_Photon24_v1" : "hlTrigger.TestBitNumber(716)",
	"HLT_DoubleMu5_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(717)",
	"HLT_DoubleMu6_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(718)",
	"HLT_DoubleMu7_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(719)",
	"HLT_DoubleMu8_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(720)",
	"HLT_DoubleMu9_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(721)",
	"HLT_DoubleMu12_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(722)",
	"HLT_DoubleMu13_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(723)",
	"HLT_DoubleMu13_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(724)",
	"HLT_DoubleMu14_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(725)",
	"HLT_DoubleMu14_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(726)",
	"HLT_DoubleMu14_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(727)",
	"HLT_DoubleMu15_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(728)",
	"HLT_DoubleMu15_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(729)",
	"HLT_DoubleMu15_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(730)",
	"HLT_DoubleMu15_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(731)",
	"HLT_DoubleMu16_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(732)",
	"HLT_DoubleMu16_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(733)",
	"HLT_DoubleMu16_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(734)",
	"HLT_DoubleMu16_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(735)",
	"HLT_DoubleMu16_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(736)",
	"HLT_DoubleMu17_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(737)",
	"HLT_DoubleMu17_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(738)",
	"HLT_DoubleMu17_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(739)",
	"HLT_DoubleMu17_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(740)",
	"HLT_DoubleMu17_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(741)",
	"HLT_DoubleMu18_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(742)",
	"HLT_DoubleMu18_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(743)",
	"HLT_DoubleMu18_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(744)",
	"HLT_DoubleMu18_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(745)",
	"HLT_DoubleMu18_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(746)",
	"HLT_DoubleMu19_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(747)",
	"HLT_DoubleMu19_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(748)",
	"HLT_DoubleMu19_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(749)",
	"HLT_DoubleMu19_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(750)",
	"HLT_DoubleMu19_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(751)",
	"HLT_DoubleMu20_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(752)",
	"HLT_DoubleMu20_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(753)",
	"HLT_DoubleMu20_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(754)",
	"HLT_DoubleMu20_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(755)",
	"HLT_DoubleMu20_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(756)",
	"HLT_DoubleMu21_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(757)",
	"HLT_DoubleMu21_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(758)",
	"HLT_DoubleMu21_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(759)",
	"HLT_DoubleMu21_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(760)",
	"HLT_DoubleMu21_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(761)",
	"HLT_DoubleMu22_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(762)",
	"HLT_DoubleMu22_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(763)",
	"HLT_DoubleMu22_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(764)",
	"HLT_DoubleMu22_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(765)",
	"HLT_DoubleMu22_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(766)",
	"HLT_DoubleMu23_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(767)",
	"HLT_DoubleMu23_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(768)",
	"HLT_DoubleMu23_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(769)",
	"HLT_DoubleMu23_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(770)",
	"HLT_DoubleMu23_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(771)",
	"HLT_DoubleMu24_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(772)",
	"HLT_DoubleMu24_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(773)",
	"HLT_DoubleMu24_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(774)",
	"HLT_DoubleMu24_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(775)",
	"HLT_DoubleMu24_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(776)",
	"HLT_DoubleMu25_5_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(777)",
	"HLT_DoubleMu25_6_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(778)",
	"HLT_DoubleMu25_7_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(779)",
	"HLT_DoubleMu25_8_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(780)",
	"HLT_DoubleMu25_9_Mass0to30_Photon25_v1" : "hlTrigger.TestBitNumber(781)",
}




recoCut = "recoTrigger"
l1Cut = "l1Trigger"


def getEfficiency(numerator, denominator):
	numError = math.sqrt(float(numerator))
	denError = math.sqrt(float(denominator))
	value = float(numerator)/float(denominator)
	error = value*math.sqrt(( numError/numerator )**2+( denError/denominator )**2)
	# print numerator, denominator
	# print value, error
	return value, error



# loop over datasets file
os.system("rm -rf hltPlotsTree ; mkdir hltPlotsTree")
effFile = ROOT.TFile('efficiency_Tree.root')
HLTTree = effFile.HLT_Tree.Get("RECOL1HLTTree")



### RECOL1HLT / RECOL1
definition = "RECOL1HLT"
saveDir = "hltPlotsTree/"+definition 
os.system("mkdir -p "+saveDir)

# write csv file
csvFileName = "efficiencies_"+definition+".csv"
os.system("rm -rf " + saveDir+"/"+csvFileName)
with open(saveDir+"/"+csvFileName, 'wb') as csvfile:
	cvswriter = csv.writer(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	cvswriter.writerow(["HLT Path", "Efficiency", "Efficiency_Error"])
	for hltPath in hltCut:
		denominator = HLTTree.GetEntries(recoCut+AND+l1Cut)
		numerator = HLTTree.GetEntries(recoCut+AND+l1Cut+AND+hltCut[hltPath])
		eff = getEfficiency(numerator, denominator)
		# print hltPath+" = "+ str(eff[0])+" +/- "+ str(eff[1])
		cvswriter.writerow([hltPath, eff[0], eff[1]])



### RECOL1 / RECO
definition = "RECOL1"
saveDir = "hltPlotsTree/"+definition 
os.system("mkdir -p "+saveDir)

# write csv file
csvFileName = "efficiencies_"+definition+".csv"
os.system("rm -rf " + saveDir+"/"+csvFileName)
with open(saveDir+"/"+csvFileName, 'wb') as csvfile:
	cvswriter = csv.writer(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	cvswriter.writerow(["HLT Path", "Efficiency", "Efficiency_Error"])
	for hltPath in hltCut:
		denominator = HLTTree.GetEntries(recoCut)
		numerator = HLTTree.GetEntries(recoCut+AND+l1Cut)
		eff = getEfficiency(numerator, denominator)
		cvswriter.writerow([hltPath, eff[0], eff[1]])

### RECOHLT / RECO
definition = "RECOHLT"
saveDir = "hltPlotsTree/"+definition 
os.system("mkdir -p "+saveDir)

# write csv file
csvFileName = "efficiencies_"+definition+".csv"
os.system("rm -rf " + saveDir+"/"+csvFileName)
with open(saveDir+"/"+csvFileName, 'wb') as csvfile:
	cvswriter = csv.writer(csvfile, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	cvswriter.writerow(["HLT Path", "Efficiency", "Efficiency_Error"])
	for hltPath in hltCut:
		denominator = HLTTree.GetEntries(recoCut)
		numerator = HLTTree.GetEntries(recoCut+AND+hltCut[hltPath])
		eff = getEfficiency(numerator, denominator)
		cvswriter.writerow([hltPath, eff[0], eff[1]])



# print numerator



# eff_RECOHLT = open(saveDir+"/eff_RECOHLT.txt","w") 
# for configName in configSets:
# 	os.system("mkdir "+saveDir+"/"+configName)
# 	print configName

# 	# total
# 	effName = "total"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLT)
		
# 	# muon
# 	effName = "muon"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLT_Muon_pT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_Muon_pT_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLT)
		
# 	# photon
# 	effName = "photon"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLT_Photon_pT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_Photon_pT_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLT)
	
# 	# photon x muon
# 	effName = "2d"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h2_nEvtsRECOHLT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h2_nEvtsRECO_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLT)
# 	# h2_nEvtsRECOHLT_HLT_DoubleMu20_7_Mass0to30_Photon20_v1

		
# # RECOHLTMATCHMUON / RECO
# saveDir = "hltPlotsTree/RECOHLTMATCHMUON" 
# os.system("mkdir -p "+saveDir)
# eff_RECOHLTMATCHMUON = open(saveDir+"/eff_RECOHLTMATCHMUON.txt","w") 
# for configName in configSets:
# 	os.system("mkdir "+saveDir+"/"+configName)
# 	print configName

# 	# total
# 	effName = "total"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHMUON_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHMUON)
		
# 	# muon
# 	effName = "muon"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHMUON_Muon_pT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_Muon_pT_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHMUON)
		
# 	# photon
# 	effName = "photon"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHMUON_Photon_pT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_Photon_pT_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHMUON)
	
# 	# photon x muon
# 	effName = "2d"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h2_nEvtsRECOHLTMATCHMUON_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h2_nEvtsRECO_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHMUON)


# # RECOHLTMATCHPHOTON / RECO
# saveDir = "hltPlotsTree/RECOHLTMATCHPHOTON" 
# os.system("mkdir -p "+saveDir)
# eff_RECOHLTMATCHPHOTON = open(saveDir+"/eff_RECOHLTMATCHPHOTON.txt","w") 
# for configName in configSets:
# 	os.system("mkdir "+saveDir+"/"+configName)
# 	print configName

# 	# total
# 	effName = "total"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHPHOTON_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHPHOTON)
		
# 	# muon
# 	effName = "muon"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHPHOTON_Muon_pT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_Muon_pT_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHPHOTON)
		
# 	# photon
# 	effName = "photon"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHPHOTON_Photon_pT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_Photon_pT_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHPHOTON)
	
# 	# photon x muon
# 	effName = "2d"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h2_nEvtsRECOHLTMATCHPHOTON_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h2_nEvtsRECO_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHPHOTON)


# # RECOHLTMATCHMUONPHOTON / RECO
# saveDir = "hltPlotsTree/RECOHLTMATCHMUONPHOTON" 
# os.system("mkdir -p "+saveDir)
# eff_RECOHLTMATCHMUONPHOTON = open(saveDir+"/eff_RECOHLTMATCHMUONPHOTON.txt","w") 
# for configName in configSets:
# 	os.system("mkdir "+saveDir+"/"+configName)
# 	print configName

# 	# total
# 	effName = "total"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHMUONPHOTON_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHMUONPHOTON)
		
# 	# muon
# 	effName = "muon"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHMUONPHOTON_Muon_pT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_Muon_pT_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHMUONPHOTON)
		
# 	# photon
# 	effName = "photon"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLTMATCHMUONPHOTON_Photon_pT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECO_Photon_pT_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHMUONPHOTON)
	
# 	# photon x muon
# 	effName = "2d"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h2_nEvtsRECOHLTMATCHMUONPHOTON_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h2_nEvtsRECO_" + configName)
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_RECOHLTMATCHMUONPHOTON)


# # PUR = RECOHLT / ORT
# saveDir = "hltPlotsTree/PUR" 
# os.system("mkdir -p "+saveDir)
# eff_PUR = open(saveDir+"/eff_PUR.txt","w") 
# for configName in configSets:
# 	os.system("mkdir "+saveDir+"/"+configName)
# 	print configName

# 	# total
# 	effName = "purity"
# 	numerator = effFile.Get(configName+"_EffAna").Get("h_nEvtsRECOHLT_" + configName)
# 	denominator = effFile.Get(configName+"_EffAna").Get("h_nEvtsORTHLT_" + configName)
# 	# print "numerator: " + str(numerator.GetBinContent(1))
# 	# print "denominator: " + str(denominator.GetBinContent(1))
# 	plotEff(numerator, denominator, configName, effName, saveDir, eff_PUR)




