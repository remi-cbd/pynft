#!/usr/bin/env python3

from typing import Any
from typeguard import check_type
from pynft.meta import OBJ_BASE
from pynft.exceptions import PyNFTException
from pynft.enumerations import CHAIN_PRIORITY


class NFT_OBJ(OBJ_BASE):

	objname : str = ""


	def bake(self, other:list=None):
		subres = None
		tobake = other if (other != None) else self
		res = "[ *head ]" if (other != None) else \
			  "{ *head }" if (self.objname == "") else \
			  "{ \"" + self.objname + "\": { *head } }"

		fields = tobake if (other != None) else (tobake._fields)
		for field in fields:
			attribute = field if (other != None) else (tobake.__getattribute__(field))
			subres = self.__create_subres(attribute, tobake, field)

			if (other == None):
				self.__check_attr_type(field, attribute)

			if (subres != None):
				res = self.__integrate_subres(res, subres, other, field)
				subres = None

		return self.__cleanup(res)


	def __create_subres(self, attribute, tobake, field):
		if issubclass(type(attribute), NFT_OBJ):
			return attribute.bake()
		elif (type(attribute) == list):
			return self.bake(other=attribute)
		elif (attribute != None and (tobake != self or field != "objname")):
			if issubclass(type(attribute), CHAIN_PRIORITY):
				return str(attribute)
			return "\"" + str(attribute) + "\""
		else:
			return None


	def __check_attr_type(self, field:str, attribute:Any) -> int:
		try:
			field_type = self.__annotations__[field]
			check_type(field, attribute, field_type)
		except TypeError as err:
			raise PyNFTException(-1, str(self), str(err))
		return 0


	def __integrate_subres(self, res, subres, other, field):
		head = res.index("*head")
		if (other != None):
			return (res[:head] + subres + ", " + res[head:])
		else:
			return (res[:head] + "\"" + field + "\": " + subres + ", " + res[head:])


	def __cleanup(self, input:str) -> str:
		res = input.replace("*head", "")
		res = res.replace(",  ]", " ]")
		res = res.replace(",  }", " }")
		res = res.replace("_0_", " ")
		res = res.replace("_1_", "-")
		res = res.replace("{  }", "\"null\"")
		return res