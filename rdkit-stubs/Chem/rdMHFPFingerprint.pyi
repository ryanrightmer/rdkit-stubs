from typing import Any, ClassVar

class MHFPEncoder:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def CreateShinglingFromMol(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def CreateShinglingFromSmiles(cls, *args, **kwargs) -> Any: ...
    def Distance(self, *args, **kwargs) -> Any: ...
    @classmethod
    def EncodeMol(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def EncodeMolsBulk(cls, RDKit, boost) -> Any: ...
    @classmethod
    def EncodeSECFPMol(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def EncodeSECFPMolsBulk(cls, RDKit, boost) -> Any: ...
    @classmethod
    def EncodeSECFPSmiles(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def EncodeSECFPSmilesBulk(cls, RDKit, boost) -> Any: ...
    @classmethod
    def EncodeSmiles(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def EncodeSmilesBulk(cls, RDKit, boost) -> Any: ...
    @classmethod
    def FromArray(cls, RDKit, boost) -> Any: ...
    @classmethod
    def FromStringArray(cls, RDKit, boost) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
