import matplotlib.pyplot as plt


def plot_cross_sections(sm, bsm):
    labels = ["Standard Model", "BSM"]
    values = [sm, bsm]

    plt.figure()
    plt.bar(labels, values)
    plt.ylabel("Cross Section")
    plt.title("Cross Section Comparison")
    plt.tight_layout()
    plt.savefig("../results/plots/cross_section_comparison.png", dpi=300)
    plt.close()
