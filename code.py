import fitz
import json
import re

def extract_questions_and_answers(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = "\n".join([page.get_text("text") for page in doc])
    
    questions = []
    question_id = 1
    
    mcq_pattern = re.findall(r'Q\.\d+\s*(.?)\s\n\s*\(A\)\s*(.?)\s\(B\)\s*(.?)\s\(C\)\s*(.?)\s\(D\)\s*(.?)\s\n', full_text, re.DOTALL)
    
    for match in mcq_pattern:
        questions.append({
            "question_id": question_id,
            "question_type": "MCQ",
            "question_text": match[0].strip(),
            "answer_choices": {
                "A": match[1].strip(),
                "B": match[2].strip(),
                "C": match[3].strip(),
                "D": match[4].strip()
            },
            "correct_answer": None  
        })
        question_id += 1
    
    descriptive_pattern = re.findall(r'Q\.\d+\s*(.*?)\?', full_text, re.DOTALL)
    
    for match in descriptive_pattern:
        questions.append({
            "question_id": question_id,
            "question_type": "Descriptive",
            "question_text": match.strip() + "?",
            "answer_choices": [],
            "correct_answer": None
        })
        question_id += 1
    
    answer_key_match = re.search(r'Answer\s*Key[:\s\n](.)', full_text, re.DOTALL)
    if answer_key_match:
        answer_key_text = answer_key_match.group(1)
        answer_lines = re.findall(r'Q\.\d+\s*:\s*([A-D])', answer_key_text)
        for i, answer in enumerate(answer_lines):
            if i < len(questions) and questions[i]["question_type"] == "MCQ":
                questions[i]["correct_answer"] = answer
    
    return questions

pdf_path = "2024_1_English.pdf"
questions_data = extract_questions_and_answers(pdf_path)

json_output_path = "questions_output.json"
with open(json_output_path, "w", encoding="utf-8") as json_file:
    json.dump(questions_data, json_file, indent=4)

print(f"Questions saved to {json_output_path}")
