import os
from binaryninja import PluginCommand
from binaryninja.binaryview import BinaryView
from binaryninja.typelibrary import TypeLibrary
from binaryninja.types import FunctionType, Type

type_lib = TypeLibrary.load_from_file(os.path.join(os.path.dirname(__file__), 'nodejs-napi.bntl'))

def run_plugin(bv: BinaryView):
  bv.add_type_library(type_lib)
  for _, data_var in bv.data_vars.items():
    if data_var.name is not None and data_var.name.startswith('napi_'):
        func_type: FunctionType = type_lib.get_named_object(data_var.name)
        if func_type is None:
          continue
        func_ptr = Type.pointer(bv.arch, func_type)
        data_var.type = func_ptr
        
        # if not import library object manually, other types will not be imported automatically, such as napi_env
        bv.import_library_object(data_var.name, type_lib)
         
PluginCommand.register(
  "Cesar - Import NodeAPI",
  "Import types for NodeJS N-API",
  run_plugin)
