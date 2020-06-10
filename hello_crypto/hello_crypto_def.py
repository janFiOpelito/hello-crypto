# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A function hello world  and addition for crypto.

test coverage -> pytest -v --cov=hello_crypto --cov-report=html
"""

def hello_crypto_world():
    """ hello world crypto function

    :param : none
    :type : none

    :return: hello_crypto_world
    :rtype: string
    """
    return "hello_crypto_world"

def add_crypto(a,b):
    """ addition

    :param : a
    :type : int
    :param : b
    :type : int

    :return: a+b
    :rtype: int
    """
    return a-b
