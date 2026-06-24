from pathlib import Path
import base64
import shutil
import tarfile

parts = sorted(Path('.bootstrap').glob('xz-*'))
payload = ''.join(path.read_text(encoding='utf-8') for path in parts)
archive = Path('/tmp/glpi-blueprint.tar.xz')
archive.write_bytes(base64.b64decode(payload))

with tarfile.open(archive, mode='r:xz') as bundle:
    bundle.extractall(path='.', filter='data')

shutil.rmtree('.bootstrap')
workflow = Path('.github/workflows/bootstrap-glpi.yml')
if workflow.exists():
    workflow.unlink()
