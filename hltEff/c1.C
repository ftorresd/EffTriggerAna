void c1()
{
//=========Macro generated from canvas: c1/c1
//=========  (Wed May 17 17:18:57 2017) by ROOT version6.08/06
   TCanvas *c1 = new TCanvas("c1", "c1",0,69,1440,790);
   c1->SetHighLightColor(2);
   c1->Range(0.6221116,0.8803213,0.8752612,5.375513);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetRightMargin(0.2934631);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("; Efficiency ; Unprescaled Rate (at 2E34 cm^-2 s^-1) [Hz]");
   
   Double_t Graph_fx1001[1] = {
   0.7859881};
   Double_t Graph_fy1001[1] = {
   2.28128};
   Double_t Graph_fex1001[1] = {
   0};
   Double_t Graph_fey1001[1] = {
   0};
   TGraphErrors *gre = new TGraphErrors(1,Graph_fx1001,Graph_fy1001,Graph_fex1001,Graph_fey1001);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_7_Mass0to30_Photon18_v1");
   gre->SetLineColor(0);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1001 = new TH1F("Graph_Graph1001","HLT_DoubleMu17_7_Mass0to30_Photon18_v1",100,0.6859881,1.885988);
   Graph_Graph1001->SetMinimum(2.18128);
   Graph_Graph1001->SetMaximum(3.38128);
   Graph_Graph1001->SetDirectory(0);
   Graph_Graph1001->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1001->SetLineColor(ci);
   Graph_Graph1001->GetXaxis()->SetLabelFont(42);
   Graph_Graph1001->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1001->GetXaxis()->SetTitleFont(42);
   Graph_Graph1001->GetYaxis()->SetLabelFont(42);
   Graph_Graph1001->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1001->GetYaxis()->SetTitleFont(42);
   Graph_Graph1001->GetZaxis()->SetLabelFont(42);
   Graph_Graph1001->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1001->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1001->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1001);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1002[1] = {
   0.7827449};
   Double_t Graph_fy1002[1] = {
   2.1626};
   Double_t Graph_fex1002[1] = {
   0};
   Double_t Graph_fey1002[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1002,Graph_fy1002,Graph_fex1002,Graph_fey1002);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_7_Mass0to30_Photon19_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(2);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","HLT_DoubleMu17_7_Mass0to30_Photon19_v1",100,0.6827449,1.882745);
   Graph_Graph1002->SetMinimum(2.0626);
   Graph_Graph1002->SetMaximum(3.2626);
   Graph_Graph1002->SetDirectory(0);
   Graph_Graph1002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1002->SetLineColor(ci);
   Graph_Graph1002->GetXaxis()->SetLabelFont(42);
   Graph_Graph1002->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetXaxis()->SetTitleFont(42);
   Graph_Graph1002->GetYaxis()->SetLabelFont(42);
   Graph_Graph1002->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetYaxis()->SetTitleFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1002->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1002->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1002);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1003[1] = {
   0.7843665};
   Double_t Graph_fy1003[1] = {
   2.91038};
   Double_t Graph_fex1003[1] = {
   0};
   Double_t Graph_fey1003[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1003,Graph_fy1003,Graph_fex1003,Graph_fey1003);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_6_Mass0to30_Photon19_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(3);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1003 = new TH1F("Graph_Graph1003","HLT_DoubleMu17_6_Mass0to30_Photon19_v1",100,0.6843665,1.884366);
   Graph_Graph1003->SetMinimum(2.81038);
   Graph_Graph1003->SetMaximum(4.01038);
   Graph_Graph1003->SetDirectory(0);
   Graph_Graph1003->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1003->SetLineColor(ci);
   Graph_Graph1003->GetXaxis()->SetLabelFont(42);
   Graph_Graph1003->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1003->GetXaxis()->SetTitleFont(42);
   Graph_Graph1003->GetYaxis()->SetLabelFont(42);
   Graph_Graph1003->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1003->GetYaxis()->SetTitleFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1003->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1003->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1003);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1004[1] = {
   0.7171077};
   Double_t Graph_fy1004[1] = {
   1.77749};
   Double_t Graph_fex1004[1] = {
   0};
   Double_t Graph_fey1004[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1004,Graph_fy1004,Graph_fex1004,Graph_fey1004);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_8_Mass0to30_Photon19_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1004 = new TH1F("Graph_Graph1004","HLT_DoubleMu17_8_Mass0to30_Photon19_v1",100,0.6171077,1.817108);
   Graph_Graph1004->SetMinimum(1.67749);
   Graph_Graph1004->SetMaximum(2.87749);
   Graph_Graph1004->SetDirectory(0);
   Graph_Graph1004->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1004->SetLineColor(ci);
   Graph_Graph1004->GetXaxis()->SetLabelFont(42);
   Graph_Graph1004->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1004->GetXaxis()->SetTitleFont(42);
   Graph_Graph1004->GetYaxis()->SetLabelFont(42);
   Graph_Graph1004->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1004->GetYaxis()->SetTitleFont(42);
   Graph_Graph1004->GetZaxis()->SetLabelFont(42);
   Graph_Graph1004->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1004->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1004->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1004);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1005[1] = {
   0.6594678};
   Double_t Graph_fy1005[1] = {
   1.70401};
   Double_t Graph_fex1005[1] = {
   0};
   Double_t Graph_fey1005[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1005,Graph_fy1005,Graph_fex1005,Graph_fey1005);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_9_Mass0to30_Photon17_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(5);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1005 = new TH1F("Graph_Graph1005","HLT_DoubleMu17_9_Mass0to30_Photon17_v1",100,0.5594678,1.759468);
   Graph_Graph1005->SetMinimum(1.60401);
   Graph_Graph1005->SetMaximum(2.80401);
   Graph_Graph1005->SetDirectory(0);
   Graph_Graph1005->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1005->SetLineColor(ci);
   Graph_Graph1005->GetXaxis()->SetLabelFont(42);
   Graph_Graph1005->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1005->GetXaxis()->SetTitleFont(42);
   Graph_Graph1005->GetYaxis()->SetLabelFont(42);
   Graph_Graph1005->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1005->GetYaxis()->SetTitleFont(42);
   Graph_Graph1005->GetZaxis()->SetLabelFont(42);
   Graph_Graph1005->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1005->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1005->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1005);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1006[1] = {
   0.7939854};
   Double_t Graph_fy1006[1] = {
   4.76547};
   Double_t Graph_fex1006[1] = {
   0};
   Double_t Graph_fey1006[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1006,Graph_fy1006,Graph_fex1006,Graph_fey1006);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_5_Mass0to30_Photon16_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(6);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1006 = new TH1F("Graph_Graph1006","HLT_DoubleMu17_5_Mass0to30_Photon16_v1",100,0.6939854,1.893985);
   Graph_Graph1006->SetMinimum(4.66547);
   Graph_Graph1006->SetMaximum(5.86547);
   Graph_Graph1006->SetDirectory(0);
   Graph_Graph1006->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1006->SetLineColor(ci);
   Graph_Graph1006->GetXaxis()->SetLabelFont(42);
   Graph_Graph1006->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1006->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1006->GetXaxis()->SetTitleFont(42);
   Graph_Graph1006->GetYaxis()->SetLabelFont(42);
   Graph_Graph1006->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1006->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1006->GetYaxis()->SetTitleFont(42);
   Graph_Graph1006->GetZaxis()->SetLabelFont(42);
   Graph_Graph1006->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1006->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1006->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1006);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1007[1] = {
   0.6615317};
   Double_t Graph_fy1007[1] = {
   1.76067};
   Double_t Graph_fex1007[1] = {
   0};
   Double_t Graph_fey1007[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1007,Graph_fy1007,Graph_fex1007,Graph_fey1007);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_9_Mass0to30_Photon16_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(7);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1007 = new TH1F("Graph_Graph1007","HLT_DoubleMu17_9_Mass0to30_Photon16_v1",100,0.5615317,1.761532);
   Graph_Graph1007->SetMinimum(1.66067);
   Graph_Graph1007->SetMaximum(2.86067);
   Graph_Graph1007->SetDirectory(0);
   Graph_Graph1007->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1007->SetLineColor(ci);
   Graph_Graph1007->GetXaxis()->SetLabelFont(42);
   Graph_Graph1007->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1007->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1007->GetXaxis()->SetTitleFont(42);
   Graph_Graph1007->GetYaxis()->SetLabelFont(42);
   Graph_Graph1007->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1007->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1007->GetYaxis()->SetTitleFont(42);
   Graph_Graph1007->GetZaxis()->SetLabelFont(42);
   Graph_Graph1007->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1007->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1007->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1007);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1008[1] = {
   0.790816};
   Double_t Graph_fy1008[1] = {
   3.38144};
   Double_t Graph_fex1008[1] = {
   0};
   Double_t Graph_fey1008[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1008,Graph_fy1008,Graph_fex1008,Graph_fey1008);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_6_Mass0to30_Photon17_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(8);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1008 = new TH1F("Graph_Graph1008","HLT_DoubleMu17_6_Mass0to30_Photon17_v1",100,0.690816,1.890816);
   Graph_Graph1008->SetMinimum(3.28144);
   Graph_Graph1008->SetMaximum(4.48144);
   Graph_Graph1008->SetDirectory(0);
   Graph_Graph1008->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1008->SetLineColor(ci);
   Graph_Graph1008->GetXaxis()->SetLabelFont(42);
   Graph_Graph1008->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1008->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1008->GetXaxis()->SetTitleFont(42);
   Graph_Graph1008->GetYaxis()->SetLabelFont(42);
   Graph_Graph1008->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1008->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1008->GetYaxis()->SetTitleFont(42);
   Graph_Graph1008->GetZaxis()->SetLabelFont(42);
   Graph_Graph1008->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1008->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1008->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1008);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1009[1] = {
   0.7227832};
   Double_t Graph_fy1009[1] = {
   2.0036};
   Double_t Graph_fex1009[1] = {
   0};
   Double_t Graph_fey1009[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1009,Graph_fy1009,Graph_fex1009,Graph_fey1009);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_8_Mass0to30_Photon17_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(9);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1009 = new TH1F("Graph_Graph1009","HLT_DoubleMu17_8_Mass0to30_Photon17_v1",100,0.6227832,1.822783);
   Graph_Graph1009->SetMinimum(1.9036);
   Graph_Graph1009->SetMaximum(3.1036);
   Graph_Graph1009->SetDirectory(0);
   Graph_Graph1009->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1009->SetLineColor(ci);
   Graph_Graph1009->GetXaxis()->SetLabelFont(42);
   Graph_Graph1009->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1009->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1009->GetXaxis()->SetTitleFont(42);
   Graph_Graph1009->GetYaxis()->SetLabelFont(42);
   Graph_Graph1009->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1009->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1009->GetYaxis()->SetTitleFont(42);
   Graph_Graph1009->GetZaxis()->SetLabelFont(42);
   Graph_Graph1009->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1009->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1009->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1009);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1010[1] = {
   0.791553};
   Double_t Graph_fy1010[1] = {
   4.17552};
   Double_t Graph_fex1010[1] = {
   0};
   Double_t Graph_fey1010[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1010,Graph_fy1010,Graph_fex1010,Graph_fey1010);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_5_Mass0to30_Photon17_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(11);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1010 = new TH1F("Graph_Graph1010","HLT_DoubleMu17_5_Mass0to30_Photon17_v1",100,0.691553,1.891553);
   Graph_Graph1010->SetMinimum(4.07552);
   Graph_Graph1010->SetMaximum(5.27552);
   Graph_Graph1010->SetDirectory(0);
   Graph_Graph1010->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1010->SetLineColor(ci);
   Graph_Graph1010->GetXaxis()->SetLabelFont(42);
   Graph_Graph1010->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1010->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1010->GetXaxis()->SetTitleFont(42);
   Graph_Graph1010->GetYaxis()->SetLabelFont(42);
   Graph_Graph1010->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1010->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1010->GetYaxis()->SetTitleFont(42);
   Graph_Graph1010->GetZaxis()->SetLabelFont(42);
   Graph_Graph1010->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1010->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1010->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1010);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1011[1] = {
   0.7199823};
   Double_t Graph_fy1011[1] = {
   1.85968};
   Double_t Graph_fex1011[1] = {
   0};
   Double_t Graph_fey1011[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1011,Graph_fy1011,Graph_fex1011,Graph_fey1011);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_8_Mass0to30_Photon18_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(12);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1011 = new TH1F("Graph_Graph1011","HLT_DoubleMu17_8_Mass0to30_Photon18_v1",100,0.6199823,1.819982);
   Graph_Graph1011->SetMinimum(1.75968);
   Graph_Graph1011->SetMaximum(2.95968);
   Graph_Graph1011->SetDirectory(0);
   Graph_Graph1011->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1011->SetLineColor(ci);
   Graph_Graph1011->GetXaxis()->SetLabelFont(42);
   Graph_Graph1011->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1011->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1011->GetXaxis()->SetTitleFont(42);
   Graph_Graph1011->GetYaxis()->SetLabelFont(42);
   Graph_Graph1011->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1011->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1011->GetYaxis()->SetTitleFont(42);
   Graph_Graph1011->GetZaxis()->SetLabelFont(42);
   Graph_Graph1011->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1011->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1011->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1011);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1012[1] = {
   0.7883467};
   Double_t Graph_fy1012[1] = {
   3.87419};
   Double_t Graph_fex1012[1] = {
   0};
   Double_t Graph_fey1012[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1012,Graph_fy1012,Graph_fex1012,Graph_fey1012);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_5_Mass0to30_Photon18_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(13);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1012 = new TH1F("Graph_Graph1012","HLT_DoubleMu17_5_Mass0to30_Photon18_v1",100,0.6883467,1.888347);
   Graph_Graph1012->SetMinimum(3.77419);
   Graph_Graph1012->SetMaximum(4.97419);
   Graph_Graph1012->SetDirectory(0);
   Graph_Graph1012->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1012->SetLineColor(ci);
   Graph_Graph1012->GetXaxis()->SetLabelFont(42);
   Graph_Graph1012->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1012->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1012->GetXaxis()->SetTitleFont(42);
   Graph_Graph1012->GetYaxis()->SetLabelFont(42);
   Graph_Graph1012->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1012->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1012->GetYaxis()->SetTitleFont(42);
   Graph_Graph1012->GetZaxis()->SetLabelFont(42);
   Graph_Graph1012->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1012->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1012->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1012);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1013[1] = {
   0.7250682};
   Double_t Graph_fy1013[1] = {
   2.17888};
   Double_t Graph_fex1013[1] = {
   0};
   Double_t Graph_fey1013[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1013,Graph_fy1013,Graph_fex1013,Graph_fey1013);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_8_Mass0to30_Photon16_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(14);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1013 = new TH1F("Graph_Graph1013","HLT_DoubleMu17_8_Mass0to30_Photon16_v1",100,0.6250682,1.825068);
   Graph_Graph1013->SetMinimum(2.07888);
   Graph_Graph1013->SetMaximum(3.27888);
   Graph_Graph1013->SetDirectory(0);
   Graph_Graph1013->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1013->SetLineColor(ci);
   Graph_Graph1013->GetXaxis()->SetLabelFont(42);
   Graph_Graph1013->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1013->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1013->GetXaxis()->SetTitleFont(42);
   Graph_Graph1013->GetYaxis()->SetLabelFont(42);
   Graph_Graph1013->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1013->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1013->GetYaxis()->SetTitleFont(42);
   Graph_Graph1013->GetZaxis()->SetLabelFont(42);
   Graph_Graph1013->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1013->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1013->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1013);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1014[1] = {
   0.7851036};
   Double_t Graph_fy1014[1] = {
   3.64963};
   Double_t Graph_fex1014[1] = {
   0};
   Double_t Graph_fey1014[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1014,Graph_fy1014,Graph_fex1014,Graph_fey1014);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_5_Mass0to30_Photon19_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(15);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1014 = new TH1F("Graph_Graph1014","HLT_DoubleMu17_5_Mass0to30_Photon19_v1",100,0.6851036,1.885104);
   Graph_Graph1014->SetMinimum(3.54963);
   Graph_Graph1014->SetMaximum(4.74963);
   Graph_Graph1014->SetDirectory(0);
   Graph_Graph1014->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1014->SetLineColor(ci);
   Graph_Graph1014->GetXaxis()->SetLabelFont(42);
   Graph_Graph1014->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1014->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1014->GetXaxis()->SetTitleFont(42);
   Graph_Graph1014->GetYaxis()->SetLabelFont(42);
   Graph_Graph1014->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1014->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1014->GetYaxis()->SetTitleFont(42);
   Graph_Graph1014->GetZaxis()->SetLabelFont(42);
   Graph_Graph1014->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1014->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1014->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1014);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1015[1] = {
   0.7876096};
   Double_t Graph_fy1015[1] = {
   3.11667};
   Double_t Graph_fex1015[1] = {
   0};
   Double_t Graph_fey1015[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1015,Graph_fy1015,Graph_fex1015,Graph_fey1015);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_6_Mass0to30_Photon18_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(16);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1015 = new TH1F("Graph_Graph1015","HLT_DoubleMu17_6_Mass0to30_Photon18_v1",100,0.6876096,1.88761);
   Graph_Graph1015->SetMinimum(3.01667);
   Graph_Graph1015->SetMaximum(4.21667);
   Graph_Graph1015->SetDirectory(0);
   Graph_Graph1015->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1015->SetLineColor(ci);
   Graph_Graph1015->GetXaxis()->SetLabelFont(42);
   Graph_Graph1015->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1015->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1015->GetXaxis()->SetTitleFont(42);
   Graph_Graph1015->GetYaxis()->SetLabelFont(42);
   Graph_Graph1015->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1015->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1015->GetYaxis()->SetTitleFont(42);
   Graph_Graph1015->GetZaxis()->SetLabelFont(42);
   Graph_Graph1015->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1015->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1015->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1015);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1016[1] = {
   0.7932115};
   Double_t Graph_fy1016[1] = {
   3.80483};
   Double_t Graph_fex1016[1] = {
   0};
   Double_t Graph_fey1016[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1016,Graph_fy1016,Graph_fex1016,Graph_fey1016);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_6_Mass0to30_Photon16_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(17);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1016 = new TH1F("Graph_Graph1016","HLT_DoubleMu17_6_Mass0to30_Photon16_v1",100,0.6932115,1.893211);
   Graph_Graph1016->SetMinimum(3.70483);
   Graph_Graph1016->SetMaximum(4.90483);
   Graph_Graph1016->SetDirectory(0);
   Graph_Graph1016->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1016->SetLineColor(ci);
   Graph_Graph1016->GetXaxis()->SetLabelFont(42);
   Graph_Graph1016->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1016->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1016->GetXaxis()->SetTitleFont(42);
   Graph_Graph1016->GetYaxis()->SetLabelFont(42);
   Graph_Graph1016->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1016->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1016->GetYaxis()->SetTitleFont(42);
   Graph_Graph1016->GetZaxis()->SetLabelFont(42);
   Graph_Graph1016->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1016->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1016->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1016);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1017[1] = {
   0.7891944};
   Double_t Graph_fy1017[1] = {
   2.52784};
   Double_t Graph_fex1017[1] = {
   0};
   Double_t Graph_fey1017[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1017,Graph_fy1017,Graph_fex1017,Graph_fey1017);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_7_Mass0to30_Photon17_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(18);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1017 = new TH1F("Graph_Graph1017","HLT_DoubleMu17_7_Mass0to30_Photon17_v1",100,0.6891944,1.889194);
   Graph_Graph1017->SetMinimum(2.42784);
   Graph_Graph1017->SetMaximum(3.62784);
   Graph_Graph1017->SetDirectory(0);
   Graph_Graph1017->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1017->SetLineColor(ci);
   Graph_Graph1017->GetXaxis()->SetLabelFont(42);
   Graph_Graph1017->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1017->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1017->GetXaxis()->SetTitleFont(42);
   Graph_Graph1017->GetYaxis()->SetLabelFont(42);
   Graph_Graph1017->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1017->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1017->GetYaxis()->SetTitleFont(42);
   Graph_Graph1017->GetZaxis()->SetLabelFont(42);
   Graph_Graph1017->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1017->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1017->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1017);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1018[1] = {
   0.7915899};
   Double_t Graph_fy1018[1] = {
   2.81215};
   Double_t Graph_fex1018[1] = {
   0};
   Double_t Graph_fey1018[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1018,Graph_fy1018,Graph_fex1018,Graph_fey1018);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_7_Mass0to30_Photon16_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(19);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1018 = new TH1F("Graph_Graph1018","HLT_DoubleMu17_7_Mass0to30_Photon16_v1",100,0.6915899,1.89159);
   Graph_Graph1018->SetMinimum(2.71215);
   Graph_Graph1018->SetMaximum(3.91215);
   Graph_Graph1018->SetDirectory(0);
   Graph_Graph1018->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1018->SetLineColor(ci);
   Graph_Graph1018->GetXaxis()->SetLabelFont(42);
   Graph_Graph1018->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1018->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1018->GetXaxis()->SetTitleFont(42);
   Graph_Graph1018->GetYaxis()->SetLabelFont(42);
   Graph_Graph1018->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1018->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1018->GetYaxis()->SetTitleFont(42);
   Graph_Graph1018->GetZaxis()->SetLabelFont(42);
   Graph_Graph1018->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1018->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1018->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1018);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1019[1] = {
   0.6542714};
   Double_t Graph_fy1019[1] = {
   1.49624};
   Double_t Graph_fex1019[1] = {
   0};
   Double_t Graph_fey1019[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1019,Graph_fy1019,Graph_fex1019,Graph_fey1019);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_9_Mass0to30_Photon19_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(20);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1019 = new TH1F("Graph_Graph1019","HLT_DoubleMu17_9_Mass0to30_Photon19_v1",100,0.5542714,1.754271);
   Graph_Graph1019->SetMinimum(1.39624);
   Graph_Graph1019->SetMaximum(2.59624);
   Graph_Graph1019->SetDirectory(0);
   Graph_Graph1019->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1019->SetLineColor(ci);
   Graph_Graph1019->GetXaxis()->SetLabelFont(42);
   Graph_Graph1019->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1019->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1019->GetXaxis()->SetTitleFont(42);
   Graph_Graph1019->GetYaxis()->SetLabelFont(42);
   Graph_Graph1019->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1019->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1019->GetYaxis()->SetTitleFont(42);
   Graph_Graph1019->GetZaxis()->SetLabelFont(42);
   Graph_Graph1019->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1019->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1019->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1019);
   
   multigraph->Add(gre,"PMC");
   
   Double_t Graph_fx1020[1] = {
   0.6569249};
   Double_t Graph_fy1020[1] = {
   1.57826};
   Double_t Graph_fex1020[1] = {
   0};
   Double_t Graph_fey1020[1] = {
   0};
   gre = new TGraphErrors(1,Graph_fx1020,Graph_fy1020,Graph_fex1020,Graph_fey1020);
   gre->SetName("Graph");
   gre->SetTitle("HLT_DoubleMu17_9_Mass0to30_Photon18_v1");
   gre->SetLineColor(0);
   gre->SetMarkerColor(21);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1020 = new TH1F("Graph_Graph1020","HLT_DoubleMu17_9_Mass0to30_Photon18_v1",100,0.5569249,1.756925);
   Graph_Graph1020->SetMinimum(1.47826);
   Graph_Graph1020->SetMaximum(2.67826);
   Graph_Graph1020->SetDirectory(0);
   Graph_Graph1020->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1020->SetLineColor(ci);
   Graph_Graph1020->GetXaxis()->SetLabelFont(42);
   Graph_Graph1020->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1020->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1020->GetXaxis()->SetTitleFont(42);
   Graph_Graph1020->GetYaxis()->SetLabelFont(42);
   Graph_Graph1020->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1020->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1020->GetYaxis()->SetTitleFont(42);
   Graph_Graph1020->GetZaxis()->SetLabelFont(42);
   Graph_Graph1020->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1020->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1020->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1020);
   
   multigraph->Add(gre,"PMC");
   multigraph->Draw("A PMC");
   multigraph->GetXaxis()->SetTitle(" Efficiency ");
   multigraph->GetXaxis()->SetLabelFont(42);
   multigraph->GetXaxis()->SetLabelSize(0.035);
   multigraph->GetXaxis()->SetTitleSize(0.035);
   multigraph->GetXaxis()->SetTitleFont(42);
   multigraph->GetYaxis()->SetTitle(" Unprescaled Rate (at 2E34 cm^-2 s^-1) [Hz]");
   multigraph->GetYaxis()->SetLabelFont(42);
   multigraph->GetYaxis()->SetLabelSize(0.035);
   multigraph->GetYaxis()->SetTitleSize(0.035);
   multigraph->GetYaxis()->SetTitleFont(42);
   
   TLegend *leg = new TLegend(0.7121001,0.1006536,0.9972184,0.9006536,NULL,"brNDC");
   leg->SetBorderSize(1);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph","HLT_DoubleMu17_7_Mass0to30_Photon18_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_7_Mass0to30_Photon19_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(2);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_6_Mass0to30_Photon19_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(3);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_8_Mass0to30_Photon19_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(4);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_9_Mass0to30_Photon17_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(5);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_5_Mass0to30_Photon16_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(6);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_9_Mass0to30_Photon16_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(7);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_6_Mass0to30_Photon17_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(8);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_8_Mass0to30_Photon17_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(9);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_5_Mass0to30_Photon17_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(11);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_8_Mass0to30_Photon18_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(12);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_5_Mass0to30_Photon18_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(13);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_8_Mass0to30_Photon16_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(14);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_5_Mass0to30_Photon19_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(15);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_6_Mass0to30_Photon18_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(16);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_6_Mass0to30_Photon16_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(17);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_7_Mass0to30_Photon17_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(18);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_7_Mass0to30_Photon16_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(19);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_9_Mass0to30_Photon19_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(20);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","HLT_DoubleMu17_9_Mass0to30_Photon18_v1","lpf");
   entry->SetFillStyle(1001);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(21);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
