import numpy as np


def extract_cross_section(file_path):
    """
    Extract cross section value from a MadGraph output text file.
    """
    with open(file_path, "r") as f:
        for line in f:
            if "Cross-section" in line or "cross section" in line:
                parts = line.split()
                for p in parts:
                    try:
                        return float(p)
                    except ValueError:
                        continue
    return None


def compare_cross_sections(sm_file, bsm_file):
    """
    Compare Standard Model and BSM cross sections.
    """
    sm = extract_cross_section(sm_file)
    bsm = extract_cross_section(bsm_file)

    if sm is None or bsm is None:
        raise ValueError("Cross section not found in one of the files.")

    deviation = (bsm - sm) / sm

    return sm, bsm, deviation


if __name__ == "__main__":
    sm_file = "../data/raw/sm_output.txt"
    bsm_file = "../data/raw/bsm_output.txt"

    sm, bsm, dev = compare_cross_sections(sm_file, bsm_file)

    print("Standard Model cross section:", sm)
    print("BSM cross section:", bsm)
    print("Relative deviation:", dev)
