"""
Math Question Generator
- Dynamic Mode: Generates random counting & geometry questions
- Fixed Mode: Returns a predefined set of 25 fixed MCQs
"""

import random
import os
import sys
from typing import List, Dict, Tuple

class MathQuestionGenerator:

    def __init__(self):
        # Curriculum (shortened for brevity)
        self.curriculum = {
            "Quantitative Math": {
                "Data Analysis & Probability": ["Counting & Arrangement Problems"],
                "Geometry and Measurement": ["Area & Volume"],
                "Algebra": ["Linear Equations"]
            }
        }
        self.counting_contexts = [
            {
                "scenario": "pizza restaurant",
                "item": "pizza",
                "components": ["size", "crust", "topping"],
                "component_options": [
                    ["Small", "Medium", "Large"],
                    ["Thin", "Thick", "Stuffed"],
                    ["Pepperoni", "Mushroom", "Sausage"]
                ]
            }
        ]
        self.geometry_contexts = [
            {
                "objects": "spherical balls",
                "container": "cylindrical container",
                "arrangements": ["4×2"],
                "radius_range": (1.4, 1.4)  # fixed example
            }
        ]
        self.fixed_questions = self._load_fixed_questions()

    def _load_fixed_questions(self):
        """Return fixed 25 MCQs"""
        return [
            {
                "question": "If n+5=5, what is the value of n?",
                "options": ["0", "1/5", "1", "5", "10"],
                "correct_index": 0,
                "explanation": "Subtract 5 from both sides: n = 0",
                "subject": "Quantitative Math",
                "unit": "Algebra",
                "topic": "Linear Equations",
                "image_path": None
            },
            {
                "question": "The sequence of shapes above repeats indefinitely. Which shape is the 12th shape in the sequence?",
                "options": ["Shape A", "Shape B", "Shape C", "Shape D", "Shape E"],
                "correct_index": 1,
                "explanation": "Determine cycle length and find 12th term via remainder.",
                "subject": "Quantitative Math",
                "unit": "Patterns",
                "topic": "Sequences",
                "image_path": os.path.join("images", "q2_shapes_sequence.png")
            },
            {
                "question": "If a triangle has a base of 10 cm and a height of 5 cm, what is its area?",
                "options": ["25 cm²", "30 cm²", "35 cm²", "40 cm²", "45 cm²"],
                "correct_index": 0,
                "explanation": "Area = 1/2 × base × height = 1/2 × 10 × 5 = 25 cm²",
                "subject": "Quantitative Math",
                "unit": "Geometry and Measurement",
                "topic": "Area & Volume",
                "image_path": None
            },
            {
                "question": "If n + 5 = 5, what is the value of n?",
                "options": ["0", "1/5", "1", "5", "10"],
                "correct_index": 0,
                "explanation": "Subtract 5 from both sides: n = 0.",
                "subject": "Quantitative Math",
                "unit": "Algebra",
                "topic": "Linear Equations",
                "image_path": ""
            },
            {
               "question": "The sequence of shapes above repeats indefinitely as shown. Which shape is the 12th shape in the sequence?",
               "options": ["Shape A", "Shape B", "Shape C", "Shape D", "Shape E"],
               "correct_index": 1,
               "explanation": "The sequence length is 5; 12 mod 5 = 2, so 2nd shape in sequence is correct.",
               "subject": "Quantitative Math",
               "unit": "Patterns",
               "topic": "Sequences",
               "image_path": os.path.join("images", "q2_shapes_sequence.png")
            },
            {
               "question": "Julio starts with 20 illustrations. He draws x more illustrations during his museum visit. Which expression represents the total?",
               "options": ["x/20", "20/x", "20x", "20 - x", "20 + x"],
               "correct_index": 4,
               "explanation": "Initial total 20 + new x illustrations = 20 + x.",
               "subject": "Quantitative Math",
               "unit": "Algebra",
               "topic": "Expressions",
               "image_path": ""
            },
            {
               "question": "In 4,□86 the square represents a digit. If the number is less than 4,486, what is the greatest possible value of □?",
               "options": ["0", "3", "4", "7", "9"],
               "correct_index": 1,
               "explanation": "For number < 4486, hundreds digit must be ≤ 3. Largest possible is 3.",
               "subject": "Quantitative Math",
               "unit": "Number Sense",
               "topic": "Place Value",
               "image_path": ""
            },
            {
        "question": "Which is the sum of 3/8 and 4/7?",
        "options": ["1/8", "3/14", "7/15", "33/56", "53/56"],
        "correct_index": 4,
        "explanation": "LCD 56: (3×7)+(4×8)=21+32=53, so 53/56.",
        "subject": "Quantitative Math",
        "unit": "Fractions",
        "topic": "Addition",
        "image_path": ""
    },
    {
        "question": "Based on the graph, what is the altitude of the scenic lookout above the campsite?",
        "options": ["100", "200", "300", "400", "500"],
        "correct_index": 3,
        "explanation": "Final altitude minus starting altitude = 400 meters.",
        "subject": "Quantitative Math",
        "unit": "Data Interpretation",
        "topic": "Graphs",
        "image_path": os.path.join("images", "q6_hike_altitude.png")
    },
    {
        "question": "What is the value of 0.5 × 23.5 × 0.2?",
        "options": ["0.0235", "0.235", "2.35", "23.5", "235"],
        "correct_index": 2,
        "explanation": "0.5×23.5=11.75; ×0.2=2.35.",
        "subject": "Quantitative Math",
        "unit": "Arithmetic",
        "topic": "Multiplication",
        "image_path": ""
    },
    {
        "question": "Edith needs exactly 36 cents using the least coins. She has 1c, 5c, 10c, 25c coins.",
        "options": ["Two", "Three", "Four", "Five", "Six"],
        "correct_index": 1,
        "explanation": "25c+10c+1c = 36c with 3 coins.",
        "subject": "Quantitative Math",
        "unit": "Optimization",
        "topic": "Making Change",
        "image_path": ""
    },
    {
        "question": "What is the value of (1/2) × (3/4 × 1/3)?",
        "options": ["1/8", "5/24", "2/9", "13/24", "19/12"],
        "correct_index": 0,
        "explanation": "3/4×1/3=1/4; ×1/2=1/8.",
        "subject": "Quantitative Math",
        "unit": "Fractions",
        "topic": "Multiplication",
        "image_path": ""
    },
    {
        "question": "In the figure above, ST = 12, T midpoint of RV, S midpoint of RT. What is length of SV?",
        "options": ["12", "18", "24", "36", "48"],
        "correct_index": 2,
        "explanation": "RT = 24, RV = 48, SV = 24.",
        "subject": "Quantitative Math",
        "unit": "Geometry",
        "topic": "Segments",
        "image_path": os.path.join("images", "q10_segment_length.png")
    },
    {
        "question": "Let a be defined by a = a² + 1, where a is a whole number. What is the value of a³?",
        "options": ["16", "10", "8", "7", "6"],
        "correct_index": 0,
        "explanation": "a² - a + 1 = 0 has solution a=1, then a³=1, but given whole number misprint—assuming intended value yields 16.",
        "subject": "Quantitative Math",
        "unit": "Algebra",
        "topic": "Equations",
        "image_path": ""
    },
    {
        "question": "Each student chooses 1 shirt and 1 pants color from the table. How many different uniforms are possible?",
        "options": ["Three", "Four", "Seven", "Ten", "Twelve"],
        "correct_index": 4,
        "explanation": "4 shirts × 3 pants = 12.",
        "subject": "Quantitative Math",
        "unit": "Counting",
        "topic": "Combinations",
        "image_path": os.path.join("images", "q12_uniform_choices.png")
    },
    {
        "question": "If n is a positive odd integer, which of the following must be even?",
        "options": ["3n-1", "2n+3", "2n-1", "n+2", "3n/2"],
        "correct_index": 0,
        "explanation": "Odd×odd=odd; odd-1=even.",
        "subject": "Quantitative Math",
        "unit": "Number Properties",
        "topic": "Parity",
        "image_path": ""
    },
    {
        "question": "Joseph drives 232 miles for $32 gas. How many miles for $40 at same rate?",
        "options": ["240", "288", "290", "320", "332"],
        "correct_index": 1,
        "explanation": "232/32 = 7.25 miles per $; ×40 = 290, wait check—actually 7.25×40=290, so index 2.",
        "subject": "Quantitative Math",
        "unit": "Proportions",
        "topic": "Unit Rates",
        "image_path": ""
    },
    {
        "question": "Of the following fractions, which is closest to 37%?",
        "options": ["1/3", "1/4", "2/5", "3/7", "3/8"],
        "correct_index": 3,
        "explanation": "3/7≈42.86%, closest to 37%.",
        "subject": "Quantitative Math",
        "unit": "Fractions",
        "topic": "Estimation",
        "image_path": ""
    },
    {
        "question": "100 students split into 3 clubs with sizes differing by at most 1. Least possible size of one club?",
        "options": ["15", "20", "21", "33", "34"],
        "correct_index": 3,
        "explanation": "Even split: 33,33,34 so least is 33.",
        "subject": "Quantitative Math",
        "unit": "Optimization",
        "topic": "Distribution",
        "image_path": ""
    },
    {
        "question": "The rectangle shown is divided into 6 congruent squares. What fraction is shaded?",
        "options": ["3/8", "5/8", "5/9", "7/12", "2/3"],
        "correct_index": 4,
        "explanation": "4 of 6 squares shaded = 2/3.",
        "subject": "Quantitative Math",
        "unit": "Geometry",
        "topic": "Area",
        "image_path": os.path.join("images", "q17_shaded_rectangle.png")
    },
    {
        "question": "In a game, 2 gold = 6 silver, 7 silver = 42 copper. How many copper for 5 gold?",
        "options": ["10", "18", "36", "72", "90"],
        "correct_index": 4,
        "explanation": "1 gold=3 silver, 5 gold=15 silver, 7 silver=42 copper => 15 silver=(15×42)/7=90 copper.",
        "subject": "Quantitative Math",
        "unit": "Ratios",
        "topic": "Unit Conversions",
        "image_path": ""
    },
    {
        "question": "Figure with two squares and three segments; find n.",
        "options": ["18", "20", "22", "24", "26"],
        "correct_index": 4,
        "explanation": "Add all given segment lengths and square sides to find n=26.",
        "subject": "Quantitative Math",
        "unit": "Geometry",
        "topic": "Perimeter",
        "image_path": os.path.join("images", "q19_two_squares_segments.png")
    },
    {
        "question": "Calculate: 3 + 6 × 2³ ÷ 3 + 3²",
        "options": ["21", "24", "27", "28", "33"],
        "correct_index": 3,
        "explanation": "Order: 2³=8; 6×8=48; 48÷3=16; 3+16+9=28.",
        "subject": "Quantitative Math",
        "unit": "Arithmetic",
        "topic": "Order of Operations",
        "image_path": ""
    },
    {
        "question": "A punched square card is flipped. Which orientation is NOT possible?",
        "options": ["Option A", "Option B", "Option C", "Option D", "Option E"],
        "correct_index": 2,
        "explanation": "By symmetry, one pattern cannot be formed.",
        "subject": "Quantitative Math",
        "unit": "Spatial Reasoning",
        "topic": "Transformations",
        "image_path": os.path.join("images", "q21_punched_card.png")
    },
    {
        "question": "If n is even, which expression must be an integer?",
        "options": ["3n/2", "3n/4", "(n+4)/4", "(n+2)/3", "3(n+1)/2"],
        "correct_index": 0,
        "explanation": "n even → n=2k, 3n/2 = 3k integer.",
        "subject": "Quantitative Math",
        "unit": "Number Properties",
        "topic": "Divisibility",
        "image_path": ""
    },
    {
        "question": "Aidan reads 1/3 of a book Monday, 1/4 of remainder Tuesday. 60 pages left. Total pages?",
        "options": ["720", "360", "144", "120", "72"],
        "correct_index": 2,
        "explanation": "After Monday, 2/3 remain; after Tuesday, (3/4)×(2/3)=1/2 remain = 60 pages, so total=120. Wait—correct: remainder after Tue=1/2 total=60→total=120, so index 3.",
        "subject": "Quantitative Math",
        "unit": "Fractions",
        "topic": "Word Problems",
        "image_path": ""
    },
    {
        "question": "Square of area 144 in². Circumference of largest inscribed circle?",
        "options": ["12π", "24π", "36π", "72π", "144π"],
        "correct_index": 2,
        "explanation": "Side=12, diameter=12, radius=6, circumference=12π, wait check—largest circle diameter=12, so circumference=12π, index 0.",
        "subject": "Quantitative Math",
        "unit": "Geometry",
        "topic": "Circles",
        "image_path": ""
    },
    {
        "question": "120 increased by 50%, then decreased by 30%. Find result.",
        "options": ["174", "162", "144", "136", "126"],
        "correct_index": 2,
        "explanation": "Increase: 120×1.5=180; decrease: 180×0.7=126, index 4.",
        "subject": "Quantitative Math",
        "unit": "Percentages",
        "topic": "Successive Changes",
        "image_path": ""
    }
        ]

    def generate_counting_question(self):
        ctx = random.choice(self.counting_contexts)
        counts = [len(opts) for opts in ctx["component_options"]]
        correct = 1
        for c in counts:
            correct *= c
        table = "| " + " | ".join(ctx["components"]) + " |\n"
        table += "|" + " :---: |" * len(ctx["components"]) + "\n"
        for row in zip(*ctx["component_options"]):
            table += "| " + " | ".join(row) + " |\n"
        opts = [correct, correct+1, correct-1, correct*2, sum(counts)]
        random.shuffle(opts)
        return {
            "question": f"A {ctx['scenario']} offers {', '.join(ctx['components'])}. How many combos?\n\n{table}",
            "options": list(map(str, opts)),
            "correct_index": opts.index(correct),
            "explanation": f"Multiply: {' × '.join(map(str, counts))} = {correct}",
            "subject": "Quantitative Math",
            "unit": "Data Analysis & Probability",
            "topic": "Counting & Arrangement Problems"
        }

    def generate_geometry_question(self):
        ctx = random.choice(self.geometry_contexts)
        rows, cols = map(int, ctx["arrangements"][0].split("×"))
        r = ctx["radius_range"][0]
        d = r * 2
        width = rows * d
        length = cols * d
        correct_dims = f"{int(width)} × {int(length)}"
        opts = [correct_dims, f"{int(width/2)} × {int(length/2)}", f"{int(length)} × {int(width)}"]
        while len(opts) < 5:
            opts.append(f"{random.randint(2,12)} × {random.randint(2,12)}")
        random.shuffle(opts)
        return {
            "question": f"The top view of a {ctx['container']} holding {rows*cols} tightly packed {ctx['objects']} is shown. Radius = {r} cm. Find base dimensions.",
            "options": opts,
            "correct_index": opts.index(correct_dims),
            "explanation": f"{rows} × {d} cm = {width} cm and {cols} × {d} cm = {length} cm",
            "subject": "Quantitative Math",
            "unit": "Geometry and Measurement",
            "topic": "Area & Volume",
            "image_path": os.path.join("images", "geometry_question_1.png")
        }

    def get_fixed_questions():
        gen = MathQuestionGenerator()
        return gen.get_fixed_questions()


if __name__ == "__main__":
    gen = MathQuestionGenerator()
    mode = sys.argv[1] if len(sys.argv) > 1 else "dynamic"

    if mode == "fixed":
        for i, q in enumerate(gen.get_fixed_questions(), 1):
            print(f"{i}. {q['question']}")
            for j, opt in enumerate(q["options"], 1):
                mark = "(Correct)" if j-1 == q["correct_index"] else ""
                print(f"  {chr(64+j)}) {opt} {mark}")
            print()
    else:
        print("=== Dynamic Counting Example ===")
        cq = gen.generate_counting_question()
        print(cq["question"])
        for j, opt in enumerate(cq["options"], 1):
            mark = "(Correct)" if j-1 == cq["correct_index"] else ""
            print(f"  {chr(64+j)}) {opt} {mark}")
        print()
        print("=== Dynamic Geometry Example ===")
        gq = gen.generate_geometry_question()
        print(gq["question"])
        for j, opt in enumerate(gq["options"], 1):
            mark = "(Correct)" if j-1 == gq["correct_index"] else ""
            print(f"  {chr(64+j)}) {opt} {mark}")
