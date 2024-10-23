from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get('/', response_class=HTMLResponse)
async def index():
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
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

        .spinner {
            border: 16px solid #f3f3f3; /* Light grey */
            border-top: 16px solid #3498db; /* Blue */
            border-radius: 50%;
            width: 120px;
            height: 120px;
            animation: spin 2s linear infinite;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        @keyframes spin {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Coding Assignment Auto-Review Tool</h1>

    <div class="input-group">
        <label for="assignment">Assignment Description</label>
        <textarea id="assignment" placeholder="Assignment..."></textarea>
    </div>

    <div class="input-group">
        <label for="repo-url">GitHub Repo URL</label>
        <input type="text" id="repo-url" placeholder="https://github.com/myaccount/TestTask.git">
    </div>

    <div class="input-group">
        <span class="section-title">Candidate Level:</span>
        <div class="inline-group">
            <label><input type="radio" name="level" value="Junior"> Junior</label>
            <label><input type="radio" name="level" value="Middle"> Middle</label>
            <label><input type="radio" name="level" value="Senior"> Senior</label>
        </div>
    </div>

    <div class="input-group" id="button-group">
        <button>Review</button>
        <button type="button" style="background-color: #ccc; margin-left: 10px;">Clear</button>
    </div>

    <div id="loadingCircle" class="spinner" style="display: none;"></div>

    <div class="output-section">
        <h3>Files found in the repository:</h3>
        <ul>
        </ul>

        <div class="review-result">
            <div class="downsides">
                <strong>Downsides:</strong><br>
            </div>
            <div class="rating"></div>
            <div>

            </div>
        </div>
    </div>
</div>
<script>
    console.log('JS loaded')
    circle = $('#loadingCircle')

    async function postData(data) {
        console.log('Posting data...')
        console.log(data)
        strData = JSON.stringify(data)
        console.log(strData)
        
        const url = 'http://127.0.0.1:8000/api/v1/review'
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: strData
            })
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }

            const json = await response.json();
            fill_data(json)
        } catch (error) {
            console.error(error.message);
        }
    }

    function clear_data() {
        console.log('Clearing data')
        $('#assignment').val('');
        $('#repo-url').val('');

        $('input[name="level"]').prop('checked', false);

        $('ul').empty();
        $('.review-result .downsides').html('<strong>Downsides:</strong><br>');
        $('.review-result .rating').empty();
    }

    function fill_data(json) {
        const filesList = json.files || [];
        const ul = $('ul');
        ul.empty();
        filesList.forEach(file => {
            ul.append(`<li>${file}</li>`);
        });

        const downsides = json.analysis || [];
        const downsidesDiv = $('.review-result .downsides');
        downsidesDiv.html('<strong>Downsides:</strong><br>');
        downsides.forEach(downside => {
            downsidesDiv.append(`${downside}<br>`);
        });

        const rating = json.rating || '';
        $('.review-result .rating').text(`Rating: ${rating}`);
    }

    $('button:contains("Clear")').click(() => {
        clear_data();
    });


    $('button:contains("Review")').click(async () => {
        console.log('Review clicked');
        circle.css('display', 'block')

        const data = {
            "github_repo_url": $('#repo-url').val(),
            "assignment_description": $('#assignment').val(),
            "candidate_level": $('input[name="level"]:checked').val()
        }

        await postData(data)
        circle.css('display', 'none')
    })

</script>
</body>
</html>
'''
    return HTMLResponse(content=html, status_code=200)