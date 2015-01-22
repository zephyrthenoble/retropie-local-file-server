import os
from bottle import route, request, static_file, run

directory = "/home/pi/RetroPie/roms"
html  ='<h2>Upload a file to the RetroPie</h2><br>'
html +='<p>Select the correct directory for your rom, and the rom FILE, not the .zip file.  Extracting it helps.<p>'
html +='<form action="/upload" method="post" enctype="multipart/form-data">\n'
html +='    Select directory: '
html +='<select name="rom">\n'

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))]


print os.listdir(directory)
dirs = get_immediate_subdirectories(directory)
print dirs
for x in dirs:
    html +='    <option value=%s>%s</option>\n'%(x, x)
html +='    </select><br>'
html +='''
    Select a file: <input type="file" name="upload" /><br>
    <input type="submit" value="Start upload" />
</form>
'''
@route('/')
def root():
    return html


@route('/upload', method='POST')
def do_upload():
    rom = request.forms.get('rom')
    upload = request.files.get('upload')

    name, ext = os.path.splitext(upload.filename)
    if ext in ('.zip',):
        return "File extension not allowed: "+ext

    save_path = os.path.join(directory,"{rom}".format(rom=rom))
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return "File successfully saved to '{0}'.".format(save_path)

if __name__ == '__main__':
    run(host='0.0.0.0', port=80, reloader=True)
