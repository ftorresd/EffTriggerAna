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

#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"

#include <map>
#include <string>
#include <stdlib.h>
#include <iostream>
#include <fstream>



class AODTriggerAnalyzer : public edm::EDAnalyzer {
	public:
		explicit AODTriggerAnalyzer(const edm::ParameterSet&);
		trigger::TriggerObjectCollection filterFinder(edm::EDGetTokenT<trigger::TriggerEvent> triggerSummaryLabel, edm::InputTag filterTag, const edm::Event &iEvent);
		bool l1Filter(edm::Handle< BXVector<l1t::Muon> > l1Muons, edm::Handle< BXVector<l1t::EGamma> > l1EGammas, const edm::Event &iEvent);
		bool recoFilter(edm::Handle< reco::MuonCollection > recoMuons, edm::Handle< reco::PhotonCollection > recoPhotons, const edm::Event &iEvent);
		bool hltFilter(trigger::TriggerObjectCollection muonL3Objects, trigger::TriggerObjectCollection photonL3Objects, const edm::Event &iEvent);
		static bool P4SortCondition(const TLorentzVector& p1, const TLorentzVector& p2) {return (p1.Pt() > p2.Pt());}

		~AODTriggerAnalyzer() {}



	private:
		virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
		bool verbose; 
		edm::EDGetTokenT< edm::TriggerResults > triggerBits_;
		edm::EDGetTokenT< BXVector<l1t::Muon> > l1Muons_;
		edm::EDGetTokenT< BXVector<l1t::EGamma> > l1EGammas_;
		edm::EDGetTokenT< reco::MuonCollection > recoMuons_;
		edm::EDGetTokenT< reco::PhotonCollection > recoPhotons_;
		edm::EDGetTokenT< trigger::TriggerEvent > triggerSummaryLabel_;
		edm::InputTag muonFilterTag_;
		edm::InputTag photonFilterTag_;

		// Reco configs
		double minMuPt;
		double maxMuEta;
		double muonLeadPt, muonTrailPt;

        //HLT Configs
        double minPhotonPt; 
        double minLeadingMuPt; 
        double minTrailMuPt;                                                                                                                                                                                                                                   
        double minDimuonMass;  
        double maxDimuonMass;  

		// L1 Configs
		bool l1MuonOS_;
		bool l1MuonIso_;
		int l1MuonQltMin_;
		int l1MuonQltMax_;
		std::vector<double> l1MuonPt_;




		// edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> triggerObjects_;
		// edm::EDGetTokenT<pat::PackedTriggerPrescales> triggerPrescales_;
};

AODTriggerAnalyzer::AODTriggerAnalyzer(const edm::ParameterSet& iConfig):
	verbose (iConfig.getParameter< bool > ("Verbose")),
	triggerBits_(consumes< edm::TriggerResults >(iConfig.getParameter<edm::InputTag>("bits"))),
	l1Muons_(consumes< BXVector<l1t::Muon> >(iConfig.getParameter<edm::InputTag>("l1MuonsLabel"))),
	l1EGammas_(consumes< BXVector<l1t::EGamma> >(iConfig.getParameter<edm::InputTag>("l1EGammasLabel"))),
	recoMuons_(consumes< reco::MuonCollection >(iConfig.getParameter<edm::InputTag>("recoMuonsLabel"))),
	recoPhotons_(consumes< reco::PhotonCollection >(iConfig.getParameter<edm::InputTag>("recoPhotonsLabel"))),
	triggerSummaryLabel_ (consumes<trigger::TriggerEvent>(iConfig.getParameter<edm::InputTag> ("triggerSummaryLabel"))),
	muonFilterTag_ (iConfig.getParameter<edm::InputTag> ("muonFilterTag")),
	photonFilterTag_ (iConfig.getParameter<edm::InputTag> ("photonFilterTag")),

	// Reco config
	minMuPt (iConfig.getUntrackedParameter<double>("minMuPt",2.0)),
	maxMuEta (iConfig.getUntrackedParameter<double>("maxMuEta",2.4)), 
	muonLeadPt (iConfig.getUntrackedParameter<double>("minMuonLeadPt",20.0)),
	muonTrailPt (iConfig.getUntrackedParameter<double>("minMuonTrailPt",4.0)),
 
    // HLT Configs
    minPhotonPt (iConfig.getUntrackedParameter<double>("minPhotonPt",12.0)),
    minLeadingMuPt (iConfig.getUntrackedParameter<double>("minLeadingMuPt",6.0)),
    minTrailMuPt   (iConfig.getUntrackedParameter<double>("minTrailMuPt",4.0)),                                                                                                                                                                                                                                 
    minDimuonMass  (iConfig.getUntrackedParameter<double>("minDimuonMass",0.0)),
    maxDimuonMass  (iConfig.getUntrackedParameter<double>("maxDimuonMass",12.0)),

	// L1 Configs
	l1MuonOS_ (iConfig.getParameter< bool > ("l1MuonOS")),
	l1MuonIso_ (iConfig.getParameter< bool > ("l1MuonIso")),
	l1MuonQltMin_ (iConfig.getParameter< int > ("l1MuonQltMin")),
	l1MuonQltMax_ (iConfig.getParameter< int > ("l1MuonQltMax")),
	l1MuonPt_ (iConfig.getParameter< std::vector<double> > ("l1MuonPt"))

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


	if (verbose) std::cout << "Configs: " << l1MuonOS_ << l1MuonIso_ << l1MuonQltMin_ << l1MuonQltMax_ << std::endl;
	for (std::vector<double>::const_iterator it = l1MuonPt_.begin(); it != l1MuonPt_.end(); it++ ){
		if (verbose) std::cout << *it << std::endl; 
	}



	// L1 Test
	bool l1Test = l1Filter(l1Muons, l1EGammas, iEvent);
	if (verbose) std::cout << "l1Test: " << l1Test << std::endl;

	// Define L3 Objects
	trigger::TriggerObjectCollection muonL3Objects = filterFinder(triggerSummaryLabel_, muonFilterTag_, iEvent);
	trigger::TriggerObjectCollection photonL3Objects = filterFinder(triggerSummaryLabel_, photonFilterTag_, iEvent);

        //trigger::TriggerObjectCollection allTriggerObjects = triggerSummary->getObjects();
        //trigger::TriggerObjectCollection hltMuons = selectTriggerObjects(allTriggerObjects, *triggerSummary, hltCuts);


	// HLT Test
	bool hltTest = hltFilter(muonL3Objects, photonL3Objects, iEvent);
	if (verbose) std::cout << "hltTest: " << hltTest << std::endl;

	// RECO Test
	bool recoTest = recoFilter(recoMuons, recoPhotons, iEvent);
	if (verbose) std::cout << "recoTest: " << recoTest << std::endl;

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
	if (verbose) std::cout<<filterObjects.size()<<endl; 
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
			if (verbose) std::cout << "HLT Muon: " << it->pt() << std::endl;
		}
         ptMuon.push_back(it->pt());
         etaMuon.push_back(it->eta());
         phiMuon.push_back(it->phi());
         if (ptMuon.size()>1) {
             math::PtEtaPhiMLorentzVectorD* mu1 = new math::PtEtaPhiMLorentzVectorD(ptMuon[0],etaMuon[0],phiMuon[0],0.106);
             math::PtEtaPhiMLorentzVectorD* mu2 = new math::PtEtaPhiMLorentzVectorD(ptMuon[1],etaMuon[1],phiMuon[1],0.106);
             (*mu1)+=(*mu2);
             DoubleMuMass=(mu1->M());
             if (verbose) std::cout << "HLT DoubleMuMass: " << DoubleMuMass << std::endl;
             if((mu1->Pt()<minLeadingMuPt) && (mu2->Pt()< minTrailMuPt)) continue ;
             if (DoubleMuMass < minDimuonMass && minDimuonMass > maxDimuonMass)continue;
          
                 
            }
             
        }
	  

	// L3 Photons
	std::vector<float> ptPhoton, etaPhoton, phiPhoton;
	for (trigger::TriggerObjectCollection::const_iterator it = photonL3Objects.begin(); it != photonL3Objects.end(); it++) {
		if(it->pt() >= 0 ) {
			if (verbose) std::cout << "HLT Photon: " << it->pt() << std::endl;
		}
		ptPhoton.push_back(it->pt());
        etaPhoton.push_back(it->eta());
        phiPhoton.push_back(it->phi());
        if(it->pt() < minPhotonPt )continue;
	} 
	return true;
}


	bool 
AODTriggerAnalyzer::recoFilter(edm::Handle< reco::MuonCollection > recoMuons, edm::Handle< reco::PhotonCollection > recoPhotons, const edm::Event &iEvent)
{

	vector<TLorentzVector> myLeptons, myPhotons; 

	// Reco Muons
	for (reco::MuonCollection::const_iterator it = recoMuons->begin(); it != recoMuons->end(); it++) {

		TLorentzVector muon_tmp = TLorentzVector(it->px(), it->py(), it->pz(), it->energy());  
		if (it->isPFMuon()){
			if (it->isTrackerMuon() || it->isGlobalMuon()){
				if (it->pt()<minMuPt && std::abs(it->eta())<maxMuEta){  
					myLeptons.push_back(muon_tmp);
					if(verbose) cout<<"Muon "<<it->pt()<<endl;
				}//eta and pt muon
			}//muon type selection
		}//PF muon
	}// Muon loop

	sort(myLeptons.begin(), myLeptons.end(), P4SortCondition);
	if(verbose) std::cout<<" myLeptons.size() all  " << myLeptons.size() << std::endl;
	// dimuon selection
	if (myLeptons.size() == 2 && myLeptons.size() !=0 ) {
		std::cout<<" Multiplicity of muons:  " << myLeptons.size() << std::endl;
		TLorentzVector l1 = myLeptons[0];
		TLorentzVector l2 = myLeptons[1];
		std::cout<< "Lepton 1 pt, eta, phi = " << l1.Pt() << l1.PseudoRapidity() << l1.Phi() << std::endl;
		std::cout<< "Lepton 2 pt, eta, phi = " << l2.Pt() << l2.PseudoRapidity() << l2.Phi() << std::endl;
		//Invariant mass of muons
		double Mll = (l1+l2).M();
		std::cout<< "Mll " << Mll <<std::endl;

		//double Mll_pt
		if (l1.Pt() > muonLeadPt || l2.Pt() > muonTrailPt ) {

			// ***
			//   // jpsi peak
			//     // ***
			//
			if (Mll > 2.95 && Mll < 3.25){

				std::cout<<" Invariant Mass in JPsi peak " << Mll << std::endl;
			}// Z selection
		}//lead and trail muon pT cut

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
				if (verbose) std::cout << "L1 Muon: " << it->pt() << std::endl;
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
				if (verbose) std::cout << "L1 EGamma: " << it->pt() << std::endl;
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
