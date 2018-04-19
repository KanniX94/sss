import numpy as np
import matplotlib.pyplot as plt

s = []
logLenList = [] # Logarithmierte Laengen
wertList = [] # Logarithmierte Mittelwerte

for i in range(10, 68, 3):
    s.append(str(i) + 'cm.csv')
    logLenList.append(np.log(i))

datamittelarr = []
datastdarr = []
datamittelwert = 0
average = 0

for i in s:
    data = np.genfromtxt(i, delimiter=",", skip_header=1000)
    data = data[:,0:-1]

    for j in range(0, len(data)):
        datamittelwert = data[j] + datamittelwert

    datamittelwert = datamittelwert[1:]
    datamittelwert = datamittelwert/len(data)
    datamittelarr.append(datamittelwert)
    datamittelwert = 0
    
    datastd = np.std(data[:,-1])
    datastdarr.append(datastd)
    wertList.append(np.log(np.average(data[:,-1])))
    
distanz = np.zeros((len(datamittelarr)))
indx = 0
for i in range(0,len(distanz)*3,3):
    distanz[indx] = i + 10.0
    indx += 1

# Ausgabe der berechneten Mittelwerte
for i in datamittelarr:
	print(i)
	
	
# Versuch 2
wertList2 = [] # Logarithmierte Mittelwerte
tmpSum1 = 0
tmpSum2 = 0

# Berechnung der Linearen Regression
for i in range(0, len(wertList)):
	tmpY = (wertList[i] - np.average(wertList))
	tmpX = (logLenList[i] - np.average(logLenList))
	tmpSum1 += tmpY*tmpX
for i in logLenList:
	tmpSum2 += (i - np.average(logLenList))**2
a = tmpSum1/tmpSum2
b = np.average(wertList) - (a*np.average(logLenList))
print("a = ", a , "; b = " , b)
linR = []
for x in logLenList:
	linR.append(a*x+b)
	
# Versuch 3
# Einlesen der benoetigten Dateien
s2 = []
s2.append('kurz.csv')
s2.append('lang.csv')

for i in s:
    data = np.genfromtxt(i, delimiter=",", skip_header=1000)
    data = data[:,0:-1]
    wertList2.append(np.log(np.average(data[:,-1]))) # Mittelwerte der gemessenen langen und kurzen Seite
	
kurz = (wertList2[0]/np.exp(b))**(1/a)
lang = (wertList2[1]/np.exp(b))**(1/a)
print("Kurz:", kurz, "cm")
print("Lang:", lang, "cm")
print(kurz * lang, "cm^2")
	    
# Ausgabe Kennlinie
plt.plot(distanz, datamittelarr, label='Volt')
plt.ylabel('Spannung in V')
plt.xlabel('Abstand in cm')
plt.legend()
plt.show()
	
# Ausgabe Lineare Regression
plt.plot(logLenList, wertList2, "ro")
plt.plot(logLenList, linR)
plt.ylabel('Logarithmierte Spannung in V')
plt.xlabel('Logarithmierter Abstand in cm')
plt.title('Lineare Regression')
plt.show()






