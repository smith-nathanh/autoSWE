import os
import zipfile
import logging
from dotenv import load_dotenv
from langsmith import utils
from pathlib import Path
from flask import Flask, render_template, request, flash, redirect, url_for, send_file, Response
from werkzeug.utils import secure_filename
import markdown
from langchain_core.messages import HumanMessage
from system.graph import build_graph
from system.prompts import DESIGN_PROMPT
from io import BytesIO
import time

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'md'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'development-key-change-in-production'

load_dotenv(dotenv_path="system/.env", override=True)
logging.basicConfig(filename='logfile.log', level=logging.INFO, filemode='w')
logging.info('TRACING %s', str(utils.tracing_is_enabled()))
logging.info(os.environ["LANGCHAIN_PROJECT"])

# Exclude werkzeug logs from logfile.log
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.WARNING)

# Ensure upload directory exists
Path(UPLOAD_FOLDER).mkdir(exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_artifacts(prd_file_path):
    """Generate software artifacts from a PRD file using autoSWE."""
    try:
        # Read the PRD content
        with open(prd_file_path, 'r') as f:
            prd_content = f.read()
        logging.info("PRD content read successfully")
    except Exception as e:
        flash(f"Error reading PRD file: {str(e)}")
        logging.error(f"Error reading PRD file: {str(e)}")
        return None
    
    try:
        # Build the graph and initialize state
        graph = build_graph()
        state = {
            'documents': {'PRD': prd_content},
            'messages': [HumanMessage(content=DESIGN_PROMPT.format(PRD=prd_content))]
        }
        
        # Generate artifacts using the graph
        logging.info("Starting artifact generation")
        final_state = graph.invoke(state)
        logging.info("Artifact generation completed")
        
        # Map the final state to our web display structure
        artifacts = {
            'prd': final_state['documents'].get('PRD', ''),
            'class_diagram': final_state['documents'].get('UML_class', ''),
            'sequence_diagram': final_state['documents'].get('UML_sequence', ''),
            'architecture': final_state['documents'].get('architecture_design', ''),
            'code_files': final_state['documents']['code'],
            'unit_tests': final_state['documents']['unit_tests'],
            'acceptance_tests': final_state['documents']['acceptance_tests'],
        }
        
        return artifacts
        
    except Exception as e:
        flash(f"Error generating artifacts: {str(e)}")
        logging.error(f"Error generating artifacts: {str(e)}")
        return None

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Generate artifacts
            artifacts = generate_artifacts(filepath)
            
            if artifacts is None:
                return redirect(request.url)
                
            # Convert PRD markdown to HTML
            if 'prd' in artifacts:
                artifacts['prd'] = markdown.markdown(artifacts['prd'])
            
            return render_template('view_artifacts.html', artifacts=artifacts)
    
    return render_template('index.html')

@app.route('/download_temp')
def download_temp():
    temp_dir = Path('temp')
    
    # Create zip file in memory
    memory_file = BytesIO()
    
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in temp_dir.rglob('*'):
            arcname = file_path.relative_to(temp_dir)
            zf.write(file_path, arcname)
    
    memory_file.seek(0)
    
    return send_file(
        memory_file,
        mimetype='application/zip',
        as_attachment=True,
        download_name='generated_artifacts.zip'
    )

@app.route('/progress')
def progress():
    def generate():
        # Ensure the log file exists
        open('logfile.log', 'a').close()
        
        with open('logfile.log') as f:
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)
                    continue
                yield f"data: {line}\n\n"
    
    return Response(generate(), mimetype='text/event-stream')
