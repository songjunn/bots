# coding: utf-8
import struct
import binascii


class Protocol(object):
    def __init__(self):
        self._headsize = 2
        self._size = 0
        self._type = 0
        self._data = ""

    def package(self, type, data):
        self._size = len(data) + 2
        self._type = type
        self._data = data

        s = struct.Struct('hh' + str(len(data)) + 's')
        v = (self._size, self._type, self._data)
        return s.pack(*v)

    def unpackage(self, data):
        # get header
        if len(data) < self._headsize:
            return False
        self._size, = struct.unpack('h', data[0:self._headsize])
        # get body
        if len(data) < self._size:
            return False
        self._type, self._data, = struct.unpack('h' + 
            str(self._size - self._headsize) + 's', data[self._headsize:self._size])
        return True

    def type(self):
        return self._type

    def size(self):
        return self._size

    def data(self):
        return self._data
