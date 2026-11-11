import openpyxl, re, json, sys
wb=openpyxl.load_workbook(sys.argv[1]); ws=wb.active
def link(c):
    v=c.hyperlink.target if c.hyperlink else c.value
    return v.strip() if isinstance(v,str) and v.strip().startswith('http') else None
hts=[]; ht=unit=lesson=None
for r in range(4, ws.max_row+1):
    c=ws.cell(r,3).value
    if c: ht={'name':' '.join(c.split()),'units':[]}; hts.append(ht)
    d=ws.cell(r,4).value; e=ws.cell(r,5).value
    d=' '.join(str(d).split()) if d else None
    if d and re.match(r'^\d+\.',d) and not e:
        unit={'name':re.sub(r'^\d+\.\s*','',d),'num':int(d.split('.')[0]),'lessons':[]}; ht['units'].append(unit); lesson=None; continue
    if d:
        lesson={'name':d,'objectives':[],'videos':[],'questions':[]}; unit['lessons'].append(lesson)
    if e and lesson is not None: lesson['objectives'].append(' '.join(str(e).split()))
    for col in (6,7):
        u=link(ws.cell(r,col))
        if u and lesson is not None:
            k='questions' if 'mathsgenie' in u or u.endswith('.pdf') else 'videos'
            if u not in lesson[k]: lesson[k].append(u)
json.dump(hts,open(sys.argv[2],'w'),indent=1,ensure_ascii=False)
for h in hts:
    print(h['name'])
    for u in h['units']: print('  ',u['num'],u['name'],len(u['lessons']),'lessons', sum(len(l['videos']) for l in u['lessons']),'vids',sum(len(l['questions']) for l in u['lessons']),'qs')
