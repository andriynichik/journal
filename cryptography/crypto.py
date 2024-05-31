""" Implementation of crypto operations based on EUSignCP library """

# -*- coding: utf-8 -*-
from EUSignCP import *
import json
import base64
import datetime

class CryptoLibrary():
	""" 
		Class implements wrapper over EUSignCP library to simplify work with base library functions.
		The class should be used as singleton

	"""
	def __init__(self):
		self.lib = None
		self.cas = None
		self.context = None
		self.pk_context = None
		self.pk_sign_cert = None
		self.pk_env_cert = None

	def __del__(self):
		self.__finalize()
	
	def __finalize(self):
		if self.lib != None:
			if self.context != None:
				self.lib.CtxFree(self.context)
				self.context = None
			if self.pk_context != None:
				self.lib.CtxFreePrivateKey(self.pk_context)
				self.pk_context = None
			self.pk_sign_cert = None
			self.pk_env_cert = None
			self.lib.Finalize()
			self.lib = None
		EUUnload()


	def __map_date(self, date):
		return datetime.datetime(
			date['wYear'], date['wMonth'], date['wDay'], 
			date['wHour'], date['wMinute'], date['wSecond'])

	def __map_sign_info(self, sign_info):
		return {
			'ownerInfo': {
				'issuer': sign_info['pszIssuer'],
				'issuerCN': sign_info['pszIssuerCN'],
				'serial': sign_info['pszSerial'],
				'subject': sign_info['pszSubject'],
				'subjCN': sign_info['pszSubjCN'],
				'subjOrg': sign_info['pszSubjOrg'],
				'subjOrgUnit': sign_info['pszSubjOrgUnit'],
				'subjTitle': sign_info['pszSubjTitle'],
				'subjState': sign_info['pszSubjState'],
				'subjLocality': sign_info['pszSubjLocality'],
				'subjFullName': sign_info['pszSubjFullName'],
				'subjAddress': sign_info['pszSubjAddress'],
				'subjPhone': sign_info['pszSubjPhone'],
				'subjEMail': sign_info['pszSubjEMail'],
				'subjDNS': sign_info['pszSubjDNS'],
				'subjEDRPOUCode': sign_info['pszSubjEDRPOUCode'],
				'subjDRFOCode': sign_info['pszSubjDRFOCode']
			},
			'timeInfo': {
				'isTimeAvail': sign_info['bTimeAvail'],
				'isTimeStamp': sign_info['bTimeStamp'],
				'time': self.__map_date(sign_info['Time'])
			}
		}

	def __set_settings(self, cas_file_name, ca_certs_file_name):
		""" Configure library by set settings: 
			FileStore, Proxy, OCSP, TSP, LDAP, CMP 
			using CAs.json and CACertificates.p7b files

		"""

		# Disable save settings to system registry or osplm.ini file
		self.lib.SetRuntimeParameter(
			EU_SAVE_SETTINGS_PARAMETER, EU_SETTINGS_ID_NONE)

		# Set file store settings
		fs = {
			'szPath': '', # Using virtual (in memory) file store for certificates 
			'bCheckCRLs': False,
			'bAutoRefresh': False,
			'bOwnCRLsOnly': False,
			'bFullAndDeltaCRLs': False,
			'bAutoDownloadCRLs': False,
			'bSaveLoadedCerts': False,
			'dwExpireTime': 3600
		}
		self.lib.SetFileStoreSettings(fs)

		# Set proxy server settings
		proxy = {
			'bUseProxy': False,
			'bAnonymous': False,
			'szAddress': "",
			'szPort': "",
			'szUser': "",
			'szPassword': "",
			'bSavePassword': False
		}
		self.lib.SetProxySettings(proxy)

		# Set OCSP server settings: enables using OCSP
		ocsp = {
			'bUseOCSP': True,
			'bBeforeStore': True,
			'szAddress': "czo.gov.ua",
			'szPort': "80"
		}
		self.lib.SetOCSPSettings(ocsp)

		# Set TSP server settings
		tsp = {
			'bGetStamps': False,
			'szAddress': "",
			'szPort': ""
		}
		self.lib.SetTSPSettings(tsp)

		# Set LDAP server settings
		ldap = {
			'bUseLDAP': False,
			'szAddress': "",
			'szPort': "",
			'bAnonymous': False,
			'szUser': "",
			'szPassword': ""
		}
		self.lib.SetLDAPSettings(ldap)

		# Set CMP server settings
		cmp = {
			'bUseCMP': False,
			'szAddress': "",
			'szPort': "",
			'szCommonName': ""
		}
		self.lib.SetCMPSettings(cmp)

		# Set online\offline mode settings
		offline_mode = {
			'bOfflineMode': False
		}
		self.lib.SetModeSettings(offline_mode)

		# Set OCSP server access points settings using CAs.json
		with open(cas_file_name, "r", encoding='utf-8') as cas_file:
			cas = json.load(cas_file)
		self.cas = cas

		ocsp_access_info_mode = {
			'bEnabled': True
		}
		self.lib.SetOCSPAccessInfoModeSettings(ocsp_access_info_mode)

		for ca in cas:
			for issuer_cn in ca['issuerCNs']:
				ocsp_access_info = {
					'szIssuerCN': issuer_cn,
					'szAddress': ca['ocspAccessPointAddress'], 
					'szPort': ca['ocspAccessPointPort']
				}
				self.lib.SetOCSPAccessInfoSettings(ocsp_access_info)	

		# Save trusted root certificates to the library certificates storage 
		with open(ca_certs_file_name, "rb") as ca_certs_file:
			ca_certs = ca_certs_file.read()
			self.lib.SaveCertificates(ca_certs, len(ca_certs))

		context = []
		self.lib.CtxCreate(context)
		self.context = context[0]

	def __get_ca_settings(self, issuer_cn):
		""" Search for CA settings by issuer_cn """
		
		
		for ca in self.cas:
			for _issuer_cn in ca['issuerCNs']:
				if issuer_cn == _issuer_cn:
					return ca
			
			# return ca
		raise Exception(f'No CA settings found for {issuer_cn}')

	def print_km(self):
		type = 0
		device = 0
		descr = []

		while self.lib.EnumKeyMediaTypes(type, descr):
			print(f'{type}.{descr[0]}')
			device = 0
			while self.lib.EnumKeyMediaDevices(type, device, descr):
				print(f'    {device}.{descr[0]}')
				device += 1
			type += 1
	def __get_km(self, km_type_name, km_device_name, km_password):
		"""
			Search for key media type and device indexes 
			using km_type_name and km_device_name 

		"""
		self.print_km()
		exit()
		type = 0
		device = 0
		descr = []

		self.lib.EnumKeyMediaTypes(type, descr)
		print("EnumKeyMediaTypes", type, descr)
		while descr[0] != km_type_name:
			type += 1

			if not self.lib.EnumKeyMediaTypes(type, descr):
				raise Exception(f'EnumKeyMediaTypes No key media found for {km_device_name}({km_type_name})')
			print("EnumKeyMediaDevices", type, device, descr)
			self.lib.EnumKeyMediaDevices(type, device, descr)
			while descr[0] != km_device_name:
				device += 1
				if not self.lib.EnumKeyMediaDevices(type, device, descr):
					pass
					# print(self.lib.EnumKeyMediaDevices(type, device, descr))
					# raise Exception(f'EnumKeyMediaDevices No key media found for {km_device_name}({km_type_name})')
				else:
					print(self.lib.EnumKeyMediaDevices(type, device, descr))
					print("EnumKeyMediaDevices TRUE")
			if device > 1000000:
				break


		return {
			"szPassword": km_password,
			"dwTypeIndex": type,
			"dwDevIndex": device
		}

	def __read_private_key(self,
		pk_file_name, pk_km_type, pk_km_device, pk_password,
		pk_certs_files_names, pk_issuer_cn):
		"""
			Read private key. Method supports reading private key from file (pk_file_name) 
			or key media device (pk_km_type, pk_km_device).
			
			If the CA that issued the private key certificates does not support downloading 
			private key certificates from the CMP server, please provide the certificate files (*.cer, *.crt)
			in pk_certs_files_names parameter. Otherwise set pk_certs_files_names to None

			If the CA that issued the private key certificates supports downloading 
			private key certificates from the CMP server, please provide the CA issuer common name from certificate 
			in pk_issuer_cn parameter. Otherwise set pk_issuer_cn to None

		"""
		print("__read_private_key")
		# Save private key certificates to the library certificates store
		if pk_certs_files_names != None:
			for pk_cert_file_name in pk_certs_files_names:
				with open(pk_cert_file_name, "rb") as pk_cert_file:
					print("pk_cert_file")
					pk_cert = pk_cert_file.read()
					self.lib.SaveCertificate(pk_cert, len(pk_cert))
		print("Set CMP server settings")
		# Set CMP server settings
		if pk_issuer_cn != None and pk_issuer_cn != '':
			
			ca = self.__get_ca_settings(pk_issuer_cn)
			if ca['cmpAddress'] != '':
				cmp = {
					'bUseCMP': True,
					'szAddress': ca['cmpAddress'],
					'szPort': '80',
					'szCommonName': ""
				}
				self.lib.SetCMPSettings(cmp)
		print("Set CMP server settings DONE")
		pk_context = []
		owner_info = {}
		if pk_file_name != None and pk_file_name != '':
			with open(pk_file_name, "rb") as pk_file:
				pk = pk_file.read()
			# Read private key from file 
			self.lib.CtxReadPrivateKeyBinary(self.context,
				pk, len(pk), pk_password, pk_context, owner_info)
		else:
			# Search for private key media parameters
			km = self.__get_km(pk_km_type, pk_km_device, pk_password)
			# Read private key from key media (HSMs, Secure tokens, etc)
			self.lib.CtxReadPrivateKey(self.context, km, pk_context, owner_info)
		self.pk_context = pk_context[0]

		# Check that private key can sign data or files using DSTU-4145 algorithm
		# (has certificate for DSTU-4145 digital signature)
		cert = []
		self.lib.CtxGetOwnCertificate(self.pk_context, 
			EU_CERT_KEY_TYPE_DSTU4145, EU_KEY_USAGE_DIGITAL_SIGNATURE,
			None, cert)
		self.pk_sign_cert = cert[0]


		# Check that private key can envelop&develop data or files using DSTU-4145 algorithm
		# (has certificate for DSTU-4145 key agreement)
		cert = []
		self.lib.CtxGetOwnCertificate(self.pk_context, 
			EU_CERT_KEY_TYPE_DSTU4145, EU_KEY_USAGE_KEY_AGREEMENT,
			None, cert)
		self.pk_env_cert = cert[0]	

	def initialize(self, cas_file_name, ca_certs_file_name, 
		pk_file_name, pk_km_type, pk_km_device, pk_password,
		pk_certs_files_names, pk_issuer_cn):
		"""	Initialize library. Method loads and initializes library, 
			sets library settings using CAs.json (cas_file_name) and 
			CACertificates.p7b (ca_certs_file_name) files, 
			reads private key from file (pk_file_name) or 
			key media (pk_km_type, pk_km_device).

			If the CA that issued the private key certificates does not support downloading 
			private key certificates from the CMP server, please provide the certificate files (*.cer, *.crt)
			in pk_certs_files_names parameter. Otherwise set pk_certs_files_names to None

			If the CA that issued the private key certificates supports downloading 
			private key certificates from the CMP server, please provide the CA issuer common name from certificate 
			in pk_issuer_cn parameter. Otherwise set pk_issuer_cn to None

			Production CAs.json and CACertificates.p7b can be downloaded from
			https://iit.com.ua/download/productfiles/CAs.json
			https://iit.com.ua/download/productfiles/CACertificates.p7b

		"""

		if self.lib != None:
			return

		try:
			EULoad()
			self.lib = EUGetInterface()

			self.lib.SetUIMode(False)
			self.lib.Initialize()
			self.lib.SetUIMode(False)

			self.__set_settings(cas_file_name, ca_certs_file_name)
			
			self.__read_private_key(
				pk_file_name, pk_km_type, pk_km_device, pk_password,
				pk_certs_files_names, pk_issuer_cn)
			print("initialize EU  DONE")
		except Exception as e:
			self.__finalize()
			raise e

	def get_own_envelop_certificate(self):
		""" Method returns own certificate for enveloping encoded in base64 string """

		return base64.b64encode(self.pk_env_cert)

	def hash_data(self, data):
		""" Method returns hash (GOST34-311) encoded in base64 string calculated for data """

		hash = []
		self.lib.CtxHashData(self.context,
			EU_CTX_HASH_ALGO_GOST34311, None, 0, data, len(data), hash)

		return base64.b64encode(hash[0])

	def verify_data(self, data, signature):
		""" Method verifies CAdES detached signature (in base64) for data and returns signature information """

		sign_info = {}
		sign_index = 0

		self.lib.VerifyDataOnTimeEx(
			data, len(data), sign_index, signature,
			None, 0, None, False, False, sign_info)

		return self.__map_sign_info(sign_info)

	def develop_data(self, enveloped_data):
		""" Method develops enveloped data (in base64) and returns data and sender information """

		data = []
		sender_info = {}

		self.lib.CtxDevelopData(
			self.pk_context, enveloped_data,
			None, 0, None, 0, data, sender_info)

		sender_info = self.__map_sign_info(sender_info)

		return data[0], sender_info