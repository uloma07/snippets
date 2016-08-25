#written in python 3.0
#author : Ogechi Onuoha
#Description: sign a policy document 

import base64
import hmac, hashlib

policy_document = b'''{"expiration": "2009-01-01T00:00:00Z",
  "conditions": [ 
    {"bucket": "syllabibkt"}, 
    ["starts-with", "$key", "syllabi/"],
    {"acl": "private"},
    {"success_action_redirect": "http://localhost/"},
    ["starts-with", "$Content-Type", ""]    
  ]
}'''

policy = base64.b64encode(policy_document)

secretkey = b'<enter_key_here>'

signature = base64.b64encode(hmac.new(secretkey, policy, hashlib.sha1).digest())

print(policy)
print(signature)
