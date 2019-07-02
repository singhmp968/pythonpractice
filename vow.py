x=str(input())
li=['a','e','i','o','u','A','E','I','O','U']
li2=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R',
'S','T','V','W','X','Y','Z','b','c','d','f',
    'g', 'h', 'j', 'k','l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
if x in li:
    print("Vowel")
elif x in li2:
    print("Consonant")
else:
    print("invalid")
      
