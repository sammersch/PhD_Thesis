import re, collections, regex
from MicroTopoLoadAllData import microTopoAll as m

# help(regex)

RULES = collections.OrderedDict()
    # type: typing.collections.OrderedDict[typing.Pattern[str], str]
# RULES[re.compile(r".[AEIJOUYÄÖÜ].", re.I)]    = "0"

# rules for dark vowels before ch
# RULES[re.compile(r".(UE|A|AA|OI|O|UO|OO).", re.I)]    = "9"
RULES[re.compile(r".(UE|A|O).", re.I)]    = "9"
RULES[re.compile(r".[A](CHT).", re.I)]    = r"9\2"
RULES[re.compile(r".(AA)(CHT).", re.I)]    = r"9\2"
RULES[re.compile(r".(OI)(CHT).", re.I)]    = r"9\2"
RULES[re.compile(r".[O](CHT).", re.I)]    = r"9\2"
RULES[re.compile(r".(UO)(CHT).", re.I)]    = r"9\2"
# RULES[re.compile(r".[AE][CHT].", re.I)]    = "9"

# rules for rounded back vowels
RULES[re.compile(r".[O].", re.I)]    = "0"
RULES[re.compile(r".[U][^E].", re.I)]    = "0"
RULES[re.compile(r".(OU).", re.I)]    = "0"
RULES[re.compile(r".(OH).", re.I)]    = "0"
RULES[re.compile(r".(OO).", re.I)]    = "0"

# rules for for dark back vowels
RULES[re.compile(r".[A](^CHT).", re.I)]    = "@"
RULES[re.compile(r".[Ë].", re.UNICODE)]    = "@"
RULES[re.compile(r".[E][R].", re.I)]    = "@"
RULES[re.compile(r".[E](SCH).", re.I)]    = r"@\2"
RULES[re.compile(r".[E][L].", re.I)]    = "@"
#
RULES[re.compile(r".[Ä].", re.UNICODE)]    = "?"
RULES[re.compile(r".(AE).", re.I)]    = "?"
RULES[re.compile(r".(EE).", re.I)]    = "?"
RULES[re.compile(r".(IE)(CHT).", re.I)]    = r"?\2"
RULES[re.compile(r".(IE)(RG).", re.I)]    = r"?\2"
RULES[re.compile(r".[E][^R].", re.I)]    = "?"
RULES[re.compile(r".[E](^SCH).", re.I)]    = "?"
RULES[re.compile(r".[E](^CHT).", re.I)]    = "?"
# RULES[re.compile(r".[Ë].", re.I)]    = "?"
RULES[re.compile(r".[É].", re.UNICODE)]    = "?"
RULES[re.compile(r".(ÉI).", re.UNICODE)]    = "?"
RULES[re.compile(r".(OE).", re.I)]    = "?"
RULES[re.compile(r".(ÈI).", re.UNICODE)]    = "?"
RULES[re.compile(r".[È].", re.UNICODE)]    = "?"
#
RULES[re.compile(r".(IE).", re.I)]    = "¿"
RULES[re.compile(r".[I].", re.I)]    = "¿"
RULES[re.compile(r".(II).", re.I)]    = "¿"
RULES[re.compile(r".[J].", re.I)]    = "¿"
#
RULES[re.compile(r".[B].", re.I)]             = "1"
RULES[re.compile(r".[P][^H]", re.I)]          = "1"
RULES[re.compile(r".[DT][^CSZ]", re.I)]       = "2"
RULES[re.compile(r".[FVW].", re.I)]           = "3"
RULES[re.compile(r".[P][H]", re.I)]           = "3"
RULES[re.compile(r".[GKQ].", re.I)]           = "4"
RULES[re.compile(r"\s[C][AHKLOQRUX]", re.I)]  = "4"
RULES[re.compile(r"[^SZ][C][AHKOQUX]", re.I)] = "4"
RULES[re.compile(r"[^CKQ][X].", re.I)]        = "48"
RULES[re.compile(r".[L].", re.I)]             = "5"
RULES[re.compile(r".[MN].", re.I)]            = "6"
RULES[re.compile(r".[R].", re.I)]             = "7"
RULES[re.compile(r".[SZß].", re.I)]           = "8"
RULES[re.compile(r"[SZ][C].", re.I)]          = "8"
RULES[re.compile(r"\s[C][^AHKLOQRUX]", re.I)] = "8"
RULES[re.compile(r"[C][^AHKOQUX]", re.I)]     = "8"
RULES[re.compile(r".[DT][CSZ]", re.I)]        = "8"
RULES[re.compile(r"[CKQ][X].", re.I)]         = "8"

# INVALID_CHAR_PATTERN = re.compile(r"[^a-zäöüß\s]", re.I)

RULEZ = collections.OrderedDict()
RULEZ[re.compile(r".(UE|A|AA|OI|O|UO|OO)CHT.", re.I)]    = "9"
RULEZ[re.compile(r".[DT][^CSZ]", re.I)]       = "2"
RULEZ[re.compile(r"[^SZ][C][AHKOQUX]", re.I)] = "4"


def encode(inputstring):  # type: (str) -> str
    """
    encode(string inputstring) -> string
      Returns the phonetic code of given inputstring.
    """

    # remove anything except characters and whitespace
    # inputstring = INVALID_CHAR_PATTERN.sub("", inputstring)

    encoded = ""
    for i in range(len(inputstring)):
        part = inputstring[i-1 : i+2]
        if len(inputstring) == 1:
            part = " %s " % inputstring[0]
        elif i == 0:
            part = " %s" % inputstring[:2]
        elif i == len(inputstring) - 1:
            part = "%s " % inputstring[i - 1:]

        for rule, code in RULES.items():
            if rule.match(part):
                encoded += code
                break

    # remove immediately repeated occurrences of phonetic codes
    # while [v for v in RULES.values() if encoded.find(v*2) != -1]:
    #     for v in RULES.values():
    #         encoded = encoded.replace(v*2, v)

    # if encoded:
    #     encoded = encoded[0] + encoded[1:].replace("0", "")

    return encoded


encoding_dict = {'vowels': {'ue': '@',
                            'a': '@'},
                 'consonants': {'ch': 'X',
                                't': '1'}}

