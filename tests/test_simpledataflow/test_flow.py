import os
from typing import Any, Dict, Generator, Union

from simpledataflow.flow import Flow, FlowSkipData


#
# Flow functions
#
def init_range_value(context: Dict) -> None:
    """
    Initializes a range value.

    Args:
        context (Dict): The initial context.
    """
    context['range_size'] = int(os.environ.get('range_size', 99))
    context['log_mod'] = 13
    context['nums'] = []


def read_data_one_by_one(context) -> Generator[Dict[str, int], Any, None]:
    """
    Reads data one by one.

    Args:
        context (Dict): The initial context.

    Yields:
        Dict[str, int]: A dictionary of data.
    """
    for i in range(context['range_size']):
        yield {
            'num': i,
        }


def filter_even(data: Dict, context: Dict) -> Union[Dict, None]:
    """
    Filters even numbers.

    Args:
        data (Dict): The data to filter.
        context (Dict): The initial context.

    Returns:
        Union[Dict, None]: The filtered data or None if the number is not between 5 and 8.
    """
    if (data.get('num', 0) > 5 and data.get('num', 0) < 20) or data.get('num', 0) % 5 == 0:
        raise FlowSkipData('Ignore this num %d' % data.get('num', None))
    if data.get('num', 0) % 2 == 0:
        return data


def print_data(data: Dict, context: Dict) -> None:
    """
    Prints the data.

    Args:
        data (Dict): The data to print.
    """
    print("data is: %s" % data)
    context['nums'].append(data.get('num', None))


def call_48(idx: int) -> None:
    print("CALL_48:%d" % idx)


def call_49(idx: int, context: Dict) -> None:
    print("CALL_49:%d (%s)" % (idx, context))


def call_49bis(idx: int) -> None:
    print("CALL_49BIS:%d" % (idx))


def finalyze_1() -> None:
    print('Finalyze 1')


def finalyze_2(context: Dict) -> None:
    print('Finalyze 2, context=%s' % context)


def test_run_flow() -> None:
    cur_nb_data_total: int = 0
    cur_nb_data_processed: int = 0
    cur_nb_data_skip: int = 0
    cur_nb_data_stopped_by_none: int = 0
    cur_context: Dict = {}
    (cur_nb_data_total, cur_nb_data_processed, cur_nb_data_skip, cur_nb_data_stopped_by_none) = Flow(
        fct_init=[
            init_range_value,
        ],
        fct_load=read_data_one_by_one,
        fct_filter=[
            filter_even,
            print_data,
        ],
        fct_finalyze=[
            finalyze_1,
            finalyze_2,
        ],
        continue_if_none=False,
        context=cur_context,
        log_modulo='context:log_mod',
        size_of_set='context:range_size',
        fct_modulo={
            48: call_48,
            49: [call_49, call_49bis],
        }
    ).run()

    print("End of flow")
    print("context is: %s" % cur_context)

    if cur_nb_data_total > 0:
        print(
            "nb_data_all=%d / nb_data_ok=%d (%3.2f%%) / self.nb_data_skip=%d (%3.2f%%) / nb_data_none=%d (%3.2f%%)" %
            (
                cur_nb_data_total,
                cur_nb_data_processed,
                cur_nb_data_processed * 100 / cur_nb_data_total,
                cur_nb_data_skip,
                cur_nb_data_skip * 100 / cur_nb_data_total,
                cur_nb_data_stopped_by_none,
                cur_nb_data_stopped_by_none * 100 / cur_nb_data_total
            )
        )
    else:
        print("no data")
