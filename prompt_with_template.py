# 2. Bekerja Dengan Prompt
# Membuat Bot Surat Pengantar

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
import gradio as gr

openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key

# Mendefinisikan model AI
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key= openai_api_key
)

# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
prompt = PromptTemplate(
    input_variables=["posisi", "perusahaan", "keterampilan"],
    template="Yang terhormat HRD Manajer {perusahaan},\n\nDengan surat ini, saya [NAMA KAMU], ingin melamar untuk posisi {posisi} di {perusahaan}. Saya memiliki pengalaman di bidang {keterampilan}. Terima kasih telah mempertimbangkan lamaran saya.\n\nHormat saya,\n[NAMA KAMU]",
)

# Define a function to generate a cover letter using the llm and user input
def generate_cover_letter(posisi: str, perusahaan: str, keterampilan: str) -> str:
    formatted_prompt = prompt.format(posisi=posisi, perusahaan=perusahaan, keterampilan=keterampilan)
    response = llm.invoke(formatted_prompt).content
    return response

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Posisi"),
    gr.Textbox(label="Perusahaan"),
    gr.Textbox(label="Keterampilan")
]

# Define the Gradio interface output
output = gr.Textbox(label="Template Surat")

# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(server_name="0.0.0.0", server_port= 7860, share=True)

# Practice Define for Step by step output
def chatbot(user_input):
    # defining a template
    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return llm.invoke(formated_prompt).content

# Practice for step by step output (Comment (# Launch the Gradio interface) above)
#gr.Interface(fn=chatbot, inputs="text", outputs="text").launch(share=True)