from typing import Any, ClassVar

from typing import overload

class MolChemicalFeature:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def ClearCache(cls, RDKit) -> Any: ...
    @classmethod
    def GetActiveConformer(cls, RDKit) -> Any: ...
    @classmethod
    def GetAtomIds(cls, RDKit) -> Any: ...
    @classmethod
    def GetFactory(cls, RDKit) -> Any: ...
    @classmethod
    def GetFamily(cls, RDKit) -> Any: ...
    @classmethod
    def GetId(cls, RDKit) -> Any: ...
    @classmethod
    def GetMol(cls, RDKit) -> Any: ...
    @overload
    @classmethod
    def GetPos(cls, RDKit, int) -> Any: ...
    @overload
    @classmethod
    def GetPos(cls, RDKit) -> Any: ...
    @classmethod
    def GetType(cls, RDKit) -> Any: ...
    @classmethod
    def SetActiveConformer(cls, RDKit, int) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class MolChemicalFeatureFactory:
    GetFeaturesForMol: ClassVar[function] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetFeatureDefs(cls, RDKit) -> Any: ...
    @classmethod
    def GetFeatureFamilies(cls, RDKit) -> Any: ...
    @classmethod
    def GetMolFeature(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumFeatureDefs(cls, RDKit) -> Any: ...
    @classmethod
    def GetNumMolFeatures(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

def BuildFeatureFactory(*args, **kwargs) -> Any: ...
def BuildFeatureFactoryFromString(*args, **kwargs) -> Any: ...
def GetAtomMatch(boost) -> Any: ...
