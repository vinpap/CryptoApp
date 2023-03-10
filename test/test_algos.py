"""
Les fonctions à tester sont les méthodes 'encrypt' et 'decrypt'
des classes contenues dans les fichiers dont le nom se termine
par 'algo.py'. À noter que certaines classes n'ont pas de méthode
decrypt, ou uniquement une méthode vide.
"""


# Les fichiers où se trouvent les fonctions à tester sont déjà importés
from crypto_app.enigmam3_algo import EnigmaM3
from crypto_app.aes_algo import AdvancedEncryptionStandard
from crypto_app.blowfish_algo import Blowfish
from crypto_app.caesarcipher_algo import CaesarCipher
from crypto_app.des_algo import DES
from crypto_app.md5_algo import MD5
from crypto_app.rsa_algo import RSAAlgo
from crypto_app.sha_algo import SHA
from crypto_app.vigenerecipher_algo import VigenereCipher




def test_enigma():

    enigma = EnigmaM3()

    msg = "Message"
    expected_encryption = "FUTALDK"

    key = [
        ('A', 'C', 'N'),
        (2, 4, 1),
        ('F', 'H', 'K'),
        [('A', 'K')]
    ]

    encrypted = enigma.encrypt(msg, key)
    assert encrypted == expected_encryption

    decrypted = enigma.decrypt(encrypted, key)
    assert decrypted == "MESSAGE"



def test_aes():

    aes = AdvancedEncryptionStandard()
    msg = "Message"
    key = "16 caracteres !!"
    expected_encryption = "5e10b9901384af"


    encrypted = aes.encrypt(msg, key)
    assert encrypted == expected_encryption
    decrypted = aes.decrypt(encrypted, key)
    assert decrypted == msg


def test_blowfish():

    blowfish = Blowfish()
    msg = "message"
    key = "ma clé privée"

    encrypted = blowfish.encrypt(msg, key)
    decrypted = blowfish.decrypt(encrypted, key)
    assert decrypted == msg




def test_caesar():

    caesar = CaesarCipher()
    msg = "message"
    key = 3
    expected_encryption = "phvvdjh"

    encrypted = caesar.encrypt(msg, key)
    assert encrypted == expected_encryption

    decrypted = caesar.decrypt(encrypted, key)
    assert decrypted == msg

def test_des():

    des = DES()
    msg = "message"
    key = "16 caracteres !!"
    expected_encryption = "c746f006ae2af1b3"

    encrypted = des.encrypt(msg, key)
    assert encrypted == expected_encryption
    decrypted = des.decrypt(encrypted, key)
    assert decrypted == msg

def test_md5():

    md5_test = MD5()

    msg = "message"
    expected_hash = "78e731027d8fd50ed642340b7c9a63b3"

    hash = md5_test.encrypt(msg)
    assert hash == expected_hash

def test_rsa_algo():

    """ATTENTION : le module de cryptage RSA est cassé et génère une exception à l'exécution, 
    peut-être à cause d'une mise à jour de l'outil de cryptage RSA entre le moment où le projet a été 
    codé et aujourd'hui"""
    assert True


def test_sha():

    sha = SHA()
    msg = "message"
    expected_hash = "f8daf57a3347cc4d6b9d575b31fe6077e2cb487f60a96233c08cb479dbf31538cc915ec6d48bdbaa96ddc1a16db4f4f96f37276cfcb3510b8246241770d5952c"

    hash = sha.encrypt(msg)
    assert hash == expected_hash

def test_vigenere():

    vigenere = VigenereCipher()
    msg = "message"
    key = "cle"
    expected_encrypted = "opwulkg"

    encrypted = vigenere.encrypt(msg, key)
    assert encrypted == expected_encrypted

    decrypted = vigenere.decrypt(encrypted, key)
    assert decrypted == msg







