from typing import Any, ClassVar



class HashFunction:
    AnonymousGraph: ClassVar[HashFunction] = ...
    ArthorSubstructureOrder: ClassVar[HashFunction] = ...
    AtomBondCounts: ClassVar[HashFunction] = ...
    CanonicalSmiles: ClassVar[HashFunction] = ...
    DegreeVector: ClassVar[HashFunction] = ...
    ElementGraph: ClassVar[HashFunction] = ...
    ExtendedMurcko: ClassVar[HashFunction] = ...
    HetAtomProtomer: ClassVar[HashFunction] = ...
    HetAtomTautomer: ClassVar[HashFunction] = ...
    Mesomer: ClassVar[HashFunction] = ...
    MolFormula: ClassVar[HashFunction] = ...
    MurckoScaffold: ClassVar[HashFunction] = ...
    NetCharge: ClassVar[HashFunction] = ...
    RedoxPair: ClassVar[HashFunction] = ...
    Regioisomer: ClassVar[HashFunction] = ...
    SmallWorldIndexBR: ClassVar[HashFunction] = ...
    SmallWorldIndexBRL: ClassVar[HashFunction] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

def MolHash(*args, **kwargs) -> Any: ...