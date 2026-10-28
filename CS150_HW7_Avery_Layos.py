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