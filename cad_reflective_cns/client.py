import dataclasses
import os
import threading

from cad_io.cns import CNSClient, CNSData, cns_lookup

from .data import *


class ReflectiveCNSClient(CNSClient):
    """RPC object to access CNS."""

    packer: CNSPacker
    unpacker: CNSUnpacker

    def __init__(self, port=0, overrides=None):
        host = os.getenv("REFCNSHOST", "csinject02")
        super().__init__(host, 0x36666666, 5)

    def addpackers(self):
        self.packer = CNSPacker()
        self.unpacker = CNSUnpacker(b"")

    def call_3(self, name: str, host: str, prog: int, vers: int, register_or_not: bool):
        arg = name, host, prog, vers, register_or_not
        return self.make_call(
            3, arg, self.packer.pack_mapping, self.unpacker.unpack_uint
        )
