# Meraki_labs

Overview
This project extracts questions, answer choices, and equations from JEE Advanced PDFs and structures them into a JSON format. It handles text-based and image-based equations using OCR.

Tools & Resources Utilized

Python 
PyPDF2 → Extracts text from PDFs
Regular Expressions (Regex) → Identifies questions & answers
Tesseract OCR → Extracts text from images (for equations)
OpenCV + pdf2image → Extracts images from PDFs
TrOCR (Transformer OCR) → Converts equation images to LaTeX

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

Estimate of Correctly Extracted Questions : 3



