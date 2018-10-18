notThe       :: String -> Maybe String
notThe "the" =  Nothing
notThe str   =  Just str


replaceThe :: String -> String


countTheBeforeVowel :: String -> Integer
countTheBeforeVowel str = 
	vovels = ['a', 'o', 'e', 'i', 'u', 'y']
