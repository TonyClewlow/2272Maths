import json,sys
t=open(sys.argv[1]).read(); d=json.load(open(sys.argv[2]))
open(sys.argv[3],'w').write(t.replace('__DATA__',json.dumps(d,ensure_ascii=False).replace('</','<\\/')))
