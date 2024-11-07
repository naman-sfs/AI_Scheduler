from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter
from .prompt import *
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'


class SCHEDULER:
    def __init__(self):
        self.name = "AI Scheduler"
        self.model = "gpt-4o-mini"
        
    #****************************SINGLETON OBJECT*******************************
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SCHEDULER, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    #***************************************************************************
    
    def create_events(self,date, input):
        prompt = PromptTemplate.from_template(event_prompt)
        llm = ChatOpenAI(model_name=self.model,temperature=0.7)
        llm_chain = (
            {"date":itemgetter("date"),
             "input": itemgetter("input")} 
            | prompt
            | llm
            | StrOutputParser()
        )
        answer = llm_chain.invoke({"date":date,"input":input})
        return answer
    
    
    def create_goals(self,date, input):
        prompt = PromptTemplate.from_template(goal_prompt)
        llm = ChatOpenAI(model_name=self.model,temperature=0.7)
        llm_chain = (
            {"date":itemgetter("date"),
             "input": itemgetter("input")} 
            | prompt
            | llm
            | StrOutputParser()
        )
        answer = llm_chain.invoke({"date":date,"input":input})
        return answer
    
    