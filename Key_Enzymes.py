class Key_Enzymes(object):
    '''Blueprint for key enzymes of biogeochemical cycles'''

    def __init__(self,name,pathway, EC):
        status ='Presente en metagenoma*'
        self.name = name
        self.pathway = pathway
        self.EC= EC
        self.metadata = []
    def add_info(self, information):
        self.metadata.append(information)
    def get_details(self):


DsrA = Key_Enzymes('dsrA', 'Dissimilatory [bi] sulfite reductase','EC:1.8.99.5')
DsrB = Key_Enzymes('dsrB','Dissimilatory [bi] sulfite reductase', 'EC:1.8.99.5' )
DsrC = Key_Enzymes('dsrc', 'Sulfite reduction', '')
DsrMKJOP = Key_Enzymes('dsrMKJOP complex', 'Sulfite reduction', 'EC:1.7.5.1 1.7.99.-')
DsrN = Key_Enzymes('')
DsrD = Key_Enzymes('')
Sat = Key_Enzymes('sat', 'Sulfur oxidation', 'EC:2.7.7.4')
AprBA = Key_Enzymes('aprBA', 'Sulfur oxidation', 'EC:1.8.4.9')
