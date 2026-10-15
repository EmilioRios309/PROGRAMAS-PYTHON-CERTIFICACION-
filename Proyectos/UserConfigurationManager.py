def add_setting(settings,pairs):
    key, value = pairs
    key = str(key).lower()
    value = str(value).lower()
    if key in settings:
        return f'Setting {key} already exists! Cannot add a new setting with this name.'
    else:
        settings[key] = value
        return f'Setting [{key}] added with value {value} successfully!'


def update_settings(settings,pairs):
    key, new_value = pairs
    key = str(key).lower()
    new_value = str(new_value).lower()
    if key in settings:
        settings[key] = new_value
        return f'Setting [{key}] updated to [{new_value}] successfully!'
    else:
        return f'Setting [{key}] does not exist! Cannot update a non-existing setting.'

def delete_settings(settings,key_delete):
    pass
    key_delete = str(key_delete).lower()
    if key_delete in settings:
        delete_value = settings.pop(key_delete)
        return f'Setting [{key_delete}] deleted successfully!'
    else:
        return f'Setting not found!'

dictionary = {
    'hola':'hola',
    'adios': 'adios'
}

def view_settings(settings):
    pass
    if settings is None:
        return 'No settings available.'
    else:
        result = 'Current User Settings:\n'
        for key, value in settings.items():
            result += f'{key.capitalize()}: {value}\n'
        return result


test_settings = {'theme': 'light', 'language': 'English'}
print(add_setting(test_settings, ('THEME', 'dark')))
add_setting