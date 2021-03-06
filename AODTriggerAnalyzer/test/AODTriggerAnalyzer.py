import FWCore.ParameterSet.Config as cms

process = cms.Process("L1EffAna")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer16DR80/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/RAWAODSIM/FlatPU28to62HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2A6F3D90-B0F5-E611-A742-ECF4BBE15B60.root'
        # '/store/data/Run2016G/ZeroBias/AOD/23Sep2016-v1/50000/00042352-7786-E611-90FF-0025905A6118.root'
    )
)

process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('efficiency.root')
)

process.Zerobias = cms.EDAnalyzer("AODTriggerAnalyzer",
    verbose = cms.bool(False),
    configName = cms.string("Zerobias"),
    bits = cms.InputTag("TriggerResults","","HLT"),
    # HLT Configs
    minPhotonPt = cms.double(12.0),
    minLeadingMuPt = cms.double(6.0),
    minTrailMuPt  = cms.double(4.0),                                                                                                                                                                                                                                
    minDimuonMass = cms.double(0.0),
    maxDimuonMass = cms.double(12.0),
    # L1 Labels
    l1MuonsLabel = cms.InputTag("gmtStage2Digis:Muon"),
    l1EGammasLabel = cms.InputTag("caloStage2Digis:EGamma"),
    # L1 Configs - Muons
    l1MuonN = cms.uint32(2),
    l1AsymmetricCut = cms.bool(False),
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1MuonQltMin = cms.int32(8),
    l1MuonQltMax = cms.int32(15),
    l1MuonPt = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80),
    l1AsymmetricLeadingMuonCut = cms.double(8.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    l1EGammaPt = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50),
    # RECO Labels
    recoMuonsLabel = cms.InputTag("muons"),
    recoPhotonsLabel = cms.InputTag("photons"),
    # RECO Configs
    minMuPt = cms.double(2.0),# in GeV
    maxMuEta = cms.double(2.4),
    minMuonLeadPt = cms.double(20.0),# in GeV
    minMuonTrailPt = cms.double(4.0), # in GeV
    GammaMinPtCut = cms.double(0.1),# in GeV
    DeltaRLeadMuPhotonSel = cms.double(1.0),# deltaR>DeltaRLeadMuPhotonSel
    DeltaRTrailPhotonSel  = cms.double(1.0),# deltaR>DeltaRTrailPhotonSel 
    minJPsiMass = cms.double(2.95),# in GeV
    maxJPsiMass = cms.double(3.25),# in GeV    
    #HLT Labels
    triggerSummaryLabel = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    muonFilterTag = cms.InputTag ("hltDoubleMuon0L3PreFiltered0","","HLT"),
    photonFilterTag = cms.InputTag ("hltEG22HEFilter","","HLT"),
    # photonFilterTag = cms.InputTag ("hltEGL1SingleEG18Filter","","HLT"),
)

# symmetric seeds
process.DoubleMu_X = process.Zerobias.clone(
    configName = cms.string("DoubleMu_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(False),
    # l1AsymmetricLeadingMuonCut = cms.double(8.),
    # l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.DoubleMu_X_OS = process.Zerobias.clone(
    configName = cms.string("DoubleMu_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(False),
    # l1AsymmetricLeadingMuonCut = cms.double(8.),
    # l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.DoubleMu_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("DoubleMu_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(False),
    # l1AsymmetricLeadingMuonCut = cms.double(8.),
    # l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.DoubleMu_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("DoubleMu_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(False),
    # l1AsymmetricLeadingMuonCut = cms.double(8.),
    # l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.DoubleMu_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("DoubleMu_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(False),
    # l1AsymmetricLeadingMuonCut = cms.double(8.),
    # l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
 
process.DoubleMu_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("DoubleMu_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(False),
    # l1AsymmetricLeadingMuonCut = cms.double(8.),
    # l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

# asymmetric seeds
process.Mu_9_X = process.Zerobias.clone(
    configName = cms.string("Mu_9_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(9.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_9_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_9_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(9.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_9_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_9_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(9.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_9_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_9_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(9.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_9_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_9_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(9.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_9_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_9_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(9.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
    

# asymmetric seeds
process.Mu_10_X = process.Zerobias.clone(
    configName = cms.string("Mu_10_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(10.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_10_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_10_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(10.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_10_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_10_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(10.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_10_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_10_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(10.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_10_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_10_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(10.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_10_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_10_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(10.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
    

# asymmetric seeds
process.Mu_11_X = process.Zerobias.clone(
    configName = cms.string("Mu_11_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(11.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_11_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_11_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(11.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_11_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_11_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(11.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_11_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_11_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(11.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_11_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_11_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(11.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_11_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_11_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(11.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
    

# asymmetric seeds
process.Mu_12_X = process.Zerobias.clone(
    configName = cms.string("Mu_12_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(12.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_12_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_12_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(12.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_12_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_12_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(12.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_12_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_12_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(12.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_12_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_12_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(12.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_12_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_12_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(12.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
    

# asymmetric seeds
process.Mu_13_X = process.Zerobias.clone(
    configName = cms.string("Mu_13_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(13.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_13_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_13_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(13.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_13_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_13_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(13.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_13_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_13_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(13.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_13_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_13_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(13.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_13_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_13_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(13.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
    

# asymmetric seeds
process.Mu_8_X = process.Zerobias.clone(
    configName = cms.string("Mu_8_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(8.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_8_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_8_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(8.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_8_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_8_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(8.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_8_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_8_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(8.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_8_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_8_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(8.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_8_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_8_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(8.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
# asymmetric seeds
process.Mu_7_X = process.Zerobias.clone(
    configName = cms.string("Mu_7_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(7.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_7_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_7_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(7.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_7_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_7_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(7.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_7_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_7_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(7.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_7_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_7_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(7.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_7_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_7_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(7.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
# asymmetric seeds
process.Mu_6_X = process.Zerobias.clone(
    configName = cms.string("Mu_6_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(6.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_6_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_6_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(6.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_6_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_6_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(6.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_6_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_6_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(6.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_6_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_6_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(6.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_6_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_6_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(6.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

# asymmetric seeds
process.Mu_5_X = process.Zerobias.clone(
    configName = cms.string("Mu_5_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(5.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_5_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_5_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(5.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_5_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_5_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(5.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_5_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_5_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(5.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_5_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_5_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(5.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_5_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_5_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(5.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

# asymmetric seeds
process.Mu_4_X = process.Zerobias.clone(
    configName = cms.string("Mu_4_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(4.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_4_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_4_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(4.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_4_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_4_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(4.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_4_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_4_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(4.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_4_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_4_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(4.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_4_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_4_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(4.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

# asymmetric seeds
process.Mu_3_X = process.Zerobias.clone(
    configName = cms.string("Mu_3_X"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    Mu_4l1AsymmetricLeadingMuonCut = cms.double(3.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_3_X_OS = process.Zerobias.clone(
    configName = cms.string("Mu_3_X_OS"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    Mu_4l1AsymmetricLeadingMuonCut = cms.double(3.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(0),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_3_X_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_3_X_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    Mu_4l1AsymmetricLeadingMuonCut = cms.double(3.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_3_X_OS_EG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_3_X_OS_EG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    Mu_4l1AsymmetricLeadingMuonCut = cms.double(3.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(False),
    )

process.Mu_3_X_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_3_X_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(False),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    l1AsymmetricLeadingMuonCut = cms.double(3.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )

process.Mu_3_X_OS_IsoEG_Y = process.Zerobias.clone(
    configName = cms.string("Mu_3_X_OS_IsoEG_Y"),
    # L1 Configs - Muons
    l1MuonOS = cms.bool(True),
    l1MuonIso = cms.bool(False),
    l1AsymmetricCut = cms.bool(True),
    Mu_4l1AsymmetricLeadingMuonCut = cms.double(3.),
    l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2.),
    # L1 Configs - EGammas
    l1EGammaN = cms.uint32(1),
    l1EGammaIso = cms.bool(True),
    )
process.p = cms.Path(
                     process.Zerobias
                     # symmetric cuts
                     + process.DoubleMu_X
                     + process.DoubleMu_X_OS 
                     + process.DoubleMu_X_EG_Y 
                     + process.DoubleMu_X_OS_EG_Y 
                     + process.DoubleMu_X_IsoEG_Y 
                     + process.DoubleMu_X_OS_IsoEG_Y
                     # asymmetric cuts
                     + process.Mu_9_X
                     + process.Mu_9_X_OS 
                     + process.Mu_9_X_EG_Y 
                     + process.Mu_9_X_OS_EG_Y 
                     + process.Mu_9_X_IsoEG_Y 
                     + process.Mu_9_X_OS_IsoEG_Y
                     

                     + process.Mu_10_X
                     + process.Mu_10_X_OS 
                     + process.Mu_10_X_EG_Y 
                     + process.Mu_10_X_OS_EG_Y 
                     + process.Mu_10_X_IsoEG_Y 
                     + process.Mu_10_X_OS_IsoEG_Y
                     

                     + process.Mu_11_X
                     + process.Mu_11_X_OS 
                     + process.Mu_11_X_EG_Y 
                     + process.Mu_11_X_OS_EG_Y 
                     + process.Mu_11_X_IsoEG_Y 
                     + process.Mu_11_X_OS_IsoEG_Y
                     

                     + process.Mu_12_X
                     + process.Mu_12_X_OS 
                     + process.Mu_12_X_EG_Y 
                     + process.Mu_12_X_OS_EG_Y 
                     + process.Mu_12_X_IsoEG_Y 
                     + process.Mu_12_X_OS_IsoEG_Y
                     

                     + process.Mu_13_X
                     + process.Mu_13_X_OS 
                     + process.Mu_13_X_EG_Y 
                     + process.Mu_13_X_OS_EG_Y 
                     + process.Mu_13_X_IsoEG_Y 
                     + process.Mu_13_X_OS_IsoEG_Y
                     
                     + process.Mu_8_X
                     + process.Mu_8_X_OS 
                     + process.Mu_8_X_EG_Y 
                     + process.Mu_8_X_OS_EG_Y 
                     + process.Mu_8_X_IsoEG_Y 
                     + process.Mu_8_X_OS_IsoEG_Y
                     + process.Mu_7_X
                     + process.Mu_7_X_OS 
                     + process.Mu_7_X_EG_Y 
                     + process.Mu_7_X_OS_EG_Y 
                     + process.Mu_7_X_IsoEG_Y 
                     + process.Mu_7_X_OS_IsoEG_Y
                     + process.Mu_6_X
                     + process.Mu_6_X_OS 
                     + process.Mu_6_X_EG_Y 
                     + process.Mu_6_X_OS_EG_Y 
                     + process.Mu_6_X_IsoEG_Y 
                     + process.Mu_6_X_OS_IsoEG_Y
                     + process.Mu_5_X
                     + process.Mu_5_X_OS 
                     + process.Mu_5_X_EG_Y 
                     + process.Mu_5_X_OS_EG_Y 
                     + process.Mu_5_X_IsoEG_Y 
                     + process.Mu_5_X_OS_IsoEG_Y
                     + process.Mu_4_X
                     + process.Mu_4_X_OS 
                     + process.Mu_4_X_EG_Y 
                     + process.Mu_4_X_OS_EG_Y 
                     + process.Mu_4_X_IsoEG_Y 
                     + process.Mu_4_X_OS_IsoEG_Y
                     + process.Mu_3_X
                     + process.Mu_3_X_OS 
                     + process.Mu_3_X_EG_Y 
                     + process.Mu_3_X_OS_EG_Y 
                     + process.Mu_3_X_IsoEG_Y 
                     + process.Mu_3_X_OS_IsoEG_Y
                     # + process.Mu_2_X
                     # + process.Mu_2_X_OS 
                     # + process.Mu_2_X_EG_Y 
                     # + process.Mu_2_X_OS_EG_Y 
                     # + process.Mu_2_X_IsoEG_Y 
                     # + process.Mu_2_X_OS_IsoEG_Y
                     )

