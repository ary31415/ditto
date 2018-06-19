from __future__ import absolute_import, division, print_function
from builtins import super, range, zip, round, map

from .base import DiTToHasTraits, Float, Unicode, Any, Int, List, observe, Instance

from .position import Position


class Node(DiTToHasTraits):
    """Inheritance:
    Asset (self._asset)
        -> Location (self._loc)

    ConnectivityNode (self._cn)
    """

    name = Unicode(help="""Name of the node object""")
    nominal_voltage = Float(
        help="""This parameter defines the base voltage at the node.""",
        default_value=None,
    )
    phases = List(
        Instance(Unicode),
        help="""This parameter is a list of all the phases at the node.""",
    )
    positions = List(
        Instance(Position),
        help="""This parameter is a list of positional points describing the node - it should only contain one.
        The positions are objects containing elements of long, lat and elevation.""",
    )

    network_name = Unicode(
        help="""The name of the network the object is part of.""", default=None
    )

    is_subnetwork_connection = Int(
        help="""1 if the node connects from inside a subnetwork to outside, 0 otherwise.""",
        default=None,
    )

    def build(self, model, Asset=None, ConnectivityNode=None, Location=None):

        self._model = model


#        if ConnectivityNode is None:
#            self._cn = self._model.env.ConnectivityNode()
#        else:
#            self._cn = ConnectivityNode
#
#        if Asset is None:
#            self._asset = self._model.env.Asset()
#        else:
#            self._asset = Asset
#        self._asset.PowerSystemResource = self._asset.PowerSystemResource + (self._cn, )
#
#        if Location is None:
#            self._loc = self._model.env.Location()
#        else:
#            self._loc = Location
#        self._asset.Location = self._loc
#        self._loc.Assets = self._loc.Assets + (self._asset, )
#
#        self._model.model_store[self.name] = self
#
#    @observe('name', type='change')
#    def _set_name(self, bunch):
#        self._cn.name = bunch['new']
#
#    @observe('name', type='fetch')
#    def _get_name(self, bunch):
#        return self._cn.name
#
#    @observe('positions', type='change')
#    def _set_positions(self, bunch):
#        position_list = bunch['new']
#        self._loc.PositionPoints=[]
#        for position in position_list:
#            p = self._model.env.PositionPoint()
#            p.xPosition = position.long
#            p.yPosition = position.lat
#            p.zPosition = position.elevation
#            p.Location = self._loc
#            self._loc.PositionPoints = self._loc.PositionPoints + (p, )
#
#    @observe('positions', type='fetch')
#    def _get_positions(self, bunch):
#        positions = []
#        for p in self._loc.PositionPoints:
#            position = Position()
#            position.lat = p.xPosition
#            position.long = p.yPosition
#            position.elevation = p.zPosition
#            positions.append(position)
#        return positions
