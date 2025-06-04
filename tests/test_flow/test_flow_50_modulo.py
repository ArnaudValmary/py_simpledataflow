import json
from typing import Any, Dict, Generator

from pysimpledataflow.flow import Flow


def __init_part(context: Dict) -> None:
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


def __modulo_2(idx: int, context: Dict) -> None:
    print("modulo_2: idx=%s" % idx)


def __modulo_3a(idx: int) -> None:
    print("modulo_3a: idx=%s" % idx)


def __modulo_3b(idx: int) -> None:
    print("modulo_3b: idx=%s" % idx)


def test_flow_modulo() -> None:
    Flow(
        fct_init=[
            __init_part,
        ],
        fct_load=__read_data_one_by_one,
        fct_filter=__filter,
        fct_finalyze=__finalyze,
        fct_modulo={
            2: __modulo_2,
            3: [__modulo_3a, __modulo_3b],
        }
    ).run()
