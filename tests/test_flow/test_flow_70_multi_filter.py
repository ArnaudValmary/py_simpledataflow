import json
from typing import Any, Dict, Generator, Tuple, Union

from pysimpledataflow.flow import Flow


def __init_part(context: Dict) -> None:
    pass


def __read_data_one_by_one(context: Dict) -> Generator[Dict[str, int], Any, None]:
    for i in range(1, 5):
        yield {
            'num': i,
        }


def __filter_1(data: Dict) -> Union[Dict, None]:
    new_data: Dict = {
        'num': data['num']
    }
    return new_data


def __filter_2(data: Dict) -> Union[Dict, None]:
    new_data: Dict = {
        'num_chars': str(data['num'])
    }
    return new_data


def __filter_3(data: Dict) -> Union[Dict, None]:
    new_data: Dict = {
        'len': len(data['num_chars']) + int(data['num_chars'])
    }
    return new_data


def __filter_4(data: Dict) -> Union[Dict, None]:
    print('data=%s' % json.dumps(data, indent=2))
    return data


def test_flow_multi_filter_return_none() -> None:
    r: Tuple[int, int, int, int] = Flow(
        fct_init=[
            __init_part,
        ],
        fct_load=__read_data_one_by_one,
        fct_filter=[
            __filter_1,
            __filter_2,
            __filter_3,
            __filter_4,
        ]
    ).run()
    print("r=%s" % json.dumps(r, indent=2))
