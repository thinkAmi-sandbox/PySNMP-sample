OID_MARKER_PROCESS_COLORANTS = "1.3.6.1.2.1.43.10.2.1.6.1.1"
IP = "target ip address"
PORT = 161
SNMP_COMMUNITY = "public"


def call_hlapi():
    import pysnmp.hlapi

    g = pysnmp.hlapi.getCmd(
        pysnmp.hlapi.SnmpEngine(),
        pysnmp.hlapi.CommunityData(SNMP_COMMUNITY, mpModel=0),
        pysnmp.hlapi.UdpTransportTarget((IP, PORT)),
        pysnmp.hlapi.ContextData(),
        pysnmp.hlapi.ObjectType(pysnmp.hlapi.ObjectIdentity(OID_MARKER_PROCESS_COLORANTS))
    )
        
    errIndication, errorStatus, errorIndex, varBinds = next(g)
    
    print(varBinds)


def call_command_generator():
    from pysnmp.entity.rfc3413.oneliner import cmdgen

    cg = cmdgen.CommandGenerator()
    errIndication, errorStatus, errorIndex, varBinds = cg.getCmd(
        cmdgen.CommunityData("my-manager", SNMP_COMMUNITY, mpModel=0),
        cmdgen.UdpTransportTarget((IP, PORT)),
        OID_MARKER_PROCESS_COLORANTS
    )

    print(varBinds)



if __name__ == "__main__":
    call_hlapi()
    call_command_generator()