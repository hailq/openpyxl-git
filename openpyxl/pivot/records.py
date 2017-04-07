#Autogenerated schema
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors import (
    Typed,
    DateTime,
    Bool,
    Float,
    String,
    Integer,
)

from openpyxl.descriptors.excel import HexBinary, ExtensionList
from openpyxl.descriptors.nested import NestedInteger

from .cache import (
    Tuples,
    DateTime,
    String,
)


class Index(Serialisable):

    v = Integer()

    def __init__(self,
                 v=None,
                ):
        self.v = v

class Error(Serialisable):

    v = String()
    u = Bool()
    f = Bool()
    c = String()
    cp = Integer()
    _in = Integer(allow_none=True)
    bc = HexBinary()
    fc = HexBinary()
    i = Bool(allow_none=True)
    un = Bool(allow_none=True)
    st = Bool(allow_none=True)
    b = Bool(allow_none=True)
    tpls = Typed(expected_type=Tuples, allow_none=True)
    x = NestedInteger(allow_none=True)

    __elements__ = ('tpls', 'x')

    def __init__(self,
                 v=None,
                 u=None,
                 f=None,
                 c=None,
                 cp=None,
                 _in=None,
                 bc=None,
                 fc=None,
                 i=None,
                 un=None,
                 st=None,
                 b=None,
                 tpls=None,
                 x=None,
                ):
        self.v = v
        self.u = u
        self.f = f
        self.c = c
        self.cp = cp
        self.bc = bc
        self.fc = fc
        self.i = i
        self.un = un
        self.st = st
        self.b = b
        self.tpls = tpls
        self.x = x
        self._in = _in

class Boolean(Serialisable):

    v = Bool()
    u = Bool()
    f = Bool()
    c = String()
    cp = Integer()
    x = NestedInteger(allow_none=True)

    __elements__ = ('x',)

    def __init__(self,
                 v=None,
                 u=None,
                 f=None,
                 c=None,
                 cp=None,
                 x=None,
                ):
        self.v = v
        self.u = u
        self.f = f
        self.c = c
        self.cp = cp
        self.x = x


class Number(Serialisable):

    v = Float()
    u = Bool()
    f = Bool()
    c = String()
    cp = Integer()
    _in = Integer(allow_none=True)
    bc = HexBinary()
    fc = HexBinary()
    i = Bool(allow_none=True)
    un = Bool(allow_none=True)
    st = Bool(allow_none=True)
    b = Bool(allow_none=True)
    tpls = Typed(expected_type=Tuples, allow_none=True)
    x = NestedInteger(allow_none=True)

    __elements__ = ('tpls', 'x')

    def __init__(self,
                 v=None,
                 u=None,
                 f=None,
                 c=None,
                 cp=None,
                 _in=None,
                 bc=None,
                 fc=None,
                 i=None,
                 un=None,
                 st=None,
                 b=None,
                 tpls=None,
                 x=None,
                ):
        self.v = v
        self.u = u
        self.f = f
        self.c = c
        self.cp = cp
        self.bc = bc
        self.fc = fc
        self.i = i
        self.un = un
        self.st = st
        self.b = b
        self.tpls = tpls
        self.x = x
        self._in = _in


class Missing(Serialisable):

    u = Bool()
    f = Bool()
    c = String()
    cp = Integer()
    _in = Integer(allow_none=True)
    bc = HexBinary()
    fc = HexBinary()
    i = Bool(allow_none=True)
    un = Bool(allow_none=True)
    st = Bool(allow_none=True)
    b = Bool(allow_none=True)
    tpls = Typed(expected_type=Tuples, allow_none=True)
    x = NestedInteger(allow_none=True)

    __elements__ = ('tpls', 'x')

    def __init__(self,
                 u=None,
                 f=None,
                 c=None,
                 cp=None,
                 _in=None,
                 bc=None,
                 fc=None,
                 i=None,
                 un=None,
                 st=None,
                 b=None,
                 tpls=None,
                 x=None,
                ):
        self.u = u
        self.f = f
        self.c = c
        self.cp = cp
        self.bc = bc
        self.fc = fc
        self.i = i
        self.un = un
        self.st = st
        self.b = b
        self.tpls = tpls
        self.x = x
        self._in = _in


class Record(Serialisable):

    # some elements are choice
    m = Typed(expected_type=Missing, )
    n = Typed(expected_type=Number, )
    b = Bool(nested=True, )
    e = Typed(expected_type=Error, )
    s = Typed(expected_type=String, )
    d = Typed(expected_type=DateTime, )
    x = NestedInteger(allow_none=True)

    __elements__ = ('m', 'n', 'b', 'e', 's', 'd', 'x')

    def __init__(self,
                 m=None,
                 n=None,
                 b=None,
                 e=None,
                 s=None,
                 d=None,
                 x=None,
                ):
        self.m = m
        self.n = n
        self.b = b
        self.e = e
        self.s = s
        self.d = d
        self.x = x


class PivotCacheRecords(Serialisable):

    count = Integer()
    r = Typed(expected_type=Record, allow_none=True)
    extLst = Typed(expected_type=ExtensionList, allow_none=True)

    __elements__ = ('r', 'extLst')

    def __init__(self,
                 count=None,
                 r=None,
                 extLst=None,
                ):
        self.count = count
        self.r = r
        self.extLst = extLst
