from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem import (
    Graphs as Graphs,
    rdMolDescriptors as rdMolDescriptors,
    rdchem as rdchem,
)
from rdkit.ML.InfoTheory import entropy as entropy

ptable: Incomplete
_log2val: Incomplete

def _VertexDegrees(mat, onlyOnes: int = ...): ...
def _NumAdjacencies(mol, dMat): ...
def _GetCountDict(arr): ...

hallKierAlphas: Incomplete

def _pyHallKierAlpha(m): ...
def Ipc(mol, avg: int = ..., dMat: Incomplete | None = ..., forceDMat: int = ...): ...
def _pyKappa1(mol): ...
def _pyKappa2(mol): ...
def _pyKappa3(mol): ...

HallKierAlpha: Incomplete
Kappa1: Incomplete
Kappa2: Incomplete
Kappa3: Incomplete

def Chi0(mol): ...
def Chi1(mol): ...
def _nVal(atom): ...
def _hkDeltas(mol, skipHs: int = ...): ...
def _pyChi0v(mol): ...
def _pyChi1v(mol): ...
def _pyChiNv_(mol, order: int = ...): ...
def _pyChi2v(mol): ...
def _pyChi3v(mol): ...
def _pyChi4v(mol): ...
def _pyChi0n(mol): ...
def _pyChi1n(mol): ...
def _pyChiNn_(mol, order: int = ...): ...
def _pyChi2n(mol): ...
def _pyChi3n(mol): ...
def _pyChi4n(mol): ...

Chi0v: Incomplete
Chi1v: Incomplete
Chi2v: Incomplete
Chi3v: Incomplete
Chi4v: Incomplete
ChiNv_: Incomplete
Chi0n: Incomplete
Chi1n: Incomplete
Chi2n: Incomplete
Chi3n: Incomplete
Chi4n: Incomplete
ChiNn_: Incomplete

def BalabanJ(mol, dMat: Incomplete | None = ..., forceDMat: int = ...): ...
def _AssignSymmetryClasses(mol, vdList, bdMat, forceBDMat, numAtoms, cutoff): ...
def _LookUpBondOrder(atom1Id, atom2Id, bondDic): ...
def _CalculateEntropies(connectionDict, atomTypeDict, numAtoms): ...
def _CreateBondDictEtc(mol, numAtoms): ...
def BertzCT(
    mol, cutoff: int = ..., dMat: Incomplete | None = ..., forceDMat: int = ...
): ...