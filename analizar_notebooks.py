#!/usr/bin/env python3
"""
Analiza notebooks .ipynb comparando valores numéricos en celdas Markdown
con los outputs de las celdas de código anteriores.
"""
import json
import re
import os
from pathlib import Path

# Expresiones regulares para extraer números
def extract_numbers(text):
    """Extrae números de un texto: enteros, decimales, porcentajes."""
    numbers = []
    # Patrón para números con formato de miles (ej: 3,387.00)
    pattern1 = r'\b\d{1,3}(?:,\d{3})+(?:\.\d+)?\b'
    # Patrón para números sin separador de miles (ej: 3387, 33.51)
    pattern2 = r'\b\d+(?:\.\d+)?\b'
    # Patrón para porcentajes (ej: 83.8%)
    pattern3 = r'\b\d+(?:\.\d+)?%'
    
    for pat in [pattern1, pattern3, pattern2]:
        for match in re.finditer(pat, text):
            num_str = match.group()
            # Limpiar y convertir
            clean = num_str.replace(',', '').replace('%', '')
            try:
                val = float(clean)
                numbers.append((num_str, val, match.start(), match.end()))
            except:
                pass
    return numbers

def extract_output_numbers(cell):
    """Extrae números del output de una celda de código."""
    numbers = []
    if 'outputs' not in cell:
        return numbers
    
    for output in cell['outputs']:
        text = ""
        if output.get('output_type') in ('stream', 'error'):
            text = output.get('text', '')
        elif output.get('output_type') == 'execute_result':
            for key in ['text/plain', 'text/html']:
                if key in output.get('data', {}):
                    text += str(output['data'][key]) + "\n"
        elif output.get('output_type') == 'display_data':
            for key in ['text/plain', 'text/html']:
                if key in output.get('data', {}):
                    text += str(output['data'][key]) + "\n"
        
        nums = extract_numbers(text)
        numbers.extend(nums)
    
    return numbers

def analyze_notebook(path):
    """Analiza un notebook y busca discrepancias."""
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    issues = []
    cells = nb.get('cells', [])
    
    for i, cell in enumerate(cells):
        if cell.get('cell_type') != 'markdown':
            continue
        
        md_text = ''.join(cell.get('source', []))
        md_numbers = extract_numbers(md_text)
        
        if not md_numbers:
            continue
        
        # Buscar la celda de código anterior más cercana con output
        prev_code_cell = None
        for j in range(i-1, -1, -1):
            if cells[j].get('cell_type') == 'code':
                outputs = cells[j].get('outputs', [])
                if outputs:
                    prev_code_cell = cells[j]
                    break
        
        if not prev_code_cell:
            continue
        
        out_numbers = extract_output_numbers(prev_code_cell)
        
        # Comparar números del markdown con números del output
        for md_str, md_val, md_start, md_end in md_numbers:
            # Buscar si hay un número similar en el output
            found_match = False
            for out_str, out_val, _, _ in out_numbers:
                # Comparar con cierta tolerancia
                if md_val == out_val:
                    found_match = True
                    break
                # Para porcentajes, comparar valores absolutos
                if abs(md_val - out_val) < 0.05:
                    found_match = True
                    break
                # Para números grandes, comparar con tolerancia relativa
                if md_val != 0 and abs(md_val - out_val) / abs(md_val) < 0.02:
                    found_match = True
                    break
            
            if not found_match and out_numbers:
                # Podría ser una discrepancia
                issues.append({
                    'cell_idx': i,
                    'md_text_snippet': md_text[max(0, md_start-30):min(len(md_text), md_end+30)].replace('\n', ' '),
                    'md_number': md_str,
                    'md_value': md_val,
                    'output_numbers': [n[1] for n in out_numbers[:20]],
                    'prev_code_idx': j
                })
    
    return issues

def main():
    notebooks = sorted(Path('.').glob('*_Objetivo.ipynb'))
    
    for nb_path in notebooks:
        print(f"\n{'='*80}")
        print(f"ANALIZANDO: {nb_path.name}")
        print(f"{'='*80}")
        
        issues = analyze_notebook(nb_path)
        
        if not issues:
            print("  No se detectaron discrepancias obvias.")
            continue
        
        # Agrupar por celda
        by_cell = {}
        for issue in issues:
            idx = issue['cell_idx']
            by_cell.setdefault(idx, []).append(issue)
        
        for idx, cell_issues in sorted(by_cell.items()):
            print(f"\n  Celda Markdown #{idx}:")
            for issue in cell_issues:
                print(f"    - Número en Markdown: {issue['md_number']} (valor={issue['md_value']})")
                print(f"      Contexto: ...{issue['md_text_snippet']}...")
                print(f"      Números en output previo: {issue['output_numbers'][:10]}")

if __name__ == '__main__':
    main()
