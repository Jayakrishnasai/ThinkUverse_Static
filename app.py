from flask import Flask, render_template
import pandas as pd
import random
import datetime

app = Flask(__name__)

# Dynamic content
QUOTES = [
    "The universe is full of magical things patiently waiting for our wits to grow sharper. – Eden Phillpotts",
    "Imagination is more important than knowledge. – Albert Einstein",
    "We are an impossible existence in an impossible universe.",
    "Thoughts are the stars of our inner universe.",
    "The mind is a universe and can make a heaven of hell, a hell of heaven. – John Milton"
]

@app.context_processor
def inject_now():
    return {'now': datetime.datetime.utcnow()}

@app.route('/')
def index():
    # Quote for the hero section
    if QUOTES:
        quote = random.choice(QUOTES)
    else:
        quote = "Be the change you wish to see in the universe."
    
    # Data for the data section
    data = {
        'Celestial Body': ['Sun', 'Sirius', 'Canopus', 'Arcturus', 'Vega'],
        'Type': ['G-type Main Sequence', 'A-type Main Sequence', 'F-type Supergiant', 'K-type Giant', 'A-type Main Sequence'],
        'Distance (Light Years)': [0.00001581, 8.6, 310, 37, 25],
        'Apparent Magnitude': [-26.74, -1.46, -0.74, -0.05, 0.03]
    }
    df = pd.DataFrame(data)
    table_html = df.to_html(classes='data-table', index=False)
    
    return render_template('index.html', quote=quote, table_html=table_html, title="ThinkUverse")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
