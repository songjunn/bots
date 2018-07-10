# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DBObject.proto

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
  name='DBObject.proto',
  package='DBObj',
  serialized_pb=_b('\n\x0e\x44\x42Object.proto\x12\x05\x44\x42Obj\"\xff\x01\n\x06\x44\x42User\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0e\n\x06openid\x18\x02 \x01(\t\x12\x11\n\tlogintime\x18\x03 \x01(\t\x12\x12\n\nlogouttime\x18\x04 \x01(\t\x12\x12\n\ncreatetime\x18\x05 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x06 \x01(\x05\x12\x0c\n\x04\x61\x64\x64r\x18\x07 \x01(\t\x12\x12\n\nlastplayer\x18\x08 \x01(\x03\x12,\n\nplayerlist\x18\t \x03(\x0b\x32\x18.DBObj.DBUser.PlayerInfo\x1a<\n\nPlayerInfo\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12!\n\x04\x62\x61se\x18\x02 \x01(\x0b\x32\x13.DBObj.DBPlayerBase\"M\n\x0c\x44\x42PlayerBase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08vocation\x18\x02 \x01(\x05\x12\x0e\n\x06gender\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\"H\n\x0c\x44\x42PlayerAttr\x12\x10\n\x08goldcoin\x18\x01 \x01(\x05\x12\x12\n\nsilvercoin\x18\x02 \x01(\x05\x12\x12\n\ncoppercoin\x18\x03 \x01(\x05\"O\n\x06\x44\x42Prop\x12\x0b\n\x03iid\x18\x01 \x01(\x03\x12\x0b\n\x03tid\x18\x02 \x01(\x05\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x12\x0e\n\x06\x65xpiry\x18\x04 \x01(\x03\x12\x0c\n\x04\x62ind\x18\x05 \x01(\x08\"\xff\x01\n\x06\x44\x42Mail\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\x03\x12\x0c\n\x04read\x18\x04 \x01(\x08\x12\x0e\n\x06\x66romid\x18\x05 \x01(\x03\x12(\n\x08\x63oinlist\x18\x06 \x03(\x0b\x32\x16.DBObj.DBMail.MailCoin\x12(\n\x08proplist\x18\x07 \x03(\x0b\x32\x16.DBObj.DBMail.MailProp\x1a+\n\x08MailCoin\x12\x10\n\x08\x63urrency\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x1a&\n\x08MailProp\x12\x0b\n\x03tid\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"\xee\x01\n\x08\x44\x42Player\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x12\n\ncreatetime\x18\x02 \x01(\t\x12\x11\n\tlogintime\x18\x03 \x01(\t\x12\x12\n\nlogouttime\x18\x04 \x01(\t\x12!\n\x04\x62\x61se\x18\x05 \x01(\x0b\x32\x13.DBObj.DBPlayerBase\x12!\n\x04\x61ttr\x18\x06 \x01(\x0b\x32\x13.DBObj.DBPlayerAttr\x12\x1f\n\x08proplist\x18\x07 \x03(\x0b\x32\r.DBObj.DBProp\x12\x12\n\nfriendlist\x18\x08 \x03(\x03\x12\x1f\n\x08maillist\x18\t \x03(\x0b\x32\r.DBObj.DBMail')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DBUSER_PLAYERINFO = _descriptor.Descriptor(
  name='PlayerInfo',
  full_name='DBObj.DBUser.PlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='DBObj.DBUser.PlayerInfo.pid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base', full_name='DBObj.DBUser.PlayerInfo.base', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=221,
  serialized_end=281,
)

_DBUSER = _descriptor.Descriptor(
  name='DBUser',
  full_name='DBObj.DBUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='DBObj.DBUser.uid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='openid', full_name='DBObj.DBUser.openid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logintime', full_name='DBObj.DBUser.logintime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logouttime', full_name='DBObj.DBUser.logouttime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createtime', full_name='DBObj.DBUser.createtime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='DBObj.DBUser.channel', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='addr', full_name='DBObj.DBUser.addr', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastplayer', full_name='DBObj.DBUser.lastplayer', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playerlist', full_name='DBObj.DBUser.playerlist', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DBUSER_PLAYERINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=281,
)


_DBPLAYERBASE = _descriptor.Descriptor(
  name='DBPlayerBase',
  full_name='DBObj.DBPlayerBase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DBObj.DBPlayerBase.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocation', full_name='DBObj.DBPlayerBase.vocation', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='DBObj.DBPlayerBase.gender', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='DBObj.DBPlayerBase.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=283,
  serialized_end=360,
)


_DBPLAYERATTR = _descriptor.Descriptor(
  name='DBPlayerAttr',
  full_name='DBObj.DBPlayerAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='goldcoin', full_name='DBObj.DBPlayerAttr.goldcoin', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='silvercoin', full_name='DBObj.DBPlayerAttr.silvercoin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coppercoin', full_name='DBObj.DBPlayerAttr.coppercoin', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=362,
  serialized_end=434,
)


_DBPROP = _descriptor.Descriptor(
  name='DBProp',
  full_name='DBObj.DBProp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iid', full_name='DBObj.DBProp.iid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tid', full_name='DBObj.DBProp.tid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='DBObj.DBProp.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='DBObj.DBProp.expiry', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bind', full_name='DBObj.DBProp.bind', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=436,
  serialized_end=515,
)


_DBMAIL_MAILCOIN = _descriptor.Descriptor(
  name='MailCoin',
  full_name='DBObj.DBMail.MailCoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='DBObj.DBMail.MailCoin.currency', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='DBObj.DBMail.MailCoin.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=690,
  serialized_end=733,
)

_DBMAIL_MAILPROP = _descriptor.Descriptor(
  name='MailProp',
  full_name='DBObj.DBMail.MailProp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='DBObj.DBMail.MailProp.tid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='DBObj.DBMail.MailProp.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=735,
  serialized_end=773,
)

_DBMAIL = _descriptor.Descriptor(
  name='DBMail',
  full_name='DBObj.DBMail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='DBObj.DBMail.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='DBObj.DBMail.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='DBObj.DBMail.expiry', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read', full_name='DBObj.DBMail.read', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromid', full_name='DBObj.DBMail.fromid', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coinlist', full_name='DBObj.DBMail.coinlist', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proplist', full_name='DBObj.DBMail.proplist', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DBMAIL_MAILCOIN, _DBMAIL_MAILPROP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=773,
)


_DBPLAYER = _descriptor.Descriptor(
  name='DBPlayer',
  full_name='DBObj.DBPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='DBObj.DBPlayer.pid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createtime', full_name='DBObj.DBPlayer.createtime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logintime', full_name='DBObj.DBPlayer.logintime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logouttime', full_name='DBObj.DBPlayer.logouttime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base', full_name='DBObj.DBPlayer.base', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr', full_name='DBObj.DBPlayer.attr', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proplist', full_name='DBObj.DBPlayer.proplist', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friendlist', full_name='DBObj.DBPlayer.friendlist', index=7,
      number=8, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maillist', full_name='DBObj.DBPlayer.maillist', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=776,
  serialized_end=1014,
)

_DBUSER_PLAYERINFO.fields_by_name['base'].message_type = _DBPLAYERBASE
_DBUSER_PLAYERINFO.containing_type = _DBUSER
_DBUSER.fields_by_name['playerlist'].message_type = _DBUSER_PLAYERINFO
_DBMAIL_MAILCOIN.containing_type = _DBMAIL
_DBMAIL_MAILPROP.containing_type = _DBMAIL
_DBMAIL.fields_by_name['coinlist'].message_type = _DBMAIL_MAILCOIN
_DBMAIL.fields_by_name['proplist'].message_type = _DBMAIL_MAILPROP
_DBPLAYER.fields_by_name['base'].message_type = _DBPLAYERBASE
_DBPLAYER.fields_by_name['attr'].message_type = _DBPLAYERATTR
_DBPLAYER.fields_by_name['proplist'].message_type = _DBPROP
_DBPLAYER.fields_by_name['maillist'].message_type = _DBMAIL
DESCRIPTOR.message_types_by_name['DBUser'] = _DBUSER
DESCRIPTOR.message_types_by_name['DBPlayerBase'] = _DBPLAYERBASE
DESCRIPTOR.message_types_by_name['DBPlayerAttr'] = _DBPLAYERATTR
DESCRIPTOR.message_types_by_name['DBProp'] = _DBPROP
DESCRIPTOR.message_types_by_name['DBMail'] = _DBMAIL
DESCRIPTOR.message_types_by_name['DBPlayer'] = _DBPLAYER

DBUser = _reflection.GeneratedProtocolMessageType('DBUser', (_message.Message,), dict(

  PlayerInfo = _reflection.GeneratedProtocolMessageType('PlayerInfo', (_message.Message,), dict(
    DESCRIPTOR = _DBUSER_PLAYERINFO,
    __module__ = 'DBObject_pb2'
    # @@protoc_insertion_point(class_scope:DBObj.DBUser.PlayerInfo)
    ))
  ,
  DESCRIPTOR = _DBUSER,
  __module__ = 'DBObject_pb2'
  # @@protoc_insertion_point(class_scope:DBObj.DBUser)
  ))
_sym_db.RegisterMessage(DBUser)
_sym_db.RegisterMessage(DBUser.PlayerInfo)

DBPlayerBase = _reflection.GeneratedProtocolMessageType('DBPlayerBase', (_message.Message,), dict(
  DESCRIPTOR = _DBPLAYERBASE,
  __module__ = 'DBObject_pb2'
  # @@protoc_insertion_point(class_scope:DBObj.DBPlayerBase)
  ))
_sym_db.RegisterMessage(DBPlayerBase)

DBPlayerAttr = _reflection.GeneratedProtocolMessageType('DBPlayerAttr', (_message.Message,), dict(
  DESCRIPTOR = _DBPLAYERATTR,
  __module__ = 'DBObject_pb2'
  # @@protoc_insertion_point(class_scope:DBObj.DBPlayerAttr)
  ))
_sym_db.RegisterMessage(DBPlayerAttr)

DBProp = _reflection.GeneratedProtocolMessageType('DBProp', (_message.Message,), dict(
  DESCRIPTOR = _DBPROP,
  __module__ = 'DBObject_pb2'
  # @@protoc_insertion_point(class_scope:DBObj.DBProp)
  ))
_sym_db.RegisterMessage(DBProp)

DBMail = _reflection.GeneratedProtocolMessageType('DBMail', (_message.Message,), dict(

  MailCoin = _reflection.GeneratedProtocolMessageType('MailCoin', (_message.Message,), dict(
    DESCRIPTOR = _DBMAIL_MAILCOIN,
    __module__ = 'DBObject_pb2'
    # @@protoc_insertion_point(class_scope:DBObj.DBMail.MailCoin)
    ))
  ,

  MailProp = _reflection.GeneratedProtocolMessageType('MailProp', (_message.Message,), dict(
    DESCRIPTOR = _DBMAIL_MAILPROP,
    __module__ = 'DBObject_pb2'
    # @@protoc_insertion_point(class_scope:DBObj.DBMail.MailProp)
    ))
  ,
  DESCRIPTOR = _DBMAIL,
  __module__ = 'DBObject_pb2'
  # @@protoc_insertion_point(class_scope:DBObj.DBMail)
  ))
_sym_db.RegisterMessage(DBMail)
_sym_db.RegisterMessage(DBMail.MailCoin)
_sym_db.RegisterMessage(DBMail.MailProp)

DBPlayer = _reflection.GeneratedProtocolMessageType('DBPlayer', (_message.Message,), dict(
  DESCRIPTOR = _DBPLAYER,
  __module__ = 'DBObject_pb2'
  # @@protoc_insertion_point(class_scope:DBObj.DBPlayer)
  ))
_sym_db.RegisterMessage(DBPlayer)


# @@protoc_insertion_point(module_scope)
