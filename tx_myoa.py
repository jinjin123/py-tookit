import hashlib
import random
import time
import requests
import json
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry
class MyOaSign: timestr = str(int(time.time()))
    def __init__(self, appid=None, token=None, timet=timestr):
        self._appid = appid
        self._token = token
        self._timestamp = timet
        self._sn = None

        def SignToken(self):
            s = hashlib.sha256()
            pre_encode = self._timestamp + self._token + self._timestamp
            s.update(pre_encode.encode("utf-8"))
            self._sn = s.hexdigest()
            return self._sn


class RESTfulApiRequestAgent:
        host = "http://idc.esb.oa.com/demo/myoa"
        # host = "http://oss.esb.oa.com/demo/myoa"
        #host = "http://oss.esb.oa.com/S2-fldevops/myoa"
        timeout = 30
        verify = False
        headers = None
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=Retry(total=5, status_forcelist=[403,429, 500, 502, 503, 504],method_whitelist=frozenset(['GET', 'POST']))))
        request_map = {
                "create": {
                    "method": s.post,
                    "url": "/workitem/create",
                    "param_keys": [],
                    },
                "close": {
                    "method": s.post,
                    "url": "/workitem/close",
                    "param_keys": [],
                    },
                "discard": {
                    "method": s.get,
                    "url": "/workitem/discard",
                    "param_keys": [],
                    },
                "reset": {
                    "method": s.get,
                    "url": "/workitem/reset",
                    "param_keys": [],
                    },
                "approval": {
                    "method": s.get,
                    "url": "/workitem/approval",
                    "param_keys": [],

                },
        }

        def send_request(self, crud_key, kwargs):
            if crud_key not in self.request_map.keys():
                raise KeyError("Unsupported CRUD_KEY: `{this_key}` "
                        "not in {support_keys}".format(
                            this_key=crud_key,
                            support_keys=list(self.request_map.keys()))
                        )
             form_data = {}
             param_data = {}
             for k, v in kwargs.items():
                 if k in self.request_map[crud_key]["form_data_keys"]:
                     form_data[k] = v
                 elif k in self.request_map[crud_key]["param_keys"]:
                     param_data[k] = v
            kwargs["headers"] = {"signature": ,"timestamp":}
            request = self.request_map[crud_key]
            handled_form_data = {}
            handled_param_data = {}
        def insert_params_to_data(data_keys_name, data,
                          handled_data, check_seriously=False):
            #     """
            #             filter & check params
            #     """
             if check_seriously:
                    for key in data.keys():
                        if key not in request[data_keys_name]:
                            raise KeyError("'{}' not in data available keys: {}".format(
                                key, request[data_keys_name]
                            ))
                 for key in set(data.keys()) & set(request[data_keys_name]):
                    handled_data[key] = data[key]
             insert_params_to_data("form_data_keys", form_data, handled_form_data)
             insert_params_to_data("param_keys", param_data, handled_param_data)
             pre_work_item_data.append(handled_form_data)
             pre_dict["work_items"] = pre_work_item_data



        return request["method"](
                url=self.host + request["url"],
                data=json.dumps(kwargs),
                # json=kwargs,
                # params=kwargs,
                # timeout=self.timeout if not kwargs.get("timeout", None) else kwargs["timeout"],
                timeout=self.timeout,
                headers=self.headers if not kwargs.get("headers", None) else kwargs["headers"],
         )


        def unit_test(self, kwargs):
            test_res = []
            for rq_key in self.request_map.keys():
                if rq_key == "delete":
                    continue
                unit_res = {
                        "method": rq_key,
                        "result": getattr(self, rq_key)(**kwargs)
                 }
                test_res.append(unit_res)
            return test_res

        def create(self, *args, **kwargs):
            # return self.send_request("create", kwargs).json()

            return self.send_request("create", kwargs).text

        def close(self, *args, **kwargs):
            # return self.send_request("close", kwargs).json()

            return self.send_request("close", kwargs).text


if __name__ == "__main__":
        timestr = str(int(time.time()))
        sn = MyOaSign("demo", "myoatoken").SignToken()
        kwargs = {
                "headers": {"signature": sn, "timestamp": timestr, "Content-Type": "application/json"},
                "work_items": []
        }
        process_id = random.randint(10000,11000)
        tmp = {
                "category": "C23D7091B98844659D128773209BBF85",
                "handler": "v_minmmlin",
                "title": "test",
                "process_name": "test",
                "process_inst_id": str(process_id),
                "activity": "Default",
                "applicant": "v_minmmlin",
                "callback_url": "http://9.134.53.106:8888/api/myoa/callback/",
                "approval_history": [],
                "actions": [
                    {
                        "display_name": "同意",
                        "value": "1"
                        },
                    {
                        "display_name": "驳回",
                        "value": "2"
                    },
                    {
                        "display_name": "待定",
                        "value": "3"
                    }
                ]

           }
        kwargs["work_items"].append(tmp)
        print(RESTfulApiRequestAgent().create(**kwargs))
        time.sleep(5)
        kwargs = {
                "headers": {"signature": sn, "timestamp": timestr, "Content-Type": "application/json"},
                "category": "C23D7091B98844659D128773209BBF85",
                "process_name": "test",
                "process_inst_id": str(process_id)
        }
        print(RESTfulApiRequestAgent().close(**kwargs))
        time = int(time.time())
        sn = MyOaSign("demo", "myoatoken").SignToken()
        #sn = MyOaSign("S2-fldevops", "59f1d769c1e54ab1fb5445a90874ffafce02ab45be19cca3c8a2").SignToken()
        # print(sn, time)
        #myoa_callback_url="http://dosops.woa.com/api/myoa/callback/"
        #if  len(sys.argv[1]) >0 && len(sys.argv[2]) >=0:
        #    time = int(time.time())
          #sn = MyOaSign("demo","myoatoken").SignToken()
             first_arg = sys.argv[1]
             pag_arg = sys.argv[1]
        #else:
         #         print("miss arguments")
         #      print("finalstate:ERROR")
    #     print(sn)




