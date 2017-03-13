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

process.effana1 = cms.EDAnalyzer("AODTriggerAnalyzer",
    configName = cms.string("effana"),
    bits = cms.InputTag("TriggerResults","","HLT"),
    # L1 Labels
    l1MuonsLabel = cms.InputTag("gmtStage2Digis:Muon"),
    l1EGammasLabel = cms.InputTag("caloStage2Digis:EGamma"),
    # L1 Configs - Muons
    l1MuonN = cms.uint32(2),
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1MuonQltMin = cms.int32(0),
    l1MuonQltMax = cms.int32(99999),
    l1MuonPt = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80),
    # L1 Configs - EGammas
    l1EGammaIso = cms.bool(False),
    l1EGammaPt = cms.vdouble(3),
    # RECO Labels
    recoMuonsLabel = cms.InputTag("muons"),
    recoPhotonsLabel = cms.InputTag("photons"),
    #HLT Labels
    triggerSummaryLabel = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    muonFilterTag = cms.InputTag ("hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09","","HLT"),
    photonFilterTag = cms.InputTag ("hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09","","HLT"),
)



process.p = cms.Path(process.effana1)
# process.p = cms.Path(process.demo1 + process.demo2)