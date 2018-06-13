import pytest
from route_cipher import encode
from route_cipher import traverse
from route_cipher import Spiral_Directions
from route_cipher import Location
from route_cipher import Traverse_Directions
from route_cipher import encode_loop

"""
Class definition for unit test parameters
"""
class RouteCipherTest:
  def  __init__(
    self,
    inp_string,
    dimension,
    direction,
    expected_out_string
    ):
    self.inp_string           = inp_string
    self.dimension            = dimension
    self.direction            = direction
    self.expected_out_string  = expected_out_string

class TraverseTest:  
  def __init__(
    self,
    encoder_array,
    start_loc,
    num_step,
    traverse_dir,
    expected_out_string
    ):
    self.encoder_array        = encoder_array
    self.start_loc            = start_loc
    self.num_step             = num_step
    self.traverse_dir         = traverse_dir
    self.expected_out_string  = expected_out_string

class EncodeLoopTest:
  def __init__(
    self, 
    encoder_array,
    start_loc,
    loop_idx,
    spiral_dir,
    expected_out_string
    ):
    self.encoder_array        = encoder_array
    self.start_loc            = start_loc
    self.loop_idx             = loop_idx
    self.spiral_dir           = spiral_dir
    self.expected_out_string  = expected_out_string

"""
Objects defined for unit tests
"""
test_route_cipher__example_1 = RouteCipherTest(
  "WE ARE DISCOVERED. FLEE AT ONCE",
  (9,3),
  Spiral_Directions.CLOCKWISE,
  "CEXXECNOTAEOWEAREDISLFDEREV",
  )

test_route_cipher__example_2 = RouteCipherTest(
  "why is this professor so boring omg",
  (6, 5),
  Spiral_Directions.COUNTER_CLOCKWISE,
  "TSIYHWHFSNGOMGXIRORPSIEOBOROSS",
  )

test_route_cipher__example_3 = RouteCipherTest(
  "Solving challenges on r/dailyprogrammer is so much fun!!",
  (8,6),
  Spiral_Directions.COUNTER_CLOCKWISE,
  "CGNIVLOSHSYMUCHFUNXXMMLEGNELLAOPERISSOAIADRNROGR",
  )

test_route_cipher__example_4 = RouteCipherTest(
  "For lunch let's have peanut-butter and bologna sandwiches",
  (4, 12),
  Spiral_Directions.CLOCKWISE,
  "LHSENURBGAISEHCNNOATUPHLUFORCTVABEDOSWDALNTTEAEN",
  )

test_route_cipher__example_5 = RouteCipherTest(
  "I've even witnessed a grown man satisfy a camel",
  (9, 5),
  Spiral_Directions.CLOCKWISE,
  "IGAMXXXXXXXLETRTIVEEVENWASACAYFSIONESSEDNAMNW",
  )

test_route_cipher__example_6 = RouteCipherTest(
  "Why does it say paper jam when there is no paper jam?",
  (3, 14),
  Spiral_Directions.COUNTER_CLOCKWISE,
  "YHWDSSPEAHTRSPEAMXJPOIENWJPYTEOIAARMEHENAR",
  )

test_traverse__down = TraverseTest(
  [['A', 'B', 'C', 'D'],
   ['E', 'F', 'G', 'H'],
   ['I', 'J', 'K', 'L'],
   ['M', 'N', 'O', 'P']],
  Location(0, 0),
  3,
  Traverse_Directions.DOWN,
  "AEI",
  )

test_traverse__right = TraverseTest(
  [['A', 'B', 'C', 'D'],
   ['E', 'F', 'G', 'H'],
   ['I', 'J', 'K', 'L'],
   ['M', 'N', 'O', 'P']],
  Location(0, 0),
  3,
  Traverse_Directions.RIGHT,
  "ABC",
  )

test_traverse__up = TraverseTest(
  [['A', 'B', 'C', 'D'],
   ['E', 'F', 'G', 'H'],
   ['I', 'J', 'K', 'L'],
   ['M', 'N', 'O', 'P']],
  Location(3, 0),
  3,
  Traverse_Directions.UP,
  "MIE",
  )

test_traverse__left = TraverseTest(
  [['A', 'B', 'C', 'D'],
   ['E', 'F', 'G', 'H'],
   ['I', 'J', 'K', 'L'],
   ['M', 'N', 'O', 'P']],
  Location(0, 3),
  3,
  Traverse_Directions.LEFT,
  "DCB",
  )

test_encode_loop__clockwise_0 = EncodeLoopTest(
  [['A', 'B', 'C', 'D'],
   ['E', 'F', 'G', 'H'],
   ['I', 'J', 'K', 'L'],
   ['M', 'N', 'O', 'P']],
  Location(0, 3),
  0,
  Spiral_Directions.CLOCKWISE,
  "DHLPONMIEABC"
  )

test_encode_loop__clockwise_1 = EncodeLoopTest(
  [['A', 'B', 'C', 'D'],
   ['E', 'F', 'G', 'H'],
   ['I', 'J', 'K', 'L'],
   ['M', 'N', 'O', 'P']],
  Location(1, 2),
  1,
  Spiral_Directions.CLOCKWISE,
  "GKJF"
  )

test_encode_loop__counter_clockwise_0 = EncodeLoopTest(
  [['A', 'B', 'C', 'D'],
   ['E', 'F', 'G', 'H'],
   ['I', 'J', 'K', 'L'],
   ['M', 'N', 'O', 'P']],
  Location(0, 3),
  0,
  Spiral_Directions.COUNTER_CLOCKWISE,
  "DCBAEIMNOPLH"
  )

test_encode_loop__counter_clockwise_1 = EncodeLoopTest(
  [['A', 'B', 'C', 'D'],
   ['E', 'F', 'G', 'H'],
   ['I', 'J', 'K', 'L'],
   ['M', 'N', 'O', 'P']],
  Location(1, 2),
  1,
  Spiral_Directions.COUNTER_CLOCKWISE,
  "GFJK"
  )

"""
List of all unit test inputs
"""
test_route_cipher_clockwise_list = [

  (test_route_cipher__example_1.inp_string,
   test_route_cipher__example_1.dimension,
   test_route_cipher__example_1.direction,
   test_route_cipher__example_1.expected_out_string),

  (test_route_cipher__example_4.inp_string,
   test_route_cipher__example_4.dimension,
   test_route_cipher__example_4.direction,
   test_route_cipher__example_4.expected_out_string),

  (test_route_cipher__example_5.inp_string,
   test_route_cipher__example_5.dimension,
   test_route_cipher__example_5.direction,
   test_route_cipher__example_5.expected_out_string),
]

test_route_cipher_counter_clockwise_list = [

  (test_route_cipher__example_2.inp_string,
   test_route_cipher__example_2.dimension,
   test_route_cipher__example_2.direction,
   test_route_cipher__example_2.expected_out_string),

  (test_route_cipher__example_3.inp_string,
   test_route_cipher__example_3.dimension,
   test_route_cipher__example_3.direction,
   test_route_cipher__example_3.expected_out_string),

  (test_route_cipher__example_6.inp_string,
   test_route_cipher__example_6.dimension,
   test_route_cipher__example_6.direction,
   test_route_cipher__example_6.expected_out_string),

]

test_traverse_list = [
  
  (test_traverse__down.encoder_array,
   test_traverse__down.start_loc,
   test_traverse__down.num_step,
   test_traverse__down.traverse_dir,
   test_traverse__down.expected_out_string),

  (test_traverse__right.encoder_array,
   test_traverse__right.start_loc,
   test_traverse__right.num_step,
   test_traverse__right.traverse_dir,
   test_traverse__right.expected_out_string),

  (test_traverse__up.encoder_array,
   test_traverse__up.start_loc,
   test_traverse__up.num_step,
   test_traverse__up.traverse_dir,
   test_traverse__up.expected_out_string),

  (test_traverse__left.encoder_array,
   test_traverse__left.start_loc,
   test_traverse__left.num_step,
   test_traverse__left.traverse_dir,
   test_traverse__left.expected_out_string),
]

test_encode_loop_list = [

  (test_encode_loop__clockwise_0.encoder_array,
   test_encode_loop__clockwise_0.loop_idx,
   test_encode_loop__clockwise_0.start_loc,
   test_encode_loop__clockwise_0.spiral_dir,
   test_encode_loop__clockwise_0.expected_out_string),

  (test_encode_loop__clockwise_1.encoder_array,
   test_encode_loop__clockwise_1.loop_idx,
   test_encode_loop__clockwise_1.start_loc,
   test_encode_loop__clockwise_1.spiral_dir,
   test_encode_loop__clockwise_1.expected_out_string),

  (test_encode_loop__counter_clockwise_0.encoder_array,
   test_encode_loop__counter_clockwise_0.loop_idx,
   test_encode_loop__counter_clockwise_0.start_loc,
   test_encode_loop__counter_clockwise_0.spiral_dir,
   test_encode_loop__counter_clockwise_0.expected_out_string),

  (test_encode_loop__counter_clockwise_1.encoder_array,
   test_encode_loop__counter_clockwise_1.loop_idx,
   test_encode_loop__counter_clockwise_1.start_loc,
   test_encode_loop__counter_clockwise_1.spiral_dir,
   test_encode_loop__counter_clockwise_1.expected_out_string),

]


"""
Functions to run the unit tests
"""

@pytest.mark.parametrize(
  'inp_string, dimension,direction, expected_out_string',
  test_route_cipher_clockwise_list
  )
def test_route_cipher_clockwise(
  inp_string,
  dimension,
  direction,
  expected_out_string
  ):

  actual_out_string = encode(inp_string, dimension, direction)
  assert (actual_out_string == expected_out_string)

@pytest.mark.parametrize(
  'inp_string, dimension, direction, expected_out_string',
  test_route_cipher_counter_clockwise_list
  )
def test_route_cipher_counter_clockwise(
  inp_string,
  dimension,
  direction,
  expected_out_string
  ):

  actual_out_string = encode(inp_string, dimension, direction)
  assert (actual_out_string == expected_out_string)


@pytest.mark.parametrize(
  'encoder_array, start_loc, num_step, traverse_dir, expected_out_string',
  test_traverse_list
  )
def test_traverse(
  encoder_array,
  start_loc,
  num_step,
  traverse_dir,
  expected_out_string):

  string = traverse(encoder_array, start_loc, num_step, traverse_dir)
  assert(string == expected_out_string)

@pytest.mark.parametrize(
  'encoder_array, loop_idx, loc, spiral_dir, expected_out_string',
  test_encode_loop_list
  )
def test_encode_loop(
  encoder_array,
  loop_idx,
  loc,
  spiral_dir,
  expected_out_string
  ):

  output = encode_loop(encoder_array, loop_idx, loc, spiral_dir)
  assert(output == expected_out_string)