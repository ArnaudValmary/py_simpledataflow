import json
from typing import Any, Dict, Generator

from pysimpledataflow.flow import Flow


def __read_data_one_by_one() -> Generator[Dict[str, int], Any, None]:
    for i in range(10):
        yield {
            'num': i * 2,
        }


def __filter(data: Dict, context: Dict) -> None:
    if 'result' not in context:
        context['result'] = []
    context['result'].append(data['num'])


def __finalyze(context: Dict) -> None:
    print("final context:%s" % json.dumps(context, indent=2))


def test_flow_no_init() -> None:
    Flow(
        fct_load=__read_data_one_by_one,
        fct_filter=__filter,
        fct_finalyze=__finalyze,
    ).run()
