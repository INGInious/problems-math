
import unittest
import math
import sys

from sympy import simplify, sympify, N, E, pi, Equality, Interval, Matrix, FiniteSet, ConditionSet, EmptySet, S, Symbol
from inginious_problems_math.math_problem import MathProblem
from inginious_problems_math.math_interval import MathIntervalProblem
from inginious_problems_math.math_matrix import MathMatrixProblem
from inginious_problems_math.math_set import MathSetProblem


class TestParseAnswer(unittest.TestCase):


    def test_unique_expression(self):
        self.assertEqual((int(MathProblem.parse_answer("x").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("2x-x").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("x2-x").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{5x}{5}").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{25x}{5}-4x").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{x}{1}").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("1x").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("1x^1-5+5").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{x^2}{x}").subs("x",10))),10)


    def test_simple_expression(self):
        self.assertEqual((int(MathProblem.parse_answer("2x+1").subs("x",17))),35)
        self.assertEqual((int(MathProblem.parse_answer("1+x2").subs("x",17))),35)
        self.assertEqual((int(MathProblem.parse_answer("2x+2-1").subs("x",17))),35)
        self.assertEqual(int((MathProblem.parse_answer("x+x+1").subs("x",17))),35)
        self.assertEqual((int(MathProblem.parse_answer("2x+7-6").subs("x",17))),35)
        self.assertEqual((int(MathProblem.parse_answer("x3+2-x-1").subs("x",17))),35)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{3xxx+2xx-xxx-1xx}{xx}").subs("x",17))),35)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{15xxx+10xx-5xxx-5xx}{5xx}").subs("x",17))),35)


    def test_simple_polynomial(self):
        self.assertEqual((int(MathProblem.parse_answer("3x^2+2x+5").subs("x",18))),1013)
        self.assertEqual((int(MathProblem.parse_answer("3x^2+2x+5+x^4-x^4").subs("x",18))),1013)
        self.assertEqual((int(MathProblem.parse_answer("3x^2+5x+10-5-3x").subs("x",18))),1013)
        self.assertEqual((int(MathProblem.parse_answer("3xx+2x+5").subs("x",18))),1013)
        self.assertEqual((int(MathProblem.parse_answer("xx+2xx+2x+5").subs("x",18))),1013)
        self.assertEqual((int(MathProblem.parse_answer("2+3x^2*2+x+x+3-3xx").subs("x",18))),1013)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{2x+3x^3*2+xx+xx+3x-3xxx}{x}").subs("x",18))),1013)


    def test_multivariable_polynomial(self):
        self.assertEqual((int(MathProblem.parse_answer("3x^2+x+4y^2+2y+4").subs([("x",3), ("y", 4)]))),106)
        self.assertEqual((int(MathProblem.parse_answer("4+3x^2+x+4y^2+2y+1-1").subs([("x",3), ("y", 4)]))),106)
        self.assertEqual((int(MathProblem.parse_answer("3x^2+x+(2y+1)2y+4").subs([("x",3), ("y", 4)]))),106)
        self.assertEqual((int(MathProblem.parse_answer("x*\\left(3x+1\\right)+4y^2+2y+4").subs([("x",3), ("y", 4)]))),106)
        self.assertEqual((int(MathProblem.parse_answer("3x^2+x+2(2y^2)+2y+4").subs([("x",3), ("y", 4)]))),106)
        self.assertEqual((int(MathProblem.parse_answer("3x^2+2x-x+4y^2+2y+4").subs([("x",3), ("y", 4)]))),106)
        self.assertEqual((int(MathProblem.parse_answer("3x^2+x2-x+y^2*4+2y+4").subs([("x",3), ("y", 4)]))),106)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{3x^3+xx2-xx+y^2*4x+2yx+4x}{x}").subs([("x",3), ("y", 4)]))),106)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{3x^2y+xy2-xy+y^3*4+2yy+4y}{y}").subs([("x",3), ("y", 4)]))),106)


    def test_unique_exponent(self):
        self.assertEqual((int(MathProblem.parse_answer("x^1").subs("x",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("x^2").subs("x",10))),100)
        self.assertEqual((int(MathProblem.parse_answer("x^2x").subs("x",30))),27000)
        self.assertEqual((int(MathProblem.parse_answer("x^3").subs("x",30))),27000)
        self.assertEqual((int(MathProblem.parse_answer("x^x").subs("x",3))),27)
        self.assertEqual((int(MathProblem.parse_answer("x^x2").subs("x",3))),54)
        self.assertEqual((int(MathProblem.parse_answer("x^{x}").subs("x",3))),27)
        self.assertEqual((int(MathProblem.parse_answer("x^{1x}").subs("x",3))),27)
        self.assertEqual((int(MathProblem.parse_answer("x^{2x}").subs("x",3))),729)
        self.assertEqual((int(MathProblem.parse_answer("x^{2x}2").subs("x",3))),1458)
        self.assertEqual((int(MathProblem.parse_answer("x^{x2}2").subs("x",3))),1458)
        self.assertEqual((int(MathProblem.parse_answer("2x^{x2}").subs("x",3))),1458)
        self.assertEqual((int(MathProblem.parse_answer("xx^{2x}").subs("x",2))),32)
        self.assertEqual((int(MathProblem.parse_answer("(3x)^{2x}").subs("x",2))),1296)
        self.assertEqual((int(MathProblem.parse_answer("x^{2xx}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("x^{x2x}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("x^{2x^2}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{x^{2x^2}}{1}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{\\frac{x^{2x^2}}{1}}{1}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{\\frac{2xx^{2x^2}}{1}}{2x}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{2x^{2x^2}}{2}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{2xx^{2x^2}}{2x}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{4x^{2x^2}}{2x}").subs("x",2))),256)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{xxx^{2x^2}}{2x}").subs("x",2))),256)
        self.assertEqual((float(MathProblem.parse_answer("\\frac{2x}{xxx^{2x^2}}").subs("x",2))),1/256)
        self.assertEqual((float(MathProblem.parse_answer("\\sqrt{\\frac{2x}{xxx^{2x^2}}}").subs("x",2))),math.sqrt(1/256))


    def test_multiple_exponent(self):
        self.assertEqual((int(MathProblem.parse_answer("x^2+y^2").subs([("x",2), ("y", 3)]))),13)
        self.assertEqual((int(MathProblem.parse_answer("x^y+y^x").subs([("x",2), ("y", 3)]))),17)
        self.assertEqual((int(MathProblem.parse_answer("2x^y+y^x").subs([("x",2), ("y", 3)]))),25)
        self.assertEqual((int(MathProblem.parse_answer("x^y2+y^x").subs([("x",2), ("y", 3)]))),25)
        self.assertEqual((int(MathProblem.parse_answer("2x^y+2y^x").subs([("x",2), ("y", 3)]))),34)
        self.assertEqual((int(MathProblem.parse_answer("2x^2y+2y^x").subs([("x",2), ("y", 3)]))),42)
        self.assertEqual((int(MathProblem.parse_answer("2x^{2y}+2y^x").subs([("x",2), ("y", 3)]))),146)
        self.assertEqual((int(MathProblem.parse_answer("2x^{2y}+(2y)^x").subs([("x",2), ("y", 3)]))),164)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{6x^{2y+1}+(2y)^x3x}{3x}").subs([("x",2), ("y", 3)]))),164)
        self.assertEqual((int(MathProblem.parse_answer("2x^{y^2}").subs([("x", 2), ("y",3)]))), 1024)
        self.assertEqual((float(MathProblem.parse_answer("\\frac{x+x}{4xx^y+y^x2x}").subs([("x",2), ("y", 3)]))),1/25)
        self.assertEqual((float(MathProblem.parse_answer("\\sqrt{2x^{2y}}").subs([("x", 2), ("y",3)]))), math.sqrt(128))


    def test_log(self):
        self.assertEqual((int(MathProblem.parse_answer("\\log x").subs("x",10))),1)
        self.assertEqual((int(MathProblem.parse_answer("\\log10x").subs("x",10))),2)
        self.assertEqual((int(MathProblem.parse_answer("\\log10x+10").subs("x",10))),12)
        self.assertEqual((int(MathProblem.parse_answer("\\left(\\log x\\right)^2").subs("x",100))),4)
        self.assertEqual((int(MathProblem.parse_answer("\\log\\left(x+90\\right)").subs("x",10))),2)
        self.assertEqual((int(MathProblem.parse_answer("\\left(\\log x\\right)^{\\log1000}").subs("x",100))),8)
        self.assertEqual((int(MathProblem.parse_answer("\\log x^2").subs("x",10))),2)
        self.assertEqual((int(MathProblem.parse_answer("\\sqrt{\\log x^4}").subs("x",10))),2)
        self.assertEqual((float(MathProblem.parse_answer("\\log x^y").subs([("x", 10), ("y",3)]))),3)
        self.assertEqual((float(MathProblem.parse_answer("\\log 2x").subs("x",10))),float(math.log10(20)))
        self.assertEqual((float(MathProblem.parse_answer("2\\log 2x").subs("x",10))),float(2*math.log10(20)))
        self.assertEqual((float(MathProblem.parse_answer("\\log x^10").subs("x",2))),float(math.log10(1024)))
        self.assertEqual((float(MathProblem.parse_answer("\\left(\\left(\\log x\\right)^{\\log100}\\right)^{2}").subs("x",100))),16)
        self.assertEqual((float(MathProblem.parse_answer("\\frac{\\log1000x}{\\log10x}").subs("x",10))),2)
        self.assertEqual((float(MathProblem.parse_answer("\\left(\\log x\\right)^y").subs([("x",100), ("y", 4)]))),16)
        self.assertEqual((float(MathProblem.parse_answer("\\ln 5"))),math.log(5))
        self.assertEqual((float(MathProblem.parse_answer("\\ln 5+10").subs("x",10))),math.log(5)+10)
        self.assertEqual((float(MathProblem.parse_answer("\\ln5x").subs("x",10))),math.log(50))
        self.assertEqual((float(MathProblem.parse_answer("\\log xy").subs([("x",10), ("y",100)]))),3)
        self.assertEqual((float(MathProblem.parse_answer("\\left(\\log x\\right)y").subs([("x",100), ("y",10)]))),20)



    def test_single_char_subscripts(self):
        self.assertEqual((int(MathProblem.parse_answer("x_1").subs("x_{1}",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("x_1+x_2").subs([("x_{1}",1), ("x_{2}", 4)]))),5)
        self.assertEqual((int(MathProblem.parse_answer("x_1x_2").subs([("x_{1}",2), ("x_{2}", 5)]))),10)
        self.assertEqual((int(MathProblem.parse_answer("x_1^{x_2}").subs([("x_{1}",2), ("x_{2}", 3)]))),8)
        self.assertEqual((int(MathProblem.parse_answer("x_y").subs([("x_{y}",3)]))),3)
        self.assertEqual((int(MathProblem.parse_answer("2x_1").subs([("x_{1}",3)]))),6)
        self.assertEqual((int(MathProblem.parse_answer("x_12").subs([("x_{1}",3)]))),6)
        self.assertEqual((int(MathProblem.parse_answer("x_1^3").subs([("x_{1}",3)]))),27)
        self.assertEqual((int(MathProblem.parse_answer("x_1^{x_2}").subs([("x_{1}",3), ("x_{2}", 2)]))),9)
        self.assertEqual((int(MathProblem.parse_answer("\\frac{x_1}{x_2}").subs([("x_{1}",10), ("x_{2}", 2)]))),5)
        self.assertEqual((int(MathProblem.parse_answer("\\log x_1").subs([("x_{1}",100)]))),2)
        self.assertEqual((int(MathProblem.parse_answer("\\log2x_1").subs([("x_{1}",50)]))),2)
        self.assertEqual((int(MathProblem.parse_answer("\\log10^{x_1}").subs([("x_{1}",3)]))),3)
        self.assertEqual((int(MathProblem.parse_answer("\\sqrt{\\log2x_1}").subs([("x_{1}",5000)]))),2)
        self.assertEqual((float(MathProblem.parse_answer("\\log\\left(x_1x_2\\right)").subs([("x_{1}",10), ("x_{2}", 2)]))),math.log10(20))


    def test_multi_char_subscripts(self):
        self.assertEqual((int(MathProblem.parse_answer("x_{12}").subs("x_{12}",10))),10)
        self.assertEqual((int(MathProblem.parse_answer("x_{12}x_{13}").subs([("x_{12}",3),("x_{13}", 4)]))),12)
        self.assertEqual((int(MathProblem.parse_answer("x_{12}2").subs("x_{12}",10))),20)
        self.assertEqual((int(MathProblem.parse_answer("2x_{12}").subs("x_{12}",10))),20)
        self.assertEqual((int(MathProblem.parse_answer("2x_{12}2").subs("x_{12}",10))),40)
        self.assertEqual((int(MathProblem.parse_answer("x_{12}+x_{13}").subs([("x_{12}",3),("x_{13}", 4)]))),7)
        self.assertEqual((int(MathProblem.parse_answer("\\log x_{12}").subs("x_{12}",100))),2)
        self.assertEqual((int(MathProblem.parse_answer("2\\log x_{12}").subs("x_{12}",100))),4)
        self.assertEqual((float(MathProblem.parse_answer("\\log2x_{12}").subs("x_{12}",100))),math.log10(200))
        self.assertEqual((int(MathProblem.parse_answer("a_{xy}").subs("a_{x*y}",100))),100) # a multicharacter subscript containing letter(s) such as x_{ab} is translated into x_{a*b}
        self.assertEqual((int(MathProblem.parse_answer("\\sqrt{x_{12}}").subs("x_{12}",100))),10)
        self.assertEqual((int(MathProblem.parse_answer("5x_{11}\\sqrt{x_{12}}").subs([("x_{11}",3),("x_{12}", 4)]))),30)
        self.assertEqual((int(MathProblem.parse_answer("\\ln e+x").subs("x",5))),6)
        self.assertEqual((int(MathProblem.parse_answer("\\ln e^x").subs("x",5))),5)
        self.assertEqual((int(MathProblem.parse_answer("\\ln e^{xy}").subs([("x",2),("y", 3)]))),6)
        self.assertEqual((int(MathProblem.parse_answer("\\ln e^{x_1x_2}").subs([("x_{1}",2),("x_{2}", 3)]))),6)


    def test_math_all_together(self):
        self.assertEqual((float(MathProblem.parse_answer("\\frac{\\sqrt{x_{11}x_{12}+x_{13}x_{14}}}{\\sqrt[3]{x_{15}^{x_{12}}}x_{11}}").subs([("x_{11}",1),("x_{12}", 2),("x_{13}", 3),("x_{14}", 4),("x_{15}", 5)]))), math.sqrt(14)/(25**(1/3)))
        self.assertEqual((float(MathProblem.parse_answer("\\frac{\\sqrt{x_{11}x_{12}+x_{13}x_{14}}}{\\log\\left(\\sqrt[3]{x_{15}^{x_{12}}}\\right)}").subs([("x_{11}",1),("x_{12}", 2),("x_{13}", 3),("x_{14}", 4),("x_{15}", 5)]))), math.sqrt(14)/math.log10(25**(1/3)))
        self.assertEqual((float(MathProblem.parse_answer("\\left(\\frac{\\sqrt{x_{11}x_{12}+x_{13}x_{14}}}{\\log\\left(\\sqrt[3]{x_{15}^{x_{12}}}\\right)}\\right)^{\\log\\left(x_{12}x_{13}\\right)}").subs([("x_{11}",1),("x_{12}", 2),("x_{13}", 3),("x_{14}", 4),("x_{15}", 5)]))), (math.sqrt(14)/math.log10(25**(1/3)))**math.log10(6))
        self.assertEqual((float(MathProblem.parse_answer("\\sqrt{\\left(\\frac{x_{12}^{x_{14}}}{x_{13}^{x_{12}}}\\right)}").subs([("x_{11}",1),("x_{12}", 2),("x_{13}", 3),("x_{14}", 4),("x_{15}", 5)]))), 4/3)
        self.assertEqual((float(MathProblem.parse_answer("\\int_0^1\\sqrt{\\left(\\frac{x_{12}^{x_{14}}}{x_{13}^{x_{12}}}\\right)}").subs([("x_{11}",1),("x_{12}", 2),("x_{13}", 3),("x_{14}", 4),("x_{15}", 5)]))), 4/3)
        self.assertEqual(float(MathProblem.parse_answer("2\\pi* r_1").subs("r_{1}",10)), 2*math.pi*10)


    def test_interval(self):
        self.assertEqual(MathIntervalProblem.parse_answer("[0,x]").subs("x", 1), Interval(0, 1, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[0,x]").subs("x", 2), Interval(0, 2, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[0,x)").subs("x", 1), Interval(0, 1, False, True))
        self.assertEqual(MathIntervalProblem.parse_answer("(0,x]").subs("x", 1), Interval(0, 1, True, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[x_1,x_2]").subs([("x_{1}", 1), ("x_{2}", 2)]), Interval(1, 2, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("(x_1,x_2)").subs([("x_{1}", 1), ("x_{2}", 2)]), Interval(1, 2, True, True))
        self.assertEqual(MathIntervalProblem.parse_answer("[x,\\infty]").subs("x", 1), Interval(1, sys.maxsize, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[x,\\infinity]").subs("x", 1), Interval(1, sys.maxsize, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[1,x+x]").subs("x", 1), Interval(1, 2, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[1,x*x]").subs("x", 2), Interval(1, 4, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[1,x*(x+1)]").subs("x", 1), Interval(1, 2, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[1,x*[x+1]]").subs("x", 1), Interval(1, 2, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[0,1]\\cup[1,2]"), Interval(0, 2, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[1,2]\\cup[0,1]"), Interval(0, 2, False, False))
        self.assertEqual(MathIntervalProblem.parse_answer("[0,x]\\cup[x,2]").subs("x", 1), Interval(0, 2, False, False))


    def test_matrix(self):
        self.assertEqual(MathMatrixProblem.parse_answer("x, 2, 3").subs("x", 1), Matrix([[1, 2, 3]]))
        self.assertEqual(MathMatrixProblem.parse_answer("x, y, z").subs([("x", 1), ("y", 2), ("z", 3)]), Matrix([[1, 2, 3]]))
        self.assertEqual(MathMatrixProblem.parse_answer("x_1, x_2, x_3").subs([("x_{1}", 1), ("x_{2}", 2), ("x_{3}", 3)]), Matrix([[1, 2, 3]]))
        self.assertEqual(MathMatrixProblem.parse_answer("x_1*2, x_2, x_3").subs([("x_{1}", 1), ("x_{2}", 2), ("x_{3}", 3)]), Matrix([[2, 2, 3]]))
        self.assertEqual(MathMatrixProblem.parse_answer("x_{10}, x_2, x_3").subs([("x_{10}", 1), ("x_{2}", 2), ("x_{3}", 3)]), Matrix([[1, 2, 3]]))
        self.assertEqual(MathMatrixProblem.parse_answer("x_{10}*3, x_2, x_3").subs([("x_{10}", 1), ("x_{2}", 2), ("x_{3}", 3)]), Matrix([[3, 2, 3]]))
        self.assertEqual(MathMatrixProblem.parse_answer("1,0:0,1"), Matrix([[1, 0], [0, 1]]))
        self.assertEqual(MathMatrixProblem.parse_answer("1,1-1:5-5,1"), Matrix([[1, 0], [0, 1]]))
        self.assertEqual(MathMatrixProblem.parse_answer("\\frac{2x}{2x},0:0,1"), Matrix([[1, 0], [0, 1]]))
        self.assertEqual(MathMatrixProblem.parse_answer("-i^2,0:0,1"), Matrix([[1, 0], [0, 1]]))
        self.assertEqual(MathMatrixProblem.parse_answer("\\frac{2x}{(5-2)x}+\\frac{x}{\\frac{6x}{2}},0:0,1"), Matrix([[1, 0], [0, 1]]))
        self.assertEqual(MathMatrixProblem.parse_answer("1,0,0:0,1,0:0,0,1"), Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    def test_set_explicit(self):
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{1, 1+1, 3}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{x, 2, 3}"), FiniteSet("x", 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{x, 2x, 3}"), FiniteSet("x", "2*x", 3))
        self.assertEqual(MathSetProblem.parse_answer("{x, 2x, 3}"), FiniteSet("x", "x*2", 3))
        self.assertEqual(MathSetProblem.parse_answer("{x, 2x, 3x}"), FiniteSet("x", "x*2", "3*x"))
        self.assertEqual(MathSetProblem.parse_answer("{3, 1, 2}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}\\cup{4,5,6}"), FiniteSet(1, 2, 3, 4, 5, 6))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}\\cup{3,4,5}"), FiniteSet(1, 2, 3, 4, 5))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 2+1}\\cup{3,4,5}"), FiniteSet(1, 2, 3, 4, 5))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 2+1}\\cup{3,4,2+1+2}"), FiniteSet(1, 2, 3, 4, 5))
        self.assertEqual(MathSetProblem.parse_answer("{4, 5, 6}\\cup{1,2,3}"), FiniteSet(1, 2, 3, 4, 5, 6))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}\\cup{4, 5}\\cup{6,7}"), FiniteSet(1, 2, 3, 4, 5, 6, 7))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}\\cup{4, 5}\\cap{6,7}"), EmptySet)
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}\\cap{1,2}"), FiniteSet(1, 2))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}\\cap{1,2}\\cup{3}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}\\cap{1,2}\\cup{3}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2, 3}\\cap{1,2,3}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2}\\cup{2,3}\\cap{1,2}\\cup{3}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2}\\cup{2,3}\\cup{1,2}\\cup{3}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2}\\cup{2,3}\\cap{1,2}\\cup{3, 4, 5}"), FiniteSet(1, 2, 3))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2}\\cap{2,3}\\cap{1,2}\\cap{2, 3, 4, 5}"), FiniteSet(2))
        self.assertEqual(MathSetProblem.parse_answer("{1, 2}\\cap{2,3}\\cap{1,2}\\cap{3, 4, 5}"), EmptySet)
        self.assertEqual(MathSetProblem.parse_answer("{1, 2}\\cup{2,3}\\cap{1,2}\\cap{2, 3, 4, 5}"), FiniteSet(2))


    def test_set_implicit(self):
        x = Symbol('x')
        self.assertEqual(MathSetProblem.parse_answer("{x|x<5|N}"), ConditionSet(x, x < 5, S.Naturals))
        self.assertEqual(MathSetProblem.parse_answer("{x|x<\\frac{10}{2}|N}"), ConditionSet(x, x < 5, S.Naturals))
        self.assertEqual(MathSetProblem.parse_answer("{x|x<5|Z}"), ConditionSet(x, x < 5, S.Integers))
        self.assertEqual(MathSetProblem.parse_answer("{x|x<5|Z+}"), ConditionSet(x, x < 5, S.Naturals0))
        self.assertEqual(MathSetProblem.parse_answer("{x|x<5|Z-}"), ConditionSet(x, x < 5, S.Integers-S.Naturals))
        self.assertEqual(MathSetProblem.parse_answer("{x|x<5|R}"), ConditionSet(x, x < 5, S.Reals))
        self.assertEqual(MathSetProblem.parse_answer("{x|x<5|Q}"), ConditionSet(x, x < 5, S.Rationals))
        self.assertEqual(MathSetProblem.parse_answer("{x|(x<5)\\&(x>1)|N}"), ConditionSet(x, (x < 5) & (x > 1), S.Naturals))
        self.assertEqual(MathSetProblem.parse_answer("{x|(x>1)\\&(x<5)|N}"), ConditionSet(x, (x < 5) & (x > 1), S.Naturals))
        self.assertEqual(MathSetProblem.parse_answer("{x|(x>1)\\&(x<\\frac{10}{2})|N}"), ConditionSet(x, (x < 5) & (x > 1), S.Naturals))
        self.assertEqual(MathSetProblem.parse_answer("{x|(x>1)\\&(x<4+1)|N}"), ConditionSet(x, (x < 5) & (x > 1), S.Naturals))
        self.assertNotEqual(MathSetProblem.parse_answer("{x|(x>1)\\&(x<4+1)|N}"), ConditionSet(x, (x < 5) & (x > 1), S.Reals))
        self.assertEqual(MathSetProblem.parse_answer("{x|x<5|{1,2,3,4,5}}"), ConditionSet(x, x < 5, {1,2,3,4,5}))
        self.assertEqual(MathSetProblem.parse_answer("{x|x<5|{1,2,3,4,5}}"), FiniteSet(1,2,3,4))
        self.assertNotEqual(MathSetProblem.parse_answer("{x|x<5|{1,2,3,4,5}}"), FiniteSet(1,2,3,4,5))
        self.assertEqual(MathSetProblem.parse_answer("{x|x^2<25|{1,2,3,4,5}}"), FiniteSet(1,2,3,4))
        self.assertEqual(MathSetProblem.parse_answer("{x|(x>1)\\&(x^2<25)|{0,1,2,3,4,5,6}}"), FiniteSet(2,3,4))


class TestIsEqual(unittest.TestCase):

    def test_is_equal_math(self):
        test_instance = MathProblem("fake_id", {"fake_content": 5}, "french", "fake_taskf")
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("x+x")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("3x-x")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("4x-2x")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("2*x")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("2x+0")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("x+x+x-x")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("x-i^2x")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("\\frac{4x}{2}")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("\\frac{4x^2}{2x}")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("\\frac{6x^2}{2x}-x")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("\\frac{2x^x}{x^{x-1}}")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("x*2*\\frac{5x}{2+3x+4x-2x+1-3}")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("x+x*\\pi-x*(\\pi-1)")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("2x"), MathProblem.parse_answer("x+x*x_1*x_{12}-x*(x_1*x_{12}-1)")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\frac{1}{\\sqrt{3}}"), MathProblem.parse_answer("\\frac{\\sqrt{3}}{3}")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\frac{\\sqrt{3}}{3}"), MathProblem.parse_answer("\\frac{1}{\\sqrt{3}}")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("0.5"), MathProblem.parse_answer("\\frac{1}{2}")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\frac{1}{2}"), MathProblem.parse_answer("0.5")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("0.5"), MathProblem.parse_answer("\\frac{5}{10}")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("0.5"), MathProblem.parse_answer("\\frac{2x_1x_{12}}{4x_1x_{12}}")))

    def test_is_equal_math_tolerance(self):
        test_instance = MathProblem("fake_id", {"fake_content": 5}, "french", "fake_taskf")
        test_instance._tolerance = 0.0001
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3")))
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1")))
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.14")))
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.141")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1415")))
        test_instance._tolerance = 0.001
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3")))
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1")))
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.14")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.141")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1415")))
        test_instance._tolerance = 0.01
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3")))
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.14")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.141")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1415")))
        test_instance._tolerance = 0.1
        self.assertFalse(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.14")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.141")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1415")))
        test_instance._tolerance = 1
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.14")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.141")))
        self.assertTrue(test_instance.is_equal(MathProblem.parse_answer("\\pi"), MathProblem.parse_answer("3.1415")))




    def test_is_equal_math_interval(self):
        test_instance = MathIntervalProblem("fake_id", {"fake_content": 5}, "french", "fake_taskf")
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[0,1]"), MathIntervalProblem.parse_answer("[0,1]")))
        self.assertFalse(test_instance.is_equal(MathIntervalProblem.parse_answer("[0,1)"), MathIntervalProblem.parse_answer("[0,1]")))
        self.assertFalse(test_instance.is_equal(MathIntervalProblem.parse_answer("(0,1]"), MathIntervalProblem.parse_answer("[0,1]")))
        self.assertFalse(test_instance.is_equal(MathIntervalProblem.parse_answer("(0,1)"), MathIntervalProblem.parse_answer("[0,1]")))
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[0,1]"), MathIntervalProblem.parse_answer("[x-x,1]")))
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[x,2x]"), MathIntervalProblem.parse_answer("[x,x+x]")))
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[x,(2-1)(3x-x)]"), MathIntervalProblem.parse_answer("[x,x+x]")))
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[0,1]\\cup[1,3]"), MathIntervalProblem.parse_answer("[0,3]")))
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[0,1)\\cup[1,2]"), MathIntervalProblem.parse_answer("[0,2]")))
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[-\\infty,0]\\cup[0,\\infty]"), MathIntervalProblem.parse_answer("[-\\infty,\\infty]")))
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[-\\infty,0]\\cup[0,\\infty]"), MathIntervalProblem.parse_answer("[-\\infinity,\\infinity]")))
        self.assertTrue(test_instance.is_equal(MathIntervalProblem.parse_answer("[0,\\frac{\\sqrt{3}}{3}]"), MathIntervalProblem.parse_answer("[0,\\frac{1}{\\sqrt{3}}]")))
        self.assertFalse(test_instance.is_equal(MathIntervalProblem.parse_answer("[0,\\frac{\\sqrt{3}}{3})"), MathIntervalProblem.parse_answer("[0,\\frac{1}{\\sqrt{3}}]")))
        self.assertFalse(test_instance.is_equal(MathIntervalProblem.parse_answer("[0,\\frac{\\sqrt{3}}{3}]"), MathIntervalProblem.parse_answer("(0,\\frac{1}{\\sqrt{3}}]")))


    def test_is_equal_math_matrix(self):
        test_instance = MathMatrixProblem("fake_id", {"fake_content": 5}, "french", "fake_taskf")
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("\\left[1,0\\right]"), MathMatrixProblem.parse_answer("\\left[1,0\\right]")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("\\left[0,2x\\right]"), MathMatrixProblem.parse_answer("\\left[0,x+x]")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("\\left[1,2,3\\right]"), MathMatrixProblem.parse_answer("1,2,3")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("\\left[1,2,3\\right]"), MathMatrixProblem.parse_answer("2-1,3-1,\\frac{6}{2}")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("\\left[1,2,3\\right]"), MathMatrixProblem.parse_answer("1,2,3")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("1,0:0,1"), MathMatrixProblem.parse_answer("1,0:0,0.5+0.5")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("1,0:0,1"), MathMatrixProblem.parse_answer("1,0:0,\\frac{1}{2}+\\frac{1}{2}")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("1,0,0:0,1,0:0,0,1"), MathMatrixProblem.parse_answer("3-2,0,0:0,\\frac{10*10}{100},0:0,0,-i^2")))
        self.assertFalse(test_instance.is_equal(MathMatrixProblem.parse_answer("1,0,0:0,1,0:0,0,1"), MathMatrixProblem.parse_answer("3-2,0,0:0,\\frac{10*10}{10},0:0,0,-i^2")))
        self.assertFalse(test_instance.is_equal(MathMatrixProblem.parse_answer("1,0:0,1"), MathMatrixProblem.parse_answer("1,0:0,1:0,0")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("1,\\pi:0,0"), MathMatrixProblem.parse_answer("1,2\\pi-\\pi:0,0")))
        self.assertTrue(test_instance.is_equal(MathMatrixProblem.parse_answer("\\frac{\\sqrt{3}}{3},0:0,0"), MathMatrixProblem.parse_answer("\\frac{1}{\\sqrt{3}},0:0,0")))

    def test_is_equal_set_explicit(self):
        test_instance = MathSetProblem("fake_id", {"fake_content": 5}, "french", "fake_taskf")
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{1,2,3}"), MathSetProblem.parse_answer("{3,2,1}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{1,2,3}"), MathSetProblem.parse_answer("{2+1,2,1}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{1,2,3}"), MathSetProblem.parse_answer("{1+1+1,1+1,1}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{1,2,3}"), MathSetProblem.parse_answer("{1,2}\cup{2,3}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{1,2,3}"), MathSetProblem.parse_answer("{1,2,3}\cap{1,2,3,4,5,6,7,8,9,10}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{1,2,3}"), MathSetProblem.parse_answer("{1,2}\cup{2,3}\cap{1,2}\cup{3,4}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{1,2,3}"), MathSetProblem.parse_answer("{1,2,3+x-x}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x,2x,3x}"), MathSetProblem.parse_answer("{x,x+x,2x+x}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x_1,x_2,x_3}"), MathSetProblem.parse_answer("{1x_1,x_2,2x_3-x_3}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x_12,x_2,x_3}"), MathSetProblem.parse_answer("{2x_1,x_2,2x_3-x_3}")))
        self.assertFalse(test_instance.is_equal(MathSetProblem.parse_answer("{x_{12},x_2,x_3}"), MathSetProblem.parse_answer("{2x_1,x_2,2x_3-x_3}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x,2x,3x}"), MathSetProblem.parse_answer("{x,2x,3x}\cup{5x}\cap{x,2x,2x+x}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x,2x,3x}"), MathSetProblem.parse_answer("{x,2x,3x}\cup{5x}\cap{x,2x}\cup{x+x+x}")))

    def test_is_equal_set_implicit(self):
        test_instance = MathSetProblem("fake_id", {"fake_content": 5}, "french", "fake_taskf")
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x<5|N}"), MathSetProblem.parse_answer("{x|x<4+1|N}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x<\\frac{10}{2}|N}"), MathSetProblem.parse_answer("{x|x<5|N}")))
        self.assertFalse(test_instance.is_equal(MathSetProblem.parse_answer("{x|x>5|N}"), MathSetProblem.parse_answer("{x|x<5|N}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x<5|{1,2,3,4,5}}"), MathSetProblem.parse_answer("{1,2,3,4}")))
        self.assertFalse(test_instance.is_equal(MathSetProblem.parse_answer("{x|x>5|R}"), MathSetProblem.parse_answer("{x|x>5|N}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x<5|{1,2,3,4,5}}"), MathSetProblem.parse_answer("{y|y<5|{1,2,3,4,5}}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x>1+4|N}"), MathSetProblem.parse_answer("{x|x>5|N}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x\ge5|{4,5,6}}"), MathSetProblem.parse_answer("{5,6}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x\ge5|{4,5,6}}"), MathSetProblem.parse_answer("{x|x\ge4+1|{4,5,6}}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x\le5|{4,5,6}}"), MathSetProblem.parse_answer("{4,5}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|2x\le10|N}"), MathSetProblem.parse_answer("{x|x\le5|N}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x^2\le25|{1,2,3,4,5,6,7,8,9,10}}"), MathSetProblem.parse_answer("{x|x\le5|{1,2,3,4,5}}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|x^2\le25|{1,2,3,4,5,6,7,8,9,10}}"), MathSetProblem.parse_answer("{1,2,3,4,5}")))
        self.assertFalse(test_instance.is_equal(MathSetProblem.parse_answer("{x|x>5|N}"), MathSetProblem.parse_answer("{x|x>5|R}")))
        self.assertFalse(test_instance.is_equal(MathSetProblem.parse_answer("{x|x>5|N}"), MathSetProblem.parse_answer("{x|x>5|Q}")))
        self.assertFalse(test_instance.is_equal(MathSetProblem.parse_answer("{x|x<5|N}"), MathSetProblem.parse_answer("{x|x<5|Z+}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|(x<5)|N}"), MathSetProblem.parse_answer("{x|x<4+1|N}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|(x<5)\\&(x>3)|{1,2,3,4,5}}"), MathSetProblem.parse_answer("{4}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|(x<5)\\&(x>3)|{1,2,3,4,5}}"), MathSetProblem.parse_answer("{x|(x>3)\\&(x<5)|{1,2,3,4,5}}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|(x<5)\\&(x>3)|N}"), MathSetProblem.parse_answer("{x|(x>3)\\&(x<5)|N}")))
        self.assertTrue(test_instance.is_equal(MathSetProblem.parse_answer("{x|(x<4+1)\\&(x>\\frac{6}{2})|N}"), MathSetProblem.parse_answer("{x|(x>3)\\&(x<5)|N}")))



if __name__ == '__main__':
    unittest.main()


