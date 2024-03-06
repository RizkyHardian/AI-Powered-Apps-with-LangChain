# 1. Model: Interface Umum untuk Berbagai LLM
# Membuat chatbot sederhana

from langchain_openai import ChatOpenAI
import os

# Mengatur environment variable "OPENAI_API_KEY" dengan OpenAI API key milikmu. ini diperlukan untuk proses autentikasi ke OpenAI API.
os.environ["OPENAI_API_KEY"] = "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"

# Mendefinisikan jenis model 
gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )

text = "Berikan fakta menarik tentang kentang!"
print(gpt3.invoke(text).content)