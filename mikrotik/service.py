from librouteros import connect, exceptions
def get_api(host, username, password, port=8728):
    '''
    Connects to MikroTik RouterOS via librouteros.
    Example:
        api = get_api('192.168.88.1', 'admin', 'pass')
        add_pppoe_user(api, 'user1','pass1','default')
    '''
    return connect(host=host, username=username, password=password, port=port)
def add_pppoe_user(api, name, password, profile='default'):
    # This is a basic wrapper; adjust parameters as needed
    api('/ppp/secret/add', {'name':name, 'password':password, 'profile':profile})
def remove_pppoe_user(api, name):
    # find and remove by name
    res = api('/ppp/secret/print', {'?name': name})
    for r in res:
        api('/ppp/secret/remove', {'numbers': r['.id']})
