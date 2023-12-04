from flask import Flask, render_template, request
import stories

app = Flask(__name__)

@app.route('/')
def home_page():
    prompts = stories.story.prompts
    return render_template("home.html", story_prompts = prompts)

@app.route('/story')
def story_page():
    inputs = {}
    prompts = stories.story.prompts
    for prompt in prompts:
        if request.args.get(prompt):
            inputs[prompt] = request.args.get(prompt)
    template = stories.story.generate(inputs)
    return render_template("story.html", template=template)