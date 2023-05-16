#%%
import imaplib
import email
import urllib.request
from bs4 import BeautifulSoup
#%%
# Login details for your email account
imap_host = 'imap.gmail.com'
imap_user = 'margaret.schweihs@gmail.com'
imap_pass = 'pyzucmbnnueulcli'

# Connect to the IMAP server and select the inbox
imap = imaplib.IMAP4_SSL(imap_host)
imap.login(imap_user, imap_pass)
imap.select('inbox')
#%%
# Search for emails containing the Google Scholar alerts
# You can modify this search query to match your needs
status, response = imap.recent()
#%%
status, response = imap.search(None, 'FROM', 'scholaralerts-noreply@google.com')
#%%
# Loop through each email and extract the abstract text
for email_id in response[0].split():
    status, response = imap.fetch(email_id, '(RFC822)')
    email_body = response[0][1]
    mail = email.message_from_bytes(email_body)

    # Find the links to the academic papers in the email body
    links = []
    for part in mail.walk():
        if part.get_content_type() == 'text/html':
            soup = BeautifulSoup(part.get_payload(decode=True), 'html.parser')
            for link in soup.find_all('a'):
                if 'scholar.google.com/scholar?' in link.get('href'):
                    links.append(link.get('href'))

    # Loop through each link and extract the abstract text
    for link in links:
        print(link)
        #page = urllib.request.urlopen(link)
        #soup = BeautifulSoup(page, 'html.parser')
        #abstract = soup.find('div', {'id': 'abstract'}).text.strip()

        # Do something with the abstract text, such as save it to a database or file
        #print(abstract)
#%%
# Disconnect from the IMAP server
imap.close()
imap.logout()