# Copyright 2024 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from grpc import ServicerContext
from envoy.service.ext_proc.v3 import external_processor_pb2 as service_pb2
from extproc.service import callout_server
from extproc.service import callout_tools


class CalloutServerExample(callout_server.CalloutServer):

  def on_response_headers(
      self, headers: service_pb2.HttpHeaders, context: ServicerContext
  ) -> service_pb2.HeadersResponse:
    print("headers!")
    return callout_tools.add_header_mutation(add=[('hello', 'service-extensions')])

  def on_response_body(
      self, body: service_pb2.HttpBody, context: ServicerContext
  ) -> service_pb2.BodyResponse:
    print("body!")
    return callout_tools.add_body_mutation(body='This text was provided by DEP.')


if __name__ == '__main__':
  # Run the gRPC service
  CalloutServerExample(address=('0.0.0.0', 443),
                       insecure_address=('0.0.0.0', 8080),
                       health_check_address=('0.0.0.0', 80)).run()