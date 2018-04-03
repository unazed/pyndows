import json
import ctypes
import native_types


with open("structures.json") as structures:
  structures = json.load(structures)

for struct_name, data in structures.items():
  globals()[struct_name] = type(
    struct_name,
    (ctypes.Structure,),
    {"_fields_":
      [
        (
          field_name,
          getattr(ctypes, field_type)\
          if field_type in vars(ctypes) else\
          getattr(native_types, field_type)\
          if field_type in vars(native_types) else\
          None
        )\
        for field_name, field_type in data["fields"]
      ]
    }
  )

  for alias in data["aliases"]:
    if not alias.startswith('*'):
      globals()[alias] = globals()[struct_name]
      continue
    globals()[alias[1:]] = ctypes.POINTER(globals()[struct_name])

