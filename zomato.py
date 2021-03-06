import urllib2,json,sys
import cx_Oracle 
from Insert_data import insert

class Zomato:
    
    def __init__(self,api_key,response_content_type="application/json",base_url="https://developers.zomato.com/api/v2.1/"):
        if api_key:
            self.api_key = api_key
        else:
            print("NO API KEY GIVEN.")
            return
            
        self.response_content_type = response_content_type
        self.base_url = base_url
        self.response_content_type = response_content_type
        self.all_endpoints = ["categories","cities","collections","cuisines","establishments","geocode","location_details","locations","dailymenu","restaurant","reviews","search"]
        self.endpoint_param = {
        "categories":{},

        "cities":{"q":{'type':'string'},"lat":{'type':'double'},"lon":{'type':'double'},"city_ids":{'type':'string'},"count":{'type':'integer'}},
        
        "collections":{"lat":{'type':'double'},"lon":{'type':'double'},"city_id":{'type':'integer'},"count":{'type':'integer'}},
        
        "cuisines":{"lat":{'type':'double'},"lon":{'type':'double'},"city_id":{'type':'integer'}},
        
        "establishments":{"lat":{'type':'double'},"lon":{'type':'double'},"city_id":{'type':'integer'}},
        
        "geocode":{"required":["lat","lon"],"lat":{'type':'double'},"lon":{'type':'double'}},
        
        "location_details":{"required":["entity_id","entity_type"],"entity_id":{'type':'integer'},"entity_type":{'type':'string'}},
        
        "locations":{"required":["query"],"query":{'type':'string'},"lat":{'type':'double'},"lon":{'type':'double'},"count":{'type':'integer'}},
        
        "dailymenu":{"required":["res_id"],"res_id":{'type':'integer'}},
        
        "restaurant":{"required":["res_id"],"res_id":{'type':'integer'}},
        
        "reviews":{"required":["res_id"],"res_id":{'type':'integer'},"start":{'type':'integer'},"count":{'type':'integer'}},
        
        "search":{"entity_id":{'type':'integer'},"entity_type":{'type':'string'},"start":{'type':'integer'},"count":{'type':'integer'},
        "lat":{'type':'double'},"lon":{'type':'double'},"q":{'type':'string'},"radius":{'type':'double'},"cuisines":{'type':'string'},
        "establishment_type":{'type':'string'},"collection":{'type':'string'},"order":{'type':'string'},"sort":{'type':'string'}}
        }
    
    def parse(self,endpoint,parameters=None):
        if endpoint not in self.all_endpoints:
            print("Not a valid endpoint.")
            print(self.all_endpoints)
            return
        all_parameters = ""
        parameters = parameters.replace(" ","")
        params = parameters.split(",")
        para_value = []
        for param in params:
            para_value.extend( param.split("="))
        endpoint_dict = self.endpoint_param[endpoint]
        
        if parameters:
            if "required" in endpoint_dict.keys():
                required_param_list = endpoint_dict["required"]
                if not all(required_param in para_value for required_param  in required_param_list):
                    print("Required value missing!!!")
                    return
            i = 0
            length = len(para_value)
            while i < length:
                if para_value[i] in self.endpoint_param[endpoint.lower()].keys():
                    all_parameters = all_parameters + str(para_value[i])+"="+str(para_value[i+1])+"&"
                else:
                    print("Parameter is not valid, use help to find the list of all parameter for a given endpoint.")
                    return
                i = i + 2
        else:
            if "required" in endpoint_dict.keys():
                print("Required value missing!!!!")
                return
                
        if all_parameters:
            all_parameters = all_parameters[:-1]
        self._execute(endpoint.lower(),all_parameters)
            
    def _execute(self,endpoint,parameter):
        url = self.base_url + endpoint + "?" + parameter
        print parameter
        req = urllib2.Request(url)
        if self.response_content_type == "application/json": 
            req.add_header('Accept', self.response_content_type)
            req.add_header("user_key", self.api_key) 
            try:
                res = urllib2.urlopen(req)
                
                json_data = json.load(res) 
                 
                print type(json_data['restaurants'])
                
                json_data2=json_data['restaurants']
                
                for ite in json_data2:
                 	insert(ite['restaurant']['name'],ite['restaurant']['location']['locality'],ite['restaurant']['location']['city'],ite['restaurant']['url'])

                # for ite in json_data2:
                #     print type(ite['restaurant']['location'])   
                # for ite in json_data2:
                #     print ite['restaurant']['url']
                    #print ite['restaurant']['name']
                    #insert(ite['restaurant']['name'])
                #print json_data2[0]['restaurant']['name']
                #print json.dumps(json_data, indent=4, sort_keys=True)
                
            except urllib2.HTTPError as e:
                print(str(e.code)+"\t"+e.reason)
                return
        elif self.response_content_type == "application/xml":
            req.add_header('Accept', self.response_content_type)
            req.add_header("user_key", self.api_key) 
            try:
                res = urllib2.urlopen(req)
                print(res.code())
            except urllib2.HTTPError as e:
                print(str(e.code)+"\t"+e.reason)
                return
        else:
            print("ERROR: Response content type can only be applcation/json or application/xml.")
            return
    
            
