import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_Basics(self):
        #Základní funkčnost
        Encrypted = main.EncryptUidToURL("http://www.seznam.cz", "pes", "cool")
        Decrypted = main.DecryptUidFromURL(Encrypted, "pes")
        self.assertEqual(Decrypted, "cool")
        #Při prázdné hodnotě
        Encrypted = main.EncryptUidToURL("http://www.seznam.cz", "pes", "")
        Decrypted = main.DecryptUidFromURL(Encrypted, "pes")
        self.assertEqual(Decrypted, "")

    def test_HelpingFunctions(self):
        #Přidání argumentu do URL
        URL = "https://www.zbozi.cz"
        URL = main.AddArg(URL, "pes", "super")
        self.assertEqual(URL, "https://www.zbozi.cz?pes=super")
        # Přidání sekundárního argumentu do URL
        URL = main.AddArg(URL, "kocka", "taky_super")
        self.assertEqual(URL, "https://www.zbozi.cz?pes=super&kocka=taky_super")
        # Odebrání argumentu
        URL = main.RemoveArg(URL, "pes")
        self.assertEqual(URL, "https://www.zbozi.cz?kocka=taky_super")
        # Odebrání všech argumentů
        URL = main.RemoveArg(URL, "kocka")
        self.assertEqual(URL, "https://www.zbozi.cz")
        # Zkouška chytu neexistujícího argumentu
        self.assertRaises( KeyError, lambda: main.RemoveArg(URL, "papousek"))
        URL = main.AddArg(URL, "pes", "pes_je_zpet")
        # Další test přidání nového argumentu
        self.assertEqual(URL, "https://www.zbozi.cz?pes=pes_je_zpet")
        # Získání argumentu z URL
        self.assertEqual(main.GetArg(URL , "pes"), "pes_je_zpet")
        # Zkouška chytu neexistujícího argumentu
        self.assertRaises(KeyError, lambda: main.GetArg(URL, "kocka"))
    def test_cipher(self):
        encrypted = main.EncryptUid("Jahodovy_Kolac")
        decrypted = main.DecryptUid(encrypted.decode("UTF-8"))
        # Zkouška správného dekódování
        self.assertEqual(decrypted , "Jahodovy_Kolac")
        # Zkouška, jestli nastala nějaká změna
        self.assertNotEqual(encrypted,decrypted)

if __name__ == '__main__':
    unittest.main()
