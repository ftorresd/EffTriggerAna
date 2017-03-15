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

// HLT Configs
minPhotonPt_ (iConfig.getParameter<double>("minPhotonPt",12.0)),
minLeadingMuPt_ (iConfig.getParameter<double>("minLeadingMuPt",6.0)),
minTrailMuPt_   (iConfig.getParameter<double>("minTrailMuPt",4.0)),                                                                                                                                                                                                                                 
minDimuonMass_  (iConfig.getParameter<double>("minDimuonMass",0.0)),
maxDimuonMass_  (iConfig.getParameter<double>("maxDimuonMass",12.0)),

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
  TH1D::SetDefaultSumw2 ();  
  // eg mu
  for (std::vector<double>::const_iterator j = l1EGammaPt_.begin(); j != l1EGammaPt_.end(); j++ ){
    std::string histoNameSufix = configName_+"_EG_"+std::to_string((int) *j);
    nEvtsHistosMap["h_L1_"+histoNameSufix] = fs->make<TH1D>( ("h_L1_"+histoNameSufix).c_str() , ("h_L1_"+histoNameSufix+";  Double Mu Pt (GeV); Efficiency").c_str(), 80, 0., 80.);
    nEvtsHistosMap["h_L1RECO_"+histoNameSufix] = fs->make<TH1D>( ("h_L1RECO_"+histoNameSufix).c_str() , ("h_L1RECO_"+histoNameSufix+";  Double Mu Pt (GeV); Efficiency").c_str(), 80, 0., 80.);
    nEvtsHistosMap["h_L1HLT_"+histoNameSufix] = fs->make<TH1D>( ("h_L1HLT_"+histoNameSufix).c_str() , ("h_L1HLT_"+histoNameSufix+";  Double Mu Pt (GeV); Efficiency").c_str(), 80, 0., 80.);
    nEvtsHistosMap["h_L1HLTRECO_"+histoNameSufix] = fs->make<TH1D>( ("h_L1HLTRECO_"+histoNameSufix).c_str() , ("h_L1HLTRECO_"+histoNameSufix+";  Double Mu Pt (GeV); Efficiency").c_str(), 80, 0., 80.);
  }
  // eg histos
  for (std::vector<double>::const_iterator i = l1MuonPt_.begin(); i != l1MuonPt_.end(); i++ ){
    std::string histoNameSufix = configName_+"_DoubleMu_"+std::to_string((int) *i);
    nEvtsHistosMap["h_L1_"+histoNameSufix] = fs->make<TH1D>( ("h_L1_"+histoNameSufix).c_str() , ("h_L1_"+histoNameSufix+";  EGamma Pt (GeV); Efficiency").c_str(), 30, 0., 30.);
    nEvtsHistosMap["h_L1RECO_"+histoNameSufix] = fs->make<TH1D>( ("h_L1RECO_"+histoNameSufix).c_str() , ("h_L1RECO_"+histoNameSufix+";  EGamma Pt (GeV); Efficiency").c_str(), 30, 0., 30.);
    nEvtsHistosMap["h_L1HLT_"+histoNameSufix] = fs->make<TH1D>( ("h_L1HLT_"+histoNameSufix).c_str() , ("h_L1HLT_"+histoNameSufix+";  EGamma Pt (GeV); Efficiency").c_str(), 30, 0., 30.);
    nEvtsHistosMap["h_L1HLTRECO_"+histoNameSufix] = fs->make<TH1D>( ("h_L1HLTRECO_"+histoNameSufix).c_str() , ("h_L1HLTRECO_"+histoNameSufix+";  EGamma Pt (GeV); Efficiency").c_str(), 30, 0., 30.);
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
        // mu histos
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
  // L3 Muons
  std::vector<float> ptMuon, etaMuon, phiMuon;
  double DoubleMuMass=-1.0;
  for (trigger::TriggerObjectCollection::const_iterator it = muonL3Objects.begin(); it != muonL3Objects.end(); it++) {
    if(it->pt() >= 0 ) {
      if (verbose_) std::cout << "HLT Muon: " << it->pt() << std::endl;
    }
    ptMuon.push_back(it->pt());
    etaMuon.push_back(it->eta());
    phiMuon.push_back(it->phi());
    if (ptMuon.size()>1) {
     math::PtEtaPhiMLorentzVectorD* mu1 = new math::PtEtaPhiMLorentzVectorD(ptMuon[0],etaMuon[0],phiMuon[0],0.106);
     math::PtEtaPhiMLorentzVectorD* mu2 = new math::PtEtaPhiMLorentzVectorD(ptMuon[1],etaMuon[1],phiMuon[1],0.106);
     (*mu1)+=(*mu2);
     DoubleMuMass=(mu1->M());
     if (verbose_) std::cout << "HLT DoubleMuMass: " << DoubleMuMass << std::endl;
     if((mu1->Pt()<minLeadingMuPt_) && (mu2->Pt()< minTrailMuPt_)) continue ;
     if (DoubleMuMass < maxDimuonMass_ && minDimuonMass_ > DoubleMuMass)continue;
   }
 }


// L3 Photons
 std::vector<float> ptPhoton, etaPhoton, phiPhoton;
 for (trigger::TriggerObjectCollection::const_iterator it = photonL3Objects.begin(); it != photonL3Objects.end(); it++) {
  if(it->pt() >= 0 ) {
    if (verbose_) std::cout << "HLT Photon: " << it->pt() << std::endl;
  }
  ptPhoton.push_back(it->pt());
  etaPhoton.push_back(it->eta());
  phiPhoton.push_back(it->phi());
  if(it->pt() < minPhotonPt_ )continue;
} 
return true;

//   // L3 Muons
//   for (trigger::TriggerObjectCollection::const_iterator it = muonL3Objects.begin(); it != muonL3Objects.end(); it++) {
//     if(it->pt() >= 0 ) {
//       // std::cout << "HLT Muon: " << it->pt() << std::endl;
//     }
//   }  

// // L3 Photons
//   for (trigger::TriggerObjectCollection::const_iterator it = photonL3Objects.begin(); it != photonL3Objects.end(); it++) {
//     if(it->pt() >= 0 ) {
//       // std::cout << "HLT Photon: " << it->pt() << std::endl;
//     }
//   } 
//   return true;
}


bool 
AODTriggerAnalyzer::recoFilter(edm::Handle< reco::MuonCollection > recoMuons, edm::Handle< reco::PhotonCollection > recoPhotons, const edm::Event &iEvent)
{
  // Reco Muons
  for (reco::MuonCollection::const_iterator it = recoMuons->begin(); it != recoMuons->end(); it++) {
    if(it->pt() >= 0 ) {
      // std::cout << "Reco Muon: " << it->pt() << std::endl;
    }
  }  

// Reco Photons
  for (reco::PhotonCollection::const_iterator it = recoPhotons ->begin(); it != recoPhotons->end(); it++) {
    if(it->pt() >= 0 ) {
      // std::cout << "Reco Photon: " << it->pt() << std::endl;
    }
  } 
  return true;
}



bool 
AODTriggerAnalyzer::l1Filter(edm::Handle< BXVector<l1t::Muon> > l1Muons, edm::Handle< BXVector<l1t::EGamma> > l1EGammas, double muonPtCut, double egammaPtCut, const edm::Event &iEvent)
{
  bool l1Filter_ = false;

  // L1 Muons
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
  std::vector<l1t::EGamma> l1EGammasVec;
  for (int ibx = l1EGammas->getFirstBX(); ibx <= l1EGammas->getLastBX(); ++ibx) {
    for (BXVector<l1t::EGamma>::const_iterator it=l1EGammas->begin(); it!=l1EGammas->end(); it++){
      if (it->pt() >= 0){
        l1EGammasVec.push_back(*it);
        // std::cout << "L1 EGamma: " << it->pt() << std::endl;
        // l1upgrade_.egEt .push_back(it->pt());
        // l1upgrade_.egEta.push_back(it->eta());
        // l1upgrade_.egPhi.push_back(it->phi());
        // l1upgrade_.egIEt .push_back(it->hwPt());
        // l1upgrade_.egIEta.push_back(it->hwEta());
        // l1upgrade_.egIPhi.push_back(it->hwPhi());
        // l1upgrade_.egIso.push_back(it->hwIso());
        // l1upgrade_.egBx .push_back(ibx);
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

  // N muons
  if (l1MuonsVec.size() >= 2 && l1MuonsVec.size() >= l1MuonN_) {
    l1Filter_ = true;
  } else {
    return false;
  }

  l1t::Muon leadingMuon = l1MuonsVec.at(0);
  l1t::Muon trailingMuon = l1MuonsVec.at(1);

  // Muons OS
  if (l1MuonOS_ == true && (leadingMuon.charge() * trailingMuon.charge() < 0) ) {
    l1Filter_ = true;
  } else if (l1MuonOS_ == false && (leadingMuon.charge() * trailingMuon.charge() > 0) ) {
    l1Filter_ = true;
  } else {
    return false;
  }

  // Muons Iso
  if ( (l1MuonIso_ == true && leadingMuon.hwIso() == 1) && (l1MuonIso_ == true && trailingMuon.hwIso() == 1) ) {
    l1Filter_ = true;
  } else if ( (l1MuonIso_ == false && leadingMuon.hwIso() != 1) && (l1MuonIso_ == false && trailingMuon.hwIso() != 1) ) {
    l1Filter_ = true;
  } else {
    return false;
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
      if (l1EGammaIso_ == true && leadingEGamma.hwIso() == 1) {
        l1Filter_ = true;
      } else if (l1EGammaIso_ == false && leadingEGamma.hwIso() != 1) {
        l1Filter_ = true;
      } else {
        return false;
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