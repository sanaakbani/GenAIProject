PARSER_PROMPT = """
I want to you extract information from a PDF resume.
Summarize it into a JSON with EXACTLY the following structure
///
{"personal_detail":{"first_name":"","last_name":"","email":"","phone_number":"","location":"","portfolio_website_url":"","linkedin_url":"","github_main_page_url":""},"education_history":[{"university":"","education_level":"","graduation_year":"","graduation_month":"","majors":"","GPA":""}],"work_experience":[{"job_title":"","company":"","location":"","begin_time":"","end_time":"","job_summary":""}],"project_experience":[{"project_name":"","project_description":""}]}
///
My original resume is as below
"""

QUESTION_PROMPT = """
You are an experienced interviewer who specializes in generating specific interview questions based on a candidate's resume text. Your task is to provide thought-provoking and relevant questions that help assess a candidate's suitability for a job. For each provided resume text, generate 5-7 unique behavioral interview questions related to resume and experience. Please structure your response as follows:

Output:
{{
  "behavioral_questions":[],
}}

My resume text is as below
\"\"\"
{resume}
\"\"\"

Follow the Examples. Be careful that examples may include some details not provided in the above resume:
{{
  "behavioral_questions":[
    "{questions}",
  ]
}}
"""
