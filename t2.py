import pandas as pd
import numpy as np
import os

pathDir = ''#cole o path aqui

calculoDir = pathDir + '/' + 'Calculo1'
mdDir = pathDir + '/' + 'MD'
icDir = pathDir + '/' + 'IC'
ttccDir = pathDir + '/' + 'ttcc'
sample = pathDir + '/sample.csv'

#-------------------------------------------------- CAlC --------------------------------------------------------

fileList = os.listdir(calculoDir)

calcFrame = pd.read_csv(sample,sep=';',encoding='latin-1')
for i in range(len(fileList)):
    dTemp = pd.read_csv(calculoDir +'/'+ fileList[i],sep=';',encoding='latin-1')
    calcFrame = pd.concat([calcFrame,dTemp],ignore_index=True)
     
calcFrame.head(300)
#-------------------------------------------------- IC ----------------------------------------------------------- 

fileList = os.listdir(icDir)

icFrame = pd.read_csv(sample,sep=';',encoding='latin-1')
for i in range(len(fileList)):
    dTemp = pd.read_csv(icDir +'/'+ fileList[i],sep=';',encoding='latin-1')
    icFrame = pd.concat([icFrame,dTemp],ignore_index=True)
     
icFrame.head(300)

#-------------------------------------------------- MD ------------------------------------------------------------

fileList = os.listdir(mdDir)

mdFrame = pd.read_csv(sample,sep=';',encoding='latin-1')
for i in range(len(fileList)):
    dTemp = pd.read_csv(mdDir +'/'+ fileList[i],sep=';',encoding='latin-1')
    mdFrame = pd.concat([mdFrame,dTemp],ignore_index=True)
     
mdFrame.head(300)

#-------------------------------------------------- TTCC ----------------------------------------------------------

fileList = os.listdir(ttccDir)

ttccFrame = pd.read_csv(sample,sep=';',encoding='latin-1')
for i in range(len(fileList)):
    dTemp = pd.read_csv(ttccDir +'/'+ fileList[i],sep=';',encoding='latin-1')
    ttccFrame = pd.concat([ttccFrame,dTemp],ignore_index=True)
     
ttccFrame.head(300)

anos = calcFrame['ANO'].unique()


print('Calculo\tInt. Computação\tMatematica Discreta\tTextos Tecnicos\n')
for x in range(len(anos)):
    descarte = sum((calcFrame['ID_PESSOA'] == '#N/D') & (calcFrame['ANO'] == anos[x]))
    apCalc = sum((calcFrame['ANO'] == anos[x]) & (calcFrame['DESCR_SITUACAO'] == 'Aprovado') & (calcFrame['ID_PESSOA'] != '#N/D'))/(sum(calcFrame['ANO'] == anos[x])-descarte)
    descarte = sum((icFrame['ID_PESSOA'] == '#N/D') & (icFrame['ANO'] == anos[x]))
    apIc = sum((icFrame['ANO'] == anos[x]) & (icFrame['DESCR_SITUACAO'] == 'Aprovado') & (icFrame['ID_PESSOA'] != '#N/D'))/(sum(icFrame['ANO'] == anos[x])-descarte)
    if(anos[x] > 2015):
        descarte = sum((mdFrame['ID_PESSOA'] == '#N/D') & (mdFrame['ANO'] == anos[x]))
        apMd = sum((mdFrame['ANO'] == anos[x]) & (mdFrame['DESCR_SITUACAO'] == 'Aprovado') & (mdFrame['ID_PESSOA'] != '#N/D'))/(sum(mdFrame['ANO'] == anos[x])-descarte)
    else:
        apMd = 0
    descarte = sum((ttccFrame['ID_PESSOA'] == '#N/D') & (ttccFrame['ANO'] == anos[x]))
    apTtcc = sum((ttccFrame['ANO'] == anos[x]) & (ttccFrame['DESCR_SITUACAO'] == 'Aprovado') & (ttccFrame['ID_PESSOA'] != '#N/D'))/(sum(ttccFrame['ANO'] == anos[x])-descarte)
    print(anos[x], '\t',apCalc, '\t',apIc, '\t',apMd,'\t', apTtcc,'\t')

