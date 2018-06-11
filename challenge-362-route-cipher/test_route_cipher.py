import pytest
from route_cipher import encod
from route_cipher import Directions

"""
Class definition for unit test parameters
"""
class RouteCipherTest:
  def  __init__(self, inp_string, dimension, direction, expected_out_string):
    self.inp_string         = inp_string
    self.dimension          = dimension
    self.direction          = direction
    self.expected_out_string = expected_out_string

"""
Objects defined for unit tests
"""
test_route_cipher__example_1 = RouteCipherTest(
  "WE ARE DISCOVERED. FLEE AT ONCE",
  (9,3),
  Directions.CLOCKWISE,
  "CEXXECNOTAEOWEAREDISLFDEREV",
  )

test_route_cipher__example_2 = RouteCipherTest(
  "why is this professor so boring omg",
  (6, 5),
  Directions.COUNTER_CLOCKWISE,
  "TSIYHWHFSNGOMGXIRORPSIEOBOROSS",
  )

test_route_cipher__example_3 = RouteCipherTest(
  "Solving challenges on r/dailyprogrammer is so much fun!!",
  (8,6),
  Directions.COUNTER_CLOCKWISE,
  "CGNIVLOSHSYMUCHFUNXXMMLEGNELLAOPERISSOAIADRNROGR",
  )

test_route_cipher__example_4 = RouteCipherTest(
  "For lunch let's have peanut-butter and bologna sandwiches",
  (4, 12),
  Directions.CLOCKWISE,
  "LHSENURBGAISEHCNNOATUPHLUFORCTVABEDOSWDALNTTEAEN",
  )

test_route_cipher__example_5 = RouteCipherTest(
  "I've even witnessed a grown man satisfy a camel",
  (9, 5),
  Directions.CLOCKWISE,
  "IGAMXXXXXXXLETRTIVEEVENWASACAYFSIONESSEDNAMNW",
  )

test_route_cipher__example_6 = RouteCipherTest(
  "Why does it say paper jam when there is no paper jam?",
  (3, 14),
  Directions.COUNTER_CLOCKWISE,
  "YHWDSSPEAHTRSPEAMXJPOIENWJPYTEOIAARMEHENAR",
  )


"""
List of all unit test inputs
"""
test_route_cipher_list = [

  (test_route_cipher__example_1.inp_string,
   test_route_cipher__example_1.dimension,
   test_route_cipher__example_1.direction,
   test_route_cipher__example_1.expected_out_string),

  # TODO Uncomment once counter clockwise is implemented

  # (test_route_cipher__example_2.inp_string,
  #  test_route_cipher__example_2.dimension,
  #  test_route_cipher__example_2.direction,
  #  test_route_cipher__example_2.expected_out_string),

  # (test_route_cipher__example_3.inp_string,
  #  test_route_cipher__example_3.dimension,
  #  test_route_cipher__example_3.direction,
  #  test_route_cipher__example_3.expected_out_string),

  (test_route_cipher__example_4.inp_string,
   test_route_cipher__example_4.dimension,
   test_route_cipher__example_4.direction,
   test_route_cipher__example_4.expected_out_string),

  (test_route_cipher__example_5.inp_string,
   test_route_cipher__example_5.dimension,
   test_route_cipher__example_5.direction,
   test_route_cipher__example_5.expected_out_string),

  # TODO Uncomment once counter clockwise is implemented

  # (test_route_cipher__example_6.inp_string,
  #  test_route_cipher__example_6.dimension,
  #  test_route_cipher__example_6.direction,
  #  test_route_cipher__example_6.expected_out_string),

]

"""
Functions to run the unit tests
"""

@pytest.mark.parametrize('inp_string, dimension, direction, expected_out_string', test_route_cipher_list)
def test_route_cipher(inp_string, dimension, direction, expected_out_string):
  actual_out_string = encod(inp_string, dimension, direction)
  assert (actual_out_string == expected_out_string)