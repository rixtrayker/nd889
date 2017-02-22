# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a test for naked multi functionality"""

from board import Board as SB

# pylint: disable=invalid-name
naked_multi_board_1 = {
    'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8',
    'I7': '1', 'I4': '8', 'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3',
    'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8', 'G1': '7', 'I1': '23',
    'C8': '5', 'I3': '23', 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
    'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'A4': '2357',
    'A7': '27', 'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579',
    'C7': '9', 'C6': '6', 'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8',
    'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2', 'F6': '125', 'A9': '8',
    'G4': '9', 'A8': '6', 'E7': '345', 'E3': '379', 'F1': '6', 'F2': '4',
    'F3': '23', 'F4': '1235', 'F5': '8', 'E2': '37', 'F7': '35', 'F8': '9',
    'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17', 'D3': '2379',
    'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9',
    'B2': '5', 'B3': '6', 'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347',
    'B8': '3', 'B9': '4', 'D1': '5'
}

# pylint: disable=invalid-name
naked_multi_solutions_1 = [{
    'G7': '6', 'G6': '3', 'G5': '2', 'G4': '9', 'G3': '1', 'G2': '8',
    'G1': '7', 'G9': '5', 'G8': '4', 'C9': '1', 'C8': '5', 'C3': '8',
    'C2': '237', 'C1': '23', 'C7': '9', 'C6': '6', 'C5': '37', 'A4': '2357',
    'A9': '8', 'A8': '6', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
    'F5': '8', 'F6': '125', 'F7': '35', 'F8': '9', 'F9': '7', 'B4': '27',
    'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5',
    'B3': '6', 'C4': '4', 'B8': '3', 'B9': '4', 'I9': '9', 'I8': '7',
    'I1': '23', 'I3': '23', 'I2': '6', 'I5': '5', 'I4': '8', 'I7': '1',
    'I6': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'E8': '1',
    'A7': '27', 'A6': '257', 'E5': '347', 'E4': '6', 'E7': '345', 'E6': '579',
    'E1': '8', 'E3': '79', 'E2': '37', 'H8': '2', 'H9': '3', 'H2': '9',
    'H3': '5', 'H1': '4', 'H6': '17', 'H7': '8', 'H4': '17', 'H5': '6',
    'D8': '8', 'D9': '6', 'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347',
    'D2': '1', 'D3': '79', 'D1': '5'
}, {
    'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8',
    'I7': '1', 'I4': '8', 'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3',
    'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8', 'G1': '7', 'I1': '23',
    'C8': '5', 'I3': '23', 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
    'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'A4': '2357',
    'A7': '27', 'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23',
    'E6': '579', 'C7': '9', 'C6': '6', 'C5': '37', 'C4': '4', 'I9': '9',
    'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2', 'F6': '125',
    'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '79', 'F1': '6',
    'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'E2': '3', 'F7': '35',
    'F8': '9', 'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17',
    'D3': '79', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2',
    'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279', 'D7': '34', 'D4': '237',
    'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'
}]


def test_naked_multi_2() -> None:
    """Solve first naked twin problem with naked multi twins"""
    sbrd = SB()
    board = sbrd.naked_multi(naked_multi_board_1, 2)
    assert board in naked_multi_solutions_1


def test_naked_multi_3() -> None:
    """Solve first naked twin board with naked triplets"""
    triplet_board = naked_multi_board_1.copy()

    # add some numbers to the board that the existing triples can clear
    triplet_board['A5'] = triplet_board['A5'] + '3'  # give it a 3 to clear
    triplet_board['I2'] = triplet_board['I2'] + '7'  # give it a 7 to clear
    triplet_board['G2'] = triplet_board['G2'] + '3'  # give it a 3 to clear

    sbrd = SB()
    board = sbrd.naked_multi(triplet_board, 3)
    assert board == naked_multi_board_1


def test_naked_multi_4() -> None:
    """Solve first naked twin board with naked quads"""
    quad_board = naked_multi_board_1.copy()

    # add some numbers to the board that the existing quads can clear
    quad_board['A1'] = quad_board['A1'] + '2'  # give it a 2 to clear
    quad_board['A5'] = quad_board['A5'] + '2'  # give it a 2 to clear
    quad_board['F1'] = quad_board['F1'] + '1'  # give it a 1 to clear

    sbrd = SB()
    board = sbrd.naked_multi(quad_board, 4)
    assert board == naked_multi_board_1
