###############################################################################
##
##  Copyright (C) 2014 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import treq
from klein import Klein
from twisted.internet.defer import inlineCallbacks, returnValue

app = Klein()


@app.route('/square/submit', methods = ['POST'])
@inlineCallbacks
def square_submit(request):
   x = int(request.args.get('x', [0])[0])

   ## simulate calling out to some Web service:
   ##
   r = yield treq.get('http://www.tavendo.com/')
   content = yield r.content()
   y = len(content)

   res = x * x + y
   returnValue("{} squared plus {} is {}".format(x, y, res))



if __name__ == "__main__":
   app.run("localhost", 8080)