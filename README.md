# Automated document processing

This project aims to automate document processing using NLP (Natural Language Processing) techniques. It utilizes Optical Character Recognition (OCR) to extract text from document images and applies NLP models to process and categorize the extracted text.Additionally, it uses OpenAI for entity extraction from the text.

## Tools and Models Used

### Optical Character Recognition (OCR):
- Tesseract: An open-source OCR engine used for text extraction from document images.

### NLP Models:
- SentenceTransformer: A library for encoding sentences into dense vectors, used for sentence encoding.
- BERT: Pre-trained NLP model for document categorization based on encoded text.

### Database:
- MongoDB: Used for storing document metadata and categorization information.
  
### Entity Extraction:
- OpenAI: Utilized for extracting entities and their values from the provided text.

### Vector Indexing:
- Pinecone: A vector similarity search service used for efficient document indexing and retrieval.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/document-processing-with-nlp.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up Tesseract OCR:

   Download and install Tesseract OCR from the official website (https://github.com/tesseract-ocr/tesseract).

4. Set up MongoDB:

   Install MongoDB and create a new database named "documents".

5. Set up Pinecone:

   Sign up for a Pinecone account (https://www.pinecone.io) and obtain an API key. Initialize Pinecone with the API key in the code.

## Usage

1. Run the main application:

   ```
   python app.py
   ```

2. Use the web-based user interface to upload document images, view results, and search for documents or categories.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators and maintainers of Tesseract, SentenceTransformer, BERT, MongoDB, and Pinecone for their valuable tools and libraries.

- This project was inspired by the need for efficient document processing and organization in various domains.

---
By [Your Name](https://github.com/ChandrashekarM46) | [Project Repository](https://github.com/ChandrashekarM46/document-processing-with-nlp) | [License](LICENSE)
