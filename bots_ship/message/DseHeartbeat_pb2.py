# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DseHeartbeat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DseHeartbeat.proto',
  package='',
  serialized_pb=_b('\n\x12\x44seHeartbeat.proto\"\x1c\n\x0c\x44seHeartbeat\x12\x0c\n\x04time\x18\x01 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSEHEARTBEAT = _descriptor.Descriptor(
  name='DseHeartbeat',
  full_name='DseHeartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='DseHeartbeat.time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=50,
)

DESCRIPTOR.message_types_by_name['DseHeartbeat'] = _DSEHEARTBEAT

DseHeartbeat = _reflection.GeneratedProtocolMessageType('DseHeartbeat', (_message.Message,), dict(
  DESCRIPTOR = _DSEHEARTBEAT,
  __module__ = 'DseHeartbeat_pb2'
  # @@protoc_insertion_point(class_scope:DseHeartbeat)
  ))
_sym_db.RegisterMessage(DseHeartbeat)


# @@protoc_insertion_point(module_scope)