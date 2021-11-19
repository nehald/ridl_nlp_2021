import pdb
import sys
import string
import random
import oauth2client.contrib.multiprocess_file_storage as mfs
from oauth2client import client
from oauth2client import tools
class Flag:
    """ Flags for the flow"""
    auth_host_name = 'localhost'
    noauth_local_webserver = False
    auth_host_port = [8080, 8090]
    logging_level = 'ERROR'

class credentials(object):
    """ credential class """
    name = "cred_service"
    chars='' 
    chars += string.ascii_lowercase

    def __init__(self):
        pass

    
    def idgen(self,name):
        #return ''.join(random.choice(self.chars) for x in range(6))
        temp_name = name.replace(".","-")
        return temp_name

    def is_user(self, name):
        """ is this person a user """
        flag = -1
        if self.r.exists(name) is True:
            return 1
        return flag

    def list_users(self):
        """ list all the users"""
        users = self.r.keys()
        return ",".join(users)

    def get_new_creds(self, name):
        """ Create new credentials  """
        google_scopes = ['https://www.googleapis.com/auth/drive',
                         'https://spreadsheets.google.com/feeds']
        client_secret_file = 'desktop.json'
        application_name = 'GDrive'
        flag = Flag()
        try:
            store = mfs.MultiprocessFileStorage("creds_db", name)
            flow = client.flow_from_clientsecrets(
                client_secret_file, google_scopes)
            flow.user_agent = application_name
            credentials_ = tools.run_flow(flow, store, flag)
        except:
            print("Credentials failed\n")
            sys.exit(-1)
        return credentials_

    def get_creds(self, name):
        """ Check for the users credentials  """
        #if self.r.get(name) == None:
        #    newid = self.idgen(name)
        #    self.r.set(name,newid)
        #    self.r.set(newid,name)
        #try:
        store = mfs.MultiprocessFileStorage("creds_db", name)
        if store.get() != None:
            creds = store.get().to_json()
            return creds
        return self.get_new_creds(name).to_json()
#        except AssertionError as error:
#            print error

# pdb.set_trace()
# container = ServiceContainer(credentials,{'AMQP_URI': "pyamqp://guest:guest@localhost"})
# service_extensions = list(container.extensions)
# print service_extensions
# container.start()


if __name__ == '__main__':
    pdb.set_trace() 
    C = credentials()
    CRED_JSON = C.get_creds("getblokr@gmail.com")
    print(CRED_JSON)
