from src.question_generator import MathQuestionGenerator

# Initialize generator
gen = MathQuestionGenerator()

# Access fixed questions
fixed_questions = gen._load_fixed_questions()  # Use _load_fixed_questions() directly

# Print questions
for i, q in enumerate(fixed_questions, 1):
    print(f"Question {i}: {q['question']}")
    for j, opt in enumerate(q['options']):
        correct_marker = "(Correct)" if j == q['correct_index'] else ""
        print(f"  {j+1}. {opt} {correct_marker}")
    print(f"Explanation: {q['explanation']}")
    print(f"Subject: {q['subject']}, Unit: {q['unit']}, Topic: {q['topic']}")
    print(f"Image: {q['image_path']}")
    print("-" * 50)
