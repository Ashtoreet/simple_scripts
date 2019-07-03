from lexicon import *

def tratranslation(en_full, en):
    if en_full not in lexicon:
    	return en
    else:
    	en_ru = 'En: {}, ru: {}'.format(en,lexicon[en_full])
    	return en_ru


en = ('Cap', 'Capricornus')
# en = ('Tau', 'Taurus')

print(tratranslation(en[1], en))
