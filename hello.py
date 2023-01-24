#!/usr/bin/env python3
import os,json

import pprint
print("Content-type: application/json")
print()
#print(json.dumps(dict(os.environ), indent=4))
#prettyprint.pprint(dict(os.environ))
pprint.pprint(dict(os.environ))
