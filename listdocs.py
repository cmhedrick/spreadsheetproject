import gdata.docs.service as docserv
import getpass

username = raw_input('username: ')
password = getpass.getpass('password: ')
client = docserv.DocsService()
client.ClientLogin(username, password)
documents_feed = client.GetDocumentListFeed()

for document_entry in documents_feed.entry:
    print document_entry.title.text


