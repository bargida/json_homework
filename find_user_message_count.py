from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: list)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
  
    messages = data['messages']
    message_count ={}

    for user_id in users_id:
        count_message_user = 0
        for message in messages:
            if message.get('from_id') == user_id:
                count_message_user += 1
            message_count[user_id] = count_message_user

    return message_count

data = read_data('./data/result.json')
users_id = find_all_users_id(data)
print(find_user_message_count(data, users_id))