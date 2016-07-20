# coding: UTF8
import json
import urllib
import urllib2

import yaml

from auth import Auth


class TfsUtils:
    def __init__(self, url, auth):
        self.work_item = url["server"] + url["find_item"]
        self.query = url["server"] + url["query"]
        self.update_item = url["server"] + url["update_item"]
        # authorize
        auth_ntlm = Auth(url["server"], auth["username"], auth["password"])
        opener = urllib2.build_opener(auth_ntlm.ntlm)
        urllib2.install_opener(opener)

    def find_work_item(self, item_id):
        request = urllib2.Request(self.work_item + str(item_id))
        result = urllib2.urlopen(request)
        decode = json.loads(result.read())
        return decode["__wrappedArray"][0]["fields"]

    def update_work_item(self, item_id, data):
        form_data = {
            'updatePackage': [{
                "id": item_id,
                "rev": 5,
                "projectId": "21ae36a6-98ee-4ba7-bba8-d036f3f3b012",
                "isDirty": True,
                "fields": data
            }],
        }
        post_data = urllib.urlencode(form_data)
        request = urllib2.Request(self.update_item, post_data)
        result = urllib2.urlopen(request)
        print result.read()

    def find_stored_query(self):
        form_data = {
            "wiql": "SELECT [System.Id] FROM WorkItems WHERE [System.TeamProject] = @project AND [System.WorkItemType] = '任务' AND [System.State] = '进行中' AND [System.IterationPath] = @currentIteration",
            "fields": "System.Id;70",
            "persistenceId": "08E20883-D56C-4461-88EB-CE77C0C7936D",
            "removeCommonTeamProject": "true",
        }
        # post request data encode
        post_data = urllib.urlencode(form_data)
        request = urllib2.Request(self.query, post_data)
        result = urllib2.urlopen(request)
        decode = json.loads(result.read())
        return decode["targetIds"]


if __name__ == "__main__":
    f = open("config.yaml")
    config = yaml.safe_load(f)
    f.close()

    tfs = TfsUtils(config["url"], config["auth"])
    print tfs.find_stored_query()
    print tfs.find_work_item("161510")

    args = {"52": "1234"}
    tfs.update_work_item("161510", args)
