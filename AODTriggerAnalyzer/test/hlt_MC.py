


# /users/ftorresd/TriggerStudies2017/V17 (CMSSW_9_1_0_pre3)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "MYHLT" )
process.load("setup_dev_CMSSW_9_1_0_HLT_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/ftorresd/TriggerStudies2017/V17')
)

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    PrintL1Menu = cms.untracked.bool( False ),
    Verbosity = cms.untracked.int32( 0 ),
    EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    PrescaleSet = cms.uint32( 1 ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    BstLengthBytes = cms.int32( -1 ),
    MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu4_OS_EG12 OR L1_DoubleMu5_OS_EG12" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreDoubleMu55Mass0to30Photon12 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( 'hltGtStage2Digis','Muon' )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
    useStandardFEDid = cms.bool( True ),
    maxFEDid = cms.untracked.int32( 779 ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    minFEDid = cms.untracked.int32( 770 ),
    dataType = cms.string( "DDU" ),
    readOutParameters = cms.PSet( 
      localDAQ = cms.untracked.bool( False ),
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet( 
        localDAQ = cms.untracked.bool( False ),
        debug = cms.untracked.bool( False ),
        writeSC = cms.untracked.bool( True ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        readingDDU = cms.untracked.bool( True ),
        performDataIntegrityMonitor = cms.untracked.bool( False )
      ),
      performDataIntegrityMonitor = cms.untracked.bool( False )
    ),
    dqmOnly = cms.bool( False )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet( 
      maxTime = cms.double( 420.0 ),
      debug = cms.untracked.bool( False ),
      stepTwoFromDigi = cms.bool( False ),
      tTrigModeConfig = cms.PSet( 
        debug = cms.untracked.bool( False ),
        tofCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        wirePropCorrType = cms.int32( 0 ),
        doTOFCorrection = cms.bool( True ),
        vPropWire = cms.double( 24.4 ),
        doT0Correction = cms.bool( True ),
        doWirePropCorrection = cms.bool( True )
      ),
      useUncertDB = cms.bool( True ),
      doVdriftCorr = cms.bool( True ),
      minTime = cms.double( -3.0 ),
      tTrigMode = cms.string( "DTTTrigSyncFromDB" )
    ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet( 
      Reco2DAlgoConfig = cms.PSet( 
        AlphaMaxPhi = cms.double( 1.0 ),
        debug = cms.untracked.bool( False ),
        segmCleanerMode = cms.int32( 2 ),
        AlphaMaxTheta = cms.double( 0.9 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        recAlgoConfig = cms.PSet( 
          maxTime = cms.double( 420.0 ),
          debug = cms.untracked.bool( False ),
          stepTwoFromDigi = cms.bool( False ),
          tTrigModeConfig = cms.PSet( 
            debug = cms.untracked.bool( False ),
            tofCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            wirePropCorrType = cms.int32( 0 ),
            doTOFCorrection = cms.bool( True ),
            vPropWire = cms.double( 24.4 ),
            doT0Correction = cms.bool( True ),
            doWirePropCorrection = cms.bool( True )
          ),
          useUncertDB = cms.bool( True ),
          doVdriftCorr = cms.bool( True ),
          minTime = cms.double( -3.0 ),
          tTrigMode = cms.string( "DTTTrigSyncFromDB" )
        ),
        MaxAllowedHits = cms.uint32( 50 ),
        nUnSharedHitsMin = cms.int32( 2 ),
        nSharedHitsMax = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      debug = cms.untracked.bool( False ),
      segmCleanerMode = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      recAlgoConfig = cms.PSet( 
        maxTime = cms.double( 420.0 ),
        debug = cms.untracked.bool( False ),
        stepTwoFromDigi = cms.bool( False ),
        tTrigModeConfig = cms.PSet( 
          debug = cms.untracked.bool( False ),
          tofCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          wirePropCorrType = cms.int32( 0 ),
          doTOFCorrection = cms.bool( True ),
          vPropWire = cms.double( 24.4 ),
          doT0Correction = cms.bool( True ),
          doWirePropCorrection = cms.bool( True )
        ),
        useUncertDB = cms.bool( True ),
        doVdriftCorr = cms.bool( True ),
        minTime = cms.double( -3.0 ),
        tTrigMode = cms.string( "DTTTrigSyncFromDB" )
      ),
      nUnSharedHitsMin = cms.int32( 2 ),
      nSharedHitsMax = cms.int32( 2 ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool( False ),
    SuppressZeroLCT = cms.untracked.bool( True ),
    UseExaminer = cms.bool( True ),
    Debug = cms.untracked.bool( False ),
    ErrorMask = cms.uint32( 0 ),
    InputObjects = cms.InputTag( "rawDataCollector" ),
    ExaminerMask = cms.uint32( 535557110 ),
    runDQM = cms.untracked.bool( False ),
    UnpackStatusDigis = cms.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    UseFormatStatus = cms.bool( True ),
    UseSelectiveUnpacking = cms.bool( True ),
    VisualFEDShort = cms.untracked.bool( False )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCWireTimeWindowHigh = cms.int32( 15 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    CSCWireTimeWindowLow = cms.int32( 0 ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( False ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    UseParabolaFit = cms.bool( False ),
    CSCUseReducedWireTimeWindow = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    CSCDebug = cms.untracked.bool( False ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet( 
      cms.PSet(  parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  dYclusBoxMax = cms.double( 8.0 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            maxRatioResidualPrune = cms.double( 3.0 ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            useShowering = cms.bool( False ),
            BPMinImprovement = cms.double( 10000.0 ),
            curvePenalty = cms.double( 2.0 ),
            ForceCovariance = cms.bool( False ),
            yweightPenalty = cms.double( 1.5 ),
            dPhiFineMax = cms.double( 0.025 ),
            SeedBig = cms.double( 0.0015 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            Covariance = cms.double( 0.0 ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            Pruning = cms.bool( True ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dXclusBoxMax = cms.double( 4.0 ),
            maxDTheta = cms.double( 999.0 ),
            preClustering = cms.bool( True ),
            preClusteringUseChaining = cms.bool( True ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            prePrun = cms.bool( True ),
            CorrectTheErrors = cms.bool( True ),
            ForceCovarianceAll = cms.bool( False ),
            NormChi2Cut2D = cms.double( 20.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            minHitsPerSegment = cms.int32( 3 ),
            dRPhiFineMax = cms.double( 8.0 ),
            maxDPhi = cms.double( 999.0 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            BrutePruning = cms.bool( True ),
            prePrunLimit = cms.double( 3.17 )
          ),
          cms.PSet(  dYclusBoxMax = cms.double( 8.0 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            maxRatioResidualPrune = cms.double( 3.0 ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            useShowering = cms.bool( False ),
            BPMinImprovement = cms.double( 10000.0 ),
            curvePenalty = cms.double( 2.0 ),
            ForceCovariance = cms.bool( False ),
            yweightPenalty = cms.double( 1.5 ),
            dPhiFineMax = cms.double( 0.025 ),
            SeedBig = cms.double( 0.0015 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            Covariance = cms.double( 0.0 ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            Pruning = cms.bool( True ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dXclusBoxMax = cms.double( 4.0 ),
            maxDTheta = cms.double( 999.0 ),
            preClustering = cms.bool( True ),
            preClusteringUseChaining = cms.bool( True ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            prePrun = cms.bool( True ),
            CorrectTheErrors = cms.bool( True ),
            ForceCovarianceAll = cms.bool( False ),
            NormChi2Cut2D = cms.double( 20.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            minHitsPerSegment = cms.int32( 3 ),
            dRPhiFineMax = cms.double( 8.0 ),
            maxDPhi = cms.double( 999.0 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            BrutePruning = cms.bool( True ),
            prePrunLimit = cms.double( 3.17 )
          )
        ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        chamber_types = cms.vstring( 'ME1/a',
          'ME1/b',
          'ME1/2',
          'ME1/3',
          'ME2/1',
          'ME2/2',
          'ME3/1',
          'ME3/2',
          'ME4/1',
          'ME4/2' )
      )
    ),
    algo_type = cms.int32( 1 )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
process.hltL2OfflineMuonSeeds = cms.EDProducer( "MuonSeedGenerator",
    SMB_21 = cms.vdouble( 1.043, -0.124, 0.0, 0.183, 0.0, 0.0 ),
    SMB_20 = cms.vdouble( 1.011, -0.052, 0.0, 0.188, 0.0, 0.0 ),
    SMB_22 = cms.vdouble( 1.474, -0.758, 0.0, 0.185, 0.0, 0.0 ),
    OL_2213 = cms.vdouble( 0.117, 0.0, 0.0, 0.044, 0.0, 0.0 ),
    SME_11 = cms.vdouble( 3.295, -1.527, 0.112, 0.378, 0.02, 0.0 ),
    SME_13 = cms.vdouble( -1.286, 1.711, 0.0, 0.356, 0.0, 0.0 ),
    SME_12 = cms.vdouble( 0.102, 0.599, 0.0, 0.38, 0.0, 0.0 ),
    DT_34_2_scale = cms.vdouble( -11.901897, 0.0 ),
    OL_1213_0_scale = cms.vdouble( -4.488158, 0.0 ),
    OL_1222_0_scale = cms.vdouble( -5.810449, 0.0 ),
    DT_13 = cms.vdouble( 0.315, 0.068, -0.127, 0.051, -0.002, 0.0 ),
    DT_12 = cms.vdouble( 0.183, 0.054, -0.087, 0.028, 0.002, 0.0 ),
    DT_14 = cms.vdouble( 0.359, 0.052, -0.107, 0.072, -0.004, 0.0 ),
    CSC_13_3_scale = cms.vdouble( -1.701268, 0.0 ),
    DT_24_2_scale = cms.vdouble( -6.63094, 0.0 ),
    CSC_23 = cms.vdouble( -0.081, 0.113, -0.029, 0.015, 0.008, 0.0 ),
    CSC_24 = cms.vdouble( 0.004, 0.021, -0.002, 0.053, 0.0, 0.0 ),
    OL_2222 = cms.vdouble( 0.107, 0.0, 0.0, 0.04, 0.0, 0.0 ),
    DT_14_2_scale = cms.vdouble( -4.808546, 0.0 ),
    SMB_10 = cms.vdouble( 1.387, -0.038, 0.0, 0.19, 0.0, 0.0 ),
    SMB_11 = cms.vdouble( 1.247, 0.72, -0.802, 0.229, -0.075, 0.0 ),
    SMB_12 = cms.vdouble( 2.128, -0.956, 0.0, 0.199, 0.0, 0.0 ),
    SME_21 = cms.vdouble( -0.529, 1.194, -0.358, 0.472, 0.086, 0.0 ),
    SME_22 = cms.vdouble( -1.207, 1.491, -0.251, 0.189, 0.243, 0.0 ),
    DT_13_2_scale = cms.vdouble( -4.257687, 0.0 ),
    CSC_34 = cms.vdouble( 0.062, -0.067, 0.019, 0.021, 0.003, 0.0 ),
    SME_22_0_scale = cms.vdouble( -3.457901, 0.0 ),
    DT_24_1_scale = cms.vdouble( -7.490909, 0.0 ),
    OL_1232_0_scale = cms.vdouble( -5.964634, 0.0 ),
    DT_23_1_scale = cms.vdouble( -5.320346, 0.0 ),
    SME_13_0_scale = cms.vdouble( 0.104905, 0.0 ),
    SMB_22_0_scale = cms.vdouble( 1.346681, 0.0 ),
    CSC_12_1_scale = cms.vdouble( -6.434242, 0.0 ),
    DT_34 = cms.vdouble( 0.044, 0.004, -0.013, 0.029, 0.003, 0.0 ),
    SME_32 = cms.vdouble( -0.901, 1.333, -0.47, 0.41, 0.073, 0.0 ),
    SME_31 = cms.vdouble( -1.594, 1.482, -0.317, 0.487, 0.097, 0.0 ),
    CSC_13_2_scale = cms.vdouble( -6.077936, 0.0 ),
    crackEtas = cms.vdouble( 0.2, 1.6, 1.7 ),
    SME_11_0_scale = cms.vdouble( 1.325085, 0.0 ),
    SMB_20_0_scale = cms.vdouble( 1.486168, 0.0 ),
    DT_13_1_scale = cms.vdouble( -4.520923, 0.0 ),
    CSC_24_1_scale = cms.vdouble( -6.055701, 0.0 ),
    CSC_01_1_scale = cms.vdouble( -1.915329, 0.0 ),
    DT_23 = cms.vdouble( 0.13, 0.023, -0.057, 0.028, 0.004, 0.0 ),
    DT_24 = cms.vdouble( 0.176, 0.014, -0.051, 0.051, 0.003, 0.0 ),
    SMB_12_0_scale = cms.vdouble( 2.283221, 0.0 ),
    deltaPhiSearchWindow = cms.double( 0.25 ),
    SMB_30_0_scale = cms.vdouble( -3.629838, 0.0 ),
    SME_42 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    SME_41 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    deltaEtaSearchWindow = cms.double( 0.2 ),
    CSC_12_2_scale = cms.vdouble( -1.63622, 0.0 ),
    DT_34_1_scale = cms.vdouble( -13.783765, 0.0 ),
    CSC_34_1_scale = cms.vdouble( -11.520507, 0.0 ),
    OL_2213_0_scale = cms.vdouble( -7.239789, 0.0 ),
    SMB_32_0_scale = cms.vdouble( -3.054156, 0.0 ),
    CSC_12_3_scale = cms.vdouble( -1.63622, 0.0 ),
    deltaEtaCrackSearchWindow = cms.double( 0.25 ),
    SME_21_0_scale = cms.vdouble( -0.040862, 0.0 ),
    OL_1232 = cms.vdouble( 0.184, 0.0, 0.0, 0.066, 0.0, 0.0 ),
    DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
    SMB_10_0_scale = cms.vdouble( 2.448566, 0.0 ),
    EnableDTMeasurement = cms.bool( True ),
    CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
    CSC_23_2_scale = cms.vdouble( -6.079917, 0.0 ),
    scaleDT = cms.bool( True ),
    DT_12_2_scale = cms.vdouble( -3.518165, 0.0 ),
    OL_1222 = cms.vdouble( 0.848, -0.591, 0.0, 0.062, 0.0, 0.0 ),
    CSC_23_1_scale = cms.vdouble( -19.084285, 0.0 ),
    OL_1213 = cms.vdouble( 0.96, -0.737, 0.0, 0.052, 0.0, 0.0 ),
    CSC_02 = cms.vdouble( 0.612, -0.207, 0.0, 0.067, -0.001, 0.0 ),
    CSC_03 = cms.vdouble( 0.787, -0.338, 0.029, 0.101, -0.008, 0.0 ),
    CSC_01 = cms.vdouble( 0.166, 0.0, 0.0, 0.031, 0.0, 0.0 ),
    SMB_32 = cms.vdouble( 0.67, -0.327, 0.0, 0.22, 0.0, 0.0 ),
    SMB_30 = cms.vdouble( 0.505, -0.022, 0.0, 0.215, 0.0, 0.0 ),
    SMB_31 = cms.vdouble( 0.549, -0.145, 0.0, 0.207, 0.0, 0.0 ),
    crackWindow = cms.double( 0.04 ),
    CSC_14_3_scale = cms.vdouble( -1.969563, 0.0 ),
    SMB_31_0_scale = cms.vdouble( -3.323768, 0.0 ),
    DT_12_1_scale = cms.vdouble( -3.692398, 0.0 ),
    SMB_21_0_scale = cms.vdouble( 1.58384, 0.0 ),
    DT_23_2_scale = cms.vdouble( -5.117625, 0.0 ),
    SME_12_0_scale = cms.vdouble( 2.279181, 0.0 ),
    DT_14_1_scale = cms.vdouble( -5.644816, 0.0 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    SMB_11_0_scale = cms.vdouble( 2.56363, 0.0 ),
    EnableCSCMeasurement = cms.bool( True ),
    CSC_14 = cms.vdouble( 0.606, -0.181, -0.002, 0.111, -0.003, 0.0 ),
    OL_2222_0_scale = cms.vdouble( -7.667231, 0.0 ),
    CSC_13 = cms.vdouble( 0.901, -1.302, 0.533, 0.045, 0.005, 0.0 ),
    CSC_12 = cms.vdouble( -0.161, 0.254, -0.047, 0.042, -0.007, 0.0 )
)
process.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGeneratorFromL1T",
    OfflineSeedLabel = cms.untracked.InputTag( "hltL2OfflineMuonSeeds" ),
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' )
    ),
    CentralBxOnly = cms.bool( True ),
    InputObjects = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1MaxEta = cms.double( 2.5 ),
    EtaMatchingBins = cms.vdouble( 0.0, 2.5 ),
    L1MinPt = cms.double( 0.0 ),
    L1MinQuality = cms.uint32( 7 ),
    GMTReadoutCollection = cms.InputTag( "" ),
    UseUnassociatedL1 = cms.bool( False ),
    UseOfflineSeed = cms.untracked.bool( True ),
    MatchDR = cms.vdouble( 0.3 ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" )
)
process.hltL2Muons = cms.EDProducer( "L2MuonProducer",
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' )
    ),
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    SeedTransformerParameters = cms.PSet( 
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      NMinRecHits = cms.uint32( 2 ),
      RescaleError = cms.double( 100.0 ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      UseSubRecHits = cms.bool( False ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
    ),
    L2TrajBuilderParameters = cms.PSet( 
      BWFilterParameters = cms.PSet( 
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        BWSeedType = cms.string( "fromGenerator" ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        EnableRPCMeasurement = cms.bool( True ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          ExcludeRPCFromFit = cms.bool( False ),
          Granularity = cms.int32( 0 ),
          MaxChi2 = cms.double( 25.0 ),
          RescaleError = cms.bool( False ),
          RescaleErrorFactor = cms.double( 100.0 ),
          UseInvalidHits = cms.bool( True )
        ),
        EnableCSCMeasurement = cms.bool( True ),
        MaxChi2 = cms.double( 100.0 ),
        FitDirection = cms.string( "outsideIn" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        NumberOfSigma = cms.double( 3.0 ),
        EnableDTMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False ),
      FilterParameters = cms.PSet( 
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        EnableRPCMeasurement = cms.bool( True ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          ExcludeRPCFromFit = cms.bool( False ),
          Granularity = cms.int32( 0 ),
          MaxChi2 = cms.double( 25.0 ),
          RescaleError = cms.bool( False ),
          RescaleErrorFactor = cms.double( 100.0 ),
          UseInvalidHits = cms.bool( True )
        ),
        EnableCSCMeasurement = cms.bool( True ),
        MaxChi2 = cms.double( 1000.0 ),
        FitDirection = cms.string( "insideOut" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        NumberOfSigma = cms.double( 3.0 ),
        EnableDTMeasurement = cms.bool( True )
      ),
      SeedPosition = cms.string( "in" ),
      DoBackwardFilter = cms.bool( True ),
      DoRefit = cms.bool( False ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet( 
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        NMinRecHits = cms.uint32( 2 ),
        RescaleError = cms.double( 100.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        UseSubRecHits = cms.bool( False ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
    ),
    DoSeedRefit = cms.bool( False ),
    TrackLoaderParameters = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( False ),
      VertexConstraint = cms.bool( True ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
      ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonTrajectoryBuilder = cms.string( "Exhaustive" )
)
process.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 = cms.EDFilter( "HLTMuonL2FromL1TPreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( False ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    CablingMapLabel = cms.string( "" ),
    UserErrorList = cms.vint32(  )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 40000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltSiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClusters" ),
    onDemand = cms.bool( False )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      useCMMeanMap = cms.bool( False ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      PedestalSubtractionFedMode = cms.bool( True )
    ),
    Clusterizer = cms.PSet( 
      QualityLabel = cms.string( "" ),
      ClusterThreshold = cms.double( 5.0 ),
      SeedThreshold = cms.double( 3.0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      ChannelThreshold = cms.double( 2.0 ),
      MaxAdjacentBad = cms.uint32( 0 ),
      setDetId = cms.bool( True ),
      MaxSequentialHoles = cms.uint32( 0 ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
      MaxSequentialBad = cms.uint32( 1 )
    ),
    onDemand = cms.bool( True )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
    pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" )
)
process.hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      copyMuonRecHit = cms.bool( False ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
      errorMatrixPset = cms.PSet( 
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet( 
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          pf3_V14 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V25 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V13 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V24 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V35 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V12 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V23 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V34 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V45 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V11 = cms.PSet( 
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V22 = cms.PSet( 
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V33 = cms.PSet( 
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V44 = cms.PSet( 
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V55 = cms.PSet( 
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
            action = cms.string( "scale" )
          ),
          pf3_V15 = cms.PSet( 
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
            action = cms.string( "scale" )
          )
        )
      ),
      ComponentName = cms.string( "TSGForRoadSearch" ),
      maxChi2 = cms.double( 40.0 ),
      manySeeds = cms.bool( False ),
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 )
    ),
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSteppingHelixPropagatorOpposite',
        'hltESPSteppingHelixPropagatorAlong' )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet(  ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2OIState = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedOIState" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIState" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 1.0 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonTrackingRegionBuilder8356" ) ),
      TrackTransformer = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      GlbRefitterParameters = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" )
    ),
    TrackLoaderParameters = cms.PSet( 
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( True ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      iterativeTSG = cms.PSet( 
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        beamSpot = cms.InputTag( "unused" ),
        MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
        SelectState = cms.bool( False ),
        ErrorRescaling = cms.double( 3.0 ),
        UseVertexState = cms.bool( True ),
        SigmaZ = cms.double( 25.0 ),
        MaxChi2 = cms.double( 40.0 ),
        errorMatrixPset = cms.PSet( 
          atIP = cms.bool( True ),
          action = cms.string( "use" ),
          errorMatrixValuesPSet = cms.PSet( 
            xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
            zAxis = cms.vdouble( -3.14159, 3.14159 ),
            yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
            pf3_V14 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V25 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V13 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V24 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V35 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V12 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V23 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V34 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V45 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V11 = cms.PSet( 
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V22 = cms.PSet( 
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V33 = cms.PSet( 
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V44 = cms.PSet( 
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V55 = cms.PSet( 
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 ),
              action = cms.string( "scale" )
            ),
            pf3_V15 = cms.PSet( 
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ),
              action = cms.string( "scale" )
            )
          )
        ),
        Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
        ComponentName = cms.string( "TSGFromPropagation" ),
        UpdateState = cms.bool( True ),
        ResetMethod = cms.string( "matrix" )
      ),
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" ),
      L3TkCollectionA = cms.InputTag( "hltL3MuonsOIState" )
    ),
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial',
        'hltESPSmartPropagatorAnyOpposite' )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      cleanerFromSharedHits = cms.bool( True ),
      directionCleaner = cms.bool( True ),
      ptCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedOIHit" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 1.0 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonTrackingRegionBuilder8356" ) ),
      TrackTransformer = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      GlbRefitterParameters = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIHit" )
    ),
    TrackLoaderParameters = cms.PSet( 
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( True ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit' )
)
process.hltPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
process.hltPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
process.hltMixedLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix2_pos+TEC1_pos',
      'FPix2_pos+TEC2_pos',
      'TEC1_pos+TEC2_pos',
      'TEC2_pos+TEC3_pos',
      'FPix2_neg+TEC1_neg',
      'FPix2_neg+TEC2_neg',
      'TEC1_neg+TEC2_neg',
      'TEC2_neg+TEC3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      useRingSlector = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
      maxRing = cms.int32( 1 )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
process.hltL3TrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      iterativeTSG = cms.PSet( 
        firstTSG = cms.PSet( 
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" ),
            ComponentName = cms.string( "StandardHitTripletGenerator" ),
            GeneratorPSet = cms.PSet( 
              SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
              maxElement = cms.uint32( 0 ),
              useFixedPreFiltering = cms.bool( False ),
              extraHitRZtolerance = cms.double( 0.06 ),
              phiPreFiltering = cms.double( 0.3 ),
              extraHitRPhitolerance = cms.double( 0.06 ),
              useBending = cms.bool( True ),
              ComponentName = cms.string( "PixelTripletHLTGenerator" ),
              useMultScattering = cms.bool( True )
            )
          ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) ),
          ComponentName = cms.string( "TSGFromOrderedHits" )
        ),
        secondTSG = cms.PSet( 
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            SeedingLayers = cms.InputTag( "hltPixelLayerPairs" ),
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            useOnDemandTracker = cms.untracked.int32( 0 )
          ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) ),
          ComponentName = cms.string( "TSGFromOrderedHits" )
        ),
        PSetNames = cms.vstring( 'firstTSG',
          'secondTSG' ),
        thirdTSG = cms.PSet( 
          etaSeparation = cms.double( 2.0 ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) ),
          PSetNames = cms.vstring( 'endcapTSG',
            'barrelTSG' ),
          barrelTSG = cms.PSet(  ),
          ComponentName = cms.string( "DualByEtaTSG" ),
          endcapTSG = cms.PSet( 
            TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
            OrderedHitsFactoryPSet = cms.PSet( 
              SeedingLayers = cms.InputTag( "hltMixedLayerPairs" ),
              maxElement = cms.uint32( 0 ),
              ComponentName = cms.string( "StandardHitPairGenerator" ),
              useOnDemandTracker = cms.untracked.int32( 0 )
            ),
            ComponentName = cms.string( "TSGFromOrderedHits" )
          )
        ),
        ComponentName = cms.string( "CombinedTSG" )
      ),
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" ),
      L3TkCollectionA = cms.InputTag( "hltL3TkFromL2OICombination" )
    ),
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial' )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonTrackingRegionBuilder8356" ) ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      cleanerFromSharedHits = cms.bool( True ),
      directionCleaner = cms.bool( True ),
      ptCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3TrajSeedIOHit" ),
    reverseTrajectories = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2IOHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 1.0 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonTrackingRegionBuilder8356" ) ),
      TrackTransformer = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      GlbRefitterParameters = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2IOHit" )
    ),
    TrackLoaderParameters = cms.PSet( 
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( True ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltL3TrajSeedIOHit','hltL3TrajSeedOIState','hltL3TrajSeedOIHit' )
)
process.hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltL3TrackCandidateFromL2IOHit','hltL3TrackCandidateFromL2OIHit','hltL3TrackCandidateFromL2OIState' )
)
process.hltL3TkTracksMergeStep1 = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltL3TkTracksFromL2OIState','hltL3TkTracksFromL2OIHit' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 100.0 ),
    LostHitPenalty = cms.double( 0.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltL3TkTracksFromL2OIState','hltL3TkTracksFromL2OIHit' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltL3TkTracksFromL2 = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltL3TkTracksMergeStep1','hltL3TkTracksFromL2IOHit' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 100.0 ),
    LostHitPenalty = cms.double( 0.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltL3TkTracksMergeStep1','hltL3TkTracksFromL2IOHit' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
process.hltL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
process.hltL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag( "hltL3MuonsLinksCombination" ),
    InputObjects = cms.InputTag( "hltL3Muons" ),
    MuonPtOption = cms.string( "Tracker" )
)
process.hltDoubleMu55Mass0to30Photon12L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 5.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FedLabel = cms.InputTag( "listfeds" ),
    eventPut = cms.bool( True ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    feUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    tccUnpacking = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    numbXtalTSamples = cms.int32( 10 ),
    feIdCheck = cms.bool( True ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    silentMode = cms.untracked.bool( True ),
    DoRegional = cms.bool( False ),
    forceToKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
)
process.hltEcalPreshowerDigis = cms.EDProducer( "ESRawToDigi",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    debugMode = cms.untracked.bool( False ),
    InstanceES = cms.string( "" ),
    ESdigiCollection = cms.string( "" ),
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet( 
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      timealgo = cms.string( "None" ),
      EEtimeNconst = cms.double( 31.8 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      EBtimeNconst = cms.double( 28.5 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      prefitMaxChiSqEB = cms.double( 15.0 ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      ampErrorCalculation = cms.bool( False ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      kPoorRecoFlagEB = cms.bool( True ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      useLumiInfoRunHeader = cms.bool( False ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      doPrefitEE = cms.bool( True ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 ),
      doPrefitEB = cms.bool( True )
    )
)
process.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeFEToBeRecovered = cms.string( "eeFE" )
)
process.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    EBLaserMAX = cms.double( 3.0 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    EELaserMAX = cms.double( 8.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    recoverEEFE = cms.bool( True ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    flagsMapDBReco = cms.PSet( 
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    skipTimeCalib = cms.bool( True ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet( 
      cThreshold_endcap = cms.double( 15.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e6e2thresh = cms.double( 0.04 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      cThreshold_double = cms.double( 10.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
process.hltEcalPreshowerRecHit = cms.EDProducer( "ESRecHitProducer",
    ESRecoAlgo = cms.int32( 0 ),
    ESrechitCollection = cms.string( "EcalRecHitsES" ),
    algo = cms.string( "ESRecHitWorker" ),
    ESdigiCollection = cms.InputTag( "hltEcalPreshowerDigis" )
)
process.hltRechitInRegionsECAL = cms.EDProducer( "HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet( 
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "EGamma" ),
        minEt = cms.double( 5.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Jet' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Jet" ),
        minEt = cms.double( 170.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Tau' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Tau" ),
        minEt = cms.double( 100.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      )
    ),
    recHitLabels = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    productLabels = cms.vstring( 'EcalRecHitsEB',
      'EcalRecHitsEE' )
)
process.hltRechitInRegionsES = cms.EDProducer( "HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet( 
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "EGamma" ),
        minEt = cms.double( 5.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Jet' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Jet" ),
        minEt = cms.double( 170.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Tau' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Tau" ),
        minEt = cms.double( 100.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      )
    ),
    recHitLabels = cms.VInputTag( 'hltEcalPreshowerRecHit:EcalRecHitsES' ),
    productLabels = cms.vstring( 'EcalRecHitsES' )
)
process.hltParticleFlowRecHitECALL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
        name = cms.string( "PFEBRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.08 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        ),
        srFlags = cms.InputTag( "hltEcalDigis" )
      ),
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
        name = cms.string( "PFEERecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.3 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        ),
        srFlags = cms.InputTag( "hltEcalDigis" )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
process.hltParticleFlowRecHitPSL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsES','EcalRecHitsES' ),
        name = cms.string( "PFPSRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
process.hltParticleFlowClusterPSL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" )
        )
      ),
      showerSigma = cms.double( 0.3 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSL1Seeded" )
)
process.hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      maxIterations = cms.uint32( 50 ),
      positionCalcForConvergence = cms.PSet( 
        minAllowedNormalization = cms.double( 0.0 ),
        T0_ES = cms.double( 1.2 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
        T0_EE = cms.double( 3.1 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 )
      ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      showerSigma = cms.double( 1.5 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet( 
      minAllowedNormalization = cms.double( 0.0 ),
      T0_ES = cms.double( 1.2 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
      T0_EE = cms.double( 3.1 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  algoName = cms.string( "SpikeAndDoubleSpikeCleaner" ),
        cleaningByDetector = cms.VPSet( 
          cms.PSet(  energyThresholdModifier = cms.double( 2.0 ),
            minS4S1_a = cms.double( 0.04 ),
            minS4S1_b = cms.double( -0.024 ),
            doubleSpikeThresh = cms.double( 10.0 ),
            singleSpikeThresh = cms.double( 4.0 ),
            doubleSpikeS6S2 = cms.double( 0.04 ),
            fractionThresholdModifier = cms.double( 3.0 ),
            detector = cms.string( "ECAL_BARREL" )
          ),
          cms.PSet(  energyThresholdModifier = cms.double( 2.0 ),
            minS4S1_a = cms.double( 0.02 ),
            minS4S1_b = cms.double( -0.0125 ),
            doubleSpikeThresh = cms.double( 1.0E9 ),
            singleSpikeThresh = cms.double( 15.0 ),
            doubleSpikeS6S2 = cms.double( -1.0 ),
            fractionThresholdModifier = cms.double( 3.0 ),
            detector = cms.string( "ECAL_ENDCAP" )
          )
        )
      )
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.15 ),
          seedingThreshold = cms.double( 0.6 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 0.23 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 8 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALL1Seeded" )
)
process.hltParticleFlowClusterECALL1Seeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    inputPS = cms.InputTag( "hltParticleFlowClusterPSL1Seeded" ),
    minimumPSEnergy = cms.double( 0.0 ),
    energyCorrector = cms.PSet( 
      algoName = cms.string( "PFClusterEMEnergyCorrector" ),
      applyCrackCorrections = cms.bool( False )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedL1Seeded" )
)
process.hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    BeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( True ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    thresh_PFClusterEndcap = cms.double( 0.5 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    thresh_PFClusterBarrel = cms.double( 0.5 ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    verbose = cms.untracked.bool( False ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet( 
      uncertaintyKeyEB = cms.string( "pfscecal_EBUncertainty_online" ),
      ecalRecHitsEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      regressionKeyEE = cms.string( "pfscecal_EECorrection_online" ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_online" ),
      uncertaintyKeyEE = cms.string( "pfscecal_EEUncertainty_online" ),
      isHLT = cms.bool( True )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    thresh_PFClusterSeedBarrel = cms.double( 1.0 ),
    ClusteringType = cms.string( "Mustache" ),
    EnergyWeight = cms.string( "Raw" ),
    thresh_PFClusterSeedEndcap = cms.double( 1.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 0.5 ),
    seedThresholdIsET = cms.bool( True ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" )
)
process.hltEgammaCandidates = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter = cms.EDFilter( "HLTEgammaL1TMatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_phi_size = cms.double( 1.044 ),
    saveTags = cms.bool( True ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    l1CenJetsTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    ncandcut = cms.int32( 1 ),
    l1TausTag = cms.InputTag( 'hltGtStage2Digis','Tau' )
)
process.hltEG12EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 12.0 ),
    etcutEB = cms.double( 12.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    ExpectedOrbitMessageTime = cms.untracked.int32( -1 ),
    FilterDataQuality = cms.bool( True ),
    silent = cms.untracked.bool( True ),
    HcalFirstFED = cms.untracked.int32( 700 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    ElectronicsMap = cms.string( "" ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackUMNio = cms.untracked.bool( True ),
    FEDs = cms.untracked.vint32(  ),
    UnpackerMode = cms.untracked.int32( 0 ),
    UnpackTTP = cms.untracked.bool( False ),
    lastSample = cms.int32( 9 ),
    UnpackZDC = cms.untracked.bool( True ),
    firstSample = cms.int32( 0 )
)
process.hltHbhePhase1Reco = cms.EDProducer( "HBHEPhase1Reconstructor",
    tsFromDB = cms.bool( False ),
    setPulseShapeFlagsQIE8 = cms.bool( True ),
    digiLabelQIE11 = cms.InputTag( "hltHcalDigis" ),
    saveDroppedInfos = cms.bool( False ),
    setNoiseFlagsQIE8 = cms.bool( True ),
    saveEffectivePedestal = cms.bool( False ),
    digiLabelQIE8 = cms.InputTag( "hltHcalDigis" ),
    processQIE11 = cms.bool( True ),
    pulseShapeParametersQIE11 = cms.PSet(  ),
    algoConfigClass = cms.string( "" ),
    saveInfos = cms.bool( False ),
    flagParametersQIE11 = cms.PSet(  ),
    makeRecHits = cms.bool( True ),
    pulseShapeParametersQIE8 = cms.PSet( 
      UseDualFit = cms.bool( True ),
      LinearCut = cms.vdouble( -3.0, -0.054, -0.054 ),
      TriangleIgnoreSlow = cms.bool( False ),
      TS4TS5LowerThreshold = cms.vdouble( 100.0, 120.0, 160.0, 200.0, 300.0, 500.0 ),
      LinearThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      RightSlopeSmallCut = cms.vdouble( 1.08, 1.16, 1.16 ),
      TS4TS5UpperThreshold = cms.vdouble( 70.0, 90.0, 100.0, 400.0 ),
      TS3TS4ChargeThreshold = cms.double( 70.0 ),
      R45PlusOneRange = cms.double( 0.2 ),
      TS4TS5LowerCut = cms.vdouble( -1.0, -0.7, -0.5, -0.4, -0.3, 0.1 ),
      RightSlopeThreshold = cms.vdouble( 250.0, 400.0, 100000.0 ),
      TS3TS4UpperChargeThreshold = cms.double( 20.0 ),
      MinimumChargeThreshold = cms.double( 20.0 ),
      RightSlopeCut = cms.vdouble( 5.0, 4.15, 4.15 ),
      RMS8MaxThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      MinimumTS4TS5Threshold = cms.double( 100.0 ),
      LeftSlopeThreshold = cms.vdouble( 250.0, 500.0, 100000.0 ),
      TS5TS6ChargeThreshold = cms.double( 70.0 ),
      TrianglePeakTS = cms.uint32( 10000 ),
      TS5TS6UpperChargeThreshold = cms.double( 20.0 ),
      RightSlopeSmallThreshold = cms.vdouble( 150.0, 200.0, 100000.0 ),
      RMS8MaxCut = cms.vdouble( -13.5, -11.5, -11.5 ),
      TS4TS5ChargeThreshold = cms.double( 70.0 ),
      R45MinusOneRange = cms.double( 0.2 ),
      LeftSlopeCut = cms.vdouble( 5.0, 2.55, 2.55 ),
      TS4TS5UpperCut = cms.vdouble( 1.0, 0.8, 0.75, 0.72 )
    ),
    flagParametersQIE8 = cms.PSet( 
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      ),
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 )
    ),
    setNegativeFlagsQIE8 = cms.bool( False ),
    setNegativeFlagsQIE11 = cms.bool( False ),
    processQIE8 = cms.bool( True ),
    algorithm = cms.PSet( 
      meanTime = cms.double( 0.0 ),
      pedSigmaHPD = cms.double( 0.5 ),
      pedSigmaSiPM = cms.double( 6.5E-4 ),
      timeSigmaSiPM = cms.double( 2.5 ),
      applyTimeSlew = cms.bool( True ),
      timeSlewParsType = cms.int32( 3 ),
      ts4Max = cms.vdouble( 100.0, 45000.0 ),
      samplesToAdd = cms.int32( 2 ),
      applyTimeConstraint = cms.bool( True ),
      timeSigmaHPD = cms.double( 5.0 ),
      correctForPhaseContainment = cms.bool( True ),
      pedestalUpperLimit = cms.double( 2.7 ),
      respCorrM3 = cms.double( 1.0 ),
      pulseJitter = cms.double( 1.0 ),
      applyPedConstraint = cms.bool( True ),
      fitTimes = cms.int32( 1 ),
      applyTimeSlewM3 = cms.bool( True ),
      meanPed = cms.double( 0.0 ),
      noiseSiPM = cms.double( 1.0 ),
      ts4Min = cms.double( 0.0 ),
      applyPulseJitter = cms.bool( False ),
      noiseHPD = cms.double( 1.0 ),
      useM2 = cms.bool( False ),
      timeMin = cms.double( -12.5 ),
      useM3 = cms.bool( True ),
      tdcTimeShift = cms.double( 0.0 ),
      correctionPhaseNS = cms.double( 6.0 ),
      firstSampleShift = cms.int32( 0 ),
      timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
      ts4chi2 = cms.vdouble( 15.0, 15.0 ),
      timeMax = cms.double( 12.5 ),
      Class = cms.string( "SimpleHBHEPhase1Algo" )
    ),
    setLegacyFlagsQIE8 = cms.bool( True ),
    setPulseShapeFlagsQIE11 = cms.bool( False ),
    setLegacyFlagsQIE11 = cms.bool( False ),
    setNoiseFlagsQIE11 = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True )
)
process.hltHbhereco = cms.EDProducer( "HBHEPlan1Combiner",
    hbheInput = cms.InputTag( "hltHbhePhase1Reco" ),
    usePlan1Mode = cms.bool( True ),
    ignorePlan1Topology = cms.bool( False ),
    algorithm = cms.PSet(  Class = cms.string( "SimplePlan1RechitCombiner" ) )
)
process.hltHfprereco = cms.EDProducer( "HFPreReconstructor",
    soiShift = cms.int32( 0 ),
    sumAllTimeSlices = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    tsFromDB = cms.bool( False ),
    forceSOI = cms.int32( -1 )
)
process.hltHfreco = cms.EDProducer( "HFPhase1Reconstructor",
    setNoiseFlags = cms.bool( False ),
    PETstat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      short_R_29 = cms.vdouble( 0.8 ),
      long_R = cms.vdouble( 0.98 ),
      short_R = cms.vdouble( 0.8 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    algoConfigClass = cms.string( "HFPhase1PMTParams" ),
    inputLabel = cms.InputTag( "hltHfprereco" ),
    S9S1stat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    checkChannelQualityForDepth3and4 = cms.bool( False ),
    useChannelQualityFromDB = cms.bool( False ),
    algorithm = cms.PSet( 
      tfallIfNoTDC = cms.double( -101.0 ),
      triseIfNoTDC = cms.double( -100.0 ),
      rejectAllFailures = cms.bool( True ),
      energyWeights = cms.vdouble( 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0 ),
      soiPhase = cms.uint32( 1 ),
      timeShift = cms.double( 0.0 ),
      tlimits = cms.vdouble( -1000.0, 1000.0, -1000.0, 1000.0 ),
      Class = cms.string( "HFFlexibleTimeCheck" )
    ),
    S8S1stat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    pedestalUpperLimit = cms.double( 2.7 ),
    timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
    respCorrM3 = cms.double( 1.0 ),
    timeSlewParsType = cms.int32( 3 ),
    applyTimeSlewM3 = cms.bool( True ),
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 0 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HO" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    noiseHPD = cms.double( 1.0 ),
    pulseJitter = cms.double( 1.0 ),
    pedSigmaSiPM = cms.double( 6.5E-4 ),
    timeMin = cms.double( -15.0 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    applyPulseJitter = cms.bool( False ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    timingshapedcutsParameters = cms.PSet(  ),
    ts4chi2 = cms.vdouble( 15.0, 15.0 ),
    ts4Min = cms.double( 5.0 ),
    pulseShapeParameters = cms.PSet(  ),
    timeSigmaSiPM = cms.double( 2.5 ),
    applyPedConstraint = cms.bool( True ),
    ts4Max = cms.vdouble( 100.0, 45000.0 ),
    noiseSiPM = cms.double( 1.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet(  ),
    pedSigmaHPD = cms.double( 0.5 ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigmaHPD = cms.double( 5.0 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet(  )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HcalPhase = cms.int32( 0 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    UseRejectedHitsOnly = cms.bool( False ),
    EBThreshold = cms.double( 0.07 ),
    HEDGrid = cms.vdouble(  ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltHcalDigisL1EGSeeded = cms.EDProducer( "HLTHcalDigisInRegionsProducer",
    inputCollTags = cms.VInputTag( 'hltHcalDigis' ),
    etaPhiRegions = cms.VPSet( 
      cms.PSet(  inputColl = cms.InputTag( "hltEgammaCandidates" ),
        type = cms.string( "RecoEcalCandidate" ),
        minEt = cms.double( 5.0 ),
        maxDeltaR = cms.double( 0.25 ),
        maxDPhi = cms.double( 0.0 ),
        maxDEta = cms.double( 0.0 ),
        maxEt = cms.double( -1.0 )
      )
    ),
    outputProductNames = cms.vstring( '' )
)
process.hltHbherecoMethod2L1EGSeeded = cms.EDProducer( "HBHEPhase1Reconstructor",
    tsFromDB = cms.bool( False ),
    setPulseShapeFlagsQIE8 = cms.bool( True ),
    digiLabelQIE11 = cms.InputTag( "" ),
    saveDroppedInfos = cms.bool( False ),
    setNoiseFlagsQIE8 = cms.bool( True ),
    saveEffectivePedestal = cms.bool( False ),
    digiLabelQIE8 = cms.InputTag( "hltHcalDigisL1EGSeeded" ),
    processQIE11 = cms.bool( False ),
    pulseShapeParametersQIE11 = cms.PSet(  ),
    algoConfigClass = cms.string( "" ),
    saveInfos = cms.bool( False ),
    flagParametersQIE11 = cms.PSet(  ),
    makeRecHits = cms.bool( True ),
    pulseShapeParametersQIE8 = cms.PSet( 
      UseDualFit = cms.bool( True ),
      LinearCut = cms.vdouble( -3.0, -0.054, -0.054 ),
      TriangleIgnoreSlow = cms.bool( False ),
      TS4TS5LowerThreshold = cms.vdouble( 100.0, 120.0, 160.0, 200.0, 300.0, 500.0 ),
      LinearThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      RightSlopeSmallCut = cms.vdouble( 1.08, 1.16, 1.16 ),
      TS4TS5UpperThreshold = cms.vdouble( 70.0, 90.0, 100.0, 400.0 ),
      TS3TS4ChargeThreshold = cms.double( 70.0 ),
      R45PlusOneRange = cms.double( 0.2 ),
      TS4TS5LowerCut = cms.vdouble( -1.0, -0.7, -0.5, -0.4, -0.3, 0.1 ),
      RightSlopeThreshold = cms.vdouble( 250.0, 400.0, 100000.0 ),
      TS3TS4UpperChargeThreshold = cms.double( 20.0 ),
      MinimumChargeThreshold = cms.double( 20.0 ),
      RightSlopeCut = cms.vdouble( 5.0, 4.15, 4.15 ),
      RMS8MaxThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      MinimumTS4TS5Threshold = cms.double( 100.0 ),
      LeftSlopeThreshold = cms.vdouble( 250.0, 500.0, 100000.0 ),
      TS5TS6ChargeThreshold = cms.double( 70.0 ),
      TrianglePeakTS = cms.uint32( 10000 ),
      TS5TS6UpperChargeThreshold = cms.double( 20.0 ),
      RightSlopeSmallThreshold = cms.vdouble( 150.0, 200.0, 100000.0 ),
      RMS8MaxCut = cms.vdouble( -13.5, -11.5, -11.5 ),
      TS4TS5ChargeThreshold = cms.double( 70.0 ),
      R45MinusOneRange = cms.double( 0.2 ),
      LeftSlopeCut = cms.vdouble( 5.0, 2.55, 2.55 ),
      TS4TS5UpperCut = cms.vdouble( 1.0, 0.8, 0.75, 0.72 )
    ),
    flagParametersQIE8 = cms.PSet( 
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      ),
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 )
    ),
    setNegativeFlagsQIE8 = cms.bool( False ),
    setNegativeFlagsQIE11 = cms.bool( False ),
    processQIE8 = cms.bool( True ),
    algorithm = cms.PSet( 
      meanTime = cms.double( 0.0 ),
      pedSigmaHPD = cms.double( 0.5 ),
      pedSigmaSiPM = cms.double( 6.5E-4 ),
      timeSigmaSiPM = cms.double( 2.5 ),
      applyTimeSlew = cms.bool( True ),
      timeSlewParsType = cms.int32( 3 ),
      ts4Max = cms.vdouble( 100.0, 45000.0 ),
      samplesToAdd = cms.int32( 2 ),
      applyTimeConstraint = cms.bool( True ),
      timeSigmaHPD = cms.double( 5.0 ),
      correctForPhaseContainment = cms.bool( True ),
      pedestalUpperLimit = cms.double( 2.7 ),
      respCorrM3 = cms.double( 1.0 ),
      pulseJitter = cms.double( 1.0 ),
      applyPedConstraint = cms.bool( True ),
      fitTimes = cms.int32( 1 ),
      applyTimeSlewM3 = cms.bool( True ),
      meanPed = cms.double( 0.0 ),
      noiseSiPM = cms.double( 1.0 ),
      ts4Min = cms.double( 0.0 ),
      applyPulseJitter = cms.bool( False ),
      noiseHPD = cms.double( 1.0 ),
      useM2 = cms.bool( True ),
      timeMin = cms.double( -12.5 ),
      useM3 = cms.bool( False ),
      tdcTimeShift = cms.double( 0.0 ),
      correctionPhaseNS = cms.double( 6.0 ),
      firstSampleShift = cms.int32( 0 ),
      timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
      ts4chi2 = cms.vdouble( 15.0, 15.0 ),
      timeMax = cms.double( 12.5 ),
      Class = cms.string( "SimpleHBHEPhase1Algo" )
    ),
    setLegacyFlagsQIE8 = cms.bool( True ),
    setPulseShapeFlagsQIE11 = cms.bool( False ),
    setLegacyFlagsQIE11 = cms.bool( False ),
    setNoiseFlagsQIE11 = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True )
)
process.hltTowerMakerMethod2L1EGSeeded = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbherecoMethod2L1EGSeeded" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HcalPhase = cms.int32( 0 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    UseRejectedHitsOnly = cms.bool( False ),
    EBThreshold = cms.double( 0.07 ),
    HEDGrid = cms.vdouble(  ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltFixedGridRhoFastjetAllCaloForMuons = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 2.5 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
process.hltEgammaHoverE = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
    effectiveAreas = cms.vdouble( 0.105, 0.17 ),
    doRhoCorrection = cms.bool( False ),
    outerCone = cms.double( 0.14 ),
    caloTowerProducer = cms.InputTag( "hltTowerMakerMethod2L1EGSeeded" ),
    innerCone = cms.double( 0.0 ),
    useSingleTower = cms.bool( False ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    depth = cms.int32( -1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    rhoMax = cms.double( 9.9999999E7 ),
    etMin = cms.double( 0.0 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
process.hltEG12HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    useEt = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG12EtFilter" )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    moduleLabelPatternsToSkip = cms.vstring(  ),
    processName = cms.string( "@" ),
    moduleLabelPatternsToMatch = cms.vstring( 'hlt*' )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)









process.hltEG14EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 14.0 ),
    etcutEB = cms.double( 14.0 ),
    ncandcut = cms.int32( 1 )
)



process.hltEG14HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    useEt = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG14EtFilter" )
)








process.hltEG15EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 15.0 ),
    etcutEB = cms.double( 15.0 ),
    ncandcut = cms.int32( 1 )
)



process.hltEG15HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    useEt = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG15EtFilter" )
)








process.hltEG16EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 16.0 ),
    etcutEB = cms.double( 16.0 ),
    ncandcut = cms.int32( 1 )
)



process.hltEG16HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    useEt = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG16EtFilter" )
)








process.hltEG17EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 17.0 ),
    etcutEB = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 )
)



process.hltEG17HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    useEt = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG17EtFilter" )
)








process.hltEG18EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 18.0 ),
    etcutEB = cms.double( 18.0 ),
    ncandcut = cms.int32( 1 )
)



process.hltEG18HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    useEt = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG18EtFilter" )
)








process.hltEG19EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 19.0 ),
    etcutEB = cms.double( 19.0 ),
    ncandcut = cms.int32( 1 )
)



process.hltEG19HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    useEt = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG19EtFilter" )
)








process.hltEG20EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 20.0 ),
    etcutEB = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 )
)



process.hltEG20HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    useEt = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEG20EtFilter" )
)








process.hltPreDoubleMu55Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu55Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 5.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu66Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu66Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 6.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu77Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu77Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 7.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu88Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu88Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 8.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 8.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu99Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu99Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 9.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 9.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu135Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu135Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 13.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu145Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu145Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu146Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu146Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu155Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu155Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu156Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu156Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu157Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu157Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu165Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu165Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu166Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu166Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu167Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu167Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu175Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu175Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu176Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu176Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu177Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu177Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu185Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu185Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu186Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu186Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu187Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu187Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu195Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu195Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu196Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu196Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu197Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu197Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu205Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu205Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu206Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu206Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu207Mass0to30Photon14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu207Mass0to30Photon14L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu55Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu55Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 5.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu66Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu66Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 6.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu77Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu77Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 7.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu88Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu88Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 8.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 8.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu99Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu99Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 9.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 9.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu135Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu135Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 13.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu145Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu145Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu146Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu146Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu155Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu155Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu156Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu156Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu157Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu157Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu165Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu165Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu166Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu166Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu167Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu167Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu175Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu175Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu176Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu176Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu177Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu177Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu185Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu185Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu186Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu186Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu187Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu187Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu195Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu195Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu196Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu196Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu197Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu197Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu205Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu205Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu206Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu206Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu207Mass0to30Photon15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu207Mass0to30Photon15L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu55Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu55Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 5.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu66Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu66Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 6.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu77Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu77Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 7.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu88Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu88Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 8.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 8.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu99Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu99Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 9.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 9.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu135Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu135Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 13.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu145Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu145Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu146Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu146Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu155Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu155Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu156Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu156Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu157Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu157Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu165Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu165Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu166Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu166Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu167Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu167Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu175Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu175Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu176Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu176Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu177Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu177Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu185Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu185Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu186Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu186Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu187Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu187Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu195Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu195Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu196Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu196Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu197Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu197Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu205Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu205Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu206Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu206Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu207Mass0to30Photon16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu207Mass0to30Photon16L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu55Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu55Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 5.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu66Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu66Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 6.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu77Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu77Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 7.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu88Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu88Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 8.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 8.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu99Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu99Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 9.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 9.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu135Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu135Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 13.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu145Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu145Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu146Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu146Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu155Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu155Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu156Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu156Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu157Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu157Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu165Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu165Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu166Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu166Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu167Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu167Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu175Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu175Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu176Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu176Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu177Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu177Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu185Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu185Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu186Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu186Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu187Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu187Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu195Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu195Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu196Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu196Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu197Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu197Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu205Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu205Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu206Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu206Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu207Mass0to30Photon17 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu207Mass0to30Photon17L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu55Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu55Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 5.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu66Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu66Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 6.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu77Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu77Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 7.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu88Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu88Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 8.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 8.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu99Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu99Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 9.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 9.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu135Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu135Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 13.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu145Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu145Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu146Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu146Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu155Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu155Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu156Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu156Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu157Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu157Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu165Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu165Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu166Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu166Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu167Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu167Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu175Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu175Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu176Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu176Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu177Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu177Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu185Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu185Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu186Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu186Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu187Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu187Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu195Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu195Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu196Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu196Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu197Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu197Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu205Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu205Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu206Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu206Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu207Mass0to30Photon18 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu207Mass0to30Photon18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu55Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu55Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 5.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu66Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu66Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 6.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu77Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu77Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 7.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu88Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu88Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 8.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 8.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu99Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu99Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 9.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 9.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu135Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu135Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 13.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu145Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu145Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu146Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu146Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu155Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu155Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu156Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu156Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu157Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu157Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu165Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu165Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu166Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu166Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu167Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu167Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu175Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu175Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu176Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu176Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu177Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu177Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu185Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu185Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu186Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu186Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu187Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu187Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu195Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu195Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu196Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu196Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu197Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu197Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu205Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu205Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu206Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu206Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu207Mass0to30Photon19 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu207Mass0to30Photon19L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu55Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu55Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 5.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu66Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu66Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 6.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu77Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu77Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 7.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu88Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu88Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 8.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 8.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu99Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu99Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 9.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 9.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu135Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu135Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 13.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu145Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu145Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu146Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu146Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 14.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu155Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu155Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu156Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu156Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu157Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu157Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 15.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu165Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu165Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu166Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu166Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu167Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu167Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 16.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu175Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu175Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu176Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu176Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu177Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu177Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 17.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu185Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu185Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu186Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu186Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu187Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu187Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 18.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu195Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu195Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu196Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu196Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu197Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu197Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 19.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu205Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu205Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 5.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu206Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu206Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 6.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)








process.hltPreDoubleMu207Mass0to30Photon20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)

process.hltDoubleMu207Mass0to30Photon20L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    PreviousCandIsL2 = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 7.0 ),
    MaxInvMass = cms.vdouble( 30.0 ),
    MinPtMax = cms.vdouble( 20.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinN = cms.int32( 1 ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)







process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtStage2Digis + process.hltGtStage2ObjectMap )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTMuonLocalRecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )
process.HLTL2muonrecoNocandSequence = cms.Sequence( process.HLTMuonLocalRecoSequence + process.hltL2OfflineMuonSeeds + process.hltL2MuonSeeds + process.hltL2Muons )
process.HLTL2muonrecoSequence = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidates )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelClustersCache + process.hltSiPixelRecHits )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )
process.HLTL3muonTkCandidateSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL3TrajSeedOIState + process.hltL3TrackCandidateFromL2OIState + process.hltL3TkTracksFromL2OIState + process.hltL3MuonsOIState + process.hltL3TrajSeedOIHit + process.hltL3TrackCandidateFromL2OIHit + process.hltL3TkTracksFromL2OIHit + process.hltL3MuonsOIHit + process.hltL3TkFromL2OICombination + process.hltPixelLayerTriplets + process.hltPixelLayerPairs + process.hltMixedLayerPairs + process.hltL3TrajSeedIOHit + process.hltL3TrackCandidateFromL2IOHit + process.hltL3TkTracksFromL2IOHit + process.hltL3MuonsIOHit + process.hltL3TrajectorySeed + process.hltL3TrackCandidateFromL2 )
process.HLTL3muonrecoNocandSequence = cms.Sequence( process.HLTL3muonTkCandidateSequence + process.hltL3TkTracksMergeStep1 + process.hltL3TkTracksFromL2 + process.hltL3MuonsLinksCombination + process.hltL3Muons )
process.HLTL3muonrecoSequence = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltL3MuonCandidates )
process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalPreshowerDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit + process.hltEcalPreshowerRecHit )
process.HLTPFClusteringForEgamma = cms.Sequence( process.hltRechitInRegionsECAL + process.hltRechitInRegionsES + process.hltParticleFlowRecHitECALL1Seeded + process.hltParticleFlowRecHitPSL1Seeded + process.hltParticleFlowClusterPSL1Seeded + process.hltParticleFlowClusterECALUncorrectedL1Seeded + process.hltParticleFlowClusterECALL1Seeded + process.hltParticleFlowSuperClusterECALL1Seeded )
process.HLTDoLocalHcalWithTowerL1EGSeededSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhePhase1Reco + process.hltHbhereco + process.hltHfprereco + process.hltHfreco + process.hltHoreco + process.hltTowerMakerForAll + process.hltHcalDigisL1EGSeeded + process.hltHbherecoMethod2L1EGSeeded + process.hltTowerMakerMethod2L1EGSeeded )
process.HLTFastJetForEgamma = cms.Sequence( process.hltFixedGridRhoFastjetAllCaloForMuons )
process.HLTPhoton12Sequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter + process.hltEG12EtFilter + process.HLTDoLocalHcalWithTowerL1EGSeededSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG12HEFilter )
process.HLTPhoton14Sequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter + process.hltEG14EtFilter + process.HLTDoLocalHcalWithTowerL1EGSeededSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG14HEFilter )
process.HLTPhoton15Sequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter + process.hltEG15EtFilter + process.HLTDoLocalHcalWithTowerL1EGSeededSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG15HEFilter )
process.HLTPhoton16Sequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter + process.hltEG16EtFilter + process.HLTDoLocalHcalWithTowerL1EGSeededSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG16HEFilter )
process.HLTPhoton17Sequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter + process.hltEG17EtFilter + process.HLTDoLocalHcalWithTowerL1EGSeededSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG17HEFilter )
process.HLTPhoton18Sequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter + process.hltEG18EtFilter + process.HLTDoLocalHcalWithTowerL1EGSeededSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG18HEFilter )
process.HLTPhoton19Sequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter + process.hltEG19EtFilter + process.HLTDoLocalHcalWithTowerL1EGSeededSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG19HEFilter )
process.HLTPhoton20Sequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGDoubleMu4OSEG12ORDoubleMu5OSEG12Filter + process.hltEG20EtFilter + process.HLTDoLocalHcalWithTowerL1EGSeededSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG20HEFilter )


process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )


process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
process.HLT_DoubleMu5_5_Mass0to30_Photon12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu55Mass0to30Photon12 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu55Mass0to30Photon12L3Filtered + process.HLTPhoton12Sequence + process.HLTEndSequence )

process.HLT_DoubleMu5_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu55Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu55Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu6_6_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu66Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu66Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu7_7_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu77Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu77Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu8_8_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu88Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu88Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu9_9_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu99Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu99Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu13_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu135Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu135Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu145Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu145Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_6_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu146Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu146Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu155Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu155Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_6_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu156Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu156Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_7_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu157Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu157Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu165Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu165Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_6_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu166Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu166Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_7_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu167Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu167Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu175Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu175Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_6_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu176Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu176Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_7_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu177Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu177Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu185Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu185Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_6_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu186Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu186Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_7_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu187Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu187Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu195Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu195Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_6_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu196Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu196Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_7_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu197Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu197Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_5_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu205Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu205Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_6_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu206Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu206Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_7_Mass0to30_Photon14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu207Mass0to30Photon14 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu207Mass0to30Photon14L3Filtered + process.HLTPhoton14Sequence + process.HLTEndSequence )

process.HLT_DoubleMu5_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu55Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu55Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu6_6_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu66Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu66Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu7_7_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu77Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu77Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu8_8_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu88Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu88Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu9_9_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu99Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu99Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu13_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu135Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu135Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu145Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu145Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_6_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu146Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu146Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu155Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu155Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_6_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu156Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu156Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_7_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu157Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu157Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu165Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu165Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_6_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu166Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu166Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_7_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu167Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu167Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu175Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu175Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_6_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu176Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu176Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_7_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu177Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu177Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu185Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu185Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_6_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu186Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu186Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_7_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu187Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu187Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu195Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu195Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_6_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu196Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu196Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_7_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu197Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu197Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_5_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu205Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu205Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_6_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu206Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu206Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_7_Mass0to30_Photon15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu207Mass0to30Photon15 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu207Mass0to30Photon15L3Filtered + process.HLTPhoton15Sequence + process.HLTEndSequence )

process.HLT_DoubleMu5_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu55Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu55Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu6_6_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu66Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu66Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu7_7_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu77Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu77Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu8_8_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu88Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu88Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu9_9_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu99Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu99Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu13_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu135Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu135Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu145Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu145Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_6_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu146Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu146Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu155Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu155Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_6_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu156Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu156Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_7_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu157Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu157Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu165Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu165Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_6_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu166Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu166Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_7_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu167Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu167Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu175Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu175Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_6_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu176Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu176Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_7_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu177Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu177Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu185Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu185Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_6_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu186Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu186Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_7_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu187Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu187Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu195Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu195Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_6_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu196Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu196Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_7_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu197Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu197Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_5_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu205Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu205Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_6_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu206Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu206Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_7_Mass0to30_Photon16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu207Mass0to30Photon16 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu207Mass0to30Photon16L3Filtered + process.HLTPhoton16Sequence + process.HLTEndSequence )

process.HLT_DoubleMu5_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu55Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu55Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu6_6_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu66Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu66Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu7_7_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu77Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu77Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu8_8_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu88Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu88Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu9_9_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu99Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu99Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu13_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu135Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu135Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu145Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu145Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_6_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu146Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu146Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu155Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu155Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_6_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu156Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu156Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_7_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu157Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu157Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu165Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu165Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_6_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu166Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu166Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_7_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu167Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu167Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu175Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu175Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_6_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu176Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu176Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_7_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu177Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu177Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu185Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu185Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_6_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu186Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu186Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_7_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu187Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu187Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu195Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu195Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_6_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu196Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu196Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_7_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu197Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu197Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_5_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu205Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu205Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_6_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu206Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu206Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_7_Mass0to30_Photon17_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu207Mass0to30Photon17 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu207Mass0to30Photon17L3Filtered + process.HLTPhoton17Sequence + process.HLTEndSequence )

process.HLT_DoubleMu5_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu55Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu55Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu6_6_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu66Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu66Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu7_7_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu77Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu77Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu8_8_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu88Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu88Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu9_9_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu99Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu99Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu13_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu135Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu135Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu145Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu145Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_6_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu146Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu146Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu155Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu155Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_6_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu156Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu156Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_7_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu157Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu157Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu165Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu165Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_6_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu166Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu166Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_7_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu167Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu167Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu175Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu175Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_6_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu176Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu176Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_7_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu177Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu177Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu185Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu185Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_6_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu186Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu186Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_7_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu187Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu187Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu195Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu195Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_6_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu196Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu196Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_7_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu197Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu197Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_5_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu205Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu205Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_6_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu206Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu206Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_7_Mass0to30_Photon18_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu207Mass0to30Photon18 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu207Mass0to30Photon18L3Filtered + process.HLTPhoton18Sequence + process.HLTEndSequence )

process.HLT_DoubleMu5_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu55Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu55Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu6_6_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu66Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu66Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu7_7_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu77Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu77Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu8_8_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu88Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu88Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu9_9_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu99Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu99Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu13_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu135Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu135Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu145Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu145Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_6_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu146Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu146Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu155Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu155Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_6_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu156Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu156Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_7_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu157Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu157Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu165Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu165Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_6_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu166Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu166Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_7_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu167Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu167Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu175Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu175Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_6_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu176Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu176Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_7_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu177Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu177Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu185Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu185Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_6_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu186Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu186Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_7_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu187Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu187Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu195Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu195Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_6_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu196Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu196Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_7_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu197Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu197Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_5_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu205Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu205Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_6_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu206Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu206Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_7_Mass0to30_Photon19_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu207Mass0to30Photon19 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu207Mass0to30Photon19L3Filtered + process.HLTPhoton19Sequence + process.HLTEndSequence )

process.HLT_DoubleMu5_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu55Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu55Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu6_6_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu66Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu66Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu7_7_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu77Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu77Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu8_8_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu88Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu88Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu9_9_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu99Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu99Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu13_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu135Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu135Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu145Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu145Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu14_6_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu146Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu146Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu155Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu155Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_6_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu156Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu156Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu15_7_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu157Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu157Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu165Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu165Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_6_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu166Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu166Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu16_7_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu167Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu167Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu175Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu175Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_6_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu176Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu176Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu17_7_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu177Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu177Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu185Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu185Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_6_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu186Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu186Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu18_7_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu187Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu187Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu195Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu195Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_6_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu196Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu196Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu19_7_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu197Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu197Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_5_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu205Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu205Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_6_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu206Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu206Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLT_DoubleMu20_7_Mass0to30_Photon20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu4OSEG12ORDoubleMu5OSEG12 + process.hltPreDoubleMu207Mass0to30Photon20 + process.hltL1fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2fL1sDoubleMu4OSEG12ORDoubleMu5OSEG12L1f0L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu207Mass0to30Photon20L3Filtered + process.HLTPhoton20Sequence + process.HLTEndSequence )

process.HLTriggerFinalPath = cms.Path( process.hltGtStage2Digis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )
process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_DoubleMu5_5_Mass0to30_Photon12_v1, process.HLT_DoubleMu5_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu6_6_Mass0to30_Photon14_v1, process.HLT_DoubleMu7_7_Mass0to30_Photon14_v1, process.HLT_DoubleMu8_8_Mass0to30_Photon14_v1, process.HLT_DoubleMu9_9_Mass0to30_Photon14_v1, process.HLT_DoubleMu13_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu14_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu14_6_Mass0to30_Photon14_v1, process.HLT_DoubleMu15_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu15_6_Mass0to30_Photon14_v1, process.HLT_DoubleMu15_7_Mass0to30_Photon14_v1, process.HLT_DoubleMu16_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu16_6_Mass0to30_Photon14_v1, process.HLT_DoubleMu16_7_Mass0to30_Photon14_v1, process.HLT_DoubleMu17_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu17_6_Mass0to30_Photon14_v1, process.HLT_DoubleMu17_7_Mass0to30_Photon14_v1, process.HLT_DoubleMu18_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu18_6_Mass0to30_Photon14_v1, process.HLT_DoubleMu18_7_Mass0to30_Photon14_v1, process.HLT_DoubleMu19_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu19_6_Mass0to30_Photon14_v1, process.HLT_DoubleMu19_7_Mass0to30_Photon14_v1, process.HLT_DoubleMu20_5_Mass0to30_Photon14_v1, process.HLT_DoubleMu20_6_Mass0to30_Photon14_v1, process.HLT_DoubleMu20_7_Mass0to30_Photon14_v1, process.HLT_DoubleMu5_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu6_6_Mass0to30_Photon15_v1, process.HLT_DoubleMu7_7_Mass0to30_Photon15_v1, process.HLT_DoubleMu8_8_Mass0to30_Photon15_v1, process.HLT_DoubleMu9_9_Mass0to30_Photon15_v1, process.HLT_DoubleMu13_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu14_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu14_6_Mass0to30_Photon15_v1, process.HLT_DoubleMu15_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu15_6_Mass0to30_Photon15_v1, process.HLT_DoubleMu15_7_Mass0to30_Photon15_v1, process.HLT_DoubleMu16_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu16_6_Mass0to30_Photon15_v1, process.HLT_DoubleMu16_7_Mass0to30_Photon15_v1, process.HLT_DoubleMu17_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu17_6_Mass0to30_Photon15_v1, process.HLT_DoubleMu17_7_Mass0to30_Photon15_v1, process.HLT_DoubleMu18_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu18_6_Mass0to30_Photon15_v1, process.HLT_DoubleMu18_7_Mass0to30_Photon15_v1, process.HLT_DoubleMu19_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu19_6_Mass0to30_Photon15_v1, process.HLT_DoubleMu19_7_Mass0to30_Photon15_v1, process.HLT_DoubleMu20_5_Mass0to30_Photon15_v1, process.HLT_DoubleMu20_6_Mass0to30_Photon15_v1, process.HLT_DoubleMu20_7_Mass0to30_Photon15_v1, process.HLT_DoubleMu5_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu6_6_Mass0to30_Photon16_v1, process.HLT_DoubleMu7_7_Mass0to30_Photon16_v1, process.HLT_DoubleMu8_8_Mass0to30_Photon16_v1, process.HLT_DoubleMu9_9_Mass0to30_Photon16_v1, process.HLT_DoubleMu13_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu14_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu14_6_Mass0to30_Photon16_v1, process.HLT_DoubleMu15_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu15_6_Mass0to30_Photon16_v1, process.HLT_DoubleMu15_7_Mass0to30_Photon16_v1, process.HLT_DoubleMu16_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu16_6_Mass0to30_Photon16_v1, process.HLT_DoubleMu16_7_Mass0to30_Photon16_v1, process.HLT_DoubleMu17_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu17_6_Mass0to30_Photon16_v1, process.HLT_DoubleMu17_7_Mass0to30_Photon16_v1, process.HLT_DoubleMu18_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu18_6_Mass0to30_Photon16_v1, process.HLT_DoubleMu18_7_Mass0to30_Photon16_v1, process.HLT_DoubleMu19_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu19_6_Mass0to30_Photon16_v1, process.HLT_DoubleMu19_7_Mass0to30_Photon16_v1, process.HLT_DoubleMu20_5_Mass0to30_Photon16_v1, process.HLT_DoubleMu20_6_Mass0to30_Photon16_v1, process.HLT_DoubleMu20_7_Mass0to30_Photon16_v1, process.HLT_DoubleMu5_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu6_6_Mass0to30_Photon17_v1, process.HLT_DoubleMu7_7_Mass0to30_Photon17_v1, process.HLT_DoubleMu8_8_Mass0to30_Photon17_v1, process.HLT_DoubleMu9_9_Mass0to30_Photon17_v1, process.HLT_DoubleMu13_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu14_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu14_6_Mass0to30_Photon17_v1, process.HLT_DoubleMu15_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu15_6_Mass0to30_Photon17_v1, process.HLT_DoubleMu15_7_Mass0to30_Photon17_v1, process.HLT_DoubleMu16_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu16_6_Mass0to30_Photon17_v1, process.HLT_DoubleMu16_7_Mass0to30_Photon17_v1, process.HLT_DoubleMu17_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu17_6_Mass0to30_Photon17_v1, process.HLT_DoubleMu17_7_Mass0to30_Photon17_v1, process.HLT_DoubleMu18_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu18_6_Mass0to30_Photon17_v1, process.HLT_DoubleMu18_7_Mass0to30_Photon17_v1, process.HLT_DoubleMu19_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu19_6_Mass0to30_Photon17_v1, process.HLT_DoubleMu19_7_Mass0to30_Photon17_v1, process.HLT_DoubleMu20_5_Mass0to30_Photon17_v1, process.HLT_DoubleMu20_6_Mass0to30_Photon17_v1, process.HLT_DoubleMu20_7_Mass0to30_Photon17_v1, process.HLT_DoubleMu5_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu6_6_Mass0to30_Photon18_v1, process.HLT_DoubleMu7_7_Mass0to30_Photon18_v1, process.HLT_DoubleMu8_8_Mass0to30_Photon18_v1, process.HLT_DoubleMu9_9_Mass0to30_Photon18_v1, process.HLT_DoubleMu13_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu14_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu14_6_Mass0to30_Photon18_v1, process.HLT_DoubleMu15_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu15_6_Mass0to30_Photon18_v1, process.HLT_DoubleMu15_7_Mass0to30_Photon18_v1, process.HLT_DoubleMu16_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu16_6_Mass0to30_Photon18_v1, process.HLT_DoubleMu16_7_Mass0to30_Photon18_v1, process.HLT_DoubleMu17_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu17_6_Mass0to30_Photon18_v1, process.HLT_DoubleMu17_7_Mass0to30_Photon18_v1, process.HLT_DoubleMu18_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu18_6_Mass0to30_Photon18_v1, process.HLT_DoubleMu18_7_Mass0to30_Photon18_v1, process.HLT_DoubleMu19_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu19_6_Mass0to30_Photon18_v1, process.HLT_DoubleMu19_7_Mass0to30_Photon18_v1, process.HLT_DoubleMu20_5_Mass0to30_Photon18_v1, process.HLT_DoubleMu20_6_Mass0to30_Photon18_v1, process.HLT_DoubleMu20_7_Mass0to30_Photon18_v1, process.HLT_DoubleMu5_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu6_6_Mass0to30_Photon19_v1, process.HLT_DoubleMu7_7_Mass0to30_Photon19_v1, process.HLT_DoubleMu8_8_Mass0to30_Photon19_v1, process.HLT_DoubleMu9_9_Mass0to30_Photon19_v1, process.HLT_DoubleMu13_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu14_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu14_6_Mass0to30_Photon19_v1, process.HLT_DoubleMu15_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu15_6_Mass0to30_Photon19_v1, process.HLT_DoubleMu15_7_Mass0to30_Photon19_v1, process.HLT_DoubleMu16_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu16_6_Mass0to30_Photon19_v1, process.HLT_DoubleMu16_7_Mass0to30_Photon19_v1, process.HLT_DoubleMu17_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu17_6_Mass0to30_Photon19_v1, process.HLT_DoubleMu17_7_Mass0to30_Photon19_v1, process.HLT_DoubleMu18_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu18_6_Mass0to30_Photon19_v1, process.HLT_DoubleMu18_7_Mass0to30_Photon19_v1, process.HLT_DoubleMu19_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu19_6_Mass0to30_Photon19_v1, process.HLT_DoubleMu19_7_Mass0to30_Photon19_v1, process.HLT_DoubleMu20_5_Mass0to30_Photon19_v1, process.HLT_DoubleMu20_6_Mass0to30_Photon19_v1, process.HLT_DoubleMu20_7_Mass0to30_Photon19_v1, process.HLT_DoubleMu5_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu6_6_Mass0to30_Photon20_v1, process.HLT_DoubleMu7_7_Mass0to30_Photon20_v1, process.HLT_DoubleMu8_8_Mass0to30_Photon20_v1, process.HLT_DoubleMu9_9_Mass0to30_Photon20_v1, process.HLT_DoubleMu13_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu14_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu14_6_Mass0to30_Photon20_v1, process.HLT_DoubleMu15_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu15_6_Mass0to30_Photon20_v1, process.HLT_DoubleMu15_7_Mass0to30_Photon20_v1, process.HLT_DoubleMu16_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu16_6_Mass0to30_Photon20_v1, process.HLT_DoubleMu16_7_Mass0to30_Photon20_v1, process.HLT_DoubleMu17_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu17_6_Mass0to30_Photon20_v1, process.HLT_DoubleMu17_7_Mass0to30_Photon20_v1, process.HLT_DoubleMu18_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu18_6_Mass0to30_Photon20_v1, process.HLT_DoubleMu18_7_Mass0to30_Photon20_v1, process.HLT_DoubleMu19_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu19_6_Mass0to30_Photon20_v1, process.HLT_DoubleMu19_7_Mass0to30_Photon20_v1, process.HLT_DoubleMu20_5_Mass0to30_Photon20_v1, process.HLT_DoubleMu20_6_Mass0to30_Photon20_v1, process.HLT_DoubleMu20_7_Mass0to30_Photon20_v1, process.HLTriggerFinalPath ))



process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/16E12322-0714-E711-B236-70106F48BD36.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# override the GlobalTag's L1T menu from an Xml file
from HLTrigger.Configuration.CustomConfigs import L1XML
process = L1XML(process,"L1Menu_20170412.xml")

# run the Full L1T emulator, then repack the data into a new RAW collection, to be used by the HLT
from HLTrigger.Configuration.CustomConfigs import L1REPACK
process = L1REPACK(process,"FullSimHcalTP")

# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', 'MYHLT' )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.hltResults = cms.InputTag( 'TriggerResults', '', 'MYHLT' )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.hltResults        = cms.InputTag( 'TriggerResults', '', 'MYHLT' )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'MYHLT' )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'MYHLT' )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.hltResults  = cms.InputTag( 'TriggerResults', '', 'MYHLT' )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'MYHLT' )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'MYHLT' )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', 'MYHLT' )
    process.hltDQMHLTScalers.processname                      = 'MYHLT'

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = 'MYHLT'

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

# enable TrigReport, TimeReport and MultiThreading
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    numberOfThreads = cms.untracked.uint32( 4 ),
    numberOfStreams = cms.untracked.uint32( 0 ),
    sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '90X_upgrade2017_TSG_Hcal_V3')
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('L1TGlobalSummary')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

# load the DQMStore and DQMRootOutputModule
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)

process.DQMOutput = cms.EndPath( process.dqmOutput )

# add specific customizations
_customInfo = {}
_customInfo['menuType'  ]= "GRun"
_customInfo['globalTags']= {}
_customInfo['globalTags'][True ] = "auto:run2_hlt_GRun"
_customInfo['globalTags'][False] = "auto:run2_mc_GRun"
_customInfo['inputFiles']={}
_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
_customInfo['maxEvents' ]=  100
_customInfo['globalTag' ]= "90X_upgrade2017_TSG_Hcal_V3"
_customInfo['inputFile' ]=  ['/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/16E12322-0714-E711-B236-70106F48BD36.root']
_customInfo['realData'  ]=  False
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,"GRun",_customInfo)

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
process = customizeHLTforCMSSW(process,"GRun")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(process)





