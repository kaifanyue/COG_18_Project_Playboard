"""Test for my functions.

Functions in my_script are not test because they don't have specific input.
They are about operating tkinter methods.

"""

from functions import move_direction, add_lists, check_bounds, multi_two, random_coordinate, next_move
from classes import Bot, AutomaticBot, ManualBot
##
##

def test_move_direction():

    assert callable(move_direction)
    assert move_direction("Up") == [-1,0]
    assert move_direction("Left") == [0,-1]
    assert isinstance(move_direction("Left"),list)


def test_add_lists():

    assert callable(add_lists)
    assert add_lists([1,2],[3,4]) == [4,6]
    assert add_lists([-1,0],[2,4]) == [1,4]
    assert isinstance(add_lists([1,1],[2,2]),list)


def test_check_bounds():

	assert callable(check_bounds)
	assert check_bounds([1,2,3,4],5) == True
	assert check_bounds([-1,2,0],3) == False
	assert check_bounds([0,2,3],2) == False
	assert isinstance(check_bounds([1,2],2),bool)


def test_multi_two():

	assert callable(multi_two)
	assert multi_two([1,2,3]) == [2,4,6]
	assert isinstance(multi_two([1,2]),list)


def test_random_coordinate():

	assert callable(random_coordinate)
	assert isinstance(random_coordinate(2,5),list)
	assert len(random_coordinate(3,4)) == 3
	assert random_coordinate(2,5)[0][0] < 5


def test_next_move():

	assert callable(next_move)


def test_Bot():

	test = Bot(5,11,5)
	assert isinstance(test,Bot)
	assert test.last_move == None
	assert test.double_num == 5
	assert test.grid_size == 11

def test_AutomaticBot():

	test = AutomaticBot()
	assert test.move() == None
	assert isinstance(test,Bot)
	assert test.prob == 0.5


def test_ManualBot():

	test = ManualBot()
	assert isinstance(test,Bot)
	assert test.grid_size == 10               
    