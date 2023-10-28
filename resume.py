pip install spacy
python -m spacy download en_core_web_sm
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def match_resume(job_description, candidate_resume):
    # Process the job description and candidate's resume using spaCy
    job_doc = nlp(job_description)
    resume_doc = nlp(candidate_resume)

    # Extract keywords from the job description
    job_keywords = set(token.text.lower() for token in job_doc if not token.is_stop and not token.is_punct)

    # Extract keywords from the candidate's resume
    resume_keywords = set(token.text.lower() for token in resume_doc if not token.is_stop and not token.is_punct)

    # Calculate the intersection of keywords
    matched_keywords = job_keywords.intersection(resume_keywords)

    # Calculate a matching score based on the number of matched keywords
    matching_score = len(matched_keywords) / len(job_keywords)

    return matching_score

if __name__ == "__main__":
    job_description = "We are looking for a software developer with experience in Python, web development, and database management."

    candidate_resume = """
    I am a software developer with strong skills in Python, web development using Django and React, and database management with PostgreSQL.
    """

    score = match_resume(job_description, candidate_resume)

    print(f"Matching Score: {score * 100:.2f}%")
