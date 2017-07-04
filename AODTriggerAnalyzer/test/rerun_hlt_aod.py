from hlt_MC import *    

# process.load(hlt83X)

# change L1 seeds in the L1 filter (not changing the filter name here)
# process.hltL1sDoubleMu100dEtaMax1p8IorDoubleMu0er1p6dEtaMax1p8OSIorDoubleMu0er1p4dEtaMax1p8OSorDoubleMu114orDoubleMu125orDoubleMu136.L1SeedsLogicalExpression = cms.string( "L1_DoubleMu6_OS_MASS0to10" )

# process.source.fileNames          = cms.untracked.vstring(
#      'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80/BdToKstarMuMu_BFilter_TuneCUEP8M1_13TeV-pythia8-evtgen/RAWAODSIM/FlatPU28to62HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/00EF74B5-3DA7-E611-90DE-0CC47A4C8E8A.root',
# )

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents.input = cms.untracked.int32(3000)

process.source = cms.Source ("PoolSource",
                fileNames=cms.untracked.vstring(
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/4C44AAC3-0914-E711-A27C-0CC47A7EEE0E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/521053B6-AF14-E711-966C-0025905A6066.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/568422C9-AF14-E711-9BCE-FA163E820A99.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/5A94D6B5-7D14-E711-9855-0025905A48C0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/862E094F-6914-E711-B17B-D4AE526A05C8.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/868389D3-1914-E711-9D71-1866DA87A5A4.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/8A2B6069-B014-E711-B813-001C23C0B763.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/90B00E74-1214-E711-ABD8-E41D2D08DF30.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/92B71F2B-2314-E711-A8DA-D4AE526A0461.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/944F3FC6-5F14-E711-81AB-0025905A612A.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/9ADFA2F8-2414-E711-8333-1866DA87A5A4.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/A068EAFA-1E14-E711-9EC5-1866DA87B21E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/A28ACDA8-AF14-E711-A134-0CC47A74525A.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B01E3242-B014-E711-9DC5-1866DA8797B0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B25304D7-1C14-E711-ABD1-D4AE526A0D2E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B8C862CC-2014-E711-BF2A-002590DB91F0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/BA49BBDA-1314-E711-88A6-002590DB91F0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/D0299278-7114-E711-B7AD-70106F4A9690.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/DCAC2901-0414-E711-B9A7-70106F4A928C.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/E07738C7-AF14-E711-BEF2-008CFA0A5844.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/FC1CC2A9-AF14-E711-89A2-FA163E36E939.root' 
 
                ),
                secondaryFileNames=cms.untracked.vstring(
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/08927635-2614-E711-8FAE-0025905A612E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/0A8B68BA-0414-E711-971C-70106F48BBEE.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/0E1420A8-1314-E711-ADBB-003048FFD75A.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/16E12322-0714-E711-B236-70106F48BD36.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/1AA6CE28-5514-E711-97F3-0025905A6094.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/280320B4-1714-E711-AC9D-0CC47A7EEE0E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/2A315E34-1514-E711-9BD4-782BCB1612C0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/2C264075-0A14-E711-A2C0-0CC47A4D764A.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/325F36D2-FA13-E711-9A29-E41D2D08E0A0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/381A63E3-FB13-E711-B4EF-D4AE526A0A4B.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/3C5FA423-0E14-E711-AA07-D4AE526A0A4B.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/428D5C9F-0514-E711-A2F0-70106F48BD36.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/4470B674-1914-E711-91BF-D4AE526A0D2E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/48FFB9AC-9A14-E711-90A2-FA163E63D50D.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/4C842015-0C14-E711-BCCF-047D7B881D3A.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/509FBF04-1314-E711-AA20-002590DB91F0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/543AC272-0314-E711-99DB-1CC1DE19286E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/62C1C0B0-9A14-E711-B760-0025905A607E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/6447F4DB-FF13-E711-A001-D4AE526A1687.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/6A1FEED1-5914-E711-A849-0CC47A010854.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/6A919A5A-FE13-E711-AF87-0025904B130E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/6C368021-FB13-E711-9425-D4AE526A0A4B.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/6EEE081E-1614-E711-A3E3-1866DA890B94.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/765825E1-5F14-E711-AEA2-008CFA1CBB34.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/78F435B1-9A14-E711-AF22-0025905A612C.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/887341AF-0C14-E711-B30C-D4AE526A0A4B.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/8C600806-4E14-E711-872E-0025905A612E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/92104629-5014-E711-8F24-0025901D4C94.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/961B1A61-0814-E711-AAD7-1866DA8797A4.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/965FB3D3-6214-E711-9BC6-D4AE527EDC5B.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/A6159821-6514-E711-94DA-0025905A612E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/A65CD526-0E14-E711-A86B-1866DA890700.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/A807467F-0614-E711-B192-70106F4A92B0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/AAB4AF41-0814-E711-9D9D-0CC47A7FC700.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B22557B9-6014-E711-A475-0025901D4940.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B262B203-6F14-E711-A659-0025905A612E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B274D066-0914-E711-85CF-047D7B881D88.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B286BED1-1114-E711-B821-D4AE526A03AD.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B2A8BB78-1E14-E711-BDF3-0025905A612E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/B6C7FCBA-9A14-E711-B13A-1866DA890B94.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/BC4C7545-0D14-E711-BB8C-D4AE526A0461.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/BC5DDBF0-1714-E711-AE3B-1866DA879444.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/BE78D32B-6814-E711-B65F-0025905A607E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/C086E3B0-0E14-E711-A21F-1CC1DE18D40A.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/C29F2378-6414-E711-A297-FA163EB2723B.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/C2F8F48D-FC13-E711-BAA4-70106F49CDF0.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/CEB19F0B-0514-E711-B751-1CC1DE18CFF6.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/D467A212-5814-E711-B59F-0CC47A7C3430.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/DC84B464-0614-E711-8B88-70106F48BD36.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/E4CAD172-9B14-E711-B17B-FA163E934E90.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/E66E4DB0-0F14-E711-9E7A-1CC1DE18D40A.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/F4B291A7-9A14-E711-B175-A0369F7FD528.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/F4B9BDC6-1614-E711-ACCF-0CC47A7EEE0E.root',
'/store/mc/PhaseIFall16DR/ZToJPsiGamma-TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/80000/FAB7D95F-6214-E711-B879-70106F4A928C.root'
                ),
            inputCommands = cms.untracked.vstring(
                'keep *'
            )
        )


process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('efficiency.root')
)





# process.HLT_DoubleMu10_6_Mass0to30_Photon12_v1_EffAna = cms.EDAnalyzer("AODTriggerAnalyzer",
#     verbose = cms.bool(False),
#     configName = cms.string("HLT_DoubleMu10_6_Mass0to30_Photon12_v1"),
#     hltPath = cms.string("HLT_DoubleMu10_6_Mass0to30_Photon12_v1"),
#     ortPath = cms.string("ZB"),
#     bits = cms.InputTag("TriggerResults","","MYHLT"),
#     # HLT Configs
#     # minPhotonPt = cms.double(12.0),
#     # minLeadingMuPt = cms.double(6.0),
#     # minTrailMuPt  = cms.double(4.0),                                                                                                                                                                                                                                
#     # minDimuonMass = cms.double(0.0),
#     # maxDimuonMass = cms.double(12.0),
#     # L1 Labels
#     l1MuonsLabel = cms.InputTag("hltGtStage2Digis:Muon"),
#     l1EGammasLabel = cms.InputTag("hltGtStage2Digis:EGamma"),
#     # L1 Configs - Muons
#     # l1MuonN = cms.uint32(2),
#     # l1AsymmetricCut = cms.bool(False),
#     # l1MuonOS = cms.bool(True),
#     # l1MuonIso = cms.bool(False),
#     # l1MuonQltMin = cms.int32(8),
#     # l1MuonQltMax = cms.int32(15),
#     # l1MuonPt = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80),
#     # l1AsymmetricLeadingMuonCut = cms.double(8.),
#     # l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
#     # # L1 Configs - EGammas
#     # l1EGammaN = cms.uint32(1),
#     # l1EGammaIso = cms.bool(False),
#     # l1EGammaPt = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50),
#     # RECO Labels
#     recoMuonsLabel = cms.InputTag("muons"),
#     recoPhotonsLabel = cms.InputTag("photons"),
#     # RECO Configs
#     minMuPt = cms.double(2.0),# in GeV
#     maxMuEta = cms.double(2.4),
#     minMuonLeadPt = cms.double(20.0),# in GeV
#     minMuonTrailPt = cms.double(4.0), # in GeV
#     GammaMinPtCut = cms.double(0.1),# in GeV
#     DeltaRLeadMuPhotonSel = cms.double(1.0),# deltaR>DeltaRLeadMuPhotonSel
#     DeltaRTrailPhotonSel  = cms.double(1.0),# deltaR>DeltaRTrailPhotonSel 
#     minJPsiMass = cms.double(2.95),# in GeV
#     maxJPsiMass = cms.double(3.25),# in GeV    
#     #HLT Labels
#     triggerSummaryLabel = cms.InputTag("hltTriggerSummaryAOD","","MYHLT"),
#     muonFilterTag = cms.InputTag ("hltDoubleMu55Mass0to30Photon12L3Filtered","","MYHLT"),
#     photonFilterTag = cms.InputTag ("hltEG12HEFilter","","MYHLT"),
#     # photonFilterTag = cms.InputTag ("hltEGL1SingleEG18Filter","","HLT"),
# )

# process.pathAna = cms.EndPath(
# process.HLT_DoubleMu10_6_Mass0to30_Photon12_v1_EffAna 
# )










process.HLT_Tree = cms.EDAnalyzer("AODTriggerAnalyzer",
    verbose = cms.bool(False),
    configName = cms.string("HLT_DoubleMu5_5_Mass0to30_Photon14_v1"),
    hltPath = cms.string("HLT_DoubleMu5_5_Mass0to30_Photon14_v1"),
    ortPath = cms.string("ZB"),
    bits = cms.InputTag("TriggerResults","","MYHLT"),
    # HLT Configs
    # minPhotonPt = cms.double(12.0),
    # minLeadingMuPt = cms.double(6.0),
    # minTrailMuPt  = cms.double(4.0),                                                                                                                                                                                                                                
    # minDimuonMass = cms.double(0.0),
    # maxDimuonMass = cms.double(12.0),
    # L1 Labels
    l1MuonsLabel = cms.InputTag("hltGtStage2Digis:Muon"),
    l1EGammasLabel = cms.InputTag("hltGtStage2Digis:EGamma"),
    # L1 Configs - Muons
    # l1MuonN = cms.uint32(2),
    # l1AsymmetricCut = cms.bool(False),
    # l1MuonOS = cms.bool(True),
    # l1MuonIso = cms.bool(False),
    # l1MuonQltMin = cms.int32(8),
    # l1MuonQltMax = cms.int32(15),
    # l1MuonPt = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80),
    # l1AsymmetricLeadingMuonCut = cms.double(8.),
    # l1AsymmetricTrailingMuonCut = cms.vdouble(0., 1., 2., 3., 4., 5., 6., 7.),
    # # L1 Configs - EGammas
    # l1EGammaN = cms.uint32(1),
    # l1EGammaIso = cms.bool(False),
    # l1EGammaPt = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50),
    # RECO Labels
    recoMuonsLabel = cms.InputTag("muons"),
    recoPhotonsLabel = cms.InputTag("photons"),
    # RECO Configs
    minMuPt = cms.double(2.0),# in GeV
    maxMuEta = cms.double(2.4),
    minMuonLeadPt = cms.double(20.0),# in GeV
    # minMuonTrailPt = cms.double(6.0), # in GeV
    minMuonTrailPt = cms.double(7.0), # in GeV
    GammaMinPtCut = cms.double(0.1),# in GeV
    DeltaRLeadMuPhotonSel = cms.double(1.0),# deltaR>DeltaRLeadMuPhotonSel
    DeltaRTrailPhotonSel  = cms.double(1.0),# deltaR>DeltaRTrailPhotonSel 
    minJPsiMass = cms.double(2.95),# in GeV
    maxJPsiMass = cms.double(3.25),# in GeV    
    #HLT Labels
    triggerSummaryLabel = cms.InputTag("hltTriggerSummaryAOD","","MYHLT"),
    muonFilterTag = cms.InputTag ("hltDoubleMu55Mass0to30Photon14L3Filtered","","MYHLT"),
    photonFilterTag = cms.InputTag ("hltEG14HEFilter","","MYHLT"),
    # photonFilterTag = cms.InputTag ("hltEGL1SingleEG18Filter","","HLT"),
)






process.pathAna = cms.EndPath( process.HLT_Tree )



