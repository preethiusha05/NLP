import pandas as pd
from config import client
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "products.csv")


def generate_eda_report(file_path):
    df = pd.read_csv(file_path)

    sample_data = df.head(10).to_dict(orient="records")

    # Structured Prompt
    prompt = f"""
Role: Data Scientist  

Task:  
Analyze the dataset and generate insights  

Context:  
Dataset sample:
{sample_data}  

Format:  
1. Column-wise Insights  
2. Overall Insights  
3. Missing Value Handling  
4. Outlier Handling  
5. Visualization Suggestions  
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    report = generate_eda_report(file_path)
    print("\nEDA REPORT:\n")
    print(report)