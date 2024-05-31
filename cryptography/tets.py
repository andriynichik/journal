from crypto import CryptoLibrary

# Parameters for crypto library:
# CAS - file path to CAs.json file with CA servers configuration
# CA_CERTIFICATES - file path to CACertificates.p7b file with root CA certificates of all ukrainian CAs.
# WARNING! The library automatically trusts all certificates in this file
# Production CAs.json and CACertificates.p7b can be downloaded from
# https://iit.com.ua/download/productfiles/CAs.json
# https://iit.com.ua/download/productfiles/CACertificates.p7b
CAS = "./data/CAs.json"
CA_CERTIFICATES = "./data/CACertificates.p7b"

# Private key parameters
# PKEY_FILE - file path to private key file (Key-6.dat, *.pfx, *.jks, *.zs2, *.pk8)
# PKEY_TYPE - key media type name with private key (e.x. "криптомод. ІІТ Гряда-301", "е.ключ ІІТ Кристал-1", etc). Set PKEY_FILE=None to read private key from key media
# PKEY_DEVICE - key media device name with private key
# PKEY_PASSWORD - password for private key file or key media
# PKEY_CERTS_FILES - an array of private key certificates files (*.cer, *.crt)
# PKEY_ISSUER_CN - private key certificate issuer common name
PKEY_FILE = ""
PKEY_TYPE = "е.ключ ІІТ Алмаз-1К"
PKEY_DEVICE = 363677
PKEY_PASSWORD = "12345"
PKEY_CERTS_FILES = ["./data/CA-02130E6113DBF9F004000000FD00000034020000.cer", "./data/CA-02130E6113DBF9F004000000FD00000034020000 (1).cer"]
PKEY_ISSUER_CN = 'Тестовий комплес КНЕДП \"Дія\"'

# File to sign
FILE_WITH_DATA_TO_SIGN = "./data/TestFile.pdf"
# File with sign
FILE_WITH_SIGN = "./data/TestFile.pdf.p7s"

FILE_CONTENT_TYPE = {
	'.ico': 'image/x-icon',
	'.html': 'text/html; charset=utf-8',
	'.js': 'text/javascript',
	'.css': 'text/css'
}

crypto_lib = CryptoLibrary()
crypto_lib.initialize(
	CAS, CA_CERTIFICATES,
	PKEY_FILE, PKEY_TYPE, PKEY_DEVICE, PKEY_PASSWORD,
	PKEY_CERTS_FILES, PKEY_ISSUER_CN)
