from cad_io import rpc


class CNSUnpacker(rpc.Unpacker):
    def unpack_name(self):
        value = self.unpack_string().decode()
        return value

    def unpack_mapping(self):
        name = self.unpack_string().decode()
        host = self.unpack_string().decode()
        prog = self.unpack_uint()
        vers = self.unpack_uint()
        register_or_not = self.unpack_bool()
        return name, host, prog, vers, register_or_not


class CNSPacker(rpc.Packer):
    def pack_mapping(self, data):
        name, host, prog, vers, register_or_not = data
        self.pack_string(name.encode("ascii"))
        self.pack_string(host.encode("ascii"))
        self.pack_uint(prog)
        self.pack_uint(vers)
        self.pack_bool(register_or_not)

    def pack_generic(self, data):
        entryType, string2, entry, value, longA, longB, string3, string4, status = data
        self.pack_enum(entryType)
        self.pack_string(entry.encode("ascii"))
        self.pack_string(value.encode("ascii"))
        self.pack_string(string2.encode("ascii"))
        self.pack_uint(longA)
        self.pack_uint(longB)
        self.pack_uint(status)
        self.pack_string(string3.encode("ascii"))
        self.pack_string(string4.encode("ascii"))
