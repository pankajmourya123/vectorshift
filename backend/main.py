from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Adjust this for production to allow specific origins
    allow_methods=['*'],  # Allow all HTTP methods
    allow_headers=['*'],  # Allow all headers
)

class PipelineData(BaseModel):
    nodes: list
    edges: list

@app.post('/pipelines/parse')
def parse_pipeline(data: PipelineData):
    nodes = data.nodes
    edges = data.edges

    num_nodes = len(nodes)
    num_edges = len(edges)

    # Placeholder logic for DAG verification
    is_dag = True  # Replace with actual DAG verification logic

    return {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': is_dag}

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}
# uvicorn main:app --reload
# http://localhost:8000/pipelines/parse