import os
import htcondor
from functools import cache

@cache
def get_schedd() -> htcondor.Schedd:
    '''
    Returns
    --------------
    Schedduler
    '''
    _collector_host = os.environ['CONDOR_COLLECTOR_HOST']
    _schedd_name    = os.environ['SCHEDD_NAME']

    _coll           = htcondor.Collector(_collector_host)
    _schedd_ad      = _coll.locate(htcondor.DaemonTypes.Schedd, _schedd_name)
    schedd          = htcondor.Schedd(_schedd_ad)

    return schedd
