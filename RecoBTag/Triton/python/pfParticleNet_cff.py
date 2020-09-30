import FWCore.ParameterSet.Config as cms

from RecoBTag.FeatureTools.pfDeepBoostedJetTagInfos_cfi import pfDeepBoostedJetTagInfos
#from RecoBTag.Triton.boostedJetONNXJetTagsProducer_cfi import boostedJetONNXJetTagsProducer
from RecoBTag.Triton.boostedJetONNXTritonJetTagsProducer_cfi import boostedJetONNXTritonJetTagsProducer
from RecoBTag.Triton.pfParticleNetDiscriminatorsJetTags_cfi import pfParticleNetDiscriminatorsJetTags

pfParticleNetTagInfos = pfDeepBoostedJetTagInfos.clone(
    use_puppiP4 = False
)

pfParticleNetJetTags = boostedJetONNXJetTagsProducer.clone(
    src = 'pfParticleNetTagInfos',
    preprocess_json = 'RecoBTag/Combined/data/ParticleNetAK8/General/V01/preprocess.json',
    model_path = 'RecoBTag/Combined/data/ParticleNetAK8/General/V01/particle-net.onnx',
    flav_names = ["probTbcq",  "probTbqq",  "probTbc",   "probTbq",  "probTbel", "probTbmu", "probTbta",
                  "probWcq",   "probWqq",   "probZbb",   "probZcc",  "probZqq",  "probHbb", "probHcc",
                  "probHqqqq", "probQCDbb", "probQCDcc", "probQCDb", "probQCDc", "probQCDothers"],
)

from CommonTools.PileupAlgos.Puppi_cff import puppi
from PhysicsTools.PatAlgos.slimming.primaryVertexAssociation_cfi import primaryVertexAssociation

# This task is not used, useful only if we run it from RECO jets (RECO/AOD)
pfParticleNetTask = cms.Task(puppi, primaryVertexAssociation, pfParticleNetTagInfos,
                             pfParticleNetJetTags, pfParticleNetDiscriminatorsJetTags)

# declare all the discriminators
# nominal: probs
_pfParticleNetJetTagsProbs = ['pfParticleNetJetTags:' + flav_name
                              for flav_name in pfParticleNetJetTags.flav_names]
# nominal: meta-taggers
_pfParticleNetJetTagsMetaDiscrs = ['pfParticleNetDiscriminatorsJetTags:' + disc.name.value()
                                   for disc in pfParticleNetDiscriminatorsJetTags.discriminators]
_pfParticleNetJetTagsAll = _pfParticleNetJetTagsProbs + _pfParticleNetJetTagsMetaDiscrs
