from typing import Any, ClassVar

class FreeChemicalFeature:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetFamily(cls, ChemicalFeatures) -> Any: ...
    @classmethod
    def GetId(cls, ChemicalFeatures) -> Any: ...
    @classmethod
    def GetPos(cls, ChemicalFeatures) -> Any: ...
    @classmethod
    def GetType(cls, ChemicalFeatures) -> Any: ...
    @classmethod
    def SetFamily(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def SetId(cls, ChemicalFeatures, int) -> Any: ...
    @classmethod
    def SetPos(cls, ChemicalFeatures, RDGeom) -> Any: ...
    @classmethod
    def SetType(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __getinitargs__(cls, ChemicalFeatures) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
