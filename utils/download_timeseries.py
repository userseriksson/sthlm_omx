import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io
from utils import config

start = datetime.datetime(2021,1,1)
end = datetime.datetime(2021,11,1)

Symbols = ['8TRA.ST',	'AAK.ST',	'ABB.ST',	'ADDT-B.ST',	'AF-B.ST',	'ALFA.ST',	'ALIV-SDB.ST',	'ALK-B.ST',
             'ALMB.ST',	'AM1.ST',	'AM1S.ST',	'AMBU-B.ST',	'ARION.ST',	'ARION-SDB.ST',	'ARJO-B.ST',	'ASSA-B.ST',
             'ATCO-A.ST',	'ATCO-B.ST',	'ATRLJ-B.ST',	'AXFO.ST',	'AZA.ST',	'AZN.ST',	'BALD-B.ST',	'BEIJ-B.ST',
             'BETS-B.ST',	'BHG.ST',	'BILL.ST',	'BOL.ST',	'BRAV.ST',	'BURE.ST',	'CARL-A.ST',	'CARL-B.ST',	
             'CAST.ST',	'CATE.ST',	'CGCBV.ST',	'CHR.ST',	'CINT.ST',	'COLO-B.ST',	'CTY1S.ST',	'DANSKE.ST',	'DEMANT.ST',
             'DFDS.ST',	'DOM.ST',	'DRLCO.ST',	'DSV.ST',	'EKTA-B.ST',	'ELISA.ST',	'ELUX-A.ST',	'ELUX-B.ST',	
             'EPI-A.ST',	'EPI-B.ST',	'EPRO-B.ST',	'EQT.ST',	'ERIC-A.ST',	'ERIC-B.ST',	'ESSITY-A.ST',	
             'ESSITY-B.ST',	'EVO.ST',	'FABG.ST',	'FLS.ST',	'FOI-B.ST',	'FORTUM.ST',	'FPAR-A.ST',	'FPAR-D.ST',
             'FPAR-PREF.ST',	'FSKRS.ST',	'G4S.ST',	'GETI-B.ST',	'GMAB.ST',	'GN.ST',	'HEXA-B.ST',	'HM-B.ST',
             'HOLM-A.ST',	'HOLM-B.ST',	'HPOL-B.ST',	'HUFV-A.ST',	'HUH1V.ST',	'HUSQ-A.ST',	'HUSQ-B.ST',	
             'ICA.ST',	'INDT.ST',	'INDU-A.ST',	'INDU-C.ST',	'INTRUM.ST',	'INVE-A.ST',	'INVE-B.ST',	'ISS.ST',
             'JDAN.ST',	'JM.ST',	'JYSK.ST',	'KBHL.ST',	'KCR.ST',	'KEMIRA.ST',	'KESKOA.ST',	'KESKOB.ST',	
             'KIND-SDB.ST',	'KINV-A.ST',	'KINV-B.ST',	'KLED.ST',	'KLOV-A.ST',	'KLOV-B.ST',	'KLOV-PREF.ST',	
             'KNEBV.ST',	'KOJAMO.ST',	'LATO-B.ST',	'LIFCO-B.ST',	'LOOMIS.ST',	'LUMI.ST',	'LUN.ST',	'LUND-B.ST',
             'LUNE.ST',	'MAERSK-A.ST',	'MAERSK-B.ST',	'MAREL.ST',	'MCOV-B.ST',	'METSA.ST',	'METSB.ST',	'MOCORP.ST',	
             'MYCR.ST',	'NCC-A.ST',	'NCC-B.ST',	'NDA-DK.ST',	'NDA-FI.ST',	'NDA-SE.ST',	'NELES.ST',	'NENT-A.ST',	
             'NENT-B.ST',	'NESTE.ST',	'NETC.ST',	'NIBE-B.ST',	'NOBI.ST',	'NOKIA.ST',	'NOLA-B.ST',	'NOVO-B.ST',	
             'NYF.ST',	'NZYM-B.ST',	'ORNAV.ST',	'ORNBV.ST',	'ORSTED.ST',	'OSSR.ST',	'OUT1V.ST',	'PEAB-B.ST',	
             'PLAZ-B.ST',	'PNDORA.ST',	'PNDX-B.ST',	'RATO-A.ST',	'RATO-B.ST',	'RBREW.ST',	'RESURS.ST',	
             'RILBA.ST',	'ROCK-A.ST',	'ROCK-B.ST',	'SAA1V.ST',	'SAAB-B.ST',	'SAGA-A.ST',	'SAGA-B.ST',	
             'SAGA-D.ST',	'SAMPO.ST',	'SAND.ST',	'SAVE.ST',	'SBB-B.ST',	'SBB-D.ST',	'SCA-A.ST',	'SCA-B.ST',	'SCHO.ST',	
             'SEB-A.ST',	'SEB-C.ST',	'SECT-B.ST',	'SECU-B.ST',	'SHB-A.ST',	'SHB-B.ST',	'SIM.ST',	'SINCH.ST',	
             'SKA-B.ST',	'SKF-A.ST',	'SKF-B.ST',	'SOBI.ST',	'SPNO.ST',	'SSAB-A.ST',	'SSAB-B.ST',	'SSABAH.ST',	
             'SSABBH.ST',	'STE-A.ST',	'STE-R.ST',	'STEAV.ST',	'STERV.ST',	'STG.ST',	'SWEC-A.ST',	'SWEC-B.ST',	
             'SWED-A.ST',	'SWMA.ST',	'SYDB.ST',	'TEL2-A.ST',	'TEL2-B.ST',	'TELIA.ST',	'TELIA1.ST',	'THULE.ST',	
             'TIETO.ST',	'TIETOS.ST',	'TIGO-SDB.ST',	'TOP.ST',	'TREL-B.ST',	'TRYG.ST',	'TTALO.ST',	'TYRES.ST',
             'UPM.ST',	'VALMT.ST',	'VITR.ST',	'VNE-SDB.ST',	'VOLV-A.ST',	'VOLV-B.ST',	'VWS.ST',	'WALL-B.ST',	
             'WIHL.ST',	'WRT1V.ST',	'YIT.ST',	'ZEAL.ST', 'STE-R.ST'
           ]

# create empty dataframe
stock_final_v2 = pd.DataFrame()

t0 = time.time()

# create empty dataframe
stock_final_v2 = pd.DataFrame()

# iterate over each symbol
for i in Symbols:

    # print the symbol which is being downloaded
    print( str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)

    try:
        # download the stock price
        stock = []
        stock = yf.download(i,start=start, end=end, progress=False)

        # append the individual stock prices
        if len(stock) == 0:
            None
        else:
            stock['Name']=i
            stock_final_v2 = stock_final_v2.append(stock,sort=False)
    except Exception:
        None

t1 = time.time()

total = t1-t0

print(stock_final_v2.head(10))

stock_final_v2.to_csv('/Users/joeriksson/Desktop/python_data/stock_swe_20211106.plk')
