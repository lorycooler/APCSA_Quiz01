"""Rebuild the offline HTML after editing bank.json; Python standard library only."""
import json,re,argparse
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bank',default=str(Path(__file__).with_name('bank.json')))
    parser.add_argument('--output',default=str(Path(__file__).with_name('index.html')))
    args=parser.parse_args()
    bank=json.loads(Path(args.bank).read_text(encoding='utf-8-sig'))
    units={u['id'] for u in bank['units']}
    seen=set();groups={}
    for q in bank['questions']:
        if q['id'] in seen:raise ValueError(f'Duplicate question ID: {q["id"]}')
        seen.add(q['id'])
        if q['unit'] not in units:raise ValueError(f'Unknown unit: {q["id"]}')
        if q['type'] not in ('fill','mcq'):raise ValueError(f'Unknown question type: {q["id"]}')
        if not isinstance(q['set'],int) or q['set']<1:raise ValueError('Set number must be a positive integer')
        groups.setdefault((q['unit'],q['type'],q['set']),[]).append(q)
        if q['type']=='fill':
            if q['code'].count('___')!=len(q['answers']):raise ValueError(f'Blank count mismatch: {q["id"]}')
            if any(not a or any(not isinstance(x,str) or not x.strip() for x in a) for a in q['answers']):raise ValueError('Empty accepted answer')
        else:
            if len(q['options'])!=4 or len(set(q['options']))!=4 or q['answer'] not in 'ABCD':raise ValueError(f'Invalid MCQ: {q["id"]}')
        if re.search(r'\b(extends|implements|super)\b',q.get('code','')):raise ValueError(f'Excluded inheritance syntax: {q["id"]}')
    for (unit,type,set_no),qs in groups.items():
        required=20 if type=='fill' else 16
        if len(qs)!=required:raise ValueError(f'Unit {unit}, {type} set {set_no}: {len(qs)} questions; requires {required}')
    template=Path(__file__).with_name('site-template.html').read_text(encoding='utf8')
    payload=json.dumps(bank,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    result=template.replace('__CONFIG__',payload)
    fill=sum(q['type']=='fill' for q in bank['questions']);mc=len(bank['questions'])-fill
    result=result.replace('__FILL_COUNT__',str(fill)).replace('__MCQ_COUNT__',str(mc)).replace('__TOTAL_COUNT__',str(len(bank['questions'])))
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True);output.write_text(result,encoding='utf8')
    print(f'Validated and built {len(bank["questions"])} questions across {len(groups)} sets: {output.resolve()}')

if __name__=='__main__':main()
