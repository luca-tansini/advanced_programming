import unittest, re

def trimPunctuation(s):
    return re.sub('[.,;:\'\"?!() ]','',s)

def ispalindrome(s):
    s = trimPunctuation(s.lower())
    return s == s[::-1]

class palindrometest(unittest.TestCase):

    knownsimplevalues = {'anna':True,'xx':True,'a':True,'itopinonavevanonipoti':True,'risetovotesir':True,'mangiounpanino':False,'dogeeseseegod':True,'sonoarrivatoconlabarca':False}

    def test_known_values(self):
        for k in self.knownsimplevalues:
            self.assertEqual(self.knownsimplevalues[k],ispalindrome(k))

    knownpunctvalues = {'a n''?na':True,'x x':True,'a':True,'i topi non avevano nipoti':True,'rise to vote, sir.':True,'mangio un panino':False,'do geese see god?':True,'sono arrivato con la barca':False}

    def test_punctuation(self):
        for k in self.knownpunctvalues:
            self.assertEqual(self.knownpunctvalues[k],ispalindrome(k))

    knowntolowervalues = {'a n''?na':True,'x x':True,'a':True,'i topi non avevano nipoti':True,'Rise to vote, sir.':True,'mangio un PANINO':False,'Do geese see God?':True,'sono arrivato CON LA BARCA':False}

    def test_tolower(self):
        for k in self.knowntolowervalues:
            self.assertEqual(self.knowntolowervalues[k],ispalindrome(k))

if __name__ == '__main__':
    unittest.main()
