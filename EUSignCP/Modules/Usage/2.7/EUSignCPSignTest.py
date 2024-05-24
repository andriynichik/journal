# -*- coding: utf-8 -*-
print("EUSignCP Python Sign Test:")

from EUSignCP import *
EULoad()
pIface = EUGetInterface()
try:
	pIface.Initialize()
except Exception as e:
	print ("Initialize failed"  + str(e))
	EUUnload()
	exit()

print("Library Initialized")

dwType = 0
lDescription = []
try:
	pIface.EnumKeyMediaTypes(dwType, lDescription)
	while lDescription[0] != u"файлова система (каталоги системи)":
		dwType += 1
		if not pIface.EnumKeyMediaTypes(dwType, lDescription):
			print ("KeyMedia not found")
			pIface.Finalize()
			EUUnload()
			exit()

except Exception as e:
	dError = eval(str(e))
	print ("EnumKeyMediaTypes failed. Error code: " + str(dError['ErrorCode']) + ". Description: " + dError['ErrorDesc'])
	pIface.Finalize()
	EUUnload()
	exit()

pKM = {"szPassword" : "12345677", "dwDevIndex": 0, "dwTypeIndex": dwType}
try:
	pIface.ReadPrivateKey(pKM, None)
except Exception as e:
	dError = eval(str(e))
	print ("Key reading failed. Error code: " + str(dError['ErrorCode']) + ". Description: " + dError['ErrorDesc'])
	pIface.Finalize()
	EUUnload()
	exit()

print("Key success read")

pData = b"Test Data"
lSign = []

try:
	pIface.SignData(pData, len(pData), None, lSign)
except Exception as e:
	dError = eval(str(e))
	print ("SignData failed. Error code: " + str(dError['ErrorCode']) + ". Description: " + dError['ErrorDesc'])
	pIface.Finalize()
	EUUnload()
	exit()

print("Data sign done")

try:
	pIface.VerifyData(pData, len(pData), None, lSign[0], len(lSign[0]), None)
except Exception as e:
	dError = eval(str(e))
	print ("VerifyData failed. Error code: " + str(dError['ErrorCode']) + ". Description: " + dError['ErrorDesc'])
	pIface.Finalize()
	EUUnload()
	exit()

pIface.Finalize()
EUUnload()

print("EUSignCP Python Sign Test done.")
