import json
from typing import Any, Dict, Generator, Union

from pysimpledataflow.flow import Flow


def __init_part_1(context: Dict) -> None:
    context['mult'] = 2
    context['range_size'] = 10


def __init_part_2(context: Dict) -> None:
    context['result'] = []


def __read_data_one_by_one(context: Dict) -> Generator[Dict[str, int], Any, None]:
    for i in range(context['range_size']):
        yield {
            'num': i,
        }


def __filter_odd(data: Dict) -> Union[Dict, None]:
    if data['num'] % 2:
        return None
    return data


def __filter_change_value(data: Dict, context: Dict) -> Union[Dict, None]:
    data['num'] *= context['mult']
    return data


def __filter_change_context(data: Dict, context: Dict) -> None:
    context['result'].append(data['num'])


def __finalyze(context: Dict) -> None:
    print("final context:%s" % json.dumps(context, indent=2))


flow_context: Dict[str, Any] = {
    'awesome_attr': 'VaLue'
}


def test_flow_multi_filter_return_none() -> None:
    Flow(
        context=flow_context,
        fct_init=[
            __init_part_1,
            __init_part_2,
        ],
        fct_load=__read_data_one_by_one,
        fct_filter=[
            __filter_odd,
            __filter_change_value,
            __filter_change_context,
        ],
        fct_finalyze=__finalyze,
    ).run()
