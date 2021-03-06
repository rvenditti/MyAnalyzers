import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("Demo",eras.Phase2C1)
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryExtended2023D1Reco_cff')
#process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('RecoMuon.MuonIdentification.me0MuonReco_cff')



from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.source = cms.Source("PoolSource",
                            # replace 'myfile.root',',',',',' with the source file you want to use
                            fileNames = cms.untracked.vstring(

#                                                              'root://xrootd-cms.infn.it:1194//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/81X_mcRun2_asymptotic_v5_2023D1-v1/00000/044DA3BD-7770-E611-B8C0-0CC47A78A3D8.root',
#'root://cms-xrd-global.cern.ch/store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/002571DC-BA80-E611-B4D2-0CC47A7C340E.root',
       'root://xrootd-cms.infn.it//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/06AA4767-C480-E611-A2AD-0CC47A4D76B8.root',
       'root://xrootd-cms.infn.it//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/06B79AA7-E780-E611-9E10-0CC47A78A2EC.root',
       'root://xrootd-cms.infn.it//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/0CD16A6C-C480-E611-8325-0CC47A4D769C.root',
       'root://xrootd-cms.infn.it//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/0CFC48D2-EC7F-E611-9744-0CC47A74525A.root',
       'root://xrootd-cms.infn.it//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/0EE5DD8A-D180-E611-9E10-0025905B857A.root',
       'root://xrootd-cms.infn.it//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/0EFCBF80-ED7F-E611-A99C-0CC47A7C34A6.root',
  #     'root://xrootd-cms.infn.it:1194//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/16CB2F93-0181-E611-9382-0025905A609E.root',
   #    'root://xrootd-cms.infn.it:1194//store/relval/CMSSW_8_1_0_pre11/RelValTenMuExtendedE_0_200/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v5_2023D1rePU200-v2/00000/1A3EAD07-0380-E611-B12E-0CC47A7C34D0.root',
                                                              
                                                              
        ))
                                                              
process.me0SegAna = cms.EDAnalyzer('ME0SegmentAnalyzerMuonGun',
                                  wp = cms.string("tight"),
                                  minEta = cms.double(2.0),
                                  maxEta = cms.double(2.8),
                                  #    etaMin = cms.double(2.0),
                                  #    etaMax = cms.double(2.8),
                                  #    dr = cms.double(0.25),
                                  #    ptMin = cms.double(5.0),
                                  timeMin = cms.double(18.3 - 3*0.1),
                                  timeMax = cms.double(18.3 + 3*0.1)
)


process.TFileService = cms.Service("TFileService",
fileName = cms.string("histoME0SegMuGun_81X_1k.root")
)

process.p = cms.Path(process.me0SegAna)


