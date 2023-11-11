from app import app, render_template
import randomname


@app.route('/pos')
def pos_index():
    return render_template('pos_screen.html')
