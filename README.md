# Meraki_labs

Overview
This project extracts questions, answer choices, and equations from JEE Advanced PDFs and structures them into a JSON format. It handles text-based and image-based equations using OCR.


Tools & Resources Utilized

Python → Core language for processing
PyMuPDF (fitz) → Extracts text from PDFs
Regular Expressions (Regex) → Identifies questions, answer choices, and answer keys
JSON → Stores extracted questions in a structured format

Approach to the Problem

1️⃣ Extract Text from PDF
Used PyMuPDF (fitz) to read text from the document.
Extracted text from all pages and combined it into a single string.

2️⃣ Extract Multiple-Choice Questions (MCQs)
Used regex to detect MCQ patterns with four options (A, B, C, D).
Stored each question with its answer choices.

3️⃣ Extract Descriptive Questions
Used regex to identify descriptive questions based on question format.
Stored each question separately without answer choices.

4️⃣ Identify Correct Answers
Extracted the answer key section using regex.
Matched answers to their corresponding MCQs.

5️⃣ Store Questions in JSON
Structured the extracted data and saved it in JSON format.
Estimate of Correctly Extracted Questions: 3OCR) → Converts equation images to LaTeX

Approach to the Problem

1️.Extract Text from PDF
Used PyPDF2 to read text from the document.
Identified question boundaries using regex patterns.
2️.Extract Answer Choices & Correct Answer
Used regex to detect multiple-choice options.
Checked for patterns indicating correct answers.
3️. Handle Mathematical Equations & Images
Used pdf2image & OpenCV to detect equation images.
Applied Tesseract OCR & TrOCR to extract LaTeX-formatted equations.

Estimate of Correctly Extracted Questions : 6
(Descriptive questions all are assessed correctly)



