test_settings = {
    'theme': 'dark',
    'language': 'english'
}

def add_setting(settings_dict, key_value_tuple):
    key = str(key_value_tuple[0]).lower()
    value = str(key_value_tuple[1]).lower()
    
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict, key_value_tuple):
    key = str(key_value_tuple[0]).lower()
    value = str(key_value_tuple[1]).lower()
    
    if key not in settings_dict:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings_dict[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings_dict, key):
    key = str(key).lower()
    
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"


def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    
    output = "Current User Settings:\n"
    for key, value in settings_dict.items():
        output += f"{key.capitalize()}: {value}\n"
        
    return output