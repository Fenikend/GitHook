import requests as r
import json
import collections

def get_response(username)-> list:
    """
    _summary_
    A function to get api response after you put your username
    return response as a list.
    
    :Example:
    >>>get_response()
    Enter your github user name>>>Username
    [{"id": "00000000000","type": "PushEvent",...}]
    """
    if username=='':
        username:str = input('Enter your github user name>>>')
        username.replace(' ','')
    if username:
        base_url: str = f'https://api.github.com/users/{username}/events'
    else:
        print('wrong username')
        return None
    response: r.Response = r.get(base_url)
    if response.status_code != 200:
        print('Something went wrong')
        return None
    return response.json()

def get_events(res:list)-> dict:
    """
    _summary_
    A function to get a dict with all events, 
    take a api response as argument
    
    :Example:
    >>>get_events(git_response)
    {('Username/RepositoryName', 'PushEvent'): 1,('Username/RepositoryName', 'CreateEvent'): 2,...}
    """
    repos:dict = {}
    for data in res:
        if (data['type'],data['repo']['name']) in repos:
            repos[(data['type'],data['repo']['name'])]+=1
        else:
            repos.update({(data['type'],data['repo']['name']):1})
    repos=collections.OrderedDict(sorted(repos.items()))
    #print(repos)
    return repos

#  try to add sorting by events and/or repos later
def group_events(events: dict,repo:str=None,ev_type:str =None)->None:
    res:list = []
    """
    Print all events to every repository\n
    :Example:
    >>>print_events(events)\n
    Created new repository :"USERNAME/REPOSITORY1"\n
    Created new repository :"USERNAME/REPOSITORY2"\n
    ...\n
    """
    if repo:
        for ev in events.items():
            ...
           
    elif ev_type:
        print(f'Results by "{ev_type}"')
        for ev in events.items():
            if ev_type=='PushEvent' and 0:
                print(events[ev_type])
                
    
    else:
        ...
       
    
            

            
            
if __name__ == "__main__":
    resp: list =get_response('Fenikend')
    repos: dict =get_events(resp)  
    print(repos.items())     
    group_events(repos,ev_type='PushEvent')

    