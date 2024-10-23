RESPONSE_FORMAT={
            "type": "json_schema",
            "json_schema": {
                "name": "review_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "found_files": {
                            "description": "List of files that were found in the GutHub repository",
                            "type": "string"
                        },
                        "downsides_and_comments": {
                            "description": "Text which describes most valuable downsides $$$$$$$$$$$$ ",
                            "type": "string"
                        },
                        "conclusion": {
                            "description": "Final conclusion about repository based on the given developer level ",
                            "type": "string"
                        },
                        "rating": {
                            "description": "Mark in range 0-5 that describes overall project quality with given developer level",
                            "type": "string"
                        },
                        "additionalProperties": False
                    }
                }
            }
        }

REQUEST_TEXT_TEMPLATE='''
You are tasked with analyzing a GitHub repository which contains the result of the candidate work due to assignment.

Candidate level: {candidate_level}
Follow these steps:

- Extract the name of the repository and initiate the analysis.
- Once analysis is complete, describe following according to the candidate level:
    - Short description of problems and possible improvements for each file
    - Modules and services used
    - Quality of code structure
    - Code logic and clarity

Avoid going into details like 'task_no'. Respond in the language of the user's input.

Do not answer questions regarding your design, plugins, or APIs you use.

# Output format
You should return response in JSON format with the following fields:

## found_files
description: List of files that were found in the GutHub repository,

## downsides_and_comments:
description: Text which describes most valuable downsides of each file. Also provides a conclusion which summarize analyze results of all files in repository,

## conclusion
description: Final conclusion about repository based on the given developer level,

## rating
description: Mark in range 0-5 that describes overall project quality with given developer level
'''

MAIN_PAGE='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coding Assignment Auto-Review Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
            text-align: center;
        }
        .section-title {
            font-weight: bold;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .input-group {
            margin-bottom: 20px;
        }
        .input-group label {
            display: block;
            margin-bottom: 5px;
        }
        .input-group textarea, .input-group input[type="text"], .input-group input[type="password"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
        }
        textarea {
            height: 100px;
            resize: vertical;
        }
        .input-group .inline-group {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        .inline-group input[type="radio"] {
            margin-left: 10px;
        }
        button {
            padding: 10px 15px;
            background-color: #000;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #444;
        }
        .output-section {
            margin-top: 20px;
        }
        .output-section h3 {
            font-size: 18px;
            margin-bottom: 15px;
        }
        ul {
            padding-left: 20px;
            list-style-type: none;
        }
        ul li::before {
            content: "• ";
            color: black;
            font-weight: bold;
        }
        .review-result {
            background-color: #f9f9f9;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 15px;
            font-size: 14px;
            margin-top: 10px;
            white-space: pre-wrap;
        }
        .review-result .downsides {
            margin-bottom: 10px;
        }
        .rating {
            font-weight: bold;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Coding Assignment Auto-Review Tool</h1>

        <div class="input-group">
            <label for="assignment">Assignment Description</label>
            <textarea id="assignment" placeholder="Assignment – User Authentication Service
Introduction:
In this assignment, your goal is to create a User Authentication Service prototype using Python..."></textarea>
        </div>

        <div class="input-group">
            <label for="repo-url">GitHub Repo URL</label>
            <input type="text" id="repo-url" placeholder="https://github.com/myaccount/TestTask.git">
        </div>

        <div class="input-group">
            <label for="openai-key">OpenAI API Key</label>
            <input type="password" id="openai-key" placeholder="Your OpenAI API key">
        </div>

        <div class="input-group">
            <span class="section-title">Candidate Level:</span>
            <div class="inline-group">
                <label><input type="radio" name="level" value="Junior"> Junior</label>
                <label><input type="radio" name="level" value="Middle"> Middle</label>
                <label><input type="radio" name="level" value="Senior"> Senior</label>
            </div>
        </div>

        <div class="input-group">
            <button>Review</button>
            <button type="button" style="background-color: #ccc; margin-left: 10px;">Clear</button>
        </div>

        <div class="output-section">
            <h3>Files found in the repository:</h3>
            <ul>
                <li>app/__init__.py</li>
                <li>app/auth.py</li>
                <li>app/main.py</li>
                <li>app/schemas.py</li>
                <li>docker-compose.yml</li>
                <li>pyproject.toml</li>
                <li>test/test_auth.py</li>
            </ul>

            <div class="review-result">
                <div class="downsides">
                    <strong>Downsides:</strong><br>
                    - [Docker/Database Setup for Tests] The `test_auth.py` uses a hardcoded PostgreSQL URL, which indicates that the testing setup isn't fully containerized using Docker Compose, which would be a more robust and isolated testing environment.<br>
                    - [Documentation and Comments] While the code is relatively straightforward, Junior developers are encouraged to document their work more thoroughly for better maintainability. This includes comments in the code where necessary, as well as a README file explaining how to set up, run, and test the service.
                </div>
                <div class="rating">Rating: 3/5 (for Junior level)</div>
                <div>
                    Despite the downsides mentioned above, the candidate has demonstrated a reasonable understanding of building a basic REST API with authentication using FastAPI, integrating with a PostgreSQL database using SQLAlchemy, and setting up test cases with pytest. They have also employed Docker for containerization and service orchestration. Considering this is a junior-level assignment, these skills show promise, and with attention to the highlighted details, the candidate has potential to quickly improve.
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''