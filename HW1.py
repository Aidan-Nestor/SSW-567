# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:02:23 2024

@author: aidan
"""
import unittest

def classify_triangle(a, b, c):
    
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise ValueError("All inputs must be numbers.")
    
    string = ""
    
    sides = sorted([a, b, c])
    
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        string += "right"
    else:
        string += "not right"
    
    if a == b == c :
        string += " and equilateral"
    
    elif a == b or b == c or c == a :
        string += " and isosceles"
    
    else:
        string += " and scalene"
    
    return string
    

def main():
    classify_triangle(2, 2, 2)



class TriangleClassifyTest(unittest.TestCase):
    
    def testEquil(self):
        self.assertEqual(classify_triangle(2, 2, 2), "not right and equilateral")
        
    def testIso(self):
        self.assertEqual(classify_triangle(1, 2, 2), "not right and isosceles")
        
    def testScal(self):
        self.assertEqual(classify_triangle(3, 4, 5), "right and scalene")
        
    def testNotRight(self):
        self.assertEqual(classify_triangle(3, 4, 6), "not right and scalene")
        
    # below test verifies that the code above has a bug because there can be isosceles
    # triangles that are also right triangles if the hypotenuse is equal to one of the
    # equal sides nultiplied by sqrt(2)
    def testRightIso(self):
        self.assertNotEqual(classify_triangle(2*(2**0.5), 2, 2), "right and isosceles")
        
    # below test shows a bug in the code that the program thinks the input is a valid
    # triangle even though it isn't
    def testScaleneSize(self):
        self.assertNotEqual(classify_triangle(42, 2, 3), "not a possible triangle")
    
    def testInputs(self):
        with self.assertRaises(ValueError):
            classify_triangle("hello", [1, 2], 3)
        
unittest.main()