# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hetero-nn-model-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hetero-nn-model-meta.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\026HeteroNNModelMetaProto'),
  serialized_pb=_b('\n\x1ahetero-nn-model-meta.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\",\n\tOptimizer\x12\x11\n\toptimizer\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x01(\t\"!\n\x0cPredictParam\x12\x11\n\tthreshold\x18\x01 \x01(\x01\"\xb8\x02\n\x11HeteroNNModelMeta\x12\x11\n\ttask_type\x18\x01 \x01(\t\x12\x13\n\x0b\x63onfig_type\x18\x02 \x01(\t\x12\x18\n\x10\x62ottom_nn_define\x18\x03 \x03(\t\x12 \n\x18interactive_layer_define\x18\x04 \x01(\t\x12\x15\n\rtop_nn_define\x18\x05 \x03(\t\x12\x12\n\nbatch_size\x18\x06 \x01(\x05\x12\x0e\n\x06\x65pochs\x18\x07 \x01(\x05\x12\x12\n\nearly_stop\x18\x08 \x01(\t\x12\x0b\n\x03tol\x18\t \x01(\x01\x12\x0f\n\x07metrics\x18\n \x03(\t\x12\x44\n\toptimizer\x18\x0b \x01(\x0b\x32\x31.com.webank.ai.fate.core.mlmodel.buffer.Optimizer\x12\x0c\n\x04loss\x18\x0c \x01(\tB\x18\x42\x16HeteroNNModelMetaProtob\x06proto3')
)




_OPTIMIZER = _descriptor.Descriptor(
  name='Optimizer',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.Optimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='com.webank.ai.fate.core.mlmodel.buffer.Optimizer.optimizer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='com.webank.ai.fate.core.mlmodel.buffer.Optimizer.args', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=114,
)


_PREDICTPARAM = _descriptor.Descriptor(
  name='PredictParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.PredictParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='threshold', full_name='com.webank.ai.fate.core.mlmodel.buffer.PredictParam.threshold', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=149,
)


_HETERONNMODELMETA = _descriptor.Descriptor(
  name='HeteroNNModelMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_type', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.task_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config_type', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.config_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom_nn_define', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.bottom_nn_define', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interactive_layer_define', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.interactive_layer_define', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_nn_define', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.top_nn_define', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.batch_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epochs', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.epochs', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='early_stop', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.early_stop', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tol', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.tol', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.metrics', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.optimizer', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta.loss', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=464,
)

_HETERONNMODELMETA.fields_by_name['optimizer'].message_type = _OPTIMIZER
DESCRIPTOR.message_types_by_name['Optimizer'] = _OPTIMIZER
DESCRIPTOR.message_types_by_name['PredictParam'] = _PREDICTPARAM
DESCRIPTOR.message_types_by_name['HeteroNNModelMeta'] = _HETERONNMODELMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Optimizer = _reflection.GeneratedProtocolMessageType('Optimizer', (_message.Message,), dict(
  DESCRIPTOR = _OPTIMIZER,
  __module__ = 'hetero_nn_model_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.Optimizer)
  ))
_sym_db.RegisterMessage(Optimizer)

PredictParam = _reflection.GeneratedProtocolMessageType('PredictParam', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTPARAM,
  __module__ = 'hetero_nn_model_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.PredictParam)
  ))
_sym_db.RegisterMessage(PredictParam)

HeteroNNModelMeta = _reflection.GeneratedProtocolMessageType('HeteroNNModelMeta', (_message.Message,), dict(
  DESCRIPTOR = _HETERONNMODELMETA,
  __module__ = 'hetero_nn_model_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelMeta)
  ))
_sym_db.RegisterMessage(HeteroNNModelMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
