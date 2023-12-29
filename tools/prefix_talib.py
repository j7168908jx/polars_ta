"""
本脚本主要功能是将talib封装添加前缀
"""
import talib as _talib
from talib import abstract as _abstract

from tools.prefix import save


def codegen():
    txts = []
    for i, func_name in enumerate(_talib.get_functions()):
        """talib遍历"""
        info = _abstract.Function(func_name).info
        group = info['group']
        name = info['name']
        if group in ('Math Operators', 'Math Transform', 'Price Transform'):
            txts.append(f'from polars_ta.talib import {name}  # noqa')
        else:
            txts.append(f'from polars_ta.talib import {name} as ts_{name}  # noqa')
    return txts


if __name__ == '__main__':
    txts = codegen()
    save(txts, module='polars_ta.prefix.talib', write=True)
