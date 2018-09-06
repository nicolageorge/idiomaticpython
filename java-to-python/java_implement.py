import jnettool.tools.elements.NetworkElement \
       jnettool.tools.Routing \
       jnettool.tools.RouteInspector

ne = jnettool.tools.elements.NetworkElement('127.0.0.1')

try:
    routing_table - ne.getRoutingTable() # fetch table

except jnettool.tools.elements.MissingVar:
    # record table fault
    logging.exception('no routing table found')
    # undo partial changes
    ne.cleanup('rollback')
else:
    num_routes = routing_table.getSize() # determine table size
    for RToffset in range(num_routes):
        route = routing_table.getRouteByIndex(RToffset)
        name = route.getName() # route name
        ipaddr = route.getIPAddr() # ip address
        print "{0} -> {1}".format(name, ipaddr) # format nicely
finally:
    ne.cleanup('commit')
    ne.disconnect()