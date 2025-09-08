from dotenv import load_dotenv
import os
from transformers import AutoTokenizer,AutoModelForQuestionAnswering

from huggingface_hub import login
import torch

load_dotenv()

# Load environment variables
APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
APP_DESCRIPTION = os.getenv("APP_DESCRIPTION")
API_KEY = os.getenv("API_KEY")

MODEL_CHKPT = os.getenv("MODEL_CHKPT")
MAX_INPUT_LENGTH = int(os.getenv("MAX_INPUT_LENGTH"))
HF_TOKEN = os.getenv("HF_TOKEN")

# Load model and tokenizer
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

login(token=HF_TOKEN)

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_CHKPT)
    model = AutoModelForQuestionAnswering.from_pretrained(MODEL_CHKPT).to(device)

except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    raise e