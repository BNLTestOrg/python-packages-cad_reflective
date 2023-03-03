from cad_io import rpc
from cad_io.cns import EntryType


class CNSUnpacker(rpc.Unpacker):
    def unpack_name(self):
        value = self.unpack_string().decode()
        return value

    def unpack_mapping(self):
        host = self.unpack_string().decode()
        prog = self.unpack_uint()
        vers = self.unpack_uint()
        fallback = self.unpack_bool()
        register_or_not = self.unpack_bool()
        names = [name.decode() for name in self.unpack_array(self.unpack_string)]
        return names, host, prog, vers, fallback, register_or_not


class CNSPacker(rpc.Packer):
    def pack_mapping(self, data):
        names, host, prog, vers, fallback, register_or_not = data
        # self.pack_string(name.encode("ascii"))
        self.pack_string(host.encode("ascii"))
        self.pack_uint(prog)
        self.pack_uint(vers)
        self.pack_bool(fallback)
        self.pack_bool(register_or_not)
        self.pack_array([name.encode("ascii") for name in names], self.pack_string)

    def pack_generic(self, data):
        entryType, string2, entry, value, longA, longB, string3, string4, status = data
        self.pack_enum(EntryType[entryType])
        self.pack_string(entry.encode("ascii"))
        self.pack_string(value.encode("ascii"))
        self.pack_string(string2.encode("ascii"))
        self.pack_uint(longA)
        self.pack_uint(longB)
        self.pack_uint(status)
        self.pack_string(string3.encode("ascii"))
        self.pack_string(string4.encode("ascii"))

    def pack_nothing(self):
        self.pack_enum(EntryType["NO_VALUE"])
        self.pack_string("".encode("ascii"))
        self.pack_string("".encode("ascii"))
        self.pack_string("".encode("ascii"))
        self.pack_uint(0)
        self.pack_uint(0)
        self.pack_uint(0)
        self.pack_string("".encode("ascii"))
        self.pack_string("".encode("ascii"))
