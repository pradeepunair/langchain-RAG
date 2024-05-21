# Information Retrieval with RAG
Install Dependencies
```python
pip install -r requirements.txt
```
Create Vector DB
```python
python populate_database.py
```
Query the Chroma DB
```python
python query_data.py query --query "Whats the heading of pdf?"
```
Clear the Chroma DB
```python
python query_data.py clear
```
