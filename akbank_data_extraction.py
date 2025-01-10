from pdf2image import convert_from_path
from pytesseract import image_to_string

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
        print("Text extracted using OCR.")
        return extracted_text
    except Exception as e:
        print(f"Error with OCR: {e}")
        return None

# Updated function to filter transactions
def filter_transactions(text):
    # Define the list of places to search for in the normalized text
    places = ["STARBUCKS", "SBX", "YUKSELEN", "SARAY", "EKMOT", "LOKMA", "062P", "COFFY", "010SABAN"]
    count_coffee = {
        "Starbucks" : 0,
        "Coffy" : 0,
        "Simit Sarayı" : 0,
        "Fasshane" : 0,
        "Espressolab" : 0
    }
    # Filter the extracted text to include only lines containing any of the specified places
    filtered_lines = []
    for line in text.splitlines():
        normalized_line = line.replace(" ", "").upper()
        if any(place in normalized_line for place in places):
            if (("STARBUCKS" in normalized_line or "SBX" in normalized_line) and "PORT" not in normalized_line):
                count_coffee["Starbucks"] += 1
                filtered_lines.append(line)
            elif ("YUKSELEN" in normalized_line):
                count_coffee["Fasshane"] += 1
                filtered_lines.append(line)
            elif ("SARAY" in normalized_line and "PORT" not in normalized_line):
                count_coffee["Simit Sarayı"] += 1
                filtered_lines.append(line)
            elif ("EKMOT" in normalized_line or "LOKMA" in normalized_line):
                count_coffee["Espressolab"] += 1
                filtered_lines.append(line)
            elif (("062P" in normalized_line or "COFFY" in normalized_line or "010SABAN" in normalized_line) and "KOY" not in normalized_line):
                count_coffee["Coffy"] += 1
                filtered_lines.append(line)
    for item in count_coffee:
        print(item, " and " ,count_coffee[item])
        
    return "\n".join(filtered_lines)

def using_multiple_pdf_files(pdf_file):
    extracted_text = extract_text_ocr(pdf_file)
    if extracted_text and extracted_text.strip():
        print("Extracted and filtered transactions:")
        filtered_text = filter_transactions(extracted_text)
        print(filtered_text)
        with open("filtered_extracted_text.txt", "a") as text_file:
            text_file.write("\n")
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

with open("akbank-aralık.txt", "r") as aralik_file:
    aralik_lines = []
    for line in aralik_file:
        line = line.strip()
        if not line:
            continue
        aralik_lines.append(line)
    aralik_text = "\n".join(aralik_lines)

with open("filtered_extracted_text.txt", "r") as txt_file:
    extra_filtered_lines = []
    information = ""
    for line in txt_file:
        line = line.strip()
        if not line:
            continue
        normalized_line = line.replace(" ", "").upper()
        date = line[:10]
        places = ["STARBUCKS", "SBX", "YUKSELEN", "SARAY", "EKMOT", "LOKMA", "062P", "COFFY", "010SABAN"]
        if any(place in normalized_line for place in places):
            if (("STARBUCKS" in normalized_line or "SBX" in normalized_line) and "PORT" not in normalized_line):
                company = "Starbucks"
            elif ("YUKSELEN" in normalized_line):
                company = "Fasshane"
            elif ("SARAY" in normalized_line and "PORT" not in normalized_line):
                company = "Simit Sarayı"
            elif ("EKMOT" in normalized_line or "LOKMA" in normalized_line):
                company = "Espressolab"
            elif (("062P" in normalized_line or "COFFY" in normalized_line or "010SABAN" in normalized_line) and "KOY" not in normalized_line):
                company = "Coffy"
        information = date + " " + company
        extra_filtered_lines.append(information)
    extra_filtered_text = "\n".join(extra_filtered_lines)
    print (" ")
    print (" ")
    print(extra_filtered_text)
    with open("company_date_filtered_text.txt", "a") as txt_filtered_file:
        txt_filtered_file.write("\n")
        txt_filtered_file.write(extra_filtered_text)
        txt_filtered_file.write("\n")
        txt_filtered_file.write(aralik_text)
        


    



