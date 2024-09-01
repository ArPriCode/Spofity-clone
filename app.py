import os
from datetime import datetime, timedelta

start_date = datetime(2024, 9, 1)
end_date = datetime(2025, 12, 31)

current_date = start_date

while current_date <= end_date:

    with open("file.txt", "a") as file:
        file.write(f"Commit on {current_date.strftime('%Y-%m-%d')}\n")

    commit_date = current_date.strftime('%Y-%m-%d 12:00:00')

    os.system("git add .")
    os.system(
        f'GIT_AUTHOR_DATE="{commit_date}" '
        f'GIT_COMMITTER_DATE="{commit_date}" '
        f'git commit -m "daily commit" --date="{commit_date}"'
    )

    current_date += timedelta(days=1)

os.system("git push -f origin main")