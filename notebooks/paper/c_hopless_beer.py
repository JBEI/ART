"""
Custom plotting code used in `C_Hopless_Beer.ipynb`.

Keeping code separate from the notebook makes the notebook simpler and the plot code
unit testable.
"""

from pathlib import Path

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.typing import ArrayLike


def plot_target_value(  # noqa: C901
    data,
    recs: dict[str, ArrayLike],
    targets: dict[str, ArrayLike],
    draws: dict[str, ArrayLike] | None = None,
    dist=False,
    xlim=None,
    ylim=None,
    target_value=False,
    output_dir: Path | None = None,
    result_suffix="",
):
    """Plot input data and recommendations in the target molecules plane.
    Corresponding to hopless beer study."""

    def set_axeslim(xlim=None, ylim=None):
        if xlim is not None:
            plt.xlim(left=xlim[0], right=xlim[1])
        if ylim is not None:
            plt.ylim(bottom=ylim[0], top=ylim[1])

    fig = plt.figure(figsize=(8, 5.5), tight_layout=True)

    lw = 2
    fontsize = 15

    beer_marker_colors = {
        "pale ale": "#4CE599",
        "hop hunter": "#1E593B",
        "torpedo": "#339966",
    }
    beer_markers = {"pale ale": "*", "hop hunter": "o", "torpedo": "s"}
    beer_abbreviations = {"pale ale": "PA", "hop hunter": "HH", "torpedo": "T"}
    linalool_index = 0  # linalool is (input_vars[0])
    geraniol_index = 1  # Geraniol is (input_vars[1])

    gs = gridspec.GridSpec(nrows=5, ncols=5, left=0.0, right=0.5, wspace=0.0, hspace=0)

    # Scope all style changes to this function using context managers, so
    # global seaborn/matplotlib state is never mutated (prevents cross-
    # contamination between plots, e.g. during unit testing).
    with sns.axes_style("ticks"), plt.style.context("seaborn-v0_8-darkgrid"):
        if dist:
            # Plot Linalool pdf
            fig.add_subplot(gs[0, :-1])
            for beer, beer_draws in draws.items():
                sns.kdeplot(
                    beer_draws[:, linalool_index],
                    color=beer_marker_colors[beer],
                    fill=True,
                )
            plt.axis("off")

            set_axeslim(xlim=xlim)

        # Set up plot axes
        ax2 = fig.add_subplot(gs[1:, :-1])
        ax2.set_xlabel("Linalool (L)", fontsize=fontsize)
        ax2.set_ylabel("Geraniol (G)", fontsize=fontsize)

        # Plot data
        plt.scatter(
            data[:, 0], data[:, 1], s=70.0, c="r", marker="+", alpha=0.8, lw=lw, label="Data"
        )

        # Plot recommendations
        beer_rec_marker_sizes = {"pale ale": 80, "hop hunter": 70, "torpedo": 70}
        for beer, beer_recs in recs.items():
            plt.scatter(
                beer_recs[:, 0],
                beer_recs[:, 1],
                s=beer_rec_marker_sizes[beer],
                c="None",
                marker=beer_markers[beer],
                edgecolors=beer_marker_colors[beer],
                alpha=1,
                lw=lw,
                label=f"{beer_abbreviations[beer]} recommendations",
            )

        if target_value:
            target_marker_sizes = {"pale ale": 70.0, "hop hunter": 20.0, "torpedo": 20.0}
            for beer, target in targets.items():
                plt.scatter(
                    target[0],
                    target[1],
                    s=target_marker_sizes[beer],
                    c="k",
                    marker=beer_markers[beer],
                    alpha=1,
                    edgecolors="k",
                    lw=lw,
                    label=f"{beer_abbreviations[beer]} target",
                )

        set_axeslim(xlim=xlim, ylim=ylim)

        plt.tick_params(axis="both", which="major", labelsize=fontsize)

        lgd = plt.legend(
            loc="center left", bbox_to_anchor=(1.2, 0.5), fontsize=fontsize, shadow=True
        )

        if dist:
            # Plot Geraniol pdf
            fig.add_subplot(gs[1:, -1])
            for beer, beer_draws in draws.items():
                sns.kdeplot(
                    y=beer_draws[:, geraniol_index],
                    color=beer_marker_colors[beer],
                    fill=True,
                )
            plt.axis("off")

            set_axeslim(ylim=ylim)

    if output_dir:
        fig.savefig(
            Path(output_dir, f"target_values{result_suffix}.png"),
            bbox_inches="tight",
            bbox_extra_artists=(lgd,),
            transparent=False,
            dpi=150,
        )

    # Close the plot to release resources.
    plt.close(fig)
