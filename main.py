from base64 import b64encode, b64decode
from urllib.parse import urlparse, parse_qs, urlencode, ParseResult
import string
import random

def StringXor(str1, str2):
    res = ""
    for i in range(len(str1)):
        res += chr(ord(str1[i]) ^ ord(str2))
    return res

def EncryptUid(uid):
    RandomLetter = random.choice(string.ascii_letters)
    NewUid = RandomLetter + uid
    XoredString = RandomLetter + StringXor(NewUid, RandomLetter)

    return b64encode(XoredString.encode('utf-8'))

def DecryptUid(uid):
    DecryptedUid = b64decode(uid).decode('utf-8')
    UnxoredUId = StringXor(DecryptedUid, DecryptedUid[0])

    return UnxoredUId[2:]

def AddArg(URL, argName, uid):
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query, True)
    query[argName] = uid
    res = ParseResult(ParsedURL.scheme, ParsedURL.hostname, ParsedURL.path, ParsedURL.params, urlencode(query, doseq=True), ParsedURL.fragment)

    return res.geturl()

def GetArg(URL, argName):
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query, True)

    return query.get(argName)[0]

def RemoveArg(URL, argName):
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query, True)
    query.pop(argName)
    res = ParseResult(ParsedURL.scheme, ParsedURL.hostname, ParsedURL.path, ParsedURL.params, urlencode(query), ParsedURL.fragment)

    return res.geturl()

def DecryptUidFromURL(URL, argName):

    return DecryptUid(GetArg(URL, argName))

def EncryptUidToURL(URL, argName, uid):

    return AddArg(URL, argName, EncryptUid(uid))


if __name__ == '__main__':
    pass

