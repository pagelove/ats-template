"""Dependency-free source gate; it does not establish hosted composition or authorization."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.ids=set(); self.errors=[]; self.script=False; self.code=''; self.scripts=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:
   if a['id'] in self.ids:self.errors.append('duplicate DOM id '+a['id'])
   self.ids.add(a['id'])
  if tag=='script' and 'src' not in a and a.get('type','') in ('','module','text/javascript'):self.script=True;self.code=''
 def handle_endtag(self,tag):
  if tag=='script' and self.script:self.scripts.append(self.code);self.script=False
 def handle_data(self,data):
  if self.script:self.code+=data
root=Path(__file__).resolve().parents[1]
paths=subprocess.check_output(['git','ls-tree','-r','--name-only','HEAD','site'],cwd=root,text=True).splitlines()
count=0
for name in paths:
 if not name.endswith('.html'):continue
 try:text=(root/name).read_text(encoding='utf-8')
 except (OSError,ValueError):text=subprocess.check_output(['git','show','HEAD:'+name],cwd=root,text=True,encoding='utf-8')
 page=Page();page.feed(text)
 if page.errors:raise SystemExit(name+': '+', '.join(page.errors))
 for script in page.scripts:
  r=subprocess.run(['node','--check','--input-type=module'],input=script,text=True,encoding='utf-8',capture_output=True)
  if r.returncode:raise SystemExit(name+': '+r.stderr)
 count+=1
print('PASS: '+str(count)+' ATS HTML sources: unique static IDs and inline JavaScript syntax; live composition/enforcement pending.')
