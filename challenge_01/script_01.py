def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    if all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences):
        return True
    return False

def csr(data):
    safe_report_count = 0
    for report in data:
        if is_safe(report):
            safe_report_count += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_safe(modified_report):
                    safe_report_count += 1
                    break
    return safe_report_count

def load_data(filename):
    reports = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            
            report = list(map(int, line.split()))
            reports.append(report)
    return reports

filename = "file.txt"  
reports = load_data(filename)
safe_report_count = csr(reports)
print(f"Number of safe reports: {safe_report_count}")