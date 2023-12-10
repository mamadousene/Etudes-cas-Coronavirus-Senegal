"""
    MamadouLAMINESENE
    ML__SENE___17
"""
from donne_EvolutionAnalyzer import *
class DbEA:
    def __init__(self):
        pass
    """
        Function pour avoir toutes les region
        et leur department
    """
    def getDict(self):
        region,departement=dicoRegion_Departement()
        donne={}
        for key,val in region.items():
            donne[key]=[]
            for keyFils,valFils in departement.items():
                if val==valFils:
                    donne[key].append(keyFils)
        
        return donne