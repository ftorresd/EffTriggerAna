import FWCore.ParameterSet.Config as cms

process = cms.Process("EffAna")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer16DR80/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/RAWAODSIM/FlatPU28to62HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2A6F3D90-B0F5-E611-A742-ECF4BBE15B60.root'
    )
)

process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('efficiency.root')
)

process.demo1 = cms.EDAnalyzer("AODTriggerAnalyzer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    l1MuonsLabel = cms.InputTag("gmtStage2Digis:Muon"),
    l1EGammasLabel = cms.InputTag("caloStage2Digis:EGamma"),
    recoMuonsLabel = cms.InputTag("muons"),
    recoPhotonsLabel = cms.InputTag("photons"),
    triggerSummaryLabel = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    muonFilterTag = cms.InputTag ("hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09","","HLT"),
    photonFilterTag = cms.InputTag ("hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09","","HLT"),
)

process.demo2 = cms.EDAnalyzer("AODTriggerAnalyzer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    l1MuonsLabel = cms.InputTag("gmtStage2Digis:Muon"),
    l1EGammasLabel = cms.InputTag("caloStage2Digis:EGamma"),
    recoMuonsLabel = cms.InputTag("muons"),
    recoPhotonsLabel = cms.InputTag("photons"),
    triggerSummaryLabel = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    muonFilterTag = cms.InputTag ("hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09","","HLT"),
    photonFilterTag = cms.InputTag ("hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09","","HLT"),
)

process.p = cms.Path(process.demo1 + process.demo2)