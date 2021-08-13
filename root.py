#!/usr/bin/env python3


from pynft.meta import OBJ_BASE
from typing import Any
from typeguard import check_type


class NFT_OBJ(OBJ_BASE):

	objname : str = ""


	def bake(self, other:list=None) -> str:
		i = 0
		subres = None
		tobake = other if other != None else self
		res = "[ *head ]" if (other != None) else \
			  "{ *head }" if (self.objname == "") else \
			  "{ \"" + self.objname + "\": { *head } }"

		for field in tobake._fields:
			attribute = tobake.__getattribute__(field)

			if (tobake == self):
				self.__check_attr_type(field, attribute)

			if issubclass(type(attribute), NFT_OBJ):
				subres = attribute.bake() + ", "
			elif (type(attribute) == list):
				subres = self.bake(other=attribute) + ", "
			elif (attribute != None and (tobake != self or tobake._fields[i] != "objname")):
				subres = "\"" + str(attribute) + "\", "

			if (subres != None):
				res = res[:res.index("*head")] + "\"" + self._fields[i] + "\": " + subres + res[res.index("*head"):] \
					if tobake == self else \
					res[:res.index("*head")] + subres + res[res.index("*head"):]
				subres = None

			i = i + 1

		return self.__cleanup(res)


	def __check_attr_type(self, field:str, attribute:Any) -> int:
		field_type = self.__annotations__[field]

		# print("field:\t\t\t", field)
		# print("expected type(s):\t", field_type)
		# print("attribute:\t\t", attribute)
		# print("attribute type:\t\t", type(attribute))
		# print()

		try:
			check_type(field, attribute, field_type)
		except TypeError:
			print(f"TypeError: \"{field}\" attribute is not of one of the following types:\n{field_type.__args__}\n")

		# if isinstance(field_type, _GenericAlias):
		# 	if not isinstance(attribute, field_type.__args__):
		# 		raise TypeError(f"{field} attribute must be set to an instance of one of the following types {field_type.__args__}")
		# elif isinstance(field_type, type):
		# 	if (type(attribute) != field_type):
		# 		raise TypeError(f"{field} attribute must be set to an instance of {field_type}")
		# else:
		# 	# comparing attribute type with other than instance of type or Union
		# 	raise ValueError("check_attr_type() internal error")

		return 0


	def __cleanup(self, input:str) -> str:
		res = input.replace("*head", "")
		res = res.replace(",  ]", " ]")
		res = res.replace(",  }", " }")
		res = res.replace("_0_", " ")
		res = res.replace("_1_", "-")
		res = res.replace("{  }", "\"null\"")
		return res