# coding: utf-8
import struct
import binascii
import socket

class Protocol(object):
    def __init__(self):
        self._headsize = 8
        self._size = 0
        self._flag = 127
        self._type = 0
        self._data = ""

    def package(self, type, data):
        self._type = type
        self._data = data
        self._size = self._headsize + len(data)
        s = struct.Struct('ihh' + str(len(data)) + 's')
        v = (self._size, self._flag, self._type, self._data)
        return s.pack(*v)

    def unpackage(self, data):
        # get header
        if len(data) < self._headsize:
            return False
        self._size, self._flag, self._type, = struct.unpack(
            'ihh', data[0:self._headsize])
        # get body
        if len(data) < self._size:
            return False
        self._data, = struct.unpack(
            str(self._size - self._headsize) + 's', data[self._headsize:self._size])
        return True

    def type(self):
        return self._type

    def size(self):
        return self._size

    def data(self):
        return self._data
