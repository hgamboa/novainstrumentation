import novainstrumentation
import os
import matplotlib.pyplot as plt
from sklearn.utils.testing import assert_array_almost_equal, \
    assert_true, assert_less
from numpy import *
from novainstrumentation.code.waves import stdwave
from novainstrumentation.code.waves import waves
import random

base_dir = os.path.dirname(novainstrumentation.__file__)

HEADER_MESSAGE = "testing "
SUCCESS_MESSAGE = " function testing was successful"
ERROR_MESSAGE = " function testing was not successful"


class MessageColors:
    HEADER = '\033[34m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[32m'
    WARNING = '\033[33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test_stdwaves(show_graph=False):
    """ test_stdwaves tests if the function stdwaves in novainstrumentation.code.waves is functioning properly.
    This function makes two tests, one simple array and one higher dimension matrix. For the second test, information
    is extracted from the file xyzcal.txt, from the code directory, and compares the function output
    with the calculus of the standard deviation

    Parameters
    ----------
        show_graph - Boolean that controls whether a plot is shown with the tested signal

    Returns:
    --------
        None

    Output:
    -------
        If the function is not working properly a error message is displayed

     """
    print_test_output(stdwave.__name__, None)
    error_ = False

    # First test -> simple matrix (1xN)
    test_matrix = vstack([1, 44, 56, 78, 12])
    reference_values = std_aux_calculus(array([1, 44, 56, 78, 12]))
    test_values = stdwave(test_matrix)

    try:
        assert_array_almost_equal(test_values, reference_values, 6)
    except AssertionError as message:
        error_ = True
        print(MessageColors.WARNING, " ")
        print(message)

    # Second test -> A matrix (MxN) based on the xyzcal.txt content
    t, xcal, ycal, zcal = loadtxt(base_dir + '/code/data/xyzcal.txt')

    if show_graph:
        plt.plot(t, xcal, 'r-', t, ycal, 'b-', t, zcal, 'k-')
        plt.show()

    test_matrix = vstack([xcal, ycal, zcal])
    reference_values = std_calculus(test_matrix)
    test_values = stdwave(test_matrix)

    try:
        assert_array_almost_equal(test_values, reference_values, 6)
    except AssertionError as message:
        error_ = True
        print(MessageColors.WARNING, " ")
        print(message)
        print("\n")

    print_test_output(stdwave.__name__, not error_)


def test_waves():
    """test_waves is a function that tests the function waves in novainstrumentation.code.waves.
        This function tests if the function behaves in 7 different cases:
            1 - the segmented signals are inside the larger signal and the lower bound is negative;
            2 - the segmented signals are inside the larger signal and the lower bound is 0;
            3 - the segmented signals are inside the larger signal and the lower bound is positive;
            4 - the lower bound equals higher bound;
            5 - the lower bound is higher than the higher bound;
            6 - one of the segments has the lower bound before the first index of the signal;
            7 - one of the segments surpasses the last index of the signal
            8 - the signal is a matrix (Nx2);

    Returns:
    --------
        None

    Output:
    -------
        message regarding if the test fails or passes. If the was not successful, the number of the
        failed case is printed in console.
    """

    print_test_output(waves.__name__, None)
    error_ = False
    test_signal = array([-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0,
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    test_signal_matrix = vstack([test_signal, test_signal ** 2]).transpose()

    test_events = array([5, 10, 24])
    test_lowerbound_array = [-3, 0, 1, 1, 1, -10, 0, 0]
    test_higherbound_array = [3, 3, 3, 1, -1, 1, 10, 10]
    test_wave_result_hash = {0: array([[-11, -10, -9, -8, -7, -6],
                                       [-6, -5, -4, -3, -2, -1],
                                       [8, 9, 10, 11, 12, 13]]),
                             1: array([[-8, -7, -6],
                                       [-3, -2, -1],
                                       [11, 12, 13]]),
                             2: array([[-7, -6],
                                       [-2, -1],
                                       [12, 13]]),
                             3: array([[], [], []]),
                             4: None,
                             5: array([[-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3],
                                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]),
                             6: array([[-8, -7, -6, -5, -4, -3, -2, -1, 0, 1],
                                       [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]]),
                             7: array([vstack([[-8, -7, -6, -5, -4, -3, -2, -1, 0, 1],
                                               array(
                                                   [-8., -7., -6., -5., -4., -3., -2., -1., 0., 1.]) ** 2]).transpose(),
                                       vstack([[-3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
                                               array([-3., -2., -1., 0., 1., 2., 3., 4., 5., 6.]) ** 2]).transpose()])
                             }

    for i in range(len(test_lowerbound_array)):
        try:
            if i < 7:
                assert_array_almost_equal(waves(test_signal, test_events, test_lowerbound_array[i],
                                                test_higherbound_array[i]),
                                          test_wave_result_hash[i])
            else:
                assert_array_almost_equal(waves(test_signal_matrix, test_events, test_lowerbound_array[i],
                                                test_higherbound_array[i]),
                                          test_wave_result_hash[i])
        except AssertionError as message:
            error_ = True
            print(MessageColors.WARNING + "Error in case ", i, " :")
            print(message)
            print("")

    print_test_output(waves.__name__, not error_)


def test_getarray():
    """TODO: make a structure with several data types:
            - ok in array data with strings
            - ok in array data with ints
            - ok in array data with floats
            - not ok with other data types???"""


def std_calculus(matrix_values):
    """ Auxiliary function that calculates the standard deviation of a matrix (MxN) without the numpy.std method

    Parameters:
    -----------
        matrix_values - matrix (MxN) where M is the number of channels and N is the number of samples to whom standard
        deviation is going to be calculated

    Returns:
    --------
        If the value of M is 1 than a float with the value of the calculated standard deviation. If the value of M is
        higher than one than a matrix (1xN) will be returned, containing the values of the standard deviation values of
        each column

    """
    if len(matrix_values) > 1:
        return [std_array_calculus(matrix_values[:, i]) for i in range(len(matrix_values[1, :]))]
    else:
        return std_array_calculus(matrix_values);


def std_array_calculus(array_values):
    """ Auxiliary function that calculates the standard deviation of an array without the numpy.std method

    Parameters:
    -----------
        array_values - array to whom the standard deviation is going to be calculated

    Returns:
    --------
        Value of the calculated standard deviation.

    """
    return sqrt(mean(abs(array_values -array_values.mean()) ** 2))


def print_test_output(function_name, is_success=True):
    """ Prints the test output of the test function.

    Parameters:
    -----------
        function_name:  the string name of the function that is being tested (function_name.__name__)
        is_success (optional, default True):    boolean value that is True when the testing was successful

    Returns:
    --------
        None

    Output:
    -------
        Displays a default message when the testing has been successful or not with the
        respective blue or red text color
     """

    if is_success == None:
        print(MessageColors.HEADER + HEADER_MESSAGE + function_name + "....")
    elif is_success:
        print(MessageColors.OKGREEN + function_name + SUCCESS_MESSAGE)
    else:
        print(MessageColors.FAIL + function_name + ERROR_MESSAGE)


test_waves()
test_stdwaves()
