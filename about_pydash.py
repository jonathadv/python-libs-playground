"""
The kitchen sink of Python utility libraries for doing “stuff”
 in a functional way. Based on the Lo-Dash Javascript library.

source: https://pydash.readthedocs.io/en/latest/

"""

import pydash


def test_in_arrays():
    partially_flatten = pydash.flatten([1, 2, [3, [4, 5, [6, 7]]]])
    print(f"{partially_flatten=}")

    deep_flatten = pydash.flatten_deep([1, 2, [3, [4, 5, [6, 7]]]])
    print(f"{deep_flatten=}")


def deep_path_strings():
    data = {"a": {"b": {"c": [0, 0, {"d": [0, {1: 2}]}]}}}
    data_lookup_result = pydash.get(data, "a.b.c.2.d.1.[1]")
    print(f"{data_lookup_result=}")


def method_chaining_support():
    chain_result = (
        pydash.chaining.chain([1, 2, 3, 4]).map(lambda x: x * 2).sum().value()
    )
    print(f"{chain_result=}")


if __name__ == "__main__":
    print("-" * 20)
    test_in_arrays()

    print("-" * 20)
    deep_path_strings()

    print("-" * 20)
    method_chaining_support()
