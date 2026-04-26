# Tic Tac Toe — Neurosymbolic AI Edition
# =========================================
# Architecture: Two Perceptrons (Neural) + Rule Engine (Symbolic)
#
# NEURAL COMPONENT:
#   - A 2-neuron Perceptron learns to detect whether two adjacent cells are identical
#   - An 8-neuron Perceptron aggregates 8 line-checks into one game-over verdict
#
# SYMBOLIC COMPONENT:
#   - An explicit rule hierarchy drives the computer's move selection
#   - Every decision is logged in plain English so the reasoning is fully visible
#
# BOARD ENCODING:
#   - Empty cells hold their position code: row 1 → [10,11,12], row 2 → [20,21,22], row 3 → [30,31,32]
#   - Any value > 2 means the cell is empty (position codes are all >= 10)
#   - Player 1 occupies a cell by writing 1; Player 2 writes 2
#   - During simulation, a tried-but-failed cell is marked negative (e.g. -10)
#     so the search loop knows to skip it on the next iteration

import random, os
from time import sleep

# ---------------------------------------------
# Symbolic Knowledge Base — the explicit rules
# ---------------------------------------------
# These are the rules the computer follows, in priority order.
# Displaying them here means a learner can read the computer's strategy
# independently of the code that implements it.

RULES = [
    "Rule 1 [WIN]   -- If placing Player 2 in any empty cell wins the game, take that cell immediately.",
    "Rule 2 [BLOCK] -- If Player 1 would win on the very next move, place Player 2 there to block.",
    "Rule 3 [SETUP] -- If a move creates a position from which Player 2 can win on the next move, prefer it.",
    "Rule 4 [FILL]  -- Otherwise, take the next available cell (centre preference, then top, then bottom row).",
]

def print_rules():
    print("\n-- Symbolic Knowledge Base (Rules) ------------------------------------------")
    for rule in RULES:
        print(" ", rule)
    print("------------------------------------------------------------------------------\n")

# ---------------------------------------------
# Explanation log — collects one plain-English
# sentence per reasoning step during a computer turn
# ---------------------------------------------

explanation_log = []

def log(msg):
    explanation_log.append(msg)

def print_explanation():
    print("\n-- Computer Reasoning Log ----------------------------------------------------")
    for line in explanation_log:
        print(" ", line)
    print("------------------------------------------------------------------------------\n")

def clear_log():
    explanation_log.clear()

# ---------------------------------------------
# Neural Component — Perceptron implementation
# ---------------------------------------------

lr   = 1  # learning rate
bias = 1  # bias node value

# Weights are initialised randomly; training will adjust them
weights_2_neurons = [random.random(), random.random(), random.random()]
weights_8_neurons = [random.random(), random.random(), random.random(), random.random(),
                     random.random(), random.random(), random.random(), random.random(),
                     random.random()]

# -- 2-Neuron Perceptron --------------
# Inputs: two difference values (abs of adjacent cell pair)
# Trained to output 1 when both differences are 0 (all three cells match)
# and 0 otherwise -- i.e. "is this a complete, uniform line segment?"

def ActivationFunction_2_neurons(input1, weights1, input2, weights2, bias, weights3):
   """Heaviside activation: output 1 if weighted sum > 0, else 0."""
   outputP = input1*weights1 + input2*weights2 + bias*weights3

   if outputP > 0:  # activation function (here Heaviside) True or False comes from Neurons getting trained
      outputP = 1
   else:
      outputP = 0

   return outputP

def Perceptron_2_neurons(input1, input2, output):
   """Single training step: compute output, measure error, adjust weights."""
   outputP = ActivationFunction_2_neurons(input1, weights_2_neurons[0], input2, weights_2_neurons[1], bias, weights_2_neurons[2])

   error = output - outputP
   weights_2_neurons[0] += error * input1 * lr
   weights_2_neurons[1] += error * input2 * lr
   weights_2_neurons[2] += error * bias   * lr


# -- 8-Neuron Perceptron --------------
# Inputs: the 8 line-check outputs (one per winning line)
# Trained to output 1 when exactly one line is complete (a win has occurred)

def ActivationFunction_8_neurons(input1, weights1, input2, weights2, input3, weights3, input4, weights4,
                                  input5, weights5, input6, weights6, input7, weights7, input8, weights8,
                                  bias, weights9):
   """Heaviside activation over 8 line inputs plus bias."""
   outputP = (input1*weights1 + input2*weights2 + input3*weights3 + input4*weights4 +
              input5*weights5 + input6*weights6 + input7*weights7 + input8*weights8 + bias*weights9)

   if outputP > 0:  # activation function (here Heaviside) True or False comes from Neurons getting trained
      outputP = 1
   else:
      outputP = 0

   return outputP

def Perceptron_8_neurons(input1, input2, input3, input4, input5, input6, input7, input8, output):
   """Single training step for the 8-neuron perceptron."""
   outputP = ActivationFunction_8_neurons(input1, weights_8_neurons[0], input2, weights_8_neurons[1],
                                           input3, weights_8_neurons[2], input4, weights_8_neurons[3],
                                           input5, weights_8_neurons[4], input6, weights_8_neurons[5],
                                           input7, weights_8_neurons[6], input8, weights_8_neurons[7],
                                           bias, weights_8_neurons[8])

   error = output - outputP
   weights_8_neurons[0] += error * input1 * lr
   weights_8_neurons[1] += error * input2 * lr
   weights_8_neurons[2] += error * input3 * lr
   weights_8_neurons[3] += error * input4 * lr
   weights_8_neurons[4] += error * input5 * lr
   weights_8_neurons[5] += error * input6 * lr
   weights_8_neurons[6] += error * input7 * lr
   weights_8_neurons[7] += error * input8 * lr
   weights_8_neurons[8] += error * bias   * lr

def Teach_2_neurons():
   """
   Train the 2-neuron perceptron to recognise a uniform line segment.
   The key insight: we feed abs(cell_a - cell_b) as inputs.
   - Both adjacent pairs are 0 -> cells all match -> output 1 (uniform line)
   - Any non-zero difference -> cells differ -> output 0
   We repeat 3 epochs so the weights converge reliably.
   """
   # Teaching the 2 Neuron Neural Network so that it learns to decide Row wise GameOver combinations
   print("[Neural Training] Teaching 2-neuron perceptron (line-segment checker)...")
   for i in range(100):
      Perceptron_2_neurons(1, 1, 0)  # differences present -> not uniform
      Perceptron_2_neurons(1, 0, 0)
      Perceptron_2_neurons(0, 1, 0)
      Perceptron_2_neurons(0, 0, 1)  # no differences -> uniform -> output 1
   print(f"  Trained weights: w1={weights_2_neurons[0]:.3f}, "
         f"w2={weights_2_neurons[1]:.3f}, bias_w={weights_2_neurons[2]:.3f}")
   print("  Learned: (diff1=0, diff2=0) -> 1  |  any non-zero diff -> 0\n")

def Teach_8_neurons():
   """
   Train the 8-neuron perceptron.
   Each training example has exactly one '1' among the 8 inputs (one line won)
   -> expected output 1.
   The all-zeros example (no line won) -> expected output 0.
   """
   # Teaching the 8 Neuron Neural Network so that it can judge GameOver
   print("[Neural Training] Teaching 8-neuron perceptron (game-status aggregator)...")
   for i in range(100):
      Perceptron_8_neurons(1, 0, 0, 0, 0, 0, 0, 0, 1)  # row 1 complete
      Perceptron_8_neurons(0, 1, 0, 0, 0, 0, 0, 0, 1)  # row 2 complete
      Perceptron_8_neurons(0, 0, 1, 0, 0, 0, 0, 0, 1)  # row 3 complete
      Perceptron_8_neurons(0, 0, 0, 1, 0, 0, 0, 0, 1)  # col 1 complete
      Perceptron_8_neurons(0, 0, 0, 0, 1, 0, 0, 0, 1)  # col 2 complete
      Perceptron_8_neurons(1, 0, 0, 0, 0, 1, 0, 0, 1)  # col 3 complete
      Perceptron_8_neurons(0, 0, 0, 0, 0, 0, 1, 0, 1)  # diagonal 1 complete
      Perceptron_8_neurons(0, 0, 0, 0, 0, 0, 0, 1, 1)  # diagonal 2 complete
      Perceptron_8_neurons(0, 0, 0, 0, 0, 0, 0, 0, 0)  # no line complete
   print("  Learned: any single line complete -> 1  |  no line complete -> 0\n")

##### End of Generic Neural Functions #####


##### Main Body #####
# Specific Functions for Tic Tac Toe

# ---------------------------------------------
# Neural Evaluation — Check_Game_Status
# ---------------------------------------------
# This is the neural-symbolic interface point.
# The rule engine calls this function; the neural network answers it.
# The verbose flag surfaces all 8 intermediate line-check results so the
# reasoning is fully visible — no black box.

def Check_Game_Status(board_row1, board_row2, board_row3, verbose=False):
   """
   Neural evaluation of the board.
   Step 1: For each of the 8 winning lines, compute two adjacent differences.
           Feed them to the 2-neuron perceptron -> 1 if line is uniform, 0 if not.
   Step 2: Feed all 8 results to the 8-neuron perceptron -> 1 if any line won.

   verbose=True prints every intermediate result, making the neural
   reasoning fully transparent.
   """

   # Check the Board Values to pass to Neural Network with 2 Neurons
   # The beauty is there are no IF conditions here — the network decides
   # abs(cell_a - cell_b): 0 means identical, non-zero means different
   check_game_row1    = [0, 0]
   check_game_row1[0] = abs(board_row1[0] - board_row1[1])
   check_game_row1[1] = abs(board_row1[1] - board_row1[2])

   check_game_row2    = [0, 0]
   check_game_row2[0] = abs(board_row2[0] - board_row2[1])
   check_game_row2[1] = abs(board_row2[1] - board_row2[2])

   check_game_row3    = [0, 0]
   check_game_row3[0] = abs(board_row3[0] - board_row3[1])
   check_game_row3[1] = abs(board_row3[1] - board_row3[2])

   check_game_down1    = [0, 0]
   check_game_down1[0] = abs(board_row1[0] - board_row2[0])
   check_game_down1[1] = abs(board_row2[0] - board_row3[0])

   check_game_down2    = [0, 0]
   check_game_down2[0] = abs(board_row1[1] - board_row2[1])
   check_game_down2[1] = abs(board_row2[1] - board_row3[1])

   check_game_down3    = [0, 0]
   check_game_down3[0] = abs(board_row1[2] - board_row2[2])
   check_game_down3[1] = abs(board_row2[2] - board_row3[2])

   check_game_across1    = [0, 0]
   check_game_across1[0] = abs(board_row1[0] - board_row2[1])
   check_game_across1[1] = abs(board_row2[1] - board_row3[2])

   check_game_across2    = [0, 0]
   check_game_across2[0] = abs(board_row3[0] - board_row2[1])
   check_game_across2[1] = abs(board_row2[1] - board_row1[2])

   # Ask the 2-neuron perceptron about each of the 8 winning lines
   game_status_row1    = ActivationFunction_2_neurons(check_game_row1[0],    weights_2_neurons[0], check_game_row1[1],    weights_2_neurons[1], bias, weights_2_neurons[2])
   game_status_row2    = ActivationFunction_2_neurons(check_game_row2[0],    weights_2_neurons[0], check_game_row2[1],    weights_2_neurons[1], bias, weights_2_neurons[2])
   game_status_row3    = ActivationFunction_2_neurons(check_game_row3[0],    weights_2_neurons[0], check_game_row3[1],    weights_2_neurons[1], bias, weights_2_neurons[2])
   game_status_down1   = ActivationFunction_2_neurons(check_game_down1[0],   weights_2_neurons[0], check_game_down1[1],   weights_2_neurons[1], bias, weights_2_neurons[2])
   game_status_down2   = ActivationFunction_2_neurons(check_game_down2[0],   weights_2_neurons[0], check_game_down2[1],   weights_2_neurons[1], bias, weights_2_neurons[2])
   game_status_down3   = ActivationFunction_2_neurons(check_game_down3[0],   weights_2_neurons[0], check_game_down3[1],   weights_2_neurons[1], bias, weights_2_neurons[2])
   game_status_across1 = ActivationFunction_2_neurons(check_game_across1[0], weights_2_neurons[0], check_game_across1[1], weights_2_neurons[1], bias, weights_2_neurons[2])
   game_status_across2 = ActivationFunction_2_neurons(check_game_across2[0], weights_2_neurons[0], check_game_across2[1], weights_2_neurons[1], bias, weights_2_neurons[2])

   # Optional: print each line result so the neural reasoning is visible
   if verbose:
      print("  [Neural Layer 1 -- 2-neuron perceptron, checking each line]")
      for name, d1, d2, result in [
         ("Row 1      ", check_game_row1[0],    check_game_row1[1],    game_status_row1),
         ("Row 2      ", check_game_row2[0],    check_game_row2[1],    game_status_row2),
         ("Row 3      ", check_game_row3[0],    check_game_row3[1],    game_status_row3),
         ("Col 1      ", check_game_down1[0],   check_game_down1[1],   game_status_down1),
         ("Col 2      ", check_game_down2[0],   check_game_down2[1],   game_status_down2),
         ("Col 3      ", check_game_down3[0],   check_game_down3[1],   game_status_down3),
         ("Diagonal 1 ", check_game_across1[0], check_game_across1[1], game_status_across1),
         ("Diagonal 2 ", check_game_across2[0], check_game_across2[1], game_status_across2),
      ]:
         status = "COMPLETE <--" if result == 1 else "not complete"
         print(f"    {name}: diff1={d1}, diff2={d2}  ->  {status}")

   # Pass the output of 2-Neuron Neural Network as Input to 8-Neuron Neural Network for Overall Status
   FinalStatus = ActivationFunction_8_neurons(game_status_row1,    weights_8_neurons[0],
                                              game_status_row2,    weights_8_neurons[1],
                                              game_status_row3,    weights_8_neurons[2],
                                              game_status_down1,   weights_8_neurons[3],
                                              game_status_down2,   weights_8_neurons[4],
                                              game_status_down3,   weights_8_neurons[5],
                                              game_status_across1, weights_8_neurons[6],
                                              game_status_across2, weights_8_neurons[7],
                                              bias,                weights_8_neurons[8])

   if verbose:
      line_results = [game_status_row1, game_status_row2, game_status_row3,
                      game_status_down1, game_status_down2, game_status_down3,
                      game_status_across1, game_status_across2]
      verdict = "WIN DETECTED" if FinalStatus == 1 else "no winner yet"
      print(f"  [Neural Layer 2 -- 8-neuron perceptron aggregates all lines]")
      print(f"    Inputs: {line_results}  ->  Neural Verdict: {verdict}\n")

   return FinalStatus


def position_name(position):
   """Human-readable name for a position code, used in the explanation log."""
   names = {10: "row1-left",   11: "row1-centre",  12: "row1-right",
            20: "row2-left",   21: "row2-centre",   22: "row2-right",
            30: "row3-left",   31: "row3-centre",   32: "row3-right"}
   return names.get(position, str(position))


def GetEmptyCell(board_row):
   """
   Return the index of the first empty cell in a row, or -1 if none.
   Empty cells hold their position code (>= 10), so any value > 2 is empty.
   Preference order within a row: centre (index 1), left (0), right (2).
   """
   #print("Cell Value", board_row[0], board_row[1], board_row[2])
   if board_row[1] > 2:  # Start looking at middle cell first
      return 1
   if board_row[0] > 2:
      return 0
   if board_row[2] > 2:
      return 2
   return -1


def GetNextPosition(board_row1, board_row2, board_row3):
   """
   Return the next available position code, preferring middle row first,
   then top row, then bottom row.
   Returns 0 if the board is full.
   """
   position = 20  # Start looking at middle row
   if GetEmptyCell(board_row2) > -1:
      return position + GetEmptyCell(board_row2)
   position = 10
   if GetEmptyCell(board_row1) > -1:
      return position + GetEmptyCell(board_row1)
   position = 30
   if GetEmptyCell(board_row3) > -1:
      return position + GetEmptyCell(board_row3)
   return 0


def WinningMove(board_row1, board_row2, board_row3):
   """
   [Rule 1 -- WIN]
   Simulate placing Player 2 in each empty cell.
   Ask the neural network: does this produce a win?
   Return the first position that wins, or 0 if none found.
   Tried-but-failed cells are marked negative so the loop skips them.
   """
   local_board_row1 = [0, 0, 0]
   local_board_row2 = [0, 0, 0]
   local_board_row3 = [0, 0, 0]
   local_board_row1[0] = board_row1[0]
   local_board_row1[1] = board_row1[1]
   local_board_row1[2] = board_row1[2]
   local_board_row2[0] = board_row2[0]
   local_board_row2[1] = board_row2[1]
   local_board_row2[2] = board_row2[2]
   local_board_row3[0] = board_row3[0]
   local_board_row3[1] = board_row3[1]
   local_board_row3[2] = board_row3[2]

   position    = 21
   FinalStatus = 0
   while FinalStatus == 0 and position > 0:
      position = GetNextPosition(local_board_row1, local_board_row2, local_board_row3)

      # Try Player 2 at this cell
      if position == 10: local_board_row1[0] = 2
      if position == 11: local_board_row1[1] = 2
      if position == 12: local_board_row1[2] = 2
      if position == 20: local_board_row2[0] = 2
      if position == 21: local_board_row2[1] = 2
      if position == 22: local_board_row2[2] = 2
      if position == 30: local_board_row3[0] = 2
      if position == 31: local_board_row3[1] = 2
      if position == 32: local_board_row3[2] = 2

      # Ask the neural network
      FinalStatus = Check_Game_Status(local_board_row1, local_board_row2, local_board_row3)

      if FinalStatus == 0:
         # Not a winning move — mark as tried (negative) and continue
         if position == 10: local_board_row1[0] = -10
         if position == 11: local_board_row1[1] = -11
         if position == 12: local_board_row1[2] = -12
         if position == 20: local_board_row2[0] = -20
         if position == 21: local_board_row2[1] = -21
         if position == 22: local_board_row2[2] = -22
         if position == 30: local_board_row3[0] = -30
         if position == 31: local_board_row3[1] = -31
         if position == 32: local_board_row3[2] = -32

   return position


def BlockingMove(board_row1, board_row2, board_row3):
   """
   [Rule 2 -- BLOCK]
   Simulate placing Player 1 in each empty cell.
   Ask the neural network: would that win for Player 1?
   If yes, that cell is where Player 2 must block.
   Tried-but-failed cells are marked negative so the loop skips them.
   """
   local_board_row1 = [0, 0, 0]
   local_board_row2 = [0, 0, 0]
   local_board_row3 = [0, 0, 0]
   local_board_row1[0] = board_row1[0]
   local_board_row1[1] = board_row1[1]
   local_board_row1[2] = board_row1[2]
   local_board_row2[0] = board_row2[0]
   local_board_row2[1] = board_row2[1]
   local_board_row2[2] = board_row2[2]
   local_board_row3[0] = board_row3[0]
   local_board_row3[1] = board_row3[1]
   local_board_row3[2] = board_row3[2]

   position    = 21
   FinalStatus = 0
   while FinalStatus == 0 and position > 0:
      position = GetNextPosition(local_board_row1, local_board_row2, local_board_row3)

      # Try Player 1 at this cell (simulating their threat)
      if position == 10: local_board_row1[0] = 1
      if position == 11: local_board_row1[1] = 1
      if position == 12: local_board_row1[2] = 1
      if position == 20: local_board_row2[0] = 1
      if position == 21: local_board_row2[1] = 1
      if position == 22: local_board_row2[2] = 1
      if position == 30: local_board_row3[0] = 1
      if position == 31: local_board_row3[1] = 1
      if position == 32: local_board_row3[2] = 1

      # Ask the neural network
      FinalStatus = Check_Game_Status(local_board_row1, local_board_row2, local_board_row3)

      if FinalStatus == 0:
         # Not a threat here — mark as tried (negative) and continue
         if position == 10: local_board_row1[0] = -10
         if position == 11: local_board_row1[1] = -11
         if position == 12: local_board_row1[2] = -12
         if position == 20: local_board_row2[0] = -20
         if position == 21: local_board_row2[1] = -21
         if position == 22: local_board_row2[2] = -22
         if position == 30: local_board_row3[0] = -30
         if position == 31: local_board_row3[1] = -31
         if position == 32: local_board_row3[2] = -32

   return position


def MakeSmartMove(board_row1, board_row2, board_row3):
   """
   [Rule 3 -- SETUP]
   One-move lookahead: for each empty cell, place Player 2 there,
   then check if WinningMove finds a follow-up win from that position.
   If it does, return the setup cell (not the follow-up).
   This finds moves that create a guaranteed next-turn win.
   """
   local_board_row1 = [0, 0, 0]
   local_board_row2 = [0, 0, 0]
   local_board_row3 = [0, 0, 0]
   local_board_row1[0] = board_row1[0]
   local_board_row1[1] = board_row1[1]
   local_board_row1[2] = board_row1[2]
   local_board_row2[0] = board_row2[0]
   local_board_row2[1] = board_row2[1]
   local_board_row2[2] = board_row2[2]
   local_board_row3[0] = board_row3[0]
   local_board_row3[1] = board_row3[1]
   local_board_row3[2] = board_row3[2]

   position    = 21
   FinalStatus = 0
   while FinalStatus == 0 and position > 0:
      position = GetNextPosition(local_board_row1, local_board_row2, local_board_row3)

      # Place Player 2 at this candidate position
      if position == 10: local_board_row1[0] = 2
      if position == 11: local_board_row1[1] = 2
      if position == 12: local_board_row1[2] = 2
      if position == 20: local_board_row2[0] = 2
      if position == 21: local_board_row2[1] = 2
      if position == 22: local_board_row2[2] = 2
      if position == 30: local_board_row3[0] = 2
      if position == 31: local_board_row3[1] = 2
      if position == 32: local_board_row3[2] = 2

      # Now check if a follow-up winning move exists from this position
      nxt_position = WinningMove(local_board_row1, local_board_row2, local_board_row3)
      if nxt_position == 10: local_board_row1[0] = 2
      if nxt_position == 11: local_board_row1[1] = 2
      if nxt_position == 12: local_board_row1[2] = 2
      if nxt_position == 20: local_board_row2[0] = 2
      if nxt_position == 21: local_board_row2[1] = 2
      if nxt_position == 22: local_board_row2[2] = 2
      if nxt_position == 30: local_board_row3[0] = 2
      if nxt_position == 31: local_board_row3[1] = 2
      if nxt_position == 32: local_board_row3[2] = 2

      FinalStatus = Check_Game_Status(local_board_row1, local_board_row2, local_board_row3)

      if FinalStatus == 0:
         # This sequence didn't lead to a win — restore both cells and continue
         if nxt_position == 10: local_board_row1[0] = 10
         if nxt_position == 11: local_board_row1[1] = 11
         if nxt_position == 12: local_board_row1[2] = 12
         if nxt_position == 20: local_board_row2[0] = 20
         if nxt_position == 21: local_board_row2[1] = 21
         if nxt_position == 22: local_board_row2[2] = 22
         if nxt_position == 30: local_board_row3[0] = 30
         if nxt_position == 31: local_board_row3[1] = 31
         if nxt_position == 32: local_board_row3[2] = 32

         if position == 10: local_board_row1[0] = -10
         if position == 11: local_board_row1[1] = -11
         if position == 12: local_board_row1[2] = -12
         if position == 20: local_board_row2[0] = -20
         if position == 21: local_board_row2[1] = -21
         if position == 22: local_board_row2[2] = -22
         if position == 30: local_board_row3[0] = -30
         if position == 31: local_board_row3[1] = -31
         if position == 32: local_board_row3[2] = -32

   return position


# ---------------------------------------------
# AutoMode — the symbolic rule engine
# ---------------------------------------------
# This is the explicit neural-symbolic interface:
# the rule engine calls the neural network as an evaluator
# and logs every decision in plain English.

def AutoMode(board_row1, board_row2, board_row3):
   """
   Apply the symbolic rules in priority order.
   Every decision is logged so the reasoning is fully transparent.
   """
   local_board_row1 = [0, 0, 0]
   local_board_row2 = [0, 0, 0]
   local_board_row3 = [0, 0, 0]
   local_board_row1[0] = board_row1[0]
   local_board_row1[1] = board_row1[1]
   local_board_row1[2] = board_row1[2]
   local_board_row2[0] = board_row2[0]
   local_board_row2[1] = board_row2[1]
   local_board_row2[2] = board_row2[2]
   local_board_row3[0] = board_row3[0]
   local_board_row3[1] = board_row3[1]
   local_board_row3[2] = board_row3[2]

   clear_log()
   log("[Symbolic Rule Engine] Computer's turn -- evaluating rules in priority order.")

   # -- Rule 1: Win if possible --
   log("[Rule 1 -- WIN] Simulating Player 2 in each empty cell to find a winning move...")
   position = WinningMove(local_board_row1, local_board_row2, local_board_row3)
   if position > 0:
      log(f"  -> Neural network confirmed: placing Player 2 at {position_name(position)} wins the game.")
      log(f"  -> Rule 1 FIRED. Move: {position_name(position)}.")
      return position
   log("  -> No immediate winning move found. Trying Rule 2.")

   # -- Rule 2: Block Player 1 --
   log("[Rule 2 -- BLOCK] Simulating Player 1 in each empty cell to detect threats...")
   position = BlockingMove(local_board_row1, local_board_row2, local_board_row3)
   if position > 0:
      log(f"  -> Neural network confirmed: Player 1 would win at {position_name(position)}.")
      log(f"  -> Rule 2 FIRED. Blocking Player 1 at {position_name(position)}.")
      return position
   log("  -> No immediate threat from Player 1. Trying Rule 3.")

   # -- Rule 3: Set up a future win --
   log("[Rule 3 -- SETUP] Looking for a move that sets up a winning follow-up...")
   position = MakeSmartMove(local_board_row1, local_board_row2, local_board_row3)
   if position > 0:
      log(f"  -> Found setup move at {position_name(position)} leading to a follow-up win.")
      log(f"  -> Rule 3 FIRED. Move: {position_name(position)}.")
      return position
   log("  -> No setup opportunity found. Falling back to Rule 4.")

   # -- Rule 4: Fallback --
   log("[Rule 4 -- FILL] No strategic move found. Taking next available cell.")
   position = GetNextPosition(local_board_row1, local_board_row2, local_board_row3)
   log(f"  -> Rule 4 FIRED. Move: {position_name(position)}.")
   return position


################################
################################
# Game Related code Starts Here
################################
################################

print("\n==============================================================")
print("  TIC TAC TOE -- Neurosymbolic AI Edition")
print("==============================================================\n")

print("-- Phase 1: Neural Network Training --------------------------\n")
Teach_2_neurons()
Teach_8_neurons()

print("-- Phase 2: Symbolic Knowledge Base --------------------------")
print_rules()

print("-- Phase 3: Game Start ----------------------------------------")
print("  You are Player 1 (X). Computer is Player 2 (O).")
print("  Enter a position code shown on the board (e.g. 10, 21, 32).")
print("  Enter 0 to exit.\n")
sleep(2)

# Tic Tac Toe Board Status — position codes act as emptiness markers (all > 2)
board_row1 = [10, 11, 12]
board_row2 = [20, 21, 22]
board_row3 = [30, 31, 32]

FinalStatus  = 0
PlayerNumber = 2   # start at 2 so first toggle gives Player 1
automode     = 1
position     = 21  # non-zero to enter loop

while FinalStatus == 0 and position > 0:
   if PlayerNumber == 1:
      PlayerNumber = 2
   else:
      PlayerNumber = 1

   _ = os.system('clear')
   print("")
   print("Tic Tac Toe Board: Player Number", PlayerNumber)
   print("[", board_row1[0], "] [", board_row1[1], "] [", board_row1[2], "]")
   print("[", board_row2[0], "] [", board_row2[1], "] [", board_row2[2], "]")
   print("[", board_row3[0], "] [", board_row3[1], "] [", board_row3[2], "]")
   print("")
   print("Input the Cell Number say 10, 20, 21 etc or 0 to EXIT")

   if PlayerNumber == 1:
      position = int(input())
   else:
      if automode == 0:
         position = int(input())
      else:
         position = AutoMode(board_row1, board_row2, board_row3)
         print_explanation()

         # Show the neural verdict for the board after the chosen move — fully transparent
         print("-- Neural Evaluation of Computer's Chosen Move -----------------------")
         tmp_r1 = list(board_row1)
         tmp_r2 = list(board_row2)
         tmp_r3 = list(board_row3)
         if position == 10: tmp_r1[0] = 2
         if position == 11: tmp_r1[1] = 2
         if position == 12: tmp_r1[2] = 2
         if position == 20: tmp_r2[0] = 2
         if position == 21: tmp_r2[1] = 2
         if position == 22: tmp_r2[2] = 2
         if position == 30: tmp_r3[0] = 2
         if position == 31: tmp_r3[1] = 2
         if position == 32: tmp_r3[2] = 2
         Check_Game_Status(tmp_r1, tmp_r2, tmp_r3, verbose=True)
         print("----------------------------------------------------------------------\n")
         sleep(3)

   if position == 10: board_row1[0] = PlayerNumber
   if position == 11: board_row1[1] = PlayerNumber
   if position == 12: board_row1[2] = PlayerNumber
   if position == 20: board_row2[0] = PlayerNumber
   if position == 21: board_row2[1] = PlayerNumber
   if position == 22: board_row2[2] = PlayerNumber
   if position == 30: board_row3[0] = PlayerNumber
   if position == 31: board_row3[1] = PlayerNumber
   if position == 32: board_row3[2] = PlayerNumber

   FinalStatus = Check_Game_Status(board_row1, board_row2, board_row3)
   print("Game Status", FinalStatus)
   sleep(2)

if FinalStatus == 1:
   print("Game Won By Player:-", PlayerNumber)
   print("[", board_row1[0], "] [", board_row1[1], "] [", board_row1[2], "]")
   print("[", board_row2[0], "] [", board_row2[1], "] [", board_row2[2], "]")
   print("[", board_row3[0], "] [", board_row3[1], "] [", board_row3[2], "]")
   print("")
else:
   print("Game Draw !!!")
