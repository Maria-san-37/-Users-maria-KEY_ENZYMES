
class Key_Enzymes(object):
    '''Blueprint for key enzymes of biogeochemical cycles'''
    def __init__(self, name, pathway, EC):
        self.name = name
        self.pathway = pathway
        self.EC = EC
        self.metadata = []
        self.taxonomy_groups = []

    def add_info(self, information):
        self.metadata.append(information)
    def add_taxonomy(self,taxonomy):
        self.taxonomy_groups.append(taxonomy)
    def get_info(self):
        print ("Enzyme:%r\nPathway:%r\nEC:%rTaxa:%r\n" %(self.name,self.pathway,self.EC,self.taxonomy_groups))




DsrA = Key_Enzymes('dsrA', 'Dissimilatory [bi] sulfite reductase','1.8.99.5')
DsrB = Key_Enzymes('dsrB','Dissimilatory [bi] sulfite reductase', '1.8.99.5' )
DsrC = Key_Enzymes('dsrc', 'Sulfite reduction', '')
DsrMKJOP = Key_Enzymes('dsrMKJOP complex', 'Sulfite reduction', '1.7.5.1 1.7.99.-')

Sat = Key_Enzymes('sat', 'Sulfur oxidation', '2.7.7.4')
aprBA = Key_Enzymes('aprBA', 'Sulfur oxidation', '1.8.4.9')
qmoABC = Key_Enzymes ('qmoABC', 'Sulfate reduction', '-')
dsr = Key_Enzymes('dsr', '', '')
mccA_sirA = Key_Enzymes('mccA/sirA', 'Dissimilatory (bi)sulfite reductase','-')
asrABC = Key_Enzymes('asrABC', 'Anaerobic sulfite reductase', '')
fsr = Key_Enzymes('fsr', 'sulfur assimilation', '')
phsABC = Key_Enzymes('phsABC', 'Thiosulfate reductase', '')

RubiscO = Key_Enzymes('RubisCO', 'Reductive pentose phosphate cycle', '2.1.1.127')
RubiscO.add_taxonomy('Cyanobacteria, Alphaproteobacteria, Betaproteobacteria, Gammaproteobacteria, Zetaproteobacteria,Sulfobacillusspp., Oscillochloridaceae')
PRK = Key_Enzymes ('phosphoribulokinase', 'Reductive pentose phosphate cycle','2.7.1.19')
PRK.add_taxonomy('Cyanobacteria, Alphaproteobacteria, Betaproteobacteria, Gammaproteobacteria, Zetaproteobacteria,Sulfobacillusspp., Oscillochloridaceae')
ATP_citrate_lyase = Key_Enzymes('ATP citrate lyase', 'Reductive tricarboxylic acid cycle', '2.3.3.8')
ATP_citrate_lyase.add_taxonomy('Aquificales, Chlorobiales, Epsilonproteobacteria,Magnetococcus,Deltaproteobacteria,Gammaproteobacteria,Nitrospirae')
two_oxoglutarate_synthase = Key_Enzymes('2-oxoglutarate synthase','Reductive tricarboxylic acid cycle', '1.2.7.3')
two_oxoglutarate_synthase.add_taxonomy('Aquificales, Chlorobiales, Epsilonproteobacteria,Magnetococcus,Deltaproteobacteria,Gammaproteobacteria,Nitrospirae')
acetyl_CoA_synthase= Key_Enzymes('acetyl-CoA synthase','Reductive acetyl-CoA pathway', '2.3.1.169')
acetyl_CoA_synthase.add_taxonomy('Clostridia,Spirochaeta,Delta-Proteobacteria, Anammox bacteria, Archaeoglobales,Methanogens')
malonyl_CoA_reductase =Key_Enzymes('Malonyl-CoA reductase', '3-Hydroxypropionate bicycle', '1.2.1.75')
malonyl_CoA_reductase.add_taxonomy('Chloroflexaceae (Chloroflexi)')
propionyl_CoA synthase = Key_Enzymes('Propionyl-CoA synthase', '3-Hydroxypropionate bicycle', '6.2.1.36')
propionyl_CoA synthase.add_taxonomy('Chloroflexaceae (Chloroflexi)')
propionyl_CoA_carboxylase = Key_Enzymes('propionyl-CoA carboxylase','3-Hydroxypropionate/ 4-hydroxybutyrate cycle','6.4.1.3')
propionyl_CoA_carboxylase.add_taxonomy('Sulfolobales, Marine group 1 Crenarchaeota')
four_hydroxybutyryl_CoA_dehydratase= Key_Enzymes('4-hydroxybutyryl-CoA dehydratase','3-Hydroxypropionate/ 4-hydroxybutyrate cycle', '4.2.1.120')
four_hydroxybutyryl_CoA_dehydratase.add_taxonomy('Sulfolobales, Marine group 1 Crenarchaeota')
malonyl_CoA_reductase_4HP_3HB= Key_Enzymes('malonyl-CoA reductase', '3-Hydroxypropionate/ 4-hydroxybutyrate cycle','1.2.1.75')
malonyl_CoA_reductase_4HP_3HB.add_taxonomy('Sulfolobales, Marine group 1 Crenarchaeota')
four_hydroxybutyryl_CoA_dehydratase_D_4HB= Key_Enzymes('four_hydroxybutyryl_CoA_dehydratase', 'Dicarboxylate/ 4-hydroxybutyrate cycle', '4.2.1.120')
four_hydroxybutyryl_CoA_dehydratase_D_4HB.add_taxonomy('Desulfurococcales, Thermoproteales')
