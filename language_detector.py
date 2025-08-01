from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # for consistent results

def detect_language(text):
    try:
        return detect(text)
    except:
        return "Could not detect"

# Test with input
sample_text = input("Enter text to detect language: ")
language = detect_language(sample_text)
print(f"Detected language: {language}")
