# -*- coding: utf-8 -*-
"""
    IsCool-e Pynba
    ~~~~~~~~~~~~~~

    :copyright: (c) 2012 by IsCool Entertainment.
    :license: MIT, see LICENSE for more details.
"""

from six import BytesIO, PY3
from collections import namedtuple
import struct

Field = namedtuple('Field', 'tag name type rule')
fields = [
    Field(1, 'hostname', 'string', 'required'),
    Field(2, 'server_name', 'string', 'required'),
    Field(3, 'script_name', 'string', 'required'),
    Field(4, 'request_count', 'uint32', 'required'),
    Field(5, 'document_size', 'uint32', 'required'),
    Field(6, 'memory_peak', 'uint32', 'required'),
    Field(7, 'request_time', 'float', 'required'),
    Field(8, 'ru_utime', 'float', 'required'),
    Field(9, 'ru_stime', 'float', 'required'),
    Field(10, 'timer_hit_count', 'uint32', 'repeated'),
    Field(11, 'timer_value', 'float', 'repeated'),
    Field(12, 'timer_tag_count', 'uint32', 'repeated'),
    Field(13, 'timer_tag_name', 'uint32', 'repeated'),
    Field(14, 'timer_tag_value', 'uint32', 'repeated'),
    Field(15, 'dictionary', 'string', 'repeated'),
    Field(16, 'status', 'uint32', 'optional'),
    Field(17, 'memory_footprint', 'uint32', 'optional'),
    Field(18, 'requests', 'Request', 'repeated'),
    Field(19, 'schema', 'string', 'optional'),
    Field(20, 'tag_name', 'uint32', 'repeated'),
    Field(21, 'tag_value', 'uint32', 'repeated'),
]


def pack_tag(tag, wire_type):
    return (tag << 3) | wire_type


def write_uvarint(file, value):
    shifted_value = True
    while shifted_value:
        shifted_value = value >> 7
        file.write(cast(chr(
            (value & 0x7F) | (0x80 if shifted_value != 0 else 0x00))))  # noqa
        value = shifted_value


def write_float(file, value):
    packed_value = struct.pack('<f', value)
    file.write(packed_value)


def write_string(file, value):
    value = cast(value)
    write_uvarint(file, len(value))
    file.write(value)


def write_tag(file, tag, wire_type):
    write_uvarint(file, pack_tag(tag, wire_type))


def dumps(**attrs):
    file = BytesIO()

    loop = (field for field in fields if field.name in attrs)
    for field in loop:
        buffer = attrs[field.name]

        if field.rule in ('repeated',):
            values = buffer
        else:
            values = [buffer]

        for value in values:
            if field.type == 'uint32':
                wire_type = 0
                write_tag(file, field.tag, wire_type)
                write_uvarint(file, value)
                continue
            elif field.type == 'float':
                wire_type = 5
                write_tag(file, field.tag, wire_type)
                write_float(file, value)
                continue
            elif field.type == 'string':
                wire_type = 2
                write_tag(file, field.tag, wire_type)
                write_string(file, value)
                continue
            raise NotImplementedError(field)

    return file.getvalue()


if PY3:
    def cast(value):
        """Cast any value to bytes()"""
        if isinstance(value, str):
            return value.encode('utf-8')
        if not isinstance(value, bytes):
            return bytes(value, 'utf-8')
        return value
else:
    def cast(value):
        """Cast any value to bytes()"""
        if isinstance(value, unicode):
            return value.encode('utf-8')
        if not isinstance(value, str):
            return str(value)
        return value
