from base64 import b64encode, b64decode
from urllib.parse import urlparse, parse_qs, urlencode, ParseResult
import string
import random

def StringXor(str1, char):
    """Xorne textový řetězec hodnotou znaku.

    Argumentem je řetězec a znak. U každého znaku v řetězci se provede XOR operace nad znakem.

    Vrací řetězec, kde každý znak je XORnutý s znakem z argumentu.
    """
    res = ""
    for i in range(len(str1)):
        res += chr(ord(str1[i]) ^ ord(char))
    return res

def EncryptUid(uid):
    """Šifruje řetězec pomocí algoritmu

    Na začátek řetězce se přidá náhodný znak. Celý řetězec následně projde XORem.
    Klíč se uloží na začátek nově vytvořeného řetězce.
    Následně se vrací řetězec v  Base64.

    Vrací zašifrovaný řetězec
    """
    RandomLetter = random.choice(string.ascii_letters)
    NewUid = RandomLetter + uid
    XoredString = RandomLetter + StringXor(NewUid, RandomLetter)

    return b64encode(XoredString.encode('utf-8'))

def DecryptUid(uid):
    """Dešifruje řetězec pomocí algoritmu

    Dešifruje se Base64. Z něho se vezme 1. znak, ve kterém je uložený klíč.
    Následně se řetězec XORne nad klíčem. Z dešifrovaného řetězce se odeberou první dva znaky.
    První, který obsahoval klíč, a druhý, který byl součástí algoritmu.

    Vrací dešifrovaný řetězec
    """
    DecryptedUid = b64decode(uid).decode('utf-8')
    UnxoredUId = StringXor(DecryptedUid, DecryptedUid[0])

    return UnxoredUId[2:]

def AddArg(URL, argName, uid):
    """Přída query do URL

    Počítá se s validnímy parametry.
    V URL je uložen řetězec s URL adresou.
    V argName název argumentu
    V uid hodnotu tohoto argumentu
    Pokud již argument v URL existuje, jeho hodnota se přepíše novou

    Vrací nově vzniklý URL s přidaným argumentem. Může dojít k neškodnému reformátování URL adresy.
    """
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query, True)
    query[argName] = uid
    res = ParseResult(ParsedURL.scheme, ParsedURL.hostname, ParsedURL.path, ParsedURL.params, urlencode(query, doseq=True), ParsedURL.fragment)

    return res.geturl()

def GetArg(URL, argName):
    """Najde hodnotu argumentu v URL adrese

    V URL je uložen řetězec s URL adresou.
    V argName název argumentu

    Vrací hodnotu argumentu. Pokud argument neexistuje, funkce hodí vyjímku 'KeyError'
    """
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query, True)

    return query[argName][0]

def RemoveArg(URL, argName):
    """Odebere query z URL

    Počítá se s validnímy parametry.
    V URL je uložen řetězec s URL adresou.
    V argName název argumentu
    Pokud argument neexistuje, funkce hodí vyjímku 'KeyError'

    Vrací nově vzniklý URL s odebraným argumentem. Může dojít k neškodnému reformátování URL adresy.
    """
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query, True)
    query.pop(argName)
    res = ParseResult(ParsedURL.scheme, ParsedURL.hostname, ParsedURL.path, ParsedURL.params, urlencode(query, doseq=True), ParsedURL.fragment)

    return res.geturl()

def DecryptUidFromURL(URL, argName):
    """Odšifruje query z URL adresy

    V URL je uložen řetězec s URL adresou.
    V argName název argumentu ze kterého se má extrahovat zašifrovaný parametr.

    Vrací odšifrovanou hodnotu argumentu.
    """

    return DecryptUid(GetArg(URL, argName))

def EncryptUidToURL(URL, argName, uid):
    """Zašifruje query do URL adresy

    Počítá se s validnímy parametry.
    V URL je uložen řetězec s URL adresou.
    V argName název argumentu.
    V uid hodnota argumentu k zašifrování

    Vrací URL adresu s přidaným zašifrovaným argumentem.
    """

    return AddArg(URL, argName, EncryptUid(uid))


if __name__ == '__main__':
    pass

