"""
Functions used by other modules

Written by Wayne Doyle unless otherwise noted

(C) 2019 Wayne Doyle GPLv2

"""
# Start log
help_log = logging.getLogger(__name__)

def check_param_num(param,
                    expected):
    """
    Checks if the number of items passed to a parameter match expectations

    Args:
        param (str,list): Parameter to check
        expected (int): Expected number of values in parameter

    To Do:
        Add support for pandas and numpy
    """
    err_msg='Expected {0} parameters, received {1}'
    if isinstance(param,str):
        if expected != 1:
            my_err=err_msg.format(expected,1)
            help_log.error(my_err)
            raise ValueError(my_err)
    elif isinstance(param,list):
        true_num = len(param)
        if true_num != expected:
            my_err = err_msg.format(expected,true_num)
            help_log.error(my_err)
            raise ValueError(my_err)
    else:
        my_err='Unsupported param type'
        help_log.error(my_err)
        raise ValueError(my_err)