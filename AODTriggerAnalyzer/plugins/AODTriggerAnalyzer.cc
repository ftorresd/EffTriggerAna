// system include files
#include <memory>
#include <cmath>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
// #include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
// #include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/L1Trigger/interface/EGamma.h"
#include "DataFormats/L1Trigger/interface/Muon.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"

#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"

// #include "TEfficiency.h"
#include "TVectorD.h"


class AODTriggerAnalyzer : public edm::EDAnalyzer {
public:
  explicit AODTriggerAnalyzer(const edm::ParameterSet&);
  trigger::TriggerObjectCollection filterFinder(edm::EDGetTokenT<trigger::TriggerEvent> triggerSummaryLabel, edm::InputTag filterTag, const edm::Event &iEvent);
  bool l1Filter(edm::Handle< BXVector<l1t::Muon> > l1Muons, edm::Handle< BXVector<l1t::EGamma> > l1EGammas, double muonPtCut, double egammaPtCut, const edm::Event &iEvent);
  bool recoFilter(edm::Handle< reco::MuonCollection > recoMuons, edm::Handle< reco::PhotonCollection > recoPhotons, const edm::Event &iEvent);
  bool hltFilter(trigger::TriggerObjectCollection muonL3Objects, trigger::TriggerObjectCollection photonL3Objects, const edm::Event &iEvent);

  ~AODTriggerAnalyzer() {}



private:
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;

  bool verbose_; 

  edm::EDGetTokenT< edm::TriggerResults > triggerBits_;
  edm::EDGetTokenT< BXVector<l1t::Muon> > l1Muons_;
  edm::EDGetTokenT< BXVector<l1t::EGamma> > l1EGammas_;
  edm::EDGetTokenT< reco::MuonCollection > recoMuons_;
  edm::EDGetTokenT< reco::PhotonCollection > recoPhotons_;
  edm::EDGetTokenT< trigger::TriggerEvent > triggerSummaryLabel_;
  edm::InputTag muonFilterTag_;
  edm::InputTag photonFilterTag_;

  // Reco configs
  double minMuPt_;
  double maxMuEta_;
  double muonLeadPt_, muonTrailPt_;
  double minJPsiMass_ ;
  double maxJPsiMass_,GammaMinPtCut_,drLeadMuPhotonSel_,drTrailPhotonSel_;  

  //HLT Configs
  double minPhotonPt_; 
  double minLeadingMuPt_; 
  double minTrailMuPt_;                                                                                                                                                                                                                                   
  double minDimuonMass_;  
  double maxDimuonMass_;  

  // L1 Configs
  std::string configName_;
  unsigned l1MuonN_;
  bool l1MuonOS_;
  bool l1MuonIso_;
  int l1MuonQltMin_;
  int l1MuonQltMax_;
  std::vector<double> l1MuonPt_;
  unsigned l1EGammaN_;
  bool l1EGammaIso_;
  std::vector<double> l1EGammaPt_;

  // Histos map
  int nEvts;
  int nEvtsRECO;
  int nEvtsHLT;
  int nEvtsHLTRECO;
  std::map<std::string, TH1D*> nEvtsHistosMap;


};

AODTriggerAnalyzer::AODTriggerAnalyzer(const edm::ParameterSet& iConfig):
verbose_ (iConfig.getParameter< bool > ("verbose")),
triggerBits_(consumes< edm::TriggerResults >(iConfig.getParameter<edm::InputTag>("bits"))),
l1Muons_(consumes< BXVector<l1t::Muon> >(iConfig.getParameter<edm::InputTag>("l1MuonsLabel"))),
l1EGammas_(consumes< BXVector<l1t::EGamma> >(iConfig.getParameter<edm::InputTag>("l1EGammasLabel"))),
recoMuons_(consumes< reco::MuonCollection >(iConfig.getParameter<edm::InputTag>("recoMuonsLabel"))),
recoPhotons_(consumes< reco::PhotonCollection >(iConfig.getParameter<edm::InputTag>("recoPhotonsLabel"))),
triggerSummaryLabel_ (consumes<trigger::TriggerEvent>(iConfig.getParameter<edm::InputTag> ("triggerSummaryLabel"))),
muonFilterTag_ (iConfig.getParameter<edm::InputTag> ("muonFilterTag")),
photonFilterTag_ (iConfig.getParameter<edm::InputTag> ("photonFilterTag")),

// Reco config
minMuPt_ (iConfig.getParameter<double>("minMuPt")),
maxMuEta_ (iConfig.getParameter<double>("maxMuEta")), 
muonLeadPt_ (iConfig.getParameter<double>("minMuonLeadPt")),
muonTrailPt_ (iConfig.getParameter<double>("minMuonTrailPt")),
minJPsiMass_ (iConfig.getParameter<double>("minJPsiMass")),
maxJPsiMass_ (iConfig.getParameter<double>("maxJPsiMass")),
GammaMinPtCut_ (iConfig.getParameter<double>("GammaMinPtCut")),
drLeadMuPhotonSel_ (iConfig.getParameter<double>("DeltaRLeadMuPhotonSel")),
drTrailPhotonSel_ (iConfig.getParameter<double>("DeltaRTrailPhotonSel")),  

// HLT Configs
minPhotonPt_ (iConfig.getParameter<double>("minPhotonPt")),
minLeadingMuPt_ (iConfig.getParameter<double>("minLeadingMuPt")),
minTrailMuPt_   (iConfig.getParameter<double>("minTrailMuPt")),                                                                                                                                                                                                                                 
minDimuonMass_  (iConfig.getParameter<double>("minDimuonMass")),
maxDimuonMass_  (iConfig.getParameter<double>("maxDimuonMass")),

// L1 Configs    
configName_ (iConfig.getParameter< std::string > ("configName")),
l1MuonN_ (iConfig.getParameter< unsigned > ("l1MuonN")),
l1MuonOS_ (iConfig.getParameter< bool > ("l1MuonOS")),
l1MuonIso_ (iConfig.getParameter< bool > ("l1MuonIso")),
l1MuonQltMin_ (iConfig.getParameter< int > ("l1MuonQltMin")),
l1MuonQltMax_ (iConfig.getParameter< int > ("l1MuonQltMax")),
l1MuonPt_ (iConfig.getParameter< std::vector<double> > ("l1MuonPt")),
l1EGammaN_ (iConfig.getParameter< unsigned > ("l1EGammaN")),
l1EGammaIso_ (iConfig.getParameter< bool > ("l1EGammaIso")),
l1EGammaPt_ (iConfig.getParameter< std::vector<double> > ("l1EGammaPt"))

{
  // Histos File
  edm::Service<TFileService> fs;

  // Define Evts count
  nEvts = 0;
  nEvtsRECO = 0;
  nEvtsHLT = 0;
  nEvtsHLTRECO = 0;

  // Define Histos
  TH1D::SetDefaultSumw2();  
  // eg mu
  for (std::vector<double>::const_iterator j = l1EGammaPt_.begin(); j != l1EGammaPt_.end(); j++ ){
    std::string histoNameSufix = configName_+"_EG_"+std::to_string((int) *j);
    nEvtsHistosMap["h_L1_"+histoNameSufix] = fs->make<TH1D>( ("h_L1_"+histoNameSufix).c_str() , ("h_L1_"+histoNameSufix+";  Double Mu Pt Cut (GeV); Efficiency").c_str(), 80, 0., 80.);
    nEvtsHistosMap["h_L1RECO_"+histoNameSufix] = fs->make<TH1D>( ("h_L1RECO_"+histoNameSufix).c_str() , ("h_L1RECO_"+histoNameSufix+";  Double Mu Pt Cut (GeV); Efficiency").c_str(), 80, 0., 80.);
    nEvtsHistosMap["h_L1HLT_"+histoNameSufix] = fs->make<TH1D>( ("h_L1HLT_"+histoNameSufix).c_str() , ("h_L1HLT_"+histoNameSufix+";  Double Mu Pt Cut (GeV); Efficiency").c_str(), 80, 0., 80.);
    nEvtsHistosMap["h_L1HLTRECO_"+histoNameSufix] = fs->make<TH1D>( ("h_L1HLTRECO_"+histoNameSufix).c_str() , ("h_L1HLTRECO_"+histoNameSufix+";  Double Mu Pt Cut (GeV); Efficiency").c_str(), 80, 0., 80.);
  }
  // eg histos
  for (std::vector<double>::const_iterator i = l1MuonPt_.begin(); i != l1MuonPt_.end(); i++ ){
    std::string histoNameSufix = configName_+"_DoubleMu_"+std::to_string((int) *i);
    nEvtsHistosMap["h_L1_"+histoNameSufix] = fs->make<TH1D>( ("h_L1_"+histoNameSufix).c_str() , ("h_L1_"+histoNameSufix+";  EGamma Pt Cut (GeV); Efficiency").c_str(), 50, 0., 50.);
    nEvtsHistosMap["h_L1RECO_"+histoNameSufix] = fs->make<TH1D>( ("h_L1RECO_"+histoNameSufix).c_str() , ("h_L1RECO_"+histoNameSufix+";  EGamma Pt Cut (GeV); Efficiency").c_str(), 50, 0., 50.);
    nEvtsHistosMap["h_L1HLT_"+histoNameSufix] = fs->make<TH1D>( ("h_L1HLT_"+histoNameSufix).c_str() , ("h_L1HLT_"+histoNameSufix+";  EGamma Pt Cut (GeV); Efficiency").c_str(), 50, 0., 50.);
    nEvtsHistosMap["h_L1HLTRECO_"+histoNameSufix] = fs->make<TH1D>( ("h_L1HLTRECO_"+histoNameSufix).c_str() , ("h_L1HLTRECO_"+histoNameSufix+";  EGamma Pt Cut (GeV); Efficiency").c_str(), 50, 0., 50.);
  }
}

void AODTriggerAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle< edm::TriggerResults > triggerBits;
  edm::Handle< BXVector<l1t::Muon> > l1Muons;
  edm::Handle< BXVector<l1t::EGamma> > l1EGammas;
  edm::Handle< reco::MuonCollection > recoMuons;
  edm::Handle< reco::PhotonCollection > recoPhotons;

  iEvent.getByToken(triggerBits_, triggerBits);
  iEvent.getByToken(l1Muons_, l1Muons);
  iEvent.getByToken(l1EGammas_, l1EGammas);
  iEvent.getByToken(recoMuons_, recoMuons);
  iEvent.getByToken(recoPhotons_, recoPhotons);

    // Define L3 Objects
  trigger::TriggerObjectCollection muonL3Objects = filterFinder(triggerSummaryLabel_, muonFilterTag_, iEvent);
  trigger::TriggerObjectCollection photonL3Objects = filterFinder(triggerSummaryLabel_, photonFilterTag_, iEvent);

    // HLT Test
  bool hltTest = hltFilter(muonL3Objects, photonL3Objects, iEvent);
    // std::cout << "hltTest: " << hltTest << std::endl;

    // RECO Test
  bool recoTest = recoFilter(recoMuons, recoPhotons, iEvent);
    // std::cout << "recoTest: " << recoTest << std::endl;

  nEvts++;
  if (recoTest == true) nEvtsRECO++;
  if (hltTest == true) nEvtsHLT++;
  if (hltTest == true && recoTest == true) nEvtsHLTRECO++;

  for (std::vector<double>::const_iterator i = l1MuonPt_.begin(); i != l1MuonPt_.end(); i++ ){
    for (std::vector<double>::const_iterator j = l1EGammaPt_.begin(); j != l1EGammaPt_.end(); j++ ){
      bool l1Test = l1Filter(l1Muons, l1EGammas, *i, *j, iEvent);
      // EG histos
      std::string histoNameSufix = configName_+"_EG_"+std::to_string((int) *j);
      if (l1Test == true) nEvtsHistosMap["h_L1_"+histoNameSufix]->Fill(*i);
      if (recoTest == true && l1Test == true) nEvtsHistosMap["h_L1RECO_"+histoNameSufix]->Fill(*i);
      if (hltTest == true && l1Test == true) nEvtsHistosMap["h_L1HLT_"+histoNameSufix]->Fill(*i);
      if (hltTest == true && recoTest == true && l1Test == true) nEvtsHistosMap["h_L1HLTRECO_"+histoNameSufix]->Fill(*i);
      // DoubleMu histos
      histoNameSufix = configName_+"_DoubleMu_"+std::to_string((int) *i);
      if (l1Test == true) nEvtsHistosMap["h_L1_"+histoNameSufix]->Fill(*j);
      if (recoTest == true && l1Test == true) nEvtsHistosMap["h_L1RECO_"+histoNameSufix]->Fill(*j);
      if (hltTest == true && l1Test == true) nEvtsHistosMap["h_L1HLT_"+histoNameSufix]->Fill(*j);
      if (hltTest == true && recoTest == true && l1Test == true) nEvtsHistosMap["h_L1HLTRECO_"+histoNameSufix]->Fill(*j);
    }
  }
}

//find the filters
trigger::TriggerObjectCollection 
AODTriggerAnalyzer::filterFinder(edm::EDGetTokenT<trigger::TriggerEvent> triggerSummaryLabel, edm::InputTag filterTag, const edm::Event &iEvent)
{

  edm::Handle<trigger::TriggerEvent> triggerSummary; 
  iEvent.getByToken(triggerSummaryLabel, triggerSummary);
  trigger::TriggerObjectCollection allTriggerObjects = triggerSummary->getObjects(); 
  //filterTag_ is the inputTag of the filter you want to match
  size_t filterIndex = (*triggerSummary).filterIndex(filterTag);
  trigger::TriggerObjectCollection filterObjects;
  if(filterIndex < (*triggerSummary).sizeFilters())
  { 
    const trigger::Keys &keysObjects = (*triggerSummary).filterKeys(filterIndex);
    for(size_t j = 0; j < keysObjects.size(); j++)
    {
      trigger::TriggerObject foundObject = (allTriggerObjects)[keysObjects[j]];
      filterObjects.push_back(foundObject);
    }
  }
  // std::cout<<filterObjects.size()<<endl; 
  return filterObjects;
}

bool 
AODTriggerAnalyzer::hltFilter(trigger::TriggerObjectCollection muonL3Objects, trigger::TriggerObjectCollection photonL3Objects, const edm::Event &iEvent)
{

  bool hltFilter_ = false;

  // L3 Muons
  std::vector<trigger::TriggerObject> hltMuonsVec;
  for (trigger::TriggerObjectCollection::const_iterator it = muonL3Objects.begin(); it != muonL3Objects.end(); it++) {
    hltMuonsVec.push_back(*it);
  }

  std::sort(hltMuonsVec.begin(),hltMuonsVec.end(), [](const trigger::TriggerObject &a, const trigger::TriggerObject &b){
    return a.pt() > b.pt();
  });

  if (hltMuonsVec.size() >= 2) {
    trigger::TriggerObject leadingMuon = hltMuonsVec.at(0);
    trigger::TriggerObject trailingMuon = hltMuonsVec.at(1);
    math::PtEtaPhiMLorentzVectorD* mu1 = new math::PtEtaPhiMLorentzVectorD(leadingMuon.pt(),leadingMuon.eta(),leadingMuon.phi(),0.106);
    math::PtEtaPhiMLorentzVectorD* mu2 = new math::PtEtaPhiMLorentzVectorD(trailingMuon.pt(),trailingMuon.eta(),trailingMuon.phi(),0.106);

    double DoubleMuMass = ( (*mu1+*mu2).M() );
    if (verbose_) std::cout << "HLT DoubleMuMass: " << DoubleMuMass << std::endl;
    if ((mu1->Pt() >= minLeadingMuPt_) && (mu2->Pt() >= minTrailMuPt_) ) hltFilter_ = true; else return false ;
    if (DoubleMuMass < maxDimuonMass_ && minDimuonMass_ < DoubleMuMass)  hltFilter_ = true; else return false ;
  } else {
    return false;
  }

// L3 Photons
  std::vector<trigger::TriggerObject> hltPhotonsVec;
   // std::vector<float> ptPhoton, etaPhoton, phiPhoton;
  // std::cout << "### Photon ###" << std::endl;
  // std::cout << "### HLT_Photon_Size: " << photonL3Objects.size() << std::endl;
  for (trigger::TriggerObjectCollection::const_iterator it = photonL3Objects.begin(); it != photonL3Objects.end(); it++) {
    // if(it->pt() >= 0 ) {
    //   if (verbose_) std::cout << "HLT Photon: " << it->pt() << std::endl;
    // }
    // ptPhoton.push_back(it->pt());
    // etaPhoton.push_back(it->eta());
    // phiPhoton.push_back(it->phi());
    // if(it->pt() < minPhotonPt_ )continue;
    hltPhotonsVec.push_back(*it);
    // std::cout << "HLT_Photon_Pt: " << it->pt() << std::endl;
  }
  // std::cout << "### (end) Photon ###" << std::endl;
  
  std::sort(hltPhotonsVec.begin(), hltPhotonsVec.end(), [](const trigger::TriggerObject &a, const trigger::TriggerObject &b){
    return a.pt() > b.pt();
  });

  if (hltPhotonsVec.size() >= 1) {
    if ( hltPhotonsVec.at(0).pt() >= minPhotonPt_ ) hltFilter_ = true; else return false ;
  } else {
    return false;
  }


  return hltFilter_;
}


bool 
AODTriggerAnalyzer::recoFilter(edm::Handle< reco::MuonCollection > recoMuons, edm::Handle< reco::PhotonCollection > recoPhotons, const edm::Event &iEvent)
{
  int nDimuon = 0, nJpsi = 0, nPhoton = 0;       
  std::vector<reco::Muon> myLeptons;
  std::vector<reco::Photon> myPhotons; 

  // Reco Muons
  for (reco::MuonCollection::const_iterator muon = recoMuons->begin(); muon != recoMuons->end(); muon++) {
    if (muon->isPFMuon()){
      if (muon->isTrackerMuon() || muon->isGlobalMuon()){
        // if (verbose_) std::cout << muon->charge() << std::endl;
        if (muon->pt() > minMuPt_ && std::abs(muon->eta()) < maxMuEta_){
          myLeptons.push_back(*muon);
          // if(verbose_) cout<<"REcoMuon "<<muon->pt()<<endl;
        }  //eta and pt muon
      }  //muon type selection
    }  //PF muon
  }// Muon loop

  std::sort(myLeptons.begin(),myLeptons.end(), [](const reco::Muon &a, const reco::Muon &b){
    return a.pt() > b.pt();
  });

  // Print Reco Muons
  for (std::vector<reco::Muon>::const_iterator muon = myLeptons.begin(); muon != myLeptons.end(); muon++) {
    if(verbose_) std::cout<<"RECO myLeptons->pt():  " << muon->pt() << std::endl;
  }// Muon loop

  if(verbose_) std::cout<<"RECO myLeptons.size() all  " << myLeptons.size() << std::endl;
  
  // dimuon selection
  if (myLeptons.size() >= 2) {
    //recoFilter_ = true;
    nDimuon++;
    if(verbose_) std::cout<<"RECO  Muons Multiplicity:  " << myLeptons.size() << std::endl; 
    // if(verbose_) std::cout<<"RECO Dimuons Multiplicity:  " << nDimuon << std::endl;
    reco::Muon leadingMuon = myLeptons[0];
    reco::Muon trailingMuon = myLeptons[1];
    //Dimuons  selection
    if ((leadingMuon.charge() != trailingMuon.charge())) {
    } else {return false;}

    if(verbose_) std::cout<< "Leading Muon pt, eta, phi, charge = " << leadingMuon.pt() << " "<< leadingMuon.eta() << " "<< leadingMuon.phi() << " " << leadingMuon.charge() << std::endl;
    if(verbose_) std::cout<< "Trailing Muon  pt, eta, phi,charge = " << trailingMuon.pt() << " " << trailingMuon.eta() << " " << trailingMuon.phi() << " " << trailingMuon.charge()<< std::endl;

    //Invariant mass of dimuons
    double Mll = (leadingMuon.p4() + trailingMuon.p4()).mass();
    double MllpT = (leadingMuon.p4() + trailingMuon.p4()).pt();
    double Mlleta = (leadingMuon.p4() + trailingMuon.p4()).eta();
    double Mllphi = (leadingMuon.p4() + trailingMuon.p4()).phi();
    if(verbose_) std::cout<< "Dimuons Invariant Mass Mll, pT, eta, phi: " << Mll << " " << MllpT << " " << Mlleta << " " << Mllphi << std::endl;
    if (leadingMuon.pt() >= muonLeadPt_ || trailingMuon.pt() >= muonTrailPt_ ) {

      // ***
      //   // jpsi peak
      //     // ***
      //
      if (Mll > minJPsiMass_ && Mll < maxJPsiMass_){
        nJpsi++;                           
        if(verbose_) std::cout<<" Invariant Mass in JPsi peak, pT, eta, phi " << Mll << " " << MllpT << " " << Mlleta << " " << Mllphi << std::endl;
        // if(verbose_) std::cout<<" Jpsi Multiplicity:  " <<  nJpsi << std::endl;
      } else {return false;}// jpsi selection
    } else {return false;}//lead and trail muon pT cut


    // Reco Photons
    for (reco::PhotonCollection::const_iterator photon = recoPhotons ->begin(); photon != recoPhotons->end(); photon++) {
      if(photon->pt() > GammaMinPtCut_ && photon->isPhoton()) {
        myPhotons.push_back(*photon);                       
        // if(verbose_) std::cout << "RECO Photon: " << photon->pt() << std::endl;
      }
    }

    std::sort(myPhotons.begin(),myPhotons.end(), [](const reco::Photon &a, const reco::Photon &b){
      return a.pt() > b.pt();
    });

    if (  myPhotons.size() >= 1 ) {
      nPhoton++;
      if(verbose_) std::cout<<" Photon Multiplicity:  " <<  nPhoton << std::endl;
      reco::Photon Gamma = myPhotons[0];         
      DeltaR<reco::Muon, reco::Photon> deltaR;
      double drLeadMuPhoton = deltaR(leadingMuon,Gamma);
      double drTrailPhoton = deltaR(trailingMuon,Gamma);
      if(verbose_) std::cout << " photon: pT, eta, phi " << Gamma.pt() << " "<< Gamma.eta() << " " << Gamma.phi() <<std::endl;                         
      if(verbose_) std::cout<< " DeltaR(LeadMu,Photon) " << drLeadMuPhoton << " DeltaR(TrailMu,Photon) " << drTrailPhoton <<std::endl;
      if (drLeadMuPhoton > drLeadMuPhotonSel_ && drTrailPhoton > drTrailPhotonSel_){

        double Mllg = (leadingMuon.p4() + trailingMuon.p4() + Gamma.p4()).mass();
        double MllgpT = (leadingMuon.p4() + trailingMuon.p4() + Gamma.p4()).pt();
        double Mllgeta = (leadingMuon.p4() + trailingMuon.p4() + Gamma.p4()).eta();
        double Mllgphi = (leadingMuon.p4() + trailingMuon.p4() + Gamma.p4()).phi();    
        if(verbose_) std::cout<< "Invariant Mass Mllg, pT, eta, phi: " << Mllg << " " << MllgpT << " " << Mllgeta << " " << Mllgphi << std::endl;  
      } else {return false;}// deltaR cuts 
    } else {return false;}//photon selection
  } else {return false;}//dimuons selection
  ////////////////// 

  return true;
}//end RecoFilter



bool 
AODTriggerAnalyzer::l1Filter(edm::Handle< BXVector<l1t::Muon> > l1Muons, edm::Handle< BXVector<l1t::EGamma> > l1EGammas, double muonPtCut, double egammaPtCut, const edm::Event &iEvent)
{
  bool l1Filter_ = false;

  // L1 Muons
  // ref: https://github.com/cms-sw/cmssw/blob/master/L1Trigger/L1TNtuples/src/L1AnalysisL1Upgrade.cc
  std::vector<l1t::Muon> l1MuonsVec;
  for (int ibx = l1Muons->getFirstBX(); ibx <= l1Muons->getLastBX(); ++ibx) {
    for (BXVector<l1t::Muon>::const_iterator it=l1Muons->begin(); it!=l1Muons->end(); it++){
      if (it->pt() >= 0){
        l1MuonsVec.push_back(*it);
        // std::cout << "L1 Muon: " << it->pt() << std::endl;
        // l1upgrade_.muonEt .push_back(it->et());
        // l1upgrade_.muonEta.push_back(it->eta());
        // l1upgrade_.muonPhi.push_back(it->phi());
        // l1upgrade_.muonEtaAtVtx.push_back(l1t::MicroGMTConfiguration::calcMuonEtaExtra(*it));
        // l1upgrade_.muonPhiAtVtx.push_back(l1t::MicroGMTConfiguration::calcMuonPhiExtra(*it));
        // l1upgrade_.muonIEt .push_back(it->hwPt());
        // l1upgrade_.muonIEta.push_back(it->hwEta());
        // l1upgrade_.muonIPhi.push_back(it->hwPhi());
        // l1upgrade_.muonIDEta.push_back(it->hwDEtaExtra());
        // l1upgrade_.muonIDPhi.push_back(it->hwDPhiExtra());
        // l1upgrade_.muonChg.push_back(it->charge());
        // l1upgrade_.muonIso.push_back(it->hwIso());
        // l1upgrade_.muonQual.push_back(it->hwQual());
        // l1upgrade_.muonTfMuonIdx.push_back(it->tfMuonIndex());
        // l1upgrade_.muonBx .push_back(ibx);
        // l1upgrade_.nMuons++;
      }
    }
  }
  // bool sortL1MuonsReverse(l1t::Muon &a, l1t::Muon &b) { 
  //   return a.pt() > b.pt(); 
  // }
  std::sort(l1MuonsVec.begin(),l1MuonsVec.end(), [](const l1t::Muon &a, const l1t::Muon &b){
    return a.pt() > b.pt();
  });


  // L1 EGammas
  // ref: https://github.com/cms-sw/cmssw/blob/master/L1Trigger/L1TNtuples/src/L1AnalysisL1Upgrade.cc
  std::vector<l1t::EGamma> l1EGammasVec;
  for (int ibx = l1EGammas->getFirstBX(); ibx <= l1EGammas->getLastBX(); ++ibx) {
    for (BXVector<l1t::EGamma>::const_iterator it=l1EGammas->begin(); it!=l1EGammas->end(); it++){
      if (it->pt() >= 0){
        l1EGammasVec.push_back(*it);
        // std::cout << "EGamaa Iso: " << it->hwIso() << std::endl;
        // std::cout << "L1 EGamma: " << it->pt() << std::endl;
        // l1upgrade_.egEt.push_back(it->pt());
        // l1upgrade_.egEta.push_back(it->eta());
        // l1upgrade_.egPhi.push_back(it->phi());
        // l1upgrade_.egIEt.push_back(it->hwPt());
        // l1upgrade_.egIEta.push_back(it->hwEta());
        // l1upgrade_.egIPhi.push_back(it->hwPhi());
        // l1upgrade_.egIso.push_back(it->hwIso());
        // l1upgrade_.egBx.push_back(ibx);
        // l1upgrade_.egTowerIPhi.push_back(it->towerIPhi());
        // l1upgrade_.egTowerIEta.push_back(it->towerIEta());
        // l1upgrade_.egRawEt.push_back(it->rawEt());
        // l1upgrade_.egIsoEt.push_back(it->isoEt());
        // l1upgrade_.egFootprintEt.push_back(it->footprintEt());
        // l1upgrade_.egNTT.push_back(it->nTT());
        // l1upgrade_.egShape.push_back(it->shape());
        // l1upgrade_.egTowerHoE.push_back(it->towerHoE());
        // l1upgrade_.nEGs++;
      }
    }
  }
  std::sort(l1EGammasVec.begin(),l1EGammasVec.end(), [](const l1t::EGamma &a, const l1t::EGamma &b){
    return a.pt() > b.pt();
  });

  // does the actual filtering
  // configName_
  // l1MuonN_
  // l1MuonOS_
  // l1MuonIso_
  // l1MuonQltMin_
  // l1MuonQltMax_
  // l1MuonPt_
  // l1EGammaIso_
  // l1EGammaPt_

  // ZB condition
  if (configName_ == "Zerobias") return true;

  // N muons
  if (l1MuonsVec.size() >= 2 && l1MuonsVec.size() >= l1MuonN_) {
    l1Filter_ = true;
  } else {
    return false;
  }

  l1t::Muon leadingMuon = l1MuonsVec.at(0);
  l1t::Muon trailingMuon = l1MuonsVec.at(1);

  // Muons OS
  if (l1MuonOS_ == true && (leadingMuon.charge() == trailingMuon.charge()) ) {
    return false;
  } else {
    l1Filter_ = true;
  }

  // Muons Iso
  if (l1MuonIso_ == true && leadingMuon.hwIso() != 1 && trailingMuon.hwIso() != 1) {
    return false;
  } else {
    l1Filter_ = true;
  }

  // Muon Qlt
  if ((leadingMuon.hwQual() >= l1MuonQltMin_ && leadingMuon.hwQual() <= l1MuonQltMax_) && (trailingMuon.hwQual() >= l1MuonQltMin_ && trailingMuon.hwQual() <= l1MuonQltMax_) ) {
    l1Filter_ = true;
  } else {
    return false;
  }

  // Muon Pt
  if (leadingMuon.pt() >= muonPtCut && trailingMuon.pt() >= muonPtCut) {
    l1Filter_ = true;
  } else {
    return false;
  }

  // EGamma
  if (l1EGammaN_ != 0) {
    if (l1EGammasVec.size() >= l1EGammaN_) {
      // std::cout << "Temos um photon!" << std::endl;
      l1t::EGamma leadingEGamma = l1EGammasVec.at(0);
      // std::cout << leadingEGamma.pt() << std::endl;
      // std::cout << leadingEGamma.hwIso() << std::endl;
      // EGamma Iso
      if (l1EGammaIso_ == true && leadingEGamma.hwIso() != 1) {
        // l1Filter_ = true;
        return false;
      } else  {
        l1Filter_ = true;
      }
      // EGamma Pt
      if (leadingEGamma.pt() >= egammaPtCut) {
        // std::cout << "Passou no corte de Pt!" << std::endl;
        l1Filter_ = true;
      } else {
        return false;
      }
    } else {
      // std::cout << "Não Temos um photon!" << std::endl;
      return false;
    }
  } else {
    // std::cout << "Vetor vazio" << std::endl;
    l1Filter_ = true;
    // return false;
  }

  // return filtering result
  return l1Filter_;
}

// ------------ method called once each job just after ending the event loop  ------------
void 
AODTriggerAnalyzer::endJob() 
{
  // eg histos
  for (std::vector<double>::const_iterator j = l1EGammaPt_.begin(); j != l1EGammaPt_.end(); j++ ) {
    std::string histoNameSufix = configName_+"_EG_"+std::to_string((int) *j);
    if (nEvts != 0) nEvtsHistosMap["h_L1_"+histoNameSufix]->Scale(1.0/nEvts);
    if (nEvtsRECO != 0) nEvtsHistosMap["h_L1RECO_"+histoNameSufix]->Scale(1.0/nEvtsRECO);
    if (nEvtsHLT != 0) nEvtsHistosMap["h_L1HLT_"+histoNameSufix]->Scale(1.0/nEvtsHLT);
    if (nEvtsHLTRECO != 0) nEvtsHistosMap["h_L1HLTRECO_"+histoNameSufix]->Scale(1.0/nEvtsHLTRECO);
  }

  // mu histos
  for (std::vector<double>::const_iterator i = l1MuonPt_.begin(); i != l1MuonPt_.end(); i++ ){
    std::string histoNameSufix = configName_+"_DoubleMu_"+std::to_string((int) *i);
    if (nEvts != 0) nEvtsHistosMap["h_L1_"+histoNameSufix]->Scale(1.0/nEvts);
    if (nEvtsRECO != 0) nEvtsHistosMap["h_L1RECO_"+histoNameSufix]->Scale(1.0/nEvtsRECO);
    if (nEvtsHLT != 0) nEvtsHistosMap["h_L1HLT_"+histoNameSufix]->Scale(1.0/nEvtsHLT);
    if (nEvtsHLTRECO != 0) nEvtsHistosMap["h_L1HLTRECO_"+histoNameSufix]->Scale(1.0/nEvtsHLTRECO);
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(AODTriggerAnalyzer);