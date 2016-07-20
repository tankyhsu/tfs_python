# coding: UTF8
import traceback

import yaml

from mail import Email
from tfs_utils import TfsUtils

# read config files
f = open("config.yaml")
config = yaml.safe_load(f)
f.close()

auth = config["auth"]
url = config["url"]

try:

    tfs = TfsUtils(url, auth)
    items = tfs.find_stored_query()
    name = set()

    for item_id in items:
        work_item = tfs.find_work_item(item_id)
        if work_item["24"] not in name:
            rest_time = work_item["10000"] - 8
            used_time = work_item["10052"] + 8

            data = {
                u"10000": rest_time,
                u"10052": used_time
            }

            tfs.update_work_item(item_id, data)
            name.add(work_item["24"])

        print item_id

except Exception, e:
    # print exception info
    print Exception, ":", e
    subject = "TFS报工失败"
    text = "失败原因" + str(e)
    traceback.print_exc()
    # Email notification
    email = Email(config)
    email.send(subject, text)
