from .utils import memoized_property as memoized_property
from _typeshed import Incomplete
from rdkit import Chem as Chem

log: Incomplete

class AcidBasePair:
    name: Incomplete
    acid_str: Incomplete
    base_str: Incomplete
    def __init__(self, name, acid, base) -> None: ...
    def acid(self): ...
    def base(self): ...
    def __repr__(self): ...
    def __str__(self): ...

ACID_BASE_PAIRS: Incomplete

class ChargeCorrection:
    name: Incomplete
    smarts_str: Incomplete
    charge: Incomplete
    def __init__(self, name, smarts, charge) -> None: ...
    def smarts(self): ...
    def __repr__(self): ...
    def __str__(self): ...

CHARGE_CORRECTIONS: Incomplete

class Reionizer:
    acid_base_pairs: Incomplete
    charge_corrections: Incomplete
    def __init__(self, acid_base_pairs=..., charge_corrections=...) -> None: ...
    def __call__(self, mol): ...
    def reionize(self, mol): ...
    def _strongest_protonated(self, mol): ...
    def _weakest_ionized(self, mol): ...

class Uncharger:
    _pos_h: Incomplete
    _pos_quat: Incomplete
    _neg: Incomplete
    _neg_acid: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, mol): ...
    def uncharge(self, mol): ...