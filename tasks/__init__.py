from invoke import Collection

from . import build, dev, lint

# Naming of the variable "ns" is very important as it's
# dynamically detected
ns = Collection()
ns.add_collection(build)
ns.add_collection(lint)
ns.add_collection(dev)
