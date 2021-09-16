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

		fields = tobake._fields if tobake == self else tobake

		for field in fields:

			attribute = field if other != None else tobake.__getattribute__(field)

			if issubclass(type(attribute), NFT_OBJ):
				subres = attribute.bake() + ", "
			elif (type(attribute) == list):
				subres = self.bake(other=attribute) + ", "
			elif (attribute != None and (tobake != self or tobake._fields[i] != "objname")):
				subres = "\"" + str(attribute) + "\", "

			if (tobake == self):
				self.__check_attr_type(field, attribute)

			if (subres != None):
				res = res[:res.index("*head")] + "\"" + field + "\": " + subres + res[res.index("*head"):] \
					if tobake == self else \
					res[:res.index("*head")] + subres + res[res.index("*head"):]
				subres = None

			i = i + 1

		return self.__cleanup(res)


	def __check_attr_type(self, field:str, attribute:Any) -> int:
		field_type = self.__annotations__[field]
		check_type(field, attribute, field_type)

		# try:
		# 	check_type(field, attribute, field_type)
		# except TypeError:
		# 	types = field_type.__args__ if isinstance(field_type, list) else field_type
		# 	print(f"TypeError: type of \"{field}\" must be one of ({types})")
		# 	exit(84)







	def __cleanup(self, input:str) -> str:
		res = input.replace("*head", "")
		res = res.replace(",  ]", " ]")
		res = res.replace(",  }", " }")
		res = res.replace("_0_", " ")
		res = res.replace("_1_", "-")
		res = res.replace("{  }", "\"null\"")
		return res