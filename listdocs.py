import gdata.docs.service as docserv
import getpass

Gusername = raw_input('username: ')
Gpassword = getpass.getpass('password: ')
client = docserv.DocsService()
client.ClientLogin(Gusername, Gpassword)
documents_feed = client.GetDocumentListFeed()

for document_entry in documents_feed.entry:
    print document_entry.title.text


