
from crypto_app.enigmam3_algo import EnigmaM3



# Lancez les tests avec la commande 'pytest test_algos.py'


def test_enigma():
    """
    Un exemple de fonction de test, ici avec le cryptage
    d'Enigma
    """

    enigma = EnigmaM3()
    msg = "Message"
    key = [
        ('A', 'C', 'N'),
        (2, 4, 1),
        ('F', 'H', 'K'),
        [('A', 'K')]
    ]

    encrypted = enigma.encrypt(msg, key)
    assert encrypted == "FUTALDK"
    decrypted = enigma.decrypt(encrypted, key)
    assert decrypted == "MESSAGE"



#######################################################
# AJOUTEZ VOS TESTS À LA SUITE
#######################################################