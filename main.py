from urllib.parse import urlparse, parse_qs, urlencode, urlsplit, DefragResult, ParseResult


def EncryptUid(uid):
    return uid
def DecryptUid(uid):
    return uid

def AddArg(URL, argName, uid):
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query)
    query[argName] = uid
    pass
def GetArg(URL, argName):
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query)
    return query.get(argName)

def RemoveArg(URL, argName):
    ParsedURL = urlparse(URL)
    query = parse_qs(ParsedURL.query)
    query.pop(argName)
    res = ParseResult(ParsedURL.scheme, ParsedURL.hostname, ParsedURL.path, ParsedURL.params, urlencode(query), ParsedURL.fragment)
    return URL

def DecryptUidFromURL(URL, argName):
    return DecryptUid(GetArg(URL, argName, False))
def EncryptUidToURL(URL, argName, uid):
    return AddArg(URL, argName, EncryptUid(uid))


if __name__ == '__main__':

    pass

