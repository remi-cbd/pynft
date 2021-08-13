# PyNFT Documentation

Welcome to PyNFT's documentation.

PyNFT is a collection of classes designed to facilitate the manipulation of NFTables in python.
It is wrapped around the JSON-NFTables python executor (python3-nftables).

The *PROTOCOL* file lists all data structures and enumeratable values used in JSON-NFTables.

NFTables documentation can be found at the end of this file.




## How it's built

> **pynft** is the name of the module.

> **NFT_OBJ** is the base class for all data structures in pynft. It contains a "bake()" method that returns itself as a JSON-NFTables compatible string.

> **CMD_OBJ** inherits from NFT_OBJ. It is the base class for command objects, which are executable with the Executor.

> **Executor** is the class that executes CMD_OBJs. It can also pretty print command outputs as well as any NFT_OBJ.




## Basic example

```python
from pynft.executor	import Executor
from pynft.objects	import RULESET
from pynft.commands	import LIST

nft = Executor()
ruleset = RULESET()
list_cmd = LIST(list=ruleset)

# print object
nft.print_obj(list_cmd)

# execute command
res = nft.execute(list_cmd)

# print command output
nft.print_cmd_output(res)
```





## NFTables references
- NFTables documentation:
	- [Ubuntu man nft(8)](http://manpages.ubuntu.com/manpages/focal/man8/nft.8.html)
	- [NFTables official wiki](https://wiki.nftables.org/wiki-nftables/index.php/Quick_reference-nftables_in_10_minutes#Extras)

- JSON-nftables documentation:
	- [Debian man libnftables-json(5)](https://manpages.debian.org/unstable/libnftables1/libnftables-json.5.en.html)
	- [libnftables-json](https://www.mankier.com/5/libnftables-json#Ruleset_Elements-Rule)

- NFTables source code:
	- [nftables.py source code](https://git.netfilter.org/nftables/tree/py/nftables.py)
