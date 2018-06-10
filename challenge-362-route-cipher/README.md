#r/dailyprogrammer Challenge \#364: Route Transposition Cipher

Link to the challenge:
<https://www.reddit.com/r/dailyprogrammer/comments/8n8tog/20180530_challenge_362_intermediate_route/>

#Problem Description:
Given input string and direction, populate the string into the array in a traditional left-to-right, up-to-down, manner. When encoding, use the same array as a reference, and create the encoded string by going through the array in a spiral in either clock-wise or counter-clockwise direction.

More detailed description and example can be found at the challenge link

#Files
route_cipher.py contains encode() which encodes given input string into route cipher
test_route_cipher.py is pytest module to test out the example string inputs from the code challenge link

#Status
Only clockwise direction is implemented right now. Also, the current logic is very specific to clockwise scenario for starting out at top-right. Need to clean up the logic to make it more generic.