from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn 
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LangChain Server",
    description=" A simple API Server",
    version="1.0",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
    
    )

model = ChatOpenAI()

# ollama llama2
llm = Ollama(model = 'llama2')

promt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
promt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words.")


add_routes(
    app,
    promt1 | model,
    path="/essay",

)
add_routes(
    app,
    promt2 | llm,
    path="/poem",

)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)