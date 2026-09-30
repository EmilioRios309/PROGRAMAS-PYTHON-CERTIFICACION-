full_dot = '●'
empty_dot = '○'

def create_character(name,streght,intelligence,charisma):

    if not isinstance(name,str):
        return 'The character name should be a string'
    if name is '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    if not isinstance(streght,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return 'All stats should be integers'
    if streght < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'

    if streght > 4 or intelligence > 4 or charisma > 4:
            return 'All stats should be no more than 4'

    if (streght+intelligence+charisma) != 7:
         return 'The character should start with 7 points'

    result = (f'{name}\n'
    f'STR {full_dot*streght}{empty_dot*(10 - streght)}\n'
    f'INT {full_dot*intelligence}{empty_dot*(10 - intelligence)}\n'
    f'CHA {full_dot*charisma}{empty_dot*(10 - charisma)}\n')

    return result

print(create_character('ren',4,2,1))