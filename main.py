import traceback
import urllib2

import yaml

from auth import Auth
from mail import Email
from tfs_utils import TfsUtils

# read config files
f = open("./config/config.yaml")
config = yaml.safe_load(f)
f.close()

auth = config["auth"]
url = config["url"]

request = urllib2.Request(url["server"])
# authorize
auth_NTLM = Auth(auth["username"], auth["password"])
opener = urllib2.build_opener(auth_NTLM)
urllib2.install_opener(opener)

try:

    query = TfsUtils.find_stored_query();

    for item in query:
        id = item["item_id"]
        work_item = TfsUtils.find_work_item(id)
        TfsUtils.update_work_item(id, [])

    print id
except Exception, e:
    print Exception, ":", e
    subject = "TFS日志填写失败"
    text = "失败原因" + str(e)
    # print exception info
    traceback.print_exc()
    email = Email(config)
    email.send(subject, text)
