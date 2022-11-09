from typing import Any, ClassVar

from typing import overload


EIGHTBITVALUE: DiscreteValueType
FOURBITVALUE: DiscreteValueType
ONEBITVALUE: DiscreteValueType
SIXTEENBITVALUE: DiscreteValueType
TWOBITVALUE: DiscreteValueType

class DiscreteValueType:
    EIGHTBITVALUE: ClassVar[DiscreteValueType] = ...
    FOURBITVALUE: ClassVar[DiscreteValueType] = ...
    ONEBITVALUE: ClassVar[DiscreteValueType] = ...
    SIXTEENBITVALUE: ClassVar[DiscreteValueType] = ...
    TWOBITVALUE: ClassVar[DiscreteValueType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class DiscreteValueVect:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetTotalVal(cls, RDKit) -> Any: ...
    @classmethod
    def GetValueType(cls, RDKit) -> Any: ...
    @classmethod
    def __add__(cls, other) -> Any: ...
    @classmethod
    def __and__(cls, other) -> Any: ...
    @classmethod
    def __getinitargs__(cls, RDKit) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def __iadd__(cls, boost, RDKit) -> Any: ...
    @classmethod
    def __isub__(cls, boost, RDKit) -> Any: ...
    @classmethod
    def __len__(cls, RDKit) -> Any: ...
    @classmethod
    def __or__(cls, other) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @classmethod
    def __setitem__(cls, index, object) -> Any: ...
    @classmethod
    def __sub__(cls, other) -> Any: ...

class ExplicitBitVect:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def FromBase64(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetBit(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumBits(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumOffBits(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumOnBits(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetOnBits(cls, ExplicitBitVect) -> Any: ...
    @classmethod
    def SetBit(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def SetBitsFromList(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def ToBase64(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def ToBinary(cls, ExplicitBitVect) -> Any: ...
    @classmethod
    def ToBitString(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def ToList(cls, ExplicitBitVect) -> Any: ...
    @classmethod
    def UnSetBit(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def UnSetBitsFromList(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __add__(cls, other) -> Any: ...
    @classmethod
    def __and__(cls, other) -> Any: ...
    @classmethod
    def __eq__(cls, other) -> Any: ...
    @classmethod
    def __getinitargs__(cls, ExplicitBitVect) -> Any: ...
    @classmethod
    def __getitem__(cls, ExplicitBitVect, int) -> Any: ...
    @classmethod
    def __iadd__(cls, boost, ExplicitBitVect) -> Any: ...
    @classmethod
    def __invert__(cls) -> Any: ...
    @classmethod
    def __len__(cls) -> Any: ...
    @classmethod
    def __ne__(cls, other) -> Any: ...
    @classmethod
    def __or__(cls, other) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @classmethod
    def __setitem__(cls, index, object) -> Any: ...
    @classmethod
    def __xor__(cls, other) -> Any: ...

class FPBReader:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetBytes(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetContainingNeighbors(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetFP(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetId(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetNumBits(cls, RDKit) -> Any: ...
    @classmethod
    def GetTanimoto(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTanimotoNeighbors(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTversky(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTverskyNeighbors(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def Init(cls, RDKit) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def __len__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class IntSparseIntVect:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetLength(cls, RDKit) -> Any: ...
    @classmethod
    def GetNonzeroElements(cls, RDKit) -> Any: ...
    @classmethod
    def GetTotalVal(cls, RDKit) -> Any: ...
    @classmethod
    def ToBinary(cls, RDKit) -> Any: ...
    @classmethod
    def ToList(cls, RDKit) -> Any: ...
    @classmethod
    def UpdateFromSequence(cls, RDKit, boost) -> Any: ...
    @classmethod
    def __add__(cls, other) -> Any: ...
    @classmethod
    def __and__(cls, other) -> Any: ...
    @classmethod
    def __eq__(cls, other) -> Any: ...
    @classmethod
    def __getinitargs__(cls, RDKit) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, int) -> Any: ...
    def __iadd__(self, RDKit) -> Any: ...
    @classmethod
    def __idiv__(cls, boost, int) -> Any: ...
    @classmethod
    def __imul__(cls, boost, int) -> Any: ...
    def __isub__(self, RDKit) -> Any: ...
    @classmethod
    def __ne__(cls, other) -> Any: ...
    @classmethod
    def __or__(cls, other) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @classmethod
    def __setitem__(cls, index, object) -> Any: ...
    @classmethod
    def __sub__(cls, other) -> Any: ...

class LongSparseIntVect:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetLength(cls, RDKit) -> Any: ...
    @classmethod
    def GetNonzeroElements(cls, RDKit) -> Any: ...
    @classmethod
    def GetTotalVal(cls, RDKit) -> Any: ...
    @classmethod
    def ToBinary(cls, RDKit) -> Any: ...
    @classmethod
    def ToList(cls, RDKit) -> Any: ...
    @classmethod
    def UpdateFromSequence(cls, RDKit, boost) -> Any: ...
    @classmethod
    def __add__(cls, other) -> Any: ...
    @classmethod
    def __and__(cls, other) -> Any: ...
    @classmethod
    def __eq__(cls, other) -> Any: ...
    @classmethod
    def __getinitargs__(cls, RDKit) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, long) -> Any: ...
    def __iadd__(self, RDKit) -> Any: ...
    @classmethod
    def __idiv__(cls, boost, int) -> Any: ...
    @classmethod
    def __imul__(cls, boost, int) -> Any: ...
    def __isub__(self, RDKit) -> Any: ...
    @classmethod
    def __ne__(cls, other) -> Any: ...
    @classmethod
    def __or__(cls, other) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @classmethod
    def __setitem__(cls, RDKit, long, int) -> Any: ...
    @classmethod
    def __sub__(cls, other) -> Any: ...

class MultiFPBReader:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def AddReader(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetContainingNeighbors(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumBits(cls, RDKit) -> Any: ...
    @classmethod
    def GetReader(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def GetTanimotoNeighbors(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTverskyNeighbors(cls, *args, **kwargs) -> Any: ...
    @overload
    @classmethod
    def Init(cls) -> Any: ...
    @overload
    @classmethod
    def Init(cls, RDKit) -> Any: ...
    @classmethod
    def __len__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SparseBitVect:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def FromBase64(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetBit(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumBits(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumOffBits(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumOnBits(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetOnBits(cls, SparseBitVect) -> Any: ...
    @classmethod
    def SetBit(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def SetBitsFromList(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def ToBase64(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def ToBinary(cls, SparseBitVect) -> Any: ...
    @classmethod
    def ToBitString(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def ToList(cls, SparseBitVect) -> Any: ...
    @classmethod
    def UnSetBit(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def UnSetBitsFromList(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __and__(cls, other) -> Any: ...
    @classmethod
    def __eq__(cls, other) -> Any: ...
    @classmethod
    def __getinitargs__(cls, SparseBitVect) -> Any: ...
    @classmethod
    def __getitem__(cls, SparseBitVect, int) -> Any: ...
    @classmethod
    def __invert__(cls) -> Any: ...
    @classmethod
    def __len__(cls) -> Any: ...
    @classmethod
    def __ne__(cls, other) -> Any: ...
    @classmethod
    def __or__(cls, other) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @classmethod
    def __setitem__(cls, index, object) -> Any: ...
    @classmethod
    def __xor__(cls, other) -> Any: ...

class UIntSparseIntVect:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetLength(cls, RDKit) -> Any: ...
    @classmethod
    def GetNonzeroElements(cls, RDKit) -> Any: ...
    @classmethod
    def GetTotalVal(cls, RDKit) -> Any: ...
    @classmethod
    def ToBinary(cls, RDKit) -> Any: ...
    @classmethod
    def ToList(cls, RDKit) -> Any: ...
    @classmethod
    def UpdateFromSequence(cls, RDKit, boost) -> Any: ...
    @classmethod
    def __add__(cls, other) -> Any: ...
    @classmethod
    def __and__(cls, other) -> Any: ...
    @classmethod
    def __eq__(cls, other) -> Any: ...
    @classmethod
    def __getinitargs__(cls, RDKit) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, unsignedint) -> Any: ...
    def __iadd__(self, RDKit) -> Any: ...
    @classmethod
    def __idiv__(cls, boost, int) -> Any: ...
    @classmethod
    def __imul__(cls, boost, int) -> Any: ...
    def __isub__(self, RDKit) -> Any: ...
    @classmethod
    def __ne__(cls, other) -> Any: ...
    @classmethod
    def __or__(cls, other) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @classmethod
    def __setitem__(cls, RDKit, unsignedint, int) -> Any: ...
    @classmethod
    def __sub__(cls, other) -> Any: ...

class ULongSparseIntVect:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetLength(cls, RDKit) -> Any: ...
    @classmethod
    def GetNonzeroElements(cls, RDKit) -> Any: ...
    @classmethod
    def GetTotalVal(cls, RDKit) -> Any: ...
    @classmethod
    def ToBinary(cls, RDKit) -> Any: ...
    @classmethod
    def ToList(cls, RDKit) -> Any: ...
    @classmethod
    def UpdateFromSequence(cls, RDKit, boost) -> Any: ...
    @classmethod
    def __add__(cls, other) -> Any: ...
    @classmethod
    def __and__(cls, other) -> Any: ...
    @classmethod
    def __eq__(cls, other) -> Any: ...
    @classmethod
    def __getinitargs__(cls, RDKit) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, unsignedlong) -> Any: ...
    def __iadd__(self, RDKit) -> Any: ...
    @classmethod
    def __idiv__(cls, boost, int) -> Any: ...
    @classmethod
    def __imul__(cls, boost, int) -> Any: ...
    def __isub__(self, RDKit) -> Any: ...
    @classmethod
    def __ne__(cls, other) -> Any: ...
    @classmethod
    def __or__(cls, other) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @classmethod
    def __setitem__(cls, RDKit, unsignedlong, int) -> Any: ...
    @classmethod
    def __sub__(cls, other) -> Any: ...

def AllBitSimilarity(*args, **kwargs) -> Any: ...
def AllProbeBitsMatch(*args, **kwargs) -> Any: ...
def AsymmetricSimilarity(*args, **kwargs) -> Any: ...
def AsymmetricSimilarityNeighbors(*args, **kwargs) -> Any: ...
def AsymmetricSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
@overload
def BitVectToBinaryText(SparseBitVect) -> Any: ...
@overload
def BitVectToBinaryText(ExplicitBitVect) -> Any: ...
@overload
def BitVectToFPSText(SparseBitVect) -> Any: ...
@overload
def BitVectToFPSText(ExplicitBitVect) -> Any: ...
@overload
def BitVectToText(SparseBitVect) -> Any: ...
@overload
def BitVectToText(ExplicitBitVect) -> Any: ...
def BraunBlanquetSimilarity(*args, **kwargs) -> Any: ...
def BraunBlanquetSimilarityNeighbors(*args, **kwargs) -> Any: ...
def BraunBlanquetSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def BulkAllBitSimilarity(*args, **kwargs) -> Any: ...
def BulkAsymmetricSimilarity(*args, **kwargs) -> Any: ...
def BulkBraunBlanquetSimilarity(*args, **kwargs) -> Any: ...
def BulkCosineSimilarity(*args, **kwargs) -> Any: ...
def BulkDiceSimilarity(RDKit, boost) -> Any: ...
def BulkKulczynskiSimilarity(*args, **kwargs) -> Any: ...
def BulkMcConnaugheySimilarity(*args, **kwargs) -> Any: ...
def BulkOnBitSimilarity(*args, **kwargs) -> Any: ...
def BulkRogotGoldbergSimilarity(*args, **kwargs) -> Any: ...
def BulkRusselSimilarity(*args, **kwargs) -> Any: ...
def BulkSokalSimilarity(*args, **kwargs) -> Any: ...
def BulkTanimotoSimilarity(RDKit, boost) -> Any: ...
def BulkTverskySimilarity(*args, **kwargs) -> Any: ...
def ComputeL1Norm(*args, **kwargs) -> Any: ...
def ConvertToExplicit(*args, **kwargs) -> Any: ...
@overload
def ConvertToNumpyArray(ExplicitBitVect, boost) -> Any: ...
@overload
def ConvertToNumpyArray(RDKit, boost) -> Any: ...
def CosineSimilarity(*args, **kwargs) -> Any: ...
def CosineSimilarityNeighbors(*args, **kwargs) -> Any: ...
def CosineSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def CreateFromBinaryText(*args, **kwargs) -> Any: ...
def CreateFromBitString(*args, **kwargs) -> Any: ...
def CreateFromFPSText(*args, **kwargs) -> Any: ...
def DiceSimilarity(*args, **kwargs) -> Any: ...
def DiceSimilarityNeighbors(*args, **kwargs) -> Any: ...
def DiceSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def FoldFingerprint(*args, **kwargs) -> Any: ...
def InitFromDaylightString(*args, **kwargs) -> Any: ...
def KulczynskiSimilarity(*args, **kwargs) -> Any: ...
def KulczynskiSimilarityNeighbors(*args, **kwargs) -> Any: ...
def KulczynskiSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def McConnaugheySimilarity(*args, **kwargs) -> Any: ...
def McConnaugheySimilarityNeighbors(*args, **kwargs) -> Any: ...
def McConnaugheySimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def NumBitsInCommon(*args, **kwargs) -> Any: ...
def OffBitProjSimilarity(*args, **kwargs) -> Any: ...
def OffBitsInCommon(*args, **kwargs) -> Any: ...
def OnBitProjSimilarity(*args, **kwargs) -> Any: ...
def OnBitSimilarity(*args, **kwargs) -> Any: ...
def OnBitsInCommon(*args, **kwargs) -> Any: ...
def RogotGoldbergSimilarity(*args, **kwargs) -> Any: ...
def RogotGoldbergSimilarityNeighbors(*args, **kwargs) -> Any: ...
def RogotGoldbergSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def RusselSimilarity(*args, **kwargs) -> Any: ...
def RusselSimilarityNeighbors(*args, **kwargs) -> Any: ...
def RusselSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def SokalSimilarity(*args, **kwargs) -> Any: ...
def SokalSimilarityNeighbors(*args, **kwargs) -> Any: ...
def SokalSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def TanimotoSimilarity(*args, **kwargs) -> Any: ...
def TanimotoSimilarityNeighbors(*args, **kwargs) -> Any: ...
def TanimotoSimilarityNeighbors_sparse(*args, **kwargs) -> Any: ...
def TverskySimilarity(*args, **kwargs) -> Any: ...