from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from OpenSSL import crypto


def generateCertificateObjects(organization, organizationalUnit):
    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, 4096)

    req = crypto.X509Req()
    subject = req.get_subject()
    subject.O = organization
    subject.OU = organizationalUnit
    req.set_pubkey(pkey)
    req.sign(pkey, "md5")

    cert = crypto.X509()
    cert.set_serial_number(1)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(60)
    cert.set_issuer(req.get_subject())
    cert.set_subject(req.get_subject())
    cert.set_pubkey(req.get_pubkey())
    cert.sign(pkey, "md5")

    return pkey, req, cert


if __name__ == '__main__':
    p_key, req, cert = generateCertificateObjects('ymtech', 'ymtech')
    public_key = crypto.dump_publickey(crypto.FILETYPE_PEM, p_key)
    private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p_key, 'aes256', b'test')
    print(p_key, req, cert)
    print(private_key)
    print(public_key)

    # dave .pem files
    fObj = open('./hsoh.pem', 'w')
    fObj.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, p_key, 'aes256', b'test').decode("utf-8"))
    fObj.close()
    # get_key = crypto.load_privatekey(crypto.FILETYPE_PEM, open('./hsoh.pem', 'rb').read(), b'test')

    # signature
    signature_data = crypto.sign(p_key, b'data..', 'SHA256')
    b = crypto.verify(cert, signature_data, data=b'data..', digest='SHA256')

    # encrypt
    rsaKey = RSA.importKey(public_key)
    pkcs1CipherTmp = PKCS1_OAEP.new(rsaKey)
    encryptedString = pkcs1CipherTmp.encrypt(b'data..')
    print(encryptedString)

    # decrypt
    # TODO ...

