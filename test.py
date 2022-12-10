import re

url = """https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBI&vehicle=23II&client=byo&paint=P0C1M&fabric=FSBJG&sa=S01LD,S0248,S0319,S0322,S0330,S0407,S0420,S0494,S04AA,S04NB,S05AC,S05AS,S05AZ,S05DM,S06AC,S06AK,S06C4,S06NX,S06U7,S09T8&date=20220705&angle=110&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=1279"""
url = re.sub("&angle=.{2}&|&angle=.{3}&|&angle=.{1}&", "&", url)
print(url)