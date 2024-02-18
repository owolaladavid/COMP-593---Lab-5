'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'Your own developer key. will be generated by login on pastebin.com'

def post_new_paste(paste_title, paste_body, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
    # Note: This function will be written as a group
    data_info = {'api_option': 'paste', 'api_dev_key': API_DEV_KEY ,'api_paste_code':paste_body,'api_paste_name':paste_title,'api_paste_expire_date':expiration,'api_paste_private':0 if listed else 1}
    requests_new = requests.post(PASTEBIN_API_POST_URL , data=data_info)
    print("Posting new paste to pastebin....success")
    return requests_new.text
