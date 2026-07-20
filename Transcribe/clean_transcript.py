import os
import re

input_file = "/app/whisper_sesi presentasi tanya jawab.txt"
output_file = "/app/antigravity_sesi presentasi tanya jawab_verbatim.txt"

hallucinations = [
    "Berkat aksi heroik Kabir",
    "Worcestershire memenangkan pertandingan",
    "Saya akan tinggal di kota ini",
    "Saya akan tinggal di luar negeri",
    "Saya akan terbangun lagi",
    "Selamat ulang tahun",
    "Selamat menikah",
    "Day One menjadi komputer",
    "Day one menjadi pengutur",
    "Beiyuan mendiri SCR Kom",
    "Wih dah panjangin jadi pendekin",
    "terima kasih sudah menonton video ini",
    "thanks for watching",
    "mau nonton video lainnya?",
    "Mouldie out!",
    "Bungan Siongkang tak",
    "Rubesh!",
    "Ditiru bojukan",
    "Lantung paranja!"
]

def clean_transcript():
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    for line in lines:
        is_hallucination = False
        for h in hallucinations:
            if h.lower() in line.lower():
                is_hallucination = True
                break
        
        if not is_hallucination:
            cleaned_lines.append(line)
            
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
        
    print(f"Cleaned transcript saved to {output_file}. Original lines: {len(lines)}, Cleaned lines: {len(cleaned_lines)}")

if __name__ == "__main__":
    clean_transcript()
