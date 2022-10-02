import random

def whatToEat():
    possible_responses = [
    'Bacon!',
    'Hamburgare!',
    'Pizza!',
    'Det som är på extrapris på Maxi.',
    'Dillkött.',
    'Pommes med bea.'
    ]

    return f'{random.choice(possible_responses)} Det är vad du borde äta till middag.'

def trailer():

    # Såg trailern för W
    whatTrailer = ['Bumblebee filmen', 'Supernatural filmen', 'Nalle Puh filmen', 'Mortal Combat and Friends', 'Fäbojäntan 2', 'Transformers, the Glorious adventure continues',
                   'Hajen 19']
    # Den stora pitchen är att den ska vara mer X,
    whatPitch = {'generation 1': 'generation 1', 'sexig': 'sexigt', 'häftig': 'häftigt',
                 'metal': 'metal', 'falukorv': 'falukorv', 'som Dennis': 'som Dennis'}
    # än Y
    thanWhat = ['föregångaren', 'Michael Bay-versionen', 'porr-parodin', 'Ernst Kirschsteiger',
                'folktandvården', 'Dennis', 'Nikes\'s gympaskor', 'en katt på en trampolin']
    # det enda som är mer X än Y är att Z
    whatMore = ['Dennis', 'Yoda', 'Bumblebee', 'Fäbojäntan', 'Dr. Snuggles',
                'Jungeldjuret Hugo', 'Kicki Danielsson', 'Ernst Kirschsteigers systedotter']
    # är Å
    whatIs = ['är en återkommande karaktär', 'käkar grapefrukt i öppningsscenen', 'åker folkvagn',
              'tror på Flat Earth', 'har en tam utter', 'luktar på falukorven innan den åker in']
    # fucking Ä är med i filmen
    fuckingThis = ['GoBots', 'Dennis', 'Avatar TAL-filmen', 'blöta papperspåsar',
                   'tandtråd', 'korvstroganoff', 'M. Nigh. Shamalamadingdong', 'Marry Poppins på LSD']

    moreThan = random.choice(list(whatPitch.keys()))
    theOriginal = random.choice(thanWhat)
    theTrailer = random.choice(whatTrailer)

    response = f'Såg trailer för {theTrailer}. Den stora pitchen är att den ska vara mer {moreThan} än {theOriginal}. DET ENDA SOM ÄR MER {whatPitch[moreThan].upper()} ÄN {theOriginal.upper()} ÄR ATT {random.choice(whatMore).upper()} {random.choice(whatIs).upper()}. FUCKING {random.choice(fuckingThis).upper()} ÄR MER {moreThan.upper()} ÄN {theOriginal.upper()}!!!'

    return str(response)

def dieRoll