def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.

    Args:
        machines: dict mapping machine name -> log file name

    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {}

    with open("info.log", "w") as info_out, \
         open("warning.log", "w") as warning_out, \
         open("error.log", "w") as error_out:

        outputs = {
            "INFO": info_out,
            "WARNING": warning_out,
            "ERROR": error_out,
        }

        for machine, log_name in machines.items():
            counts[machine] = {"INFO": 0, "WARNING": 0, "ERROR": 0}

            with open(log_name, "r") as log:
                for line in log:
                    line = line.strip()
                    if not line:
                        continue  # ignore blank lines

                    for level, out_file in outputs.items():
                        if f"[{level}]" in line:
                            out_file.write(f"{machine} | {line}\n")
                            counts[machine][level] += 1
                            break

    return counts


def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("SECURITY LOG REPORT")
    print("=" * 40)

    totals = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for machine, levels in counts.items():
        total = levels["INFO"] + levels["WARNING"] + levels["ERROR"]

        if levels["ERROR"] >= 2:
            status = "CRITICAL"
        elif levels["ERROR"] >= 1 or levels["WARNING"] >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"

        print(f"{machine}: {total} entries | INFO {levels['INFO']} | "
              f"WARNING {levels['WARNING']} | ERROR {levels['ERROR']} | "
              f"Status: {status}")

        for level in totals:
            totals[level] += levels[level]

    print("-" * 40)
    grand_total = sum(totals.values())
    print(f"Total: {grand_total} entries | INFO {totals['INFO']} | "
          f"WARNING {totals['WARNING']} | ERROR {totals['ERROR']}")

    print("Errors (see error.log):")
    with open(error_file, "r") as f:
        for line in f:
            print("  " + line.rstrip("\n"))




import json
import pickle
import os


def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""
    incidents = []

    with open(csv_file, "r") as f:
        next(f, None)  # skip the header line
        for line in f:
            line = line.strip()
            if not line:
                continue  # ignore blank lines
            id_, machine, severity, description = line.split(",")
            incidents.append({
                "id": int(id_),
                "machine": machine,
                "severity": severity,
                "description": description,
            })

    return incidents


def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""
    summary = {
        "total": len(incidents),
        "by_machine": {},
        "by_severity": {},
        "high_ids": [],
    }

    for incident in incidents:
        machine = incident["machine"]
        severity = incident["severity"]

        summary["by_machine"][machine] = summary["by_machine"].get(machine, 0) + 1
        summary["by_severity"][severity] = summary["by_severity"].get(severity, 0) + 1

        if severity == "high":
            summary["high_ids"].append(incident["id"])

    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)

    return summary


def archive(incidents, folder):
    """Pickle all incidents and write one JSON file per machine into folder."""
    os.makedirs(folder, exist_ok=True)

    # Whole list, pickled in binary mode
    with open(os.path.join(folder, "incidents.pkl"), "wb") as f:
        pickle.dump(incidents, f)

    # Group incidents by machine, keeping file order
    by_machine = {}
    for incident in incidents:
        by_machine.setdefault(incident["machine"], []).append(incident)

    for machine, items in by_machine.items():
        with open(os.path.join(folder, machine + ".json"), "w") as f:
            json.dump(items, f)

    return sorted(os.listdir(folder))


def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    with open(os.path.join(folder, "incidents.pkl"), "rb") as f:
        return pickle.load(f)