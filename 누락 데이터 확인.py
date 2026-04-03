import os

folder_path = "C:\\Users\\yunji\\Downloads"  # ← 폴더 경로 수정
target_date = "2026. 1."
missing_files = []
total = 0

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".csv") and file.startswith("France_Daily"):
            filepath = os.path.join(root, file)
            total += 1
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if target_date not in content:
                missing_files.append(filepath)

print(f"총 {total}개 파일 중 {len(missing_files)}개 누락\n")
for path in sorted(missing_files):
    print(f"  MISSING: {path}")