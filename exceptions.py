class PyNFTException(Exception):
    def __init__(self, rc, obj, msg):
        self.rc = rc
        self.obj = obj
        self.msg = msg