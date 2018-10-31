import jnettool.tools.elements.NetworkElement
import jnettool.tools.Routing
import jnettool.tools.RouteInspector

class NetworkElementError(Exception):
    pass

class Networkelement(object):
    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.clone = jnettool.tools.elements.NetworkElement(ipaddr)

    @property
    def routing_table(self):
        try:
            return RoutingTable(self.clone.getRoutingTable())
        except jnettools.elements.MissingVar:
            raise NetworkElementError('No routing table found')

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        if exctype == NetworkElementError:
            logging.exception('No routing table found')
            self.clone.cleanup('rollback')
        else:
            self.clone.cleanup('commit')
        self.clone.disconnect()

    def __repr__(self):
        return "{} : {}".format(self.__class__.__name__, self.ipaddr)


class RoutingTable(object):
    def __init__(self, oldrt):
        self.oldrt = oldrt

    def __len__(self):
        return self.oldrt.getSize()

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        return Route(self.oldrt.getRouteByIndex(index))

class Route(object):
    def __init__(self, old_route):
        self.old_route = old_route

    @property
    def name(self):
        return self.old_route.getName()

    @property
    def ipaddr(self):
        return self.old_route.getIPAddr()