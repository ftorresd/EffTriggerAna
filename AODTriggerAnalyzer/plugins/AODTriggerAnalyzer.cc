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


class AODTriggerAnalyzer : public edm::EDAnalyzer {
   public:
      explicit AODTriggerAnalyzer(const edm::ParameterSet&);
      trigger::TriggerObjectCollection filterFinder(edm::EDGetTokenT<trigger::TriggerEvent> triggerSummaryLabel, edm::InputTag filterTag, const edm::Event &iEvent);
      bool l1Filter(edm::Handle< BXVector<l1t::Muon> > l1Muons, edm::Handle< BXVector<l1t::EGamma> > l1EGammas, const edm::Event &iEvent);
      bool recoFilter(edm::Handle< reco::MuonCollection > recoMuons, edm::Handle< reco::PhotonCollection > recoPhotons, const edm::Event &iEvent);
      bool hltFilter(trigger::TriggerObjectCollection muonL3Objects, trigger::TriggerObjectCollection photonL3Objects, const edm::Event &iEvent);

      ~AODTriggerAnalyzer() {}

      

   private:
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

      edm::EDGetTokenT< edm::TriggerResults > triggerBits_;
      edm::EDGetTokenT< BXVector<l1t::Muon> > l1Muons_;
      edm::EDGetTokenT< BXVector<l1t::EGamma> > l1EGammas_;
      edm::EDGetTokenT< reco::MuonCollection > recoMuons_;
      edm::EDGetTokenT< reco::PhotonCollection > recoPhotons_;
      edm::EDGetTokenT< trigger::TriggerEvent > triggerSummaryLabel_;
      edm::InputTag muonFilterTag_;
      edm::InputTag photonFilterTag_;




      // edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> triggerObjects_;
      // edm::EDGetTokenT<pat::PackedTriggerPrescales> triggerPrescales_;
};

AODTriggerAnalyzer::AODTriggerAnalyzer(const edm::ParameterSet& iConfig):
    triggerBits_(consumes< edm::TriggerResults >(iConfig.getParameter<edm::InputTag>("bits"))),
    l1Muons_(consumes< BXVector<l1t::Muon> >(iConfig.getParameter<edm::InputTag>("l1MuonsLabel"))),
    l1EGammas_(consumes< BXVector<l1t::EGamma> >(iConfig.getParameter<edm::InputTag>("l1EGammasLabel"))),
    recoMuons_(consumes< reco::MuonCollection >(iConfig.getParameter<edm::InputTag>("recoMuonsLabel"))),
    recoPhotons_(consumes< reco::PhotonCollection >(iConfig.getParameter<edm::InputTag>("recoPhotonsLabel"))),
    triggerSummaryLabel_ (consumes<trigger::TriggerEvent>(iConfig.getParameter<edm::InputTag> ("triggerSummaryLabel"))),
    muonFilterTag_ (iConfig.getParameter<edm::InputTag> ("muonFilterTag")),
    photonFilterTag_ (iConfig.getParameter<edm::InputTag> ("photonFilterTag"))

    // triggerObjects_(consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("objects"))),
    // triggerPrescales_(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("prescales")))
{
  edm::Service<TFileService> fs;
  // TH1D* effHist =  fs->make<TH1D>(TString(histograms_[i].getParameter<string>("variable")),TString(histograms_[i].getParameter<string>("variable")),int(histograms_[i].getParameter<int>("nBins")),histograms_[i].getParameter<double>("lBin"),histograms_[i].getParameter<double>("hBin"));     
  // TH1D* tmpMatchedHist = fs->make<TH1D>(TString(histograms_[i].getParameter<string>("variable") + "_filterMatched"),TString(histograms_[i].getParameter<string>("variable") + "_filterMatched"),int(histograms_[i].getParameter<int>("nBins")),histograms_[i].getParameter<double>("lBin"),histograms_[i].getParameter<double>("hBin"));
  // TH1D* tmpEffHist = fs->make<TH1D>(TString(histograms_[i].getParameter<string>("variable") + "_filterEff"),TString(histograms_[i].getParameter<string>("variable") + "_filterEff"),int(histograms_[i].getParameter<int>("nBins")),histograms_[i].getParameter<double>("lBin"),histograms_[i].getParameter<double>("hBin"));
  // TH1F * h_pt = fs->make<TH1F>( "pt"  , "p_{t}", 100,  0., 100. );
  // TTree * h_ptt = fs->make<TTree>();
}

void AODTriggerAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    edm::Handle< edm::TriggerResults > triggerBits;
    edm::Handle< BXVector<l1t::Muon> > l1Muons;
    edm::Handle< BXVector<l1t::EGamma> > l1EGammas;
    edm::Handle< reco::MuonCollection > recoMuons;
    edm::Handle< reco::PhotonCollection > recoPhotons;
    // edm::Handle< trigger::TriggerEvent > triggerSummary; 


    // edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
    // edm::Handle<pat::PackedTriggerPrescales> triggerPrescales;

    iEvent.getByToken(triggerBits_, triggerBits);
    iEvent.getByToken(l1Muons_, l1Muons);
    iEvent.getByToken(l1EGammas_, l1EGammas);
    iEvent.getByToken(recoMuons_, recoMuons);
    iEvent.getByToken(recoPhotons_, recoPhotons);
    // iEvent.getByToken(triggerObjects_, triggerObjects);
    // iEvent.getByToken(triggerPrescales_, triggerPrescales);


    // L1 Test
    bool l1Test = l1Filter(l1Muons, l1EGammas, iEvent);
    std::cout << "l1Test: " << l1Test << std::endl;

    // Define L3 Objects
    trigger::TriggerObjectCollection muonL3Objects = filterFinder(triggerSummaryLabel_, muonFilterTag_, iEvent);
    trigger::TriggerObjectCollection photonL3Objects = filterFinder(triggerSummaryLabel_, photonFilterTag_, iEvent);

    // HLT Test
    bool hltTest = hltFilter(muonL3Objects, photonL3Objects, iEvent);
    std::cout << "hltTest: " << hltTest << std::endl;

    // RECO Test
    bool recoTest = recoFilter(recoMuons, recoPhotons, iEvent);
    std::cout << "recoTest: " << recoTest << std::endl;

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
  std::cout<<filterObjects.size()<<endl; 
  return filterObjects;
}

bool 
AODTriggerAnalyzer::hltFilter(trigger::TriggerObjectCollection muonL3Objects, trigger::TriggerObjectCollection photonL3Objects, const edm::Event &iEvent)
{
  // L3 Muons
  for (trigger::TriggerObjectCollection::const_iterator it = muonL3Objects.begin(); it != muonL3Objects.end(); it++) {
    if(it->pt() >= 0 ) {
      std::cout << "HLT Muon: " << it->pt() << std::endl;
    }
  }  

// L3 Photons
  for (trigger::TriggerObjectCollection::const_iterator it = photonL3Objects.begin(); it != photonL3Objects.end(); it++) {
    if(it->pt() >= 0 ) {
      std::cout << "HLT Photon: " << it->pt() << std::endl;
    }
  } 
  return true;
}


bool 
AODTriggerAnalyzer::recoFilter(edm::Handle< reco::MuonCollection > recoMuons, edm::Handle< reco::PhotonCollection > recoPhotons, const edm::Event &iEvent)
{
  // Reco Muons
  for (reco::MuonCollection::const_iterator it = recoMuons->begin(); it != recoMuons->end(); it++) {
    if(it->pt() >= 0 ) {
      std::cout << "Reco Muon: " << it->pt() << std::endl;
    }
  }  

// Reco Photons
  for (reco::PhotonCollection::const_iterator it = recoPhotons ->begin(); it != recoPhotons->end(); it++) {
    if(it->pt() >= 0 ) {
      std::cout << "Reco Photon: " << it->pt() << std::endl;
    }
  } 
  return true;
}



bool 
AODTriggerAnalyzer::l1Filter(edm::Handle< BXVector<l1t::Muon> > l1Muons, edm::Handle< BXVector<l1t::EGamma> > l1EGammas, const edm::Event &iEvent)
{
  // L1 Muons
  for (int ibx = l1Muons->getFirstBX(); ibx <= l1Muons->getLastBX(); ++ibx) {
    for (BXVector<l1t::Muon>::const_iterator it=l1Muons->begin(); it!=l1Muons->end(); it++){
      if (it->pt() >= 0){
        std::cout << "L1 Muon: " << it->pt() << std::endl;
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

  // L1 EGammas
  for (int ibx = l1EGammas->getFirstBX(); ibx <= l1EGammas->getLastBX(); ++ibx) {
    for (BXVector<l1t::EGamma>::const_iterator it=l1EGammas->begin(); it!=l1EGammas->end(); it++){
      if (it->pt() >= 0){
        std::cout << "L1 EGamma: " << it->pt() << std::endl;
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
  return true;
}



//define this as a plug-in
DEFINE_FWK_MODULE(AODTriggerAnalyzer);