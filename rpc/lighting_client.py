# Copyright (c) 2024 LG Electronics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0


from rpc.device_client import DeviceClient
from google.protobuf import json_format
from lighting_service import lighting_service_pb2
import time


class LightingClient(DeviceClient):
    """
    Lighting client class for creating a device.
    """

    def __init__(self, socket_addr=None):
        """
        Initialize a Lighting client instance.

        Arguments:
            socket_addr {str} -- configuration about ip address and port
        """
        super().__init__(socket_addr)

    def get(self):
        """
        Return Lighting state.
        """
        result = self.rpcs.chip.rpc.Lighting.Get()
        reply = json_format.MessageToDict(
            result[1], lighting_service_pb2.LightingState())
        return {'status': result[0].name, 'reply': reply}

    def set(self, data):
        """
        Set Lighting state and return the result.

        Arguments:
            data {str} -- the Lighting state
        """
        arg = lighting_service_pb2.LightingState()
        json_format.ParseDict(data, arg)
        result = self.rpcs.chip.rpc.Lighting.Set(arg)
        reply = json_format.MessageToDict(result[1])
        return {'status': result[0].name, 'reply': reply}


if __name__ == '__main__':
    # This is the sample only
    client = LightingClient()
    print(client.set({"on": True, "color": {"hue": 10, "saturation": 20}}))
    time.sleep(1)
    print(client.get())
    print(client.set({"on": False, "color": {"hue": 25, "saturation": 29}}))
    time.sleep(1)
    print(client.get())