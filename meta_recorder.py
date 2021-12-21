import email
import json
from os import listdir

with open('email_metadata.json','w+') as f:
  try: all_metadata = json.load(f)
  except json.decoder.JSONDecodeError: all_metadata = {}
  for filename in listdir('smallset'):
    with open(f'smallset/{filename}') as msg_file:
      msg_obj = email.message_from_file(msg_file)
      msg_id = msg_obj.get('Message-ID')
      if msg_id not in all_metadata:
        all_metadata[msg_id] = {
          'recipient': msg_obj.get('To'),
          'sender': msg_obj.get('From'),
          'subject': msg_obj.get('Subject'),
          'date': msg_obj.get('Date')
        }
  json.dump(all_metadata,f)
