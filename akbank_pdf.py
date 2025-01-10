"""from PyPDF2 import PdfReader

pdf_file = "mart 2024-akbank.PDF"
reader = PdfReader(pdf_file)

text = ""
for page in reader.pages:
    text += page.extract_text()
print(0)
print(text)


import pdfplumber

pdf_file = "/home/damla_ucar/DSA210_Fall_2024_Term_Project/mart 2024-akbank.PDF"
text = ""

with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

if text.strip():
    print(text)
else:
    print("No text could be extracted. The PDF might be image-based.")


from pdf2image import convert_from_path
from pytesseract import image_to_string

# Path to your PDF file
pdf_file = "mart 2024-akbank.PDF"

# Convert PDF pages to images
pages = convert_from_path(pdf_file)

# Initialize an empty string to store extracted text
extracted_text = ""

# Perform OCR on each page
for i, page in enumerate(pages):
    print(f"Processing page {i + 1}...")
    extracted_text += image_to_string(page, lang="eng")  # Use 'eng' for English OCR

# Save the extracted text to a file for review
with open("extracted_text.txt", "w") as text_file:
    text_file.write(extracted_text)

print("Text extraction complete. Check 'extracted_text.txt'.")"""
"""
import os
from PyPDF2 import PdfReader
import pdfplumber
from pdf2image import convert_from_path
from pytesseract import image_to_string

# Function to extract text from PDF using PyPDF2
def extract_text_pypdf2(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error with PyPDF2: {e}")
        return None

# Function to extract text from PDF using pdfplumber
def extract_text_pdfplumber(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error with pdfplumber: {e}")
        return None

# Function to extract text using OCR with pdf2image and pytesseract
def extract_text_ocr(pdf_file):
    try:
        # Convert PDF pages to images
        pages = convert_from_path(pdf_file)

        # Initialize an empty string to store extracted text
        extracted_text = ""

        # Perform OCR on each page
        for i, page in enumerate(pages):
            print(f"Processing page {i + 1}...")
            extracted_text += image_to_string(page, lang="eng")  # Use 'eng' for English OCR

        return extracted_text
    except Exception as e:
        print(f"Error with OCR: {e}")
        return None

# Function to combine all extraction methods
def extract_text_from_pdf(pdf_file):
    # First attempt: PyPDF2
    text = extract_text_pypdf2(pdf_file)
    if text:
        print("Text extracted using PyPDF2.")
        return text

    # Second attempt: pdfplumber
    text = extract_text_pdfplumber(pdf_file)
    if text:
        print("Text extracted using pdfplumber.")
        return text

    # Third attempt: OCR (pdf2image + pytesseract)
    text = extract_text_ocr(pdf_file)
    if text:
        print("Text extracted using OCR.")
        return text

    # If no text could be extracted, return None
    return None

# Main part of the script
pdf_file = "mart 2024-akbank.PDF"

# Try to extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_file)

# If text is extracted, print it or save to a file
if extracted_text and extracted_text.strip():
    print(extracted_text)  # Optionally, print the extracted text
    # Optionally, save to a file
    with open("extracted_text.txt", "w") as text_file:
        text_file.write(extracted_text)
else:
    print("No text could be extracted. The PDF might be image-based or poorly structured.")

"""
"""
import os
from PyPDF2 import PdfReader
import pdfplumber
from pdf2image import convert_from_path
from pytesseract import image_to_string

# Function to extract text from PDF using PyPDF2
def extract_text_pypdf2(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error with PyPDF2: {e}")
        return None

# Function to extract text from PDF using pdfplumber
def extract_text_pdfplumber(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error with pdfplumber: {e}")
        return None

# Function to extract text using OCR with pdf2image and pytesseract
def extract_text_ocr(pdf_file):
    try:
        # Convert PDF pages to images
        pages = convert_from_path(pdf_file)

        # Initialize an empty string to store extracted text
        extracted_text = ""

        # Perform OCR on each page
        for i, page in enumerate(pages):
            print(f"Processing page {i + 1}...")
            extracted_text += image_to_string(page, lang="eng")  # Use 'eng' for English OCR

        return extracted_text
    except Exception as e:
        print(f"Error with OCR: {e}")
        return None

# Function to combine all extraction methods
def extract_text_from_pdf(pdf_file):
    # First attempt: PyPDF2
    text = extract_text_pypdf2(pdf_file)
    if text:
        print("Text extracted using PyPDF2.")
        return text

    # Second attempt: pdfplumber
    text = extract_text_pdfplumber(pdf_file)
    if text:
        print("Text extracted using pdfplumber.")
        return text

    # Third attempt: OCR (pdf2image + pytesseract)
    text = extract_text_ocr(pdf_file)
    if text:
        print("Text extracted using OCR.")
        return text

    # If no text could be extracted, return None
    return None

# Function to filter the extracted text based on specific keywords
def filter_transactions(text):
    # Define the list of places to search for in the text
    places = ["Starbucks", "Coffee", "Fasshane", "Simit Sarayı", "EspressoLab"]
    
    # Filter the extracted text to include only lines containing any of the specified places
    filtered_lines = []
    for line in text.splitlines():
        if any(place.lower() in line.lower() for place in places):
            filtered_lines.append(line)
    
    return "\n".join(filtered_lines)

# Main part of the script
pdf_file = "mart 2024-akbank.PDF"

# Try to extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_file)

# If text is extracted, filter it and print or save to a file
if extracted_text and extracted_text.strip():
    print("Extracted and filtered transactions:")
    filtered_text = filter_transactions(extracted_text)
    
    # Print the filtered text
    print(filtered_text)
    
    # Optionally, save to a file
    with open("filtered_extracted_text.txt", "w") as text_file:
        text_file.write(filtered_text)
else:
    print("No text could be extracted. The PDF might be image-based or poorly structured.")



"""



#import os
from PyPDF2 import PdfReader
import pdfplumber
from pdf2image import convert_from_path
from pytesseract import image_to_string

# Function to extract text from PDF using PyPDF2
def extract_text_pypdf2(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error with PyPDF2: {e}")
        return None

# Function to extract text from PDF using pdfplumber
def extract_text_pdfplumber(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error with pdfplumber: {e}")
        return None

# Function to extract text using OCR with pdf2image and pytesseract
def extract_text_ocr(pdf_file):
    try:
        # Convert PDF pages to images
        pages = convert_from_path(pdf_file)

        # Initialize an empty string to store extracted text
        extracted_text = ""

        # Perform OCR on each page
        for i, page in enumerate(pages):
            print(f"Processing page {i + 1}...")
            extracted_text += image_to_string(page, lang="eng")  # Use 'eng' for English OCR

        return extracted_text
    except Exception as e:
        print(f"Error with OCR: {e}")
        return None

# Function to combine all extraction methods
def extract_text_from_pdf(pdf_file):
    # First attempt: PyPDF2
    text = extract_text_pypdf2(pdf_file)
    if text:
        print("Text extracted using PyPDF2.")
        return text

    # Second attempt: pdfplumber
    text = extract_text_pdfplumber(pdf_file)
    if text:
        print("Text extracted using pdfplumber.")
        return text

    # Third attempt: OCR (pdf2image + pytesseract)
    text = extract_text_ocr(pdf_file)
    if text:
        print("Text extracted using OCR.")
        return text

    # If no text could be extracted, return None
    return None

# Updated function to filter transactions
def filter_transactions(text):
    # Normalize text by removing spaces within words
    normalized_text = text.replace(" ", "").upper()
    
    # Define the list of places to search for in the normalized text
    places = ["STARBUCKS", "SBX", "YUKSELEN", "SARAY", "EKMOT", "LOKMA", "062P", "COFFY", "010SABAN"]
    
    # Filter the extracted text to include only lines containing any of the specified places
    filtered_lines = []
    for line in text.splitlines():
        normalized_line = line.replace(" ", "").upper()
        if any(place in normalized_line for place in places):
            filtered_lines.append(line)
    
    return "\n".join(filtered_lines)

def using_multiple_pdf_files(pdf_file):
    extracted_text = extract_text_from_pdf(pdf_file)
    if extracted_text and extracted_text.strip():
        print("Extracted and filtered transactions:")
        filtered_text = filter_transactions(extracted_text)
        print(filtered_text)
        with open("filtered_extracted_text.txt", "w") as text_file:
            text_file.write(filtered_text)
    else:
        print("No text could be extracted.") 
    return None
# Main part of the script
using_multiple_pdf_files("mart 2024-akbank.PDF")
using_multiple_pdf_files("nisan 2024-akbank.PDF")
using_multiple_pdf_files("mayıs 2024-akbank.PDF")
using_multiple_pdf_files("haziran 2024-akbank.PDF")
using_multiple_pdf_files("eylül 2024-akbank.PDF")
using_multiple_pdf_files("ekim 2024-akbank.PDF")
using_multiple_pdf_files("kasım 2024-akbank.PDF")


# Try to extract text from the PDF
#extracted_text = extract_text_from_pdf(pdf_file)

# If text is extracted, filter it and print or save to a file
#if extracted_text and extracted_text.strip():
    #print("Extracted and filtered transactions:")
    #filtered_text = filter_transactions(extracted_text)
    
    # Print the filtered text
    #print(filtered_text)
    
    # Optionally, save to a file
    #with open("filtered_extracted_text.txt", "w") as text_file:
        #text_file.write(filtered_text)
#else:
    #print("No text could be extracted.") 

# ekmot gıda anonim = espressolab
# sımıt sarayı anonim = simit sarayı
# atlı otomotiv = opet
# self gıda sanayi = piazza
# paytr/matık = otomat
# 7036 istanbul sabancı = şok
# pizza restaurantları = coffy
# sbx ist sabancı üniv = starbucks
# yukselen yıldız turı = fasshane
# Hmr restoran gıda = pizza bulls
# sabancı coffy = coffy
# 010sabancı üniversitesi = coffy (mart)
# 062sabancı üniversitesi = yemekhane
# kadıköy coffy = bunu çıkar
# sımıt sarayı viaport = bunu çıkart
# SBX ist opet atlı = starbucks opet
# starbucks ist viaport = çıkart
# Lokma Restoran = espresso lab
