from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    messages = data['messages']
    total_message = 0
    for message in messages:
        if message['type']=='message':
            total_message+=1
    return total_message

data = read_data('./data/result.json')
print(find_number_of_messages(data))