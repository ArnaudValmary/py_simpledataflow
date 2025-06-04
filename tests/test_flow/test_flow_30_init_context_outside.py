import json
from typing import Any, Dict, Generator

from pysimpledataflow.flow import Flow


def __init_part_1(context: Dict) -> None:
    context['mult'] = 2


def __init_part_2(context: Dict) -> None:
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


flow_context: Dict[str, Any] = {
    'awesome_attr': 'VaLue'
}


def test_flow_30_init_context_outside() -> None:
    Flow(
        context=flow_context,
        fct_init=[
            __init_part_1,
            __init_part_2,
        ],
        fct_load=__read_data_one_by_one,
        fct_filter=__filter,
        fct_finalyze=__finalyze,
    ).run()
