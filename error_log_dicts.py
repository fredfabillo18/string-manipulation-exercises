#from collections import defaultdict

def count_errors(logs):
    errors = {}
    for log in logs:
        entry = log.split(" | ")
        if entry[2]=="ERROR":
            errors[entry[1]] = errors.setdefault(entry[1], 0) + 1
    print(errors)

def error_logs(logs):
    #error_logs = defaultdict(list)
    error_logs = {}
    for log in logs:
        entry = log.split(" | ")
        if entry[2]=="ERROR":
            error_logs.setdefault(entry[1],[]).append(entry[0])
    print(error_logs)

logs = [
    "2026-03-19 10:00:01 | Auth-Service | SUCCESS",
    "2026-03-19 10:00:05 | Data-API | ERROR",
    "2026-03-19 10:00:10 | Auth-Service | ERROR",
    "2026-03-19 10:00:15 | Visual-UI | SUCCESS",
    "2026-03-19 10:00:20 | Data-API | ERROR",
]
count_errors(logs)
error_logs(logs)