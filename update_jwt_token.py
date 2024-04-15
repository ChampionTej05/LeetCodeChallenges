#!/usr/bin/env python
#!/usr/bin/python3
############################################################################
# ========================================================================
# Copyright 2023 VMware, Inc. All rights reserved. VMware Confidential
# ========================================================================
###

import requests
import json
import sys
import traceback
import os

sys.path.insert(1, "/opt/avi/python/lib")
sys.path.append("/opt/avi/python/bin/portal")
os.environ["DJANGO_SETTINGS_MODULE"] = "portal.settings_full"

from api.models_albservices_config import *
from avi.infrastructure.grpc.grpc_client_portalcon import GrpcClientPortalConnector
from avi.protobuf.portalconnector_grpc_pb2_grpc import PortalConnectorServiceStub
from avi.protobuf.controller_portal_registration_pb2 import ControllerPortalAuth

def save_pulse_auth_info() :
  try:
    # for avi-pulse-test user
    refresh_token = "rAIhu4pg7mlWGP8k-RoVEXvad5FMZpag52aV9CZUh8Ot-BWLY_wUjD32LbQ_41Si"
    portal_url = ""
    # We are no longer relying on instance_url. Maintaining it as a part of legacy.
    default_instance_url = "EmptyURL"
    
    # if(len(sys.argv) >= 2) :
    #   refresh_token = sys.argv[1]
    # else : 
    #   print("Refresh token is missing in the arguments.")
    #   return
    
    portal_info = ALBServicesConfig.objects.get().protobuf(decrypt=True)
    portal_url = portal_info.portal_url
    print("Portal URL is ", portal_url)

    api_refresh_token = portal_url + "/portal/controller/auth/refresh_jwt_token/"
    dummy_access_token = "a.b.c"
    
    headers = {
      "content-type" : "application/json",
      "x-portal-csp-accesstoken" : dummy_access_token
    }

    data = {
        "jwt_token" : refresh_token
    }
    json_object = json.dumps(data)

    response = requests.post(api_refresh_token, data=json_object, headers=headers, verify=False)
    if(response.status_code == 200):
      new_access_token = response.json()['access_token']

      client = GrpcClientPortalConnector(PortalConnectorServiceStub)
      pb = ControllerPortalAuth(access_token=new_access_token,
        jwt_token=refresh_token, instance_url=default_instance_url)                                    
      client.call('SaveAuthenticationInfo', pb)
      
      print("Restored portal access token")
    else :
      print("The POST request to refresh token is failed.")
  except Exception:
    traceback.print_exc()


save_pulse_auth_info()