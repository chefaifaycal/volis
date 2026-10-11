import subprocess, os, tempfile
def svg2png(svg_path, out, w, h=None, bg='transparent'):
    h = h or w
    html = f'<html><body style="margin:0;background:{bg}"><img src="file://{svg_path}" style="width:{w}px;height:{h}px;display:block"></body></html>'
    t = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False); t.write(html); t.close()
    subprocess.run(['google-chrome', '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--default-background-color=00000000', f'--window-size={w},{h}', f'--screenshot={out}', f'file://{t.name}'], capture_output=True)
    os.unlink(t.name)
