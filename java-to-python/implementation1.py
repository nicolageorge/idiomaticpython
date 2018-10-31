import jnettool.tools.elements.NetworkElement
import jnettool.tools.Routing
import jnettool.tools.RouteInspector

ne = jnettool.tools.elements.NetworkElement('127.0.0.1')

try:
    routing_table = ne.getRoutingTable()
except jnettool.tools.elements.MissingVar:
    logging.exception('no routing table found')
    ne.cleanup('rollback')
else:
    num_routes = routing_table.getSize()
    for RToffset in range(num_routes):
        route = routing_table.getRouteByIndex(RToffset)
        name = route.getName()
        ipaddr = route.getIPAddr()
        print "{0} -> {1}".format(name, ipaddr)
finally:
    ne.cleanup('commit')
    ne.disconnect()


###############################
from adapter import NetworkElement

with NetworkElement('127.0.0.1') as ne:
    for route in ne.routing_table:
        print '{} -> {}'.format(route.name, route.ipaddr)