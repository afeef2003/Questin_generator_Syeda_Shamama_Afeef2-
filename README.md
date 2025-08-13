Generated questions follow the exact specifications provided and maintain mathematical rigor suitable for educational assessments.

# Math Question Generator 🧮

## **By Syeda Shamama Afeef**

An AI-powered tool that generates **curriculum-aligned math questions** with automatic diagrams, professional formatting, and multiple output formats. Designed to demonstrate expertise in **Python, AI, and educational technology**.

---

## 🎯 Project Overview

This project automates the generation of **multiple-choice math questions** in two categories:

* **Counting & Arrangement Problems** – e.g., uniform selection or combination scenarios
* **Geometry & Spatial Reasoning** – e.g., packed object arrangements with visual aids

The tool ensures questions are **mathematically accurate**, curriculum-aligned, and formatted for **professional assessments**.

---

## 🚀 Key Features

* Generates **dynamic and fixed questions** with automatic answer validation
* Creates **diagrams for geometry questions** using `matplotlib`
* Outputs **Word documents** and **formatted text files** suitable for assessment platforms
* Configurable **number of questions** and **difficulty levels**
* Built-in **curriculum mapping** for subject, unit, and topic
* Includes **25 fixed MCQs** for testing and demonstration

---

## 🛠️ Technical Stack

* **Language**: Python 3.8+
* **Libraries**: `python-docx`, `matplotlib`, `numpy`, `Pillow`
* **Core Concepts**:
  - Object-oriented programming for question generation
  - Automated diagram creation for visual questions
  - Curriculum mapping and answer validation
  - File handling and structured output generation

---

## 📁 Project Structure


math-question-generator/

├── src/

│   └── question_generator.py    # Core question generator class

├── main.py                      # Script to generate questions

├── show_fixed.py                # Display 25 fixed MCQs

├── output/                      # Generated Word/text files

├── images/                      # Generated diagrams

├── requirements.txt             # Python dependencies

└── README.md                    # Project documentation



---
## 🎮 Usage

### Generate Questions

```bash
python main.py --output generated_questions.docx --count 5
---


### View Fixed Questions

python show_fixed.py

Displays the 25 built-in MCQs in the terminal.


#### 📝 Example Output Format

@title Middle School Mathematics Assessment
@description Questions designed to test problem-solving in counting and geometry
@question If a triangle has base 10cm and height 5cm, what is its area?
@instruction Choose the correct answer
@difficulty moderate
@Order 1
@option 25 cm²
@@option 30 cm²  # Correct answer marked with @@
@option 35 cm²
@explanation Area = 1/2 × base × height
@subject Quantitative Math
@unit Geometry and Measurement
@topic Area & Volume
@plusmarks 1



## 📊 Project Highlights

* **Automated Diagram Generation** – Top-view layouts for spatial reasoning questions
* **Mathematical Accuracy** – Answers and distractors verified programmatically
* **Professional Deliverables** – Word document, formatted text file, and images
* **Customizable** – Add new templates, adjust difficulty, or change output format easily


## 🧮 Mathematical Accuracy

* All answers are verified programmatically
* Distractors are generated using common mistake patterns
* Explanations provide complete solution steps
* Difficulty can be adjusted via parameters in the generator


## 🎨 Image Generation

* Top-view diagrams of packed objects
* Proper scaling and proportions
* Clear container outlines
* Professional formatting for assessment-ready visuals


## 🔧 Customization

### Adding New Question Templates

Edit `question_generator.py` to add new contexts, shapes, or arrangements:

self.counting_templates = {
    "contexts": ["your_new_context"],
    # ... add more options
}


### Adjusting Difficulty

Modify ranges in the generator methods:

num_options = random.randint(3, 8)  # More options = harder
radius = round(random.uniform(0.5, 5.0), 1)  # Larger range

# 📄 Installation

git clone `<your-repo-url>`
cd math-question-generator
pip install -r requirements.txt
python main.py


# 🔧 Skills Demonstrated

* Python, OOP, modular programming
* AI & algorithmic problem generation
* Data visualization (`matplotlib`)
* File handling and document automation (`python-docx`)
* Educational assessment design and curriculum mapping


# 📜 License

This project is for  **educational assessment purposes** . Please ensure compliance with institutional guidelines when using generated content.


# 🆘 Troubleshooting

**Common Issues:**

* Import errors → Ensure dependencies are installed
* Image generation fails → Check `matplotlib` backend
* Word document issues → Verify `python-docx` installation

**Getting Help:**

* Check the repository issues section
* Test with default parameters first
