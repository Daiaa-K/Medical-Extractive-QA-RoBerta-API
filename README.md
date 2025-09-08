# Medical Extractive QA API

A FastAPI-based question answering system designed for extracting answers from medical contexts using fine tuned roberta base model.

## Features

- **Extractive Question Answering**: Extract precise answers from medical text contexts
- **Batch Processing**: Handle multiple questions simultaneously
- **API Key Authentication**: Secure access with API key validation
- **Health Check Endpoint**: Monitor API status and configuration
- **CORS Support**: Cross-origin resource sharing enabled
- **GPU/CPU Support**: Automatic device detection for optimal performance

## Requirements

- Python 3.8+
- transformers==4.44.0
- datasets==2.21.0
- matplotlib==3.9.2
- accelerate>=0.20.1b
- fastapi==0.116.1
- python-multipart==0.0.20
- uvicorn==0.35.0
- pydantic==2.11.5
- torch==2.7.0+cpu
- CUDA-compatible GPU (optional, for better performance)

I used cpu becuase thats what i have, it is better to use GPU.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd medical-extractive-qa-api
cd src
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables by creating a `.env` file:
```env
APP_NAME=Medical Extractive QA API
APP_VERSION=1.0.0
APP_DESCRIPTION=API for extracting answers from medical contexts
API_KEY=your-secret-api-key
MODEL_CHKPT=your-huggingface-model-checkpoint
MAX_INPUT_LENGTH=512
HF_TOKEN=your-huggingface-token
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Health Check
```
GET /health
```
Returns the API status and configuration information.

**Headers:**
- `X-API-KEY`: Your API key

**Response:**
```json
{
  "app_name": "Medical Extractive QA API",
  "app_version": "1.0.0",
  "app_description": "API for extracting answers from medical contexts",
  "status": "Healthy"
}
```

### Question Answering
```
POST /answer
```
Extract answers from medical context based on provided questions.

**Headers:**
- `X-API-KEY`: Your API key
- `Content-Type`: application/json

**Request Body:**
```json
{
  "questions": [
    "Has the patient ever taken glyburide for their diabetes mellitus?",
    "What dose of Lasix was given for edema management?",
    "What antibiotic was given for pneumonia?"
  ],
  "context": "Mrs. Wetterauer is a 54-year-old female with coronary artery disease... [medical context text]"
}
```

**Response:**
```json
{
  "answers": [
    {
      "question": "Has the patient ever taken glyburide for their diabetes mellitus?",
      "answer": "Glyburide 5 mg p.o. q.d."
    },
    {
      "question": "What dose of Lasix was given for edema management?",
      "answer": "increase in her Lasix"
    },
    {
      "question": "What antibiotic was given for pneumonia?",
      "answer": "clindamycin 600 mg"
    }
  ]
}
```


## Project Structure

```
medical-extractive-qa-api/
├── app/
│   ├── api/
│   │   ├── answer.py          # QA endpoint
│   │   └── healthy.py         # Health check endpoint
│   ├── core/
│   │   └── config.py          # Configuration and model loading
│   ├── schemas/
│   │   └── schemas.py         # Pydantic models
│   └── services/
│       └── QAservice.py       # Core QA logic
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## Configuration

The API uses environment variables for configuration:

- `APP_NAME`: Application name
- `APP_VERSION`: Version number
- `APP_DESCRIPTION`: Application description
- `API_KEY`: Secret key for API authentication
- `MODEL_CHKPT`: Hugging Face model checkpoint identifier
- `MAX_INPUT_LENGTH`: Maximum input sequence length for the model
- `HF_TOKEN`: Hugging Face authentication token

## Model Information

This API uses fine-tuned big bird roberta base model for extractive question answering. The model automatically detects the best answer span within the provided context for each question.

**Supported Models:**
- Any Hugging Face model compatible with `AutoModelForQuestionAnswering`
- Recommended: BioBERT, ClinicalBERT, or other medical domain-specific models, better used with long sequence models
- My model: `Diaa-K/bigbird-roberta-base-finetuned-emrqa-msquad`

## Error Handling

The API includes comprehensive error handling:
- **403 Forbidden**: Invalid or missing API key
- **500 Internal Server Error**: Model inference errors or invalid answer spans
- **422 Unprocessable Entity**: Invalid request format

## Performance Considerations

- **GPU Usage**: The API automatically uses CUDA if available
- **Batch Processing**: Multiple questions are processed efficiently in sequence
- **Input Truncation**: Long contexts are automatically truncated to fit model limits
- **Memory Management**: Models are loaded once at startup for optimal performance

## License

Apache License 2.0


## Support

For questions or issues, please contact [diaa.kotb42@gmail.com](mailto:diaa.kotb42@gmail.com).