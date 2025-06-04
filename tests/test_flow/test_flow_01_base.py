import json
from typing import Any, Dict, Generator

from pysimpledataflow.flow import Flow


def __init(context: Dict) -> None:
    context['mult'] = 2
    context['result'] = []


def __read_data_one_by_one(context: Dict) -> Generator[Dict[str, int], Any, None]:
    mult: int = context['mult']
    for i in range(10):
        yield {
            'num': i * mult,
        }


def __filter(data: Dict, context: Dict) -> None:
    context['result'].append(data['num'])


def __finalyze(context: Dict) -> None:
    print("final context:%s" % json.dumps(context, indent=2))


def test_flow_base() -> None:
    Flow(
        fct_init=__init,
        fct_load=__read_data_one_by_one,
        fct_filter=__filter,
        fct_finalyze=__finalyze,
    ).run()
