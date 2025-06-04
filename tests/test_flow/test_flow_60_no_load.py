import json
from typing import Any, Dict

from pysimpledataflow.flow import Flow


def __init_part_0() -> None:
    print("Init....")


def __init_part_1(context: Dict) -> None:
    context['mult'] = 2


def __init_part_2(context: Dict) -> None:
    context['result'] = ['a', 'b', 'c']


def __init_part_3(context: Dict) -> None:
    print("init context:%s" % json.dumps(context, indent=2))


def __finalyze_part_0(context: Dict) -> None:
    context['len_result'] = len(context['result'])


def __finalyze_part_1(context: Dict) -> None:
    context['x'] = context['len_result'] * context['mult']


def test_flow_modulo() -> None:
    context: Dict[str, Any] = {}

    Flow(
        context=context,
        fct_init=[
            __init_part_0,
            __init_part_1,
            __init_part_2,
            __init_part_3,
        ],
        fct_finalyze=[
            __finalyze_part_0,
            __finalyze_part_1,
        ]
    ).run()

    print("context=%s" % context)
