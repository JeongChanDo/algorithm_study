
def ConnectToNextPort(self, minimum):
    """connect to net port, return new minimum port"""
    if minimum <= 1024:
        raise ValueError("use port over 1025")
    port = self._FindNextOpenPort(minimum)
    if not port:
        raise ConnectionError("cannot connect to %d port" % (minimum,))
    assert port >= minimum, "unexpected %d port uses. input minimum port : %d" % (port, minimum)
    return port